---
name: stripe-dispute
description: Evaluate whether a Stripe dispute is economical to contest, then gather evidence and submit only when approved. Use for Stripe disputes, chargebacks, counter-disputes, evidence packages, or Stripe dispute IDs.
---

# Stripe Dispute Evaluation and Evidence

Evaluate the economics first. When contesting is justified and approved, build an evidence package and submit it to Stripe. Works for any SaaS using Stripe and a user database with login or usage logs.

## When to Use This Skill

Use this skill when the user:

- Receives a Stripe chargeback notification and wants to fight it
- Provides a dispute ID (`du_*`) and asks to "counter" / "rebut" / "fight" it
- Asks how to gather evidence for a dispute marked `fraudulent`, `product_not_received`, `product_unacceptable`, or `subscription_canceled`
- Wants an activity-log PDF showing a customer used their product

## Required Environment Variables

```bash
STRIPE_SECRET_KEY=sk_live_...      # Stripe restricted/secret key with disputes:write scope
DATABASE_URL=postgres://...        # READ-ONLY connection to your app's user database (optional but recommended)
TERMS_URL=https://yoursite.com/terms   # URL to your published cancellation/refund policy
EVIDENCE_DIR=~/disputes            # Where to save the per-customer evidence folders
```

**Database safety:** all queries are SELECT-only. Never let this skill issue UPDATE/DELETE/INSERT.

## Inputs

The user provides any of:
- Stripe dispute ID (`du_xxxxx`) — preferred
- Customer email — skill will look up the dispute
- Charge ID (`ch_xxxxx` or `py_xxxxx`)

## Decide whether to contest first

Accepting a dispute can be the correct outcome. Never submit evidence merely because a
case exists.

1. Verify live Stripe pricing. Under current US standard pricing, Stripe charges a $15
   dispute-received fee automatically and another $15 dispute-countered fee when evidence
   is submitted. The received fee is sunk. The countered fee is returned only on a win.
   Use current live pricing if these amounts change.
2. Query the merchant's live Stripe dispute history. For defended win rate, count only
   closed disputes with `evidence_details.submission_count > 0`. Separate initial purchases
   from renewals and narrow to the same reason when the sample permits. Report wins,
   losses, open cases, and sample size. State when no exact-match precedent exists.
3. Calculate break-even probability and expected value after the countered fee and
   evidence-building labor. Do not invent a probability from case strength alone.
4. Use a conservative 30% minimum win-probability threshold unless the user provides a
   different threshold. If comparable data cannot support that threshold, recommend
   leaving the dispute unanswered. This avoids the countered fee, although the disputed
   amount and received fee remain lost.
5. Obtain explicit user approval before building files, uploading evidence, or submitting.
   Submission is final and fee-bearing.

## Steps

### 1. Pull the dispute from Stripe

```bash
curl -s -u "$STRIPE_SECRET_KEY:" \
  "https://api.stripe.com/v1/disputes/$DISPUTE_ID" | python3 -m json.tool
```

Extract: `amount`, `reason`, `charge`, `evidence_details.due_by`, `evidence_details.submission_count`, `status`.

If `submission_count > 0` the dispute has already been countered — STOP and warn the user.

### 2. Pull the surrounding context

```bash
# Charge → tells you the payment method, risk score, billing details, customer ID
curl -s -u "$STRIPE_SECRET_KEY:" "https://api.stripe.com/v1/charges/$CHARGE_ID"

# Customer → name, email, default payment source
curl -s -u "$STRIPE_SECRET_KEY:" "https://api.stripe.com/v1/customers/$CUSTOMER_ID"

# All invoices for the customer → look for previously-undisputed payments
curl -s -u "$STRIPE_SECRET_KEY:" \
  "https://api.stripe.com/v1/invoices?customer=$CUSTOMER_ID&limit=100"

# Subscription (if recurring)
curl -s -u "$STRIPE_SECRET_KEY:" "https://api.stripe.com/v1/subscriptions/$SUB_ID"
```

Prior undisputed payments on the same card are useful corroboration for `fraudulent`
claims. Always count them, but do not treat them as proof by themselves.

### 3. Look up the customer in your app database

Adapt these queries to your schema. A useful evidence shape:

