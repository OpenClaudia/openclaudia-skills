#!/usr/bin/env python3
"""
Read-only reader over a plaintext export of WeChat 3.x (macOS) databases.

Does not decrypt anything and never handles keys. Point WECHAT_EXPORT at a
directory an export tool already produced (Message/, Contact/, Group/, Session/).
Chat table = Chat_<md5(username)>. Group messages are prefixed "senderwxid:\n".

Usage:
    wechat.py list [N]                  recent conversations (name, last msg, who)
    wechat.py read <name|wxid> [N]      full thread, group senders resolved
    wechat.py search <keyword> [N]      search text messages everywhere
    wechat.py contacts <keyword>        find usernames by name/remark/nick
    wechat.py whoami                    show your own wxid
    wechat.py unreplied [days]          personal chats where THEY messaged last
    wechat.py day YYYY-MM-DD [--all]    every thread active that day

Reads are only as fresh as the export. Re-run your exporter for new messages.
Optional group filters for `day` live in WECHAT_CONFIG (default
~/.config/wechat-read): ignore_groups.txt, keep_groups.txt, relevant_keywords.txt.
"""
import sys, os, glob, sqlite3, hashlib, re
from collections import Counter
from datetime import datetime

D = os.path.expanduser(os.environ.get("WECHAT_EXPORT", "~/wechat-export"))
WORK = os.path.expanduser(os.environ.get("WECHAT_CONFIG", "~/.config/wechat-read"))

def msg_dbs(): return sorted(glob.glob(os.path.join(D, "Message", "msg_*.db")))

# ---------- name resolution ----------
_names = None
def names():
    global _names
    if _names is not None: return _names
    _names = {}
    c = os.path.join(D, "Contact", "wccontact_new2.db")
    if os.path.isfile(c):
        cx = sqlite3.connect(c)
        try:
            for u, rem, nick in cx.execute("SELECT m_nsUsrName,m_nsRemark,nickname FROM WCContact"):
                _names[u] = (rem or nick or u)
        except Exception: pass
        cx.close()
    return _names

def users():
    us = set(names())
    s = os.path.join(D, "Session", "session_new.db")
    if os.path.isfile(s):
        sx = sqlite3.connect(s)
        try:
            for (u,) in sx.execute("SELECT m_nsUserName FROM SessionAbstract"): us.add(u)
        except Exception: pass
        sx.close()
    return us

_m2u = None
def m2u():
    global _m2u
    if _m2u is None:
        _m2u = {hashlib.md5(u.encode()).hexdigest(): u for u in users()}
    return _m2u

_gnames = None
def gnames():
    """Group display names from GroupContact (the Contact DB lacks most)."""
    global _gnames
    if _gnames is None:
        _gnames = {}
        g = os.path.join(D, "Group", "group_new.db")
        if os.path.isfile(g):
            gx = sqlite3.connect(g)
            try:
                for u, nick in gx.execute("SELECT m_nsUsrName,nickname FROM GroupContact"):
                    if nick: _gnames[u] = nick
            except Exception: pass
            gx.close()
    return _gnames

def disp(u):
    if u.endswith("@chatroom"):
        return names().get(u) or gnames().get(u, u)
    return names().get(u, u)

_sexes = None
def sexes():
    """wxid -> 'he'/'she' from the contact's self-declared WeChat profile (1=m, 2=f).
    Missing for ~10% of contacts; then use the person's name, never a guessed pronoun."""
    global _sexes
    if _sexes is None:
        _sexes = {}
        c = os.path.join(D, "Contact", "wccontact_new2.db")
        if os.path.isfile(c):
            cx = sqlite3.connect(c)
            try:
                for u, s in cx.execute("SELECT m_nsUsrName,m_uiSex FROM WCContact"):
                    if s in (1, 2): _sexes[u] = "he" if s == 1 else "she"
            except Exception: pass
            cx.close()
    return _sexes
def tbl(u): return "Chat_" + hashlib.md5(u.encode()).hexdigest()
def fmt(ts): return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")

def find_table(u):
    t = tbl(u)
    for db in msg_dbs():
        cx = sqlite3.connect(db)
        try:
            if cx.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (t,)).fetchone():
                return db, t
        finally: cx.close()
    return None, None

def candidates(q):
    """All usernames matching q, exact-name first, then partial, then raw."""
    if q in names() or q.endswith("@chatroom") or q.startswith("wxid_") or q.startswith("gh_"):
        return [q]
    ql = q.lower()
    exact = [u for u, d in names().items() if d.lower() == ql]
    part = [u for u, d in names().items() if ql in d.lower() and u not in exact]
    return exact + part

