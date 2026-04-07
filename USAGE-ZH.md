# OpenClaudia 使用指南

一份实用指南，帮助你在 Claude Code 中充分利用 OpenClaudia 的 62+ 营销技能。

---

## 目录

- [前提条件](#前提条件)
- [安装](#安装)
- [第一个技能](#第一个技能)
- [技能分类与工作流](#技能分类与工作流)
  - [SEO 工作流](#seo-工作流)
  - [内容营销工作流](#内容营销工作流)
  - [社交媒体工作流](#社交媒体工作流)
  - [邮件营销工作流](#邮件营销工作流)
  - [广告与转化工作流](#广告与转化工作流)
  - [数据分析工作流](#数据分析工作流)
  - [策略与规划工作流](#策略与规划工作流)
- [配置 API 密钥](#配置-api-密钥)
- [组合使用技能](#组合使用技能)
- [项目级与全局技能](#项目级与全局技能)
- [技巧与最佳实践](#技巧与最佳实践)
- [常见问题排查](#常见问题排查)

---

## 前提条件

1. 已安装并认证 **Claude Code**。[安装指南](https://docs.anthropic.com/en/docs/claude-code)
2. 终端（macOS、Linux 或 Windows WSL）
3. Node.js 18+（用于安装 CLI）

## 安装

### 安装所有技能（推荐首次用户）

```bash
npx openclaudia install --all
```

这会将所有 62+ 技能文件复制到 `~/.claude/skills/`，使其在每个 Claude Code 会话中作为斜杠命令可用。

### 安装特定技能

```bash
# 只安装你需要的
npx openclaudia install seo-audit write-blog reddit-marketing

# 列出可用技能
npx openclaudia list
```

### 手动安装

```bash
# 克隆仓库
git clone https://github.com/OpenClaudia/openclaudia-skills.git

# 复制技能到全局目录
cp -r openclaudia-skills/skills/seo-audit ~/.claude/skills/

# 或复制到特定项目
cp -r openclaudia-skills/skills/seo-audit ./your-project/.claude/skills/
```

### 验证安装

打开 Claude Code 并输入 `/` — 你应该能看到已安装的技能列在可用斜杠命令中。

---

## 第一个技能

让我们运行一个 SEO 审计来看看技能如何工作：

```
$ claude

> /seo-audit https://yoursite.com
```

Claude 会：
1. 抓取你网站的关键页面
2. 检查 meta 标签、标题层级、Schema 结构化数据和页面速度
3. 分析关键词优化和内部链接
4. 生成详细报告和可操作的修复建议
5. 将报告保存为项目中的文件

就是这么简单。每个技能都遵循这个模式：**用斜杠命令调用，提供输入，获取输出。**

---

## 技能分类与工作流

### SEO 工作流

从审计开始，然后系统性地修复问题。

```
# 第1步：审计你的网站
> /seo-audit https://yoursite.com

# 第2步：研究你所在领域的关键词
> /keyword-research "AI 表单构建器"

# 第3步：分析竞争对手排名情况
> /serp-analyzer "最佳 AI 表单构建器 2026"

# 第4步：审计你的外链概况
> /backlink-audit https://yoursite.com

# 第5步：为关键页面生成 Schema 结构化数据
> /schema-markup https://yoursite.com/pricing

# 第6步：批量创建 SEO 页面
> /programmatic-seo "为50个美国城市创建本地着陆页"
```

**使用的技能：** `seo-audit` → `keyword-research` → `serp-analyzer` → `backlink-audit` → `schema-markup` → `programmatic-seo`

### 内容营销工作流

规划内容策略，然后生产和分发。

```
# 第1步：构建内容策略
> /content-strategy "B2B SaaS 项目管理工具"

# 第2步：找出与竞争对手的内容差距
> /content-gap-analysis competitor1.com competitor2.com

# 第3步：为作者创建内容简报
> /seo-content-brief "远程团队最佳项目管理工具"

# 第4步：撰写博客文章
> /write-blog "2026年远程团队最佳项目管理工具"

# 第5步：润色文案
> /copy-editing ./blog-post.md

# 第6步：将内容改编为社交媒体内容
> /content-repurposing ./blog-post.md
```

**使用的技能：** `content-strategy` → `content-gap-analysis` → `seo-content-brief` → `write-blog` → `copy-editing` → `content-repurposing`

### 社交媒体工作流

创建并分发跨平台内容。

```
# 第1步：规划内容日历
> /content-calendar "SaaS 产品发布，4周，重点 LinkedIn 和 Reddit"

# 第2步：写一篇 LinkedIn 思想领袖文章
> /linkedin-content "扩展到10万用户的经验教训"

# 第3步：创建 Reddit 营销活动
> /reddit-marketing "在相关子版块分享我们的 AI 表单构建器"

# 第4步：写一个 X 上的热门话题帖
> /thread-writer "我们如何在12个月内从0增长到10万月访问量"

# 第5步：交叉发布到 Bluesky
> /bluesky "宣布我们的新功能发布"

# 第6步：发送到 Discord 和 Slack
> /discord-bot "新功能：AI 驱动的表单验证"
> /slack-bot "每周营销更新：流量增长20%"
```

**使用的技能：** `content-calendar` → `linkedin-content` → `reddit-marketing` → `thread-writer` → `bluesky` → `discord-bot` / `slack-bot`

### 邮件营销工作流

构建能转化的邮件序列。

```
# 第1步：创建滴灌营销活动
> /email-sequence --type product-launch

# 第2步：A/B 测试邮件标题
> /email-subject-lines "AI 表单构建器产品发布公告"
```

**使用的技能：** `email-sequence` → `email-subject-lines`

**注意：** 需要 `RESEND_API_KEY` 才能实际发送邮件。没有密钥时，技能会生成邮件文案供你手动发送。

### 广告与转化工作流

优化广告支出和着陆页。

```
# 第1步：创建 Google Ads 广告系列
> /google-ads "AI 表单构建器，目标：中小企业主，预算：$2000/月"

# 第2步：创建 Facebook/Meta 广告
> /facebook-ads "向网站访客展示功能演示视频再营销"

# 第3步：创建 LinkedIn B2B 广告
> /linkedin-ads "定向 50-500人公司的工程VP"

# 第4步：优化着陆页转化率
> /page-cro https://yoursite.com/pricing

# 第5步：设计 A/B 测试
> /ab-test-setup "测试定价页年付与月付切换"

# 第6步：分析视频广告效果
> /video-ad-analysis "分析我们前3个 YouTube 前贴片广告"
```

**使用的技能：** `google-ads` → `facebook-ads` → `linkedin-ads` → `page-cro` → `ab-test-setup` → `video-ad-analysis`

### 数据分析工作流

从你的工具中提取数据并生成洞察。

```
# 第1步：查看 Google Analytics
> /google-analytics "显示过去90天的流量趋势"

# 第2步：分析 Search Console 表现
> /search-console "上个月的热门查询和页面"

# 第3步：运行 SemRush 竞争分析
> /semrush-research "比较我们的域名与 competitor.com"

# 第4步：拉取 Google Ads 效果
> /google-ads-report "2026年3月广告系列表现"

# 第5步：查看 YouTube 频道数据
> /youtube-analytics "过去30天的视频表现"

# 第6步：监控品牌提及
> /brand-monitor "追踪我们品牌在网络上的提及"
```

**使用的技能：** `google-analytics` → `search-console` → `semrush-research` → `google-ads-report` → `youtube-analytics` → `brand-monitor`

### 策略与规划工作流

从零开始规划营销策略。

```
# 第1步：定义理想客户画像
> /icp-builder "面向企业HR团队的B2B SaaS"

# 第2步：分析竞争对手
> /competitor-analysis competitor.com

# 第3步：制定增长策略
> /growth-strategy "6个月内将有机流量翻倍"

# 第4步：规划产品发布
> /launch-strategy "Q2发布平台v2.0"

# 第5步：优化定价
> /pricing-strategy https://yoursite.com/pricing

# 第6步：获取创意营销方案
> /marketing-ideas "我们是一家开发者工具创业公司，月营销预算$5K"
```

**使用的技能：** `icp-builder` → `competitor-analysis` → `growth-strategy` → `launch-strategy` → `pricing-strategy` → `marketing-ideas`

---

## 配置 API 密钥

技能无需 API 密钥即可工作（使用网络搜索和免费数据），但有了 API 访问会更强大。

在 `~/.claude/.env.global` 或项目的 `.env` 中创建配置：

```bash
# 最有价值的密钥（优先配置）：
RESEND_API_KEY=your_key        # 启用实际邮件发送
SEMRUSH_API_KEY=your_key       # 丰富的 SEO 和关键词数据
UNSPLASH_CLIENT_ID=your_key    # 博客文章的配图
```

完整 API 密钥列表请参见 [README](README.md#api-configuration)。

**API 配置优先级：**
1. **Resend** — 如果你想直接发送邮件
2. **SemRush 或 Ahrefs** — 获取真实的关键词和外链数据
3. **Google OAuth** — 用于 Analytics、Search Console 和 Ads 报告
4. **Unsplash** — 博客文章的免费图库图片
5. **其他** — 根据具体技能需要添加

---

## 组合使用技能

OpenClaudia 的真正威力在于串联多个技能。你可以在一次对话中让 Claude 运行多个技能：

### 示例：完整内容管线

```
> 研究"AI表单构建器"的关键词，为最佳关键词写一篇博客文章，
> 然后创建一篇 LinkedIn 帖子和一条 Reddit 评论来推广它。
```

Claude 会自动按序使用 `keyword-research` → `write-blog` → `linkedin-content` → `reddit-marketing`。

### 示例：竞争对手全面分析

```
> 对 competitor.com 进行全面竞争分析 — SEO审计、内容差距分析、
> 外链比较。然后制定超越他们的内容策略。
```

Claude 串联：`competitor-analysis` → `seo-audit` → `content-gap-analysis` → `backlink-audit` → `content-strategy`

### 示例：产品发布活动

```
> 我们下周要发布新功能。创建发布策略，写公告博客文章、
> 邮件序列、社交媒体帖子和 Discord 公告。
```

Claude 使用：`launch-strategy` → `write-blog` → `email-sequence` → `social-content` → `discord-bot`

---

## 项目级与全局技能

### 全局技能（`~/.claude/skills/`）

在每个 Claude Code 会话中可用，跨所有项目。这是 `npx openclaudia install` 默认安装的位置。

最适合：你在任何地方都会用到的通用营销技能。

### 项目级技能（`.claude/skills/`）

仅在该项目的 Claude Code 会话中可用。当你想为特定项目定制技能时使用。

```bash
# 复制并为项目定制技能
cp -r ~/.claude/skills/write-blog .claude/skills/write-blog

# 编辑 SKILL.md 添加项目特定指令
# 例如："始终将产品名称写为 'FormAI'"
```

项目级技能会覆盖同名的全局技能。

---

## 技巧与最佳实践

### 1. 提示词要具体

```
# 模糊 — 技能需要猜测
> /write-blog "AI 工具"

# 具体 — 更好的输出
> /write-blog "10款AI表单构建器对比：功能、定价及2026年选择指南"
> --target-keyword "最佳AI表单构建器" --word-count 2500
```

### 2. 在项目中提供上下文

如果你的项目有 `CLAUDE.md` 文件包含品牌指南、语调风格或产品详情，技能会自动使用这些上下文。

### 3. 审阅并迭代

技能生成的是初稿。让 Claude 进一步优化：

```
> /write-blog "主题"
> 让开头更吸引人，并添加对比表格
> 添加到我们 /pricing 和 /features 页面的内部链接
```

### 4. 使用自然语言，不仅仅是斜杠命令

你不必使用斜杠命令。Claude 会识别何时相关技能适用：

```
> 写一篇关于AI表单构建器的博客文章
# Claude 自动使用 write-blog 技能

> 审计我网站的SEO
# Claude 自动使用 seo-audit 技能
```

### 5. 串联技能执行综合活动

与其逐一运行技能，不如描述你的目标，让 Claude 协调执行：

```
> 我需要为下月的产品发布制定完整的内容营销活动。
> 从竞争分析开始，然后创建内容日历，撰写关键内容，
> 并设置邮件滴灌营销。
```

---

## 常见问题排查

### 技能没有显示为斜杠命令

```bash
# 重新安装
npx openclaudia install --all

# 检查文件是否在正确位置
ls ~/.claude/skills/
```

### API 调用失败

```bash
# 检查环境变量文件
cat ~/.claude/.env.global

# 确保密钥已设置（非空）
echo $RESEND_API_KEY
```

### 技能输出不符合预期

- 在提示词中添加更多上下文
- 检查技能是否需要 API 密钥来获取更丰富的数据
- 如果技能指令需要改进，请提交 [Issue](https://github.com/OpenClaudia/openclaudia-skills/issues)

### 技能与项目级指令冲突

项目级 `.claude/skills/` 优先于全局 `~/.claude/skills/`。如果技能在某个项目中表现不同，请检查是否有项目级覆盖。

---

## 接下来做什么？

- 浏览[完整技能列表](README.md#skills)查看所有可用技能
- 如果缺少你需要的营销工作流，[贡献一个技能](CONTRIBUTING.md)
- 在 [GitHub](https://github.com/OpenClaudia/openclaudia-skills) 上给仓库加星以保持更新
- 访问 [openclaudia.com](https://openclaudia.com) 获取教程和资讯

---

<p align="center">
  <sub>有问题？<a href="https://github.com/OpenClaudia/openclaudia-skills/issues">提交 Issue</a> 或联系 <a href="https://x.com/Claudia1569302">@Claudia1569302</a></sub>
</p>