```sql
-- User profile and self-reported cancel reason
SELECT id, email, created_at, plan_tier, stripe_customer_id,
       cancel_reason, cancelled_at, delete_reason
FROM users WHERE email ILIKE :email;

-- Login activity (timestamps + country + device)
SELECT created_at, country_code, device
FROM user_activity WHERE user_id = :uid ORDER BY created_at;

-- Things the customer created/used in your product
SELECT name, type, created_at, updated_at
FROM projects WHERE user_id = :uid AND deleted = false ORDER BY created_at;

-- Checkout / payment-related actions (proves intent)
SELECT timestamp, endpoint, payload FROM action_logs
WHERE user_id = :uid
  AND endpoint ~* '(subscribe|checkout|stripe|upgrade|pay)'
ORDER BY timestamp DESC;
```

For `product_not_received` claims, check the user's self-reported `cancel_reason`. If they
cancelled citing "Poor user experience" or anything admitting use, that field directly
contradicts the claim. Quote it verbatim, but do not infer a win rate from one fact.

### 4. Download supporting documents

```bash
FOLDER="$EVIDENCE_DIR/$(echo $CUSTOMER_NAME | tr '[:upper:] ' '[:lower:]-')-$(date +%Y-%m)"
mkdir -p "$FOLDER"

# Invoice PDFs (URLs come from the Stripe invoice objects)
curl -sL "$INVOICE_PDF_URL" -o "$FOLDER/invoice.pdf"
```

### 5. Capture your terms / cancellation policy as a PDF

Using Playwright (Node):

```bash
node -e "
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  await page.goto(process.env.TERMS_URL, { waitUntil: 'networkidle' });
  await page.pdf({ path: process.argv[1], format: 'A4', printBackground: true });
  await browser.close();
})();
" "$FOLDER/cancellation_policy.pdf"
```

### 6. Generate the activity-log PDF

Build a concise, reviewable HTML activity log, then convert it to PDF with WeasyPrint:

```python
from weasyprint import HTML
HTML('activity_log.html').write_pdf('activity_log.pdf')
```

**HTML must include `<meta charset="UTF-8">`** to avoid mangled characters in customer names/addresses.

A reviewable layout:

1. **Summary grid** — Customer / Email / Internal user ID / Stripe customer ID / Account created / Plan / Subscription start / Cancellation timestamp (with delta from signup) / Self-reported cancel reason / Credits or units consumed / Purchase IP / Billing address / Payment method (last4, brand) / Stripe risk assessment / Referral source / Payment trigger
2. **Payment History table** — every invoice with date, amount, status. **Highlight the disputed row** in red. Add a column "Disputed?" with explicit Yes/No.
3. **Checkout Attempts table** — proves deliberate purchase intent (defeats `fraudulent` by extension)
4. **Items Created / Used table** — names, types, timestamps. Concrete usage > adjectives.
5. **Login Activity Log** — every session: timestamp, country, device. Consistency = same cardholder.
6. **Timeline Summary** — single chronological narrative ending with "and then on $DATE the dispute was filed."
7. **Conclusion paragraph** — quote the user's own `cancel_reason` against the stated dispute reason, if they contradict.

Prefer concrete numbers over adjectives. "29 login sessions, 3 named projects, 29,960
credits consumed" is more useful than "used extensively."

### 7. Show everything to the user before submitting

```bash
open "$FOLDER"
```

Display the rebuttal text, the evidence files, and your win-probability assessment. **Wait for explicit user approval.**

### 8. Upload evidence files to Stripe

**Files go to `files.stripe.com`, NOT `api.stripe.com`** — different host:

```bash
curl -s -u "$STRIPE_SECRET_KEY:" \
  -F "purpose=dispute_evidence" \
  -F "file=@$FOLDER/activity_log.pdf" \
  https://files.stripe.com/v1/files
```

Returns `{"id": "file_xxx", ...}`. Capture the `id` — that's what you reference in evidence fields.

**One file_id per dispute.** Stripe rejects with `400 "That file is already attached to something else"` if you try to reuse a `file_id` across disputes (especially for `service_documentation`). When fighting N disputes for the same customer, upload N copies of every shared PDF — same content, fresh `file_id` each time.

### 9. Submit evidence (one shot — `submit=true` is final)