def resolve(q):
    c = candidates(q)
    return c[0] if c else None

_muted = None
def muted():
    """Set of usernames the user muted (消息免打扰 → unread shows as red dot)."""
    global _muted
    if _muted is None:
        _muted = set()
        s = os.path.join(D, "Session", "session_new.db")
        if os.path.isfile(s):
            sx = sqlite3.connect(s)
            try:
                for u, r in sx.execute("SELECT m_nsUserName,m_bShowUnReadAsRedDot FROM SessionAbstract"):
                    if r == 1: _muted.add(u)
            except Exception: pass
            sx.close()
    return _muted

_ignore = None
def ignored():
    """Usernames the user explicitly marked as garbage (one per line)."""
    global _ignore
    if _ignore is None:
        _ignore = set()
        f = os.path.join(WORK, "ignore_groups.txt")
        if os.path.isfile(f):
            _ignore = {l.strip() for l in open(f) if l.strip() and not l.startswith("#")}
    return _ignore

_kept = None
def kept():
    """Usernames to always keep (e.g. family group), one per line."""
    global _kept
    if _kept is None:
        _kept = set()
        f = os.path.join(WORK, "keep_groups.txt")
        if os.path.isfile(f):
            _kept = {l.strip() for l in open(f) if l.strip() and not l.startswith("#")}
    return _kept

_keywords = None
def keywords():
    """Relevance keywords matched against the group NAME (lowercased)."""
    global _keywords
    if _keywords is None:
        f = os.path.join(WORK, "relevant_keywords.txt")
        if os.path.isfile(f):
            _keywords = [l.strip().lower() for l in open(f) if l.strip() and not l.startswith("#")]
        else:
            _keywords = []
    return _keywords

_memcount = None
def member_count(u):
    """# of members in a chatroom (from GroupContact member list)."""
    global _memcount
    if _memcount is None:
        _memcount = {}
        g = os.path.join(D, "Group", "group_new.db")
        if os.path.isfile(g):
            gx = sqlite3.connect(g)
            try:
                for un, ml in gx.execute("SELECT m_nsUsrName, m_nsChatRoomMemList FROM GroupContact"):
                    if ml: _memcount[un] = len([x for x in re.split(r"[;,]", ml) if x.strip()])
            except Exception: pass
            gx.close()
    return _memcount.get(u, 0)

def relevant_group(u, you_sent=0):
    """A group is relevant only if NOT ignored, has <15 members (big groups are
    community/garbage), and either is explicitly kept or its name matches a
    business keyword. keep-list overrides the size rule."""
    if u in ignored(): return False
    if u in kept(): return True
    if member_count(u) >= 15: return False          # big groups = garbage, skip
    return any(k in disp(u).lower() for k in keywords())

_mywxid = None
def whoami():
    global _mywxid
    if _mywxid: return _mywxid
    pref = Counter()
    for db in msg_dbs()[:4]:
        cx = sqlite3.connect(db)
        for (t,) in cx.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Chat_%'"):
            u = m2u().get(t[5:], "")
            if not u.endswith("@chatroom"): continue
            try:
                for (c,) in cx.execute(f"SELECT msgContent FROM [{t}] WHERE mesDes=0 AND messageType=1 LIMIT 20"):
                    if c and ":\n" in c: pref[c.split(":\n", 1)[0]] += 1
            except Exception: pass
        cx.close()
    _mywxid = pref.most_common(1)[0][0] if pref else None
    return _mywxid

TYPE = {1:"", 3:"[image]", 34:"[voice]", 42:"[card]", 43:"[video]", 47:"[sticker]",
        48:"[location]", 49:"[file/link]", 50:"[call]", 10000:"[system]", 10002:"[recalled]"}

def body(content, is_group):
    if not content: return ""
    sender = ""
    if is_group and ":\n" in content:
        sp, content = content.split(":\n", 1)
        sender = disp(sp)
    content = re.sub(r"<[^>]+>", " ", content)
    content = re.sub(r"\s+", " ", content).strip()
    return sender, content

# ---------- commands ----------
def last_time(u):
    db, t = find_table(u)
    if not db: return None
    cx = sqlite3.connect(db)
    r = cx.execute(f"SELECT max(msgCreateTime) FROM [{t}]").fetchone()
    cx.close()
    return r[0] if r and r[0] else None