```bash
curl -s -u "$STRIPE_SECRET_KEY:" \
  -X POST "https://api.stripe.com/v1/disputes/$DISPUTE_ID" \
  -d "evidence[uncategorized_text]=$REBUTTAL_TEXT" \
  -d "evidence[uncategorized_file]=$ACTIVITY_LOG_FILE_ID" \
  -d "evidence[receipt]=$INVOICE_FILE_ID" \
  -d "evidence[cancellation_policy]=$TERMS_FILE_ID" \
  -d "evidence[cancellation_policy_disclosure]=$CANCEL_DISCLOSURE_TEXT" \
  -d "evidence[refund_policy]=$TERMS_FILE_ID" \
  -d "evidence[refund_policy_disclosure]=$REFUND_DISCLOSURE_TEXT" \
  -d "evidence[cancellation_rebuttal]=$CANCEL_REBUTTAL_TEXT" \
  -d "evidence[access_activity_log]=$ACCESS_LOG_SUMMARY" \
  -d "evidence[service_date]=$SERVICE_START_DATE" \
  -d "evidence[product_description]=$PRODUCT_DESCRIPTION" \
  -d "evidence[customer_email_address]=$CUSTOMER_EMAIL" \
  -d "evidence[customer_name]=$CUSTOMER_NAME" \
  -d "evidence[customer_purchase_ip]=$PURCHASE_IP" \
  -d "evidence[billing_address]=$BILLING_ADDRESS" \
  -d "submit=true" \
  "https://api.stripe.com/v1/disputes/$DISPUTE_ID"
```

Verify the response:
- `status` should be `under_review`
- `evidence_details.has_evidence` should be `true`
- `evidence_details.submission_count` should be `1`

## Evidence Strategy by Dispute Reason

### `fraudulent`
Goal: prove the cardholder made the purchase.
- Prior undisputed payments on the same card (strongest)
- OAuth login (Google/Apple) = identity-verified signup
- Consistent IP / country / device across sessions
- Multiple checkout attempts before purchase = real person deliberating
- Stripe's own risk assessment was `normal`
- Subscription still active and not cancelled

### `product_not_received`
Goal: prove delivery + use.
- Login activity log
- Items created / actions taken inside the product
- **The customer's own self-reported cancel reason**, if they cancelled — quoted verbatim against the dispute claim
- Receipt and welcome email

### `product_unacceptable`
Goal: show the product matched its description and the customer used it.
- Same as `product_not_received` PLUS your terms-of-service language about quality / refund policy
- Highlight that customer never opened a support ticket

### `subscription_canceled`
Goal: prove the customer never cancelled (or cancelled after the renewal).
- Subscription object showing `cancel_at_period_end=false` at the renewal date
- All login/use activity from after the renewal date
- Terms language stating annual renewals require explicit cancellation

## Rebuttal Templates

### `uncategorized_text`
> [Customer name] created a [Product name] account on [date] via [auth method] and subscribed to [plan] ($[amount]/[interval]) using the same [card brand]. The first [N] payment(s) were never disputed. The customer actively used the service: [N] login sessions from [country] on [device], [N] items created ([list]), and [N] [units] consumed. The disputed charge is the [renewal/initial] payment on [date]. The subscription was [status] and remains [active/cancelled]. The customer never contacted support to cancel or request a refund. Our cancellation and refund policies are published at [TERMS_URL]. This is not a fraudulent transaction — it is a legitimate purchase from the cardholder who [made/has made] [N] other undisputed payments on this account.

### `cancellation_policy_disclosure`
> Our cancellation policy is disclosed at [TERMS_URL]. Subscribers may cancel at any time and retain access through the end of their billing cycle. This customer never cancelled.

### `refund_policy_disclosure`
> Our refund policy is disclosed at [TERMS_URL]. We offer a [N]-day money-back guarantee. The customer did not request a refund within that window, nor at any time.

## Important Notes

- File uploads go to `files.stripe.com`, NOT `api.stripe.com`
- One submission per dispute. `submit=true` is final
- Evidence deadline is `evidence_details.due_by` (unix timestamp). After that you can no longer submit
- Database queries must be READ-ONLY — restrict the connection's role if possible
- Never include other customers' data in the activity log PDF
- Save every evidence package to disk in case you need to reference it for future disputes from the same customer

## High-value contradiction pattern

> Customer signs up, uses product briefly, cancels within hours citing "Poor user experience" in your in-app cancel form, then files a chargeback days later claiming "product not received."

The cancel form's reason directly contradicts the chargeback claim. Quote it word-for-word
in the rebuttal, while still applying the fee and historical-outcome decision gate.

Always check `users.cancel_reason` (or your equivalent) FIRST when the dispute reason is `product_not_received` or `product_unacceptable`.