def cmd_read(q, n=60):
    cands = candidates(q)
    if not cands: print("not found:", q); return
    # rank matches by most-recent activity so we never silently grab a stale namesake
    ranked = sorted(((last_time(u) or 0, u) for u in cands), reverse=True)
    ranked = [(ts, u) for ts, u in ranked if ts]
    if not ranked:
        print("no messages for", disp(cands[0]), f"({len(cands)} name matches, none with a thread)"); return
    if len(ranked) > 1:
        print(f"~ {len(ranked)} contacts match '{q}'. Showing most recent. Others:")
        for ts, u in ranked[1:6]:
            print(f"    {disp(u)[:24]:24} {u:24} (last {fmt(ts)})")
        print()
    u = ranked[0][1]
    db, t = find_table(u)
    is_group = u.endswith("@chatroom")
    cx = sqlite3.connect(db)
    rows = cx.execute(f"SELECT msgCreateTime,mesDes,messageType,msgContent FROM [{t}] "
                      f"ORDER BY msgCreateTime DESC LIMIT {n}").fetchall()
    cx.close()
    print(f"# {disp(u)}  ({u})  — last {len(rows)} of thread\n")
    for ts, des, mt, content in reversed(rows):
        sender, txt = (body(content, is_group) if is_group else ("", body(content, False)[1] if False else re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",content or "")).strip()))
        who = "ME" if des == 0 else (sender or "THEM")
        tag = TYPE.get(mt, f"[t{mt}]")
        print(f"[{fmt(ts)}] {who}: {tag}{txt[:200]}")

def cmd_list(n=40):
    s = os.path.join(D, "Session", "session_new.db")
    sx = sqlite3.connect(s)
    rows = sx.execute("SELECT m_nsUserName,m_uLastTime FROM SessionAbstract ORDER BY m_uLastTime DESC LIMIT ?", (n,)).fetchall()
    sx.close()
    for u, t in rows:
        db, tb = find_table(u)
        last = ""
        if db:
            cx = sqlite3.connect(db)
            r = cx.execute(f"SELECT mesDes,messageType,msgContent FROM [{tb}] ORDER BY msgCreateTime DESC LIMIT 1").fetchone()
            cx.close()
            if r:
                des, mt, c = r
                _, txt = body(c, u.endswith("@chatroom")) if u.endswith("@chatroom") else ("", re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",c or "")).strip())
                last = ("ME: " if des == 0 else "THEM: ") + TYPE.get(mt, f"[t{mt}]") + txt[:50]
        kind = "[group]" if u.endswith("@chatroom") else ("[official]" if u.startswith("gh_") else "")
        print(f"{fmt(t):16} {disp(u)[:22]:22} {kind:9} {u[:26]:26} {last}")

def cmd_search(kw, n=40):
    hits = []
    for db in msg_dbs():
        cx = sqlite3.connect(db)
        try:
            for (t,) in cx.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Chat_%'"):
                u = m2u().get(t[5:], t)
                try:
                    for ts, des, c in cx.execute(
                        f"SELECT msgCreateTime,mesDes,msgContent FROM [{t}] WHERE messageType=1 AND msgContent LIKE ? LIMIT 4",
                        (f"%{kw}%",)):
                        hits.append((ts, u, des, c))
                except Exception: pass
        finally: cx.close()
    hits.sort(key=lambda x: -x[0])
    for ts, u, des, c in hits[:n]:
        is_g = isinstance(u, str) and u.endswith("@chatroom")
        sender, txt = body(c, is_g) if is_g else ("", re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",c or "")).strip())
        who = "ME" if des == 0 else (sender or disp(u) if isinstance(u, str) else "?")
        print(f"[{fmt(ts)}] {disp(u)[:18] if isinstance(u,str) else u:18} {who[:14]:14}: {txt[:80]}")
    print(f"\n{len(hits)} matches for '{kw}'")

def cmd_contacts(kw):
    for u, d in names().items():
        if kw.lower() in d.lower() or kw.lower() in u.lower():
            print(f"{d[:30]:30} {u}")

def cmd_unreplied(days=30):
    import time
    since = time.time() - days*86400
    out = []
    for db in msg_dbs():
        cx = sqlite3.connect(db)
        for (t,) in cx.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Chat_%'"):
            u = m2u().get(t[5:])
            if not u or u.endswith("@chatroom") or u.startswith("gh_"): continue
            try:
                r = cx.execute(f"SELECT msgCreateTime,mesDes,messageType,msgContent FROM [{t}] WHERE msgCreateTime>=? ORDER BY msgCreateTime DESC LIMIT 1", (since,)).fetchone()
            except Exception: continue
            if r and r[1] == 1:
                txt = re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",r[3] or "")).strip()
                out.append((r[0], u, TYPE.get(r[2],"")+txt[:70]))
        cx.close()
    for ts, u, c in sorted(out, reverse=True):
        print(f"{fmt(ts)}  {disp(u)[:24]:24}  {c}")
    print(f"\n{len(out)} personal chats where they messaged last ({days}d)")

def cmd_day(date_str, allg=False, start=None, end=None):
    """Summarize one day. date_str = YYYY-MM-DD. Groups filtered for relevance
    unless allg=True. Optional start/end (unix epoch) override the default
    midnight->midnight window."""
    import datetime
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    if start is None:
        start = d.timestamp(); end = start + 86400
    persons, groups, junk = [], [], 0
    SYS = ("weixin","filehelper","medianote","qmessage","fmessage","tmessage","newsapp",
           "floatbottle","feedsapp","masssendapp","notifymessage","mphelper","brandsessionholder")
    for db in msg_dbs():
        cx = sqlite3.connect(db)
        for (t,) in cx.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Chat_%'"):
            u = m2u().get(t[5:])
            if not u: continue
            try:
                rows = cx.execute(f"SELECT msgCreateTime,mesDes,messageType,msgContent FROM [{t}] WHERE msgCreateTime>=? AND msgCreateTime<? ORDER BY msgCreateTime", (start, end)).fetchall()
            except Exception: continue
            if not rows: continue
            you = sum(1 for r in rows if r[1] == 0)
            if u.endswith("@chatroom"):
                if allg or relevant_group(u, you): groups.append((you, u, rows))
                else: junk += 1
            elif u.startswith("gh_") or u in SYS:
                continue
            else:
                persons.append((you, u, rows))
        cx.close()
    persons.sort(key=lambda x: -len(x[2])); groups.sort(key=lambda x: -len(x[2]))
    def dump(u, rows):
        is_g = u.endswith("@chatroom")
        you = sum(1 for r in rows if r[1] == 0)
        pron = "" if is_g else (f"  [{sexes()[u]}]" if u in sexes() else "  [pronoun unknown: use their name]")
        print(f"\n### {disp(u)}{pron}  ({len(rows)} msgs, you {you})  {u}")
        for ts, des, mt, c in rows:
            s, b = (body(c, is_g), "") if False else (None, None)
            sender, txt = body(c, is_g) if is_g else ("", re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",c or "")).strip())
            who = "YOU" if des == 0 else (sender or "THEM")
            tag = TYPE.get(mt, f"[t{mt}]")
            tm = datetime.datetime.fromtimestamp(ts).strftime("%H:%M")
            print(f"  {tm} {who[:12]}: {tag}{txt[:110]}")
    print(f"== {date_str} == {len(persons)} personal, {len(groups)} relevant groups ({junk} junk groups hidden)")
    print("\n" + "="*20 + " PERSONAL " + "="*20)
    for _, u, rows in persons: dump(u, rows)
    print("\n" + "="*20 + " GROUPS (relevant) " + "="*20)
    for _, u, rows in groups: dump(u, rows)

if __name__ == "__main__":
    a = sys.argv[1:]
    if not os.path.isdir(os.path.join(D, "Message")):
        sys.exit(f"No export at {D}. Set WECHAT_EXPORT to your plaintext export directory.")
    if not a or a[0] == "list": cmd_list(int(a[1]) if len(a) > 1 else 40)
    elif a[0] == "day":
        win = [float(x) for x in a[2:4] if re.fullmatch(r"\d+(\.\d+)?", x)]
        cmd_day(a[1], allg=("--all" in a), start=win[0] if len(win) == 2 else None, end=win[1] if len(win) == 2 else None)
    elif a[0] == "read": cmd_read(a[1], int(a[2]) if len(a) > 2 else 60)
    elif a[0] == "search": cmd_search(a[1], int(a[2]) if len(a) > 2 else 40)
    elif a[0] == "contacts": cmd_contacts(a[1])
    elif a[0] == "whoami": print(whoami())
    elif a[0] == "unreplied": cmd_unreplied(int(a[1]) if len(a) > 1 else 30)
    else: print(__doc__)
