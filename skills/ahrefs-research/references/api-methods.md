# API Reference

<!-- AUTO-GENERATED -- DO NOT EDIT -->



<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=1 -->

- [API Reference](#api-reference)
  - [Batch Analysis](#batch-analysis)
    - [`batch_analysis()`](#batch_analysis)
  - [Brand Radar](#brand-radar)
    - [`brand_radar_ai_responses()`](#brand_radar_ai_responses)
    - [`brand_radar_cited_domains()`](#brand_radar_cited_domains)
    - [`brand_radar_cited_pages()`](#brand_radar_cited_pages)
    - [`brand_radar_impressions_history()`](#brand_radar_impressions_history)
    - [`brand_radar_impressions_overview()`](#brand_radar_impressions_overview)
    - [`brand_radar_mentions_history()`](#brand_radar_mentions_history)
    - [`brand_radar_mentions_overview()`](#brand_radar_mentions_overview)
    - [`brand_radar_sov_history()`](#brand_radar_sov_history)
    - [`brand_radar_sov_overview()`](#brand_radar_sov_overview)
  - [Keywords Explorer](#keywords-explorer)
    - [`keywords_explorer_matching_terms()`](#keywords_explorer_matching_terms)
    - [`keywords_explorer_overview()`](#keywords_explorer_overview)
    - [`keywords_explorer_related_terms()`](#keywords_explorer_related_terms)
    - [`keywords_explorer_search_suggestions()`](#keywords_explorer_search_suggestions)
    - [`keywords_explorer_volume_by_country()`](#keywords_explorer_volume_by_country)
    - [`keywords_explorer_volume_history()`](#keywords_explorer_volume_history)
  - [Rank Tracker](#rank-tracker)
    - [`rank_tracker_competitors_overview()`](#rank_tracker_competitors_overview)
    - [`rank_tracker_competitors_pages()`](#rank_tracker_competitors_pages)
    - [`rank_tracker_competitors_stats()`](#rank_tracker_competitors_stats)
    - [`rank_tracker_overview()`](#rank_tracker_overview)
    - [`rank_tracker_serp_overview()`](#rank_tracker_serp_overview)
  - [Serp Overview](#serp-overview)
    - [`serp_overview()`](#serp_overview)
  - [Site Audit](#site-audit)
    - [`site_audit_issues()`](#site_audit_issues)
    - [`site_audit_page_content()`](#site_audit_page_content)
    - [`site_audit_page_explorer()`](#site_audit_page_explorer)
    - [`site_audit_projects()`](#site_audit_projects)
  - [Site Explorer](#site-explorer)
    - [`site_explorer_all_backlinks()`](#site_explorer_all_backlinks)
    - [`site_explorer_anchors()`](#site_explorer_anchors)
    - [`site_explorer_backlinks_stats()`](#site_explorer_backlinks_stats)
    - [`site_explorer_best_by_external_links()`](#site_explorer_best_by_external_links)
    - [`site_explorer_best_by_internal_links()`](#site_explorer_best_by_internal_links)
    - [`site_explorer_broken_backlinks()`](#site_explorer_broken_backlinks)
    - [`site_explorer_domain_rating()`](#site_explorer_domain_rating)
    - [`site_explorer_domain_rating_history()`](#site_explorer_domain_rating_history)
    - [`site_explorer_keywords_history()`](#site_explorer_keywords_history)
    - [`site_explorer_linked_anchors_external()`](#site_explorer_linked_anchors_external)
    - [`site_explorer_linked_anchors_internal()`](#site_explorer_linked_anchors_internal)
    - [`site_explorer_linkeddomains()`](#site_explorer_linkeddomains)
    - [`site_explorer_metrics()`](#site_explorer_metrics)
    - [`site_explorer_metrics_by_country()`](#site_explorer_metrics_by_country)
    - [`site_explorer_metrics_history()`](#site_explorer_metrics_history)
    - [`site_explorer_organic_competitors()`](#site_explorer_organic_competitors)
    - [`site_explorer_organic_keywords()`](#site_explorer_organic_keywords)
    - [`site_explorer_outlinks_stats()`](#site_explorer_outlinks_stats)
    - [`site_explorer_pages_by_traffic()`](#site_explorer_pages_by_traffic)
    - [`site_explorer_pages_history()`](#site_explorer_pages_history)
    - [`site_explorer_paid_pages()`](#site_explorer_paid_pages)
    - [`site_explorer_refdomains()`](#site_explorer_refdomains)
    - [`site_explorer_refdomains_history()`](#site_explorer_refdomains_history)
    - [`site_explorer_top_pages()`](#site_explorer_top_pages)
    - [`site_explorer_total_search_volume_history()`](#site_explorer_total_search_volume_history)
    - [`site_explorer_url_rating_history()`](#site_explorer_url_rating_history)

<!-- mdformat-toc end -->

All methods below are available on both `AhrefsClient` (sync) and
`AsyncAhrefsClient` (async). The async client uses the same method
names — just `await` the call.

For filter expression syntax (`where` parameter), see [Filter Syntax](filter-syntax.md).

______________________________________________________________________

## Batch Analysis

### `batch_analysis()`

Batch Analysis.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `select` | `list[str]` | Yes | A list of columns to return. See response schema for valid column identifiers. |
| `order_by` | `str` | No | |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |
| `targets` | `list[BatchAnalysisTarget]` | Yes | A list of targets to do batch analysis. |

**Returns:** `list[BatchAnalysisData]`

<details>
<summary>35 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `ahrefs_rank` | `int \| None` | The strength of your target's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |
| `backlinks` | `int \| None` | The total number of links from other websites pointing to your target. |
| `backlinks_dofollow` | `int \| None` | Links to your target that do not contain a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute. These links are also called “dofollow”. |
| `backlinks_internal` | `int \| None` | The total number of internal links pointing to the target's pages. |
| `backlinks_nofollow` | `int \| None` | Links to your target that contain a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute. |
| `backlinks_redirect` | `int \| None` | Links pointing to your target via a redirect. |
| `domain_rating` | `float \| None` | The strength of your target's backlink profile compared to the other websites in our database on a 100-point logarithmic scale. |
| `index` | `int` | Target index number. |
| `ip` | `str \| None` | The IP address of the target. |
| `linked_domains` | `int \| None` | The number of unique domains linked from your target. |
| `linked_domains_dofollow` | `int \| None` | The number of unique domains linked from your target with followed links. |
| `mode` | `str` | The target mode used for the analysis. Depending on the selected mode (Exact URL, Path, Domain, Subdomains), different parts of the website will be analyzed. |
| `org_cost` | `int \| None` | (10 units) The estimated value of your target’s monthly organic search traffic. |
| `org_keywords` | `int \| None` | The total number of keywords that your target ranks for in the top 100 organic search results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword. |
| `org_keywords_11_20` | `int \| None` | The total number of unique keywords for which your target's top organic ranking position is within the 11th to 20th results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword. |
| `org_keywords_1_3` | `int \| None` | The total number of unique keywords for which your target's top organic ranking position is within the top 3 results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword. |
| `org_keywords_21_50` | `int \| None` | The total number of unique keywords for which your target's top organic ranking position is within the 21st to 50th results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword. |
| `org_keywords_4_10` | `int \| None` | The total number of unique keywords for which your target's top organic ranking position is within the 4th to 10th results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword. |
| `org_keywords_51_plus` | `int \| None` | The total number of unique keywords for which your target's top organic ranking position is the 51st result or higher. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword. |
| `org_traffic` | `int \| None` | (10 units) The estimated number of monthly visits that your target gets from organic search. |
| `org_traffic_top_by_country` | `list[list[Any] \| None]` | (10 units) Top countries by traffic with corresponding traffic values. (Currently only a single element is being returned with the country with the most traffic.) |
| `outgoing_links` | `int \| None` | The total number of links from your target to other domains. |
| `outgoing_links_dofollow` | `int \| None` | The total number of followed links from your target to other domains. |
| `paid_ads` | `int \| None` | The total number of unique ads of a target website or URL in paid search results. |
| `paid_cost` | `int \| None` | (10 units) The estimated cost of your target’s monthly paid search traffic. |
| `paid_keywords` | `int \| None` | The total number of keywords that your target ranks for in paid search results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword. |
| `paid_traffic` | `int \| None` | (10 units) The estimated number of monthly visits that your target gets from paid search. |
| `protocol` | `str` | The protocol of the target. Possible values: `both`, `http`, `https`. |
| `refdomains` | `int \| None` | (5 units) The total number of unique domains linking to your target. |
| `refdomains_dofollow` | `int \| None` | (5 units) The number of unique domains with links to your target that do not contain a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute. These links are also called “dofollow”. |
| `refdomains_nofollow` | `int \| None` | (5 units) The number of unique domains that only have links to your target containing a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute. |
| `refips` | `int \| None` | The number of unique IP addresses with at least one domain pointing to your target. Several domains can share one IP address. |
| `refips_subnets` | `int \| None` | The number of c-class IP networks (AAA.BBB.CCC.DDD) with at least one link to your target. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the subnet. |
| `url` | `str` | The URL of the analyzed target. |
| `url_rating` | `float \| None` | URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. If you analyze a domain, the homepage's UR is shown. |

</details>

______________________________________________________________________

## Brand Radar

### `brand_radar_ai_responses()`

AI Responses.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `date` | `DateStr` | No | The date to search for in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `order_by` | `OrderByEnum` | No | A column to order the results by. |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (brand, competitors, market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `competitors` | `str` | No | A comma-separated list of competitors of your brands. |
| `brand` | `str` | No | A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarAiResponsesData]`

| Field | Type | Description |
|-------|------|-------------|
| `country` | `str` | The country of the question. |
| `links` | `list[dict[str, Any] \| None]` | (10 units) The links used for the response. |
| `question` | `str` | The question asked by the user. |
| `response` | `str` | (10 units) The response from the model. |
| `volume` | `int` | (10 units) Estimated monthly searches. This is based on our estimates for Google, combining the search volumes of related keywords where this question appears in People Also Ask section. |

### `brand_radar_cited_domains()`

Cited Domains.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `limit` | `int` | No | The number of results to return. |
| `date` | `DateStr` | No | The date to search for in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (brand, competitors, market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `competitors` | `str` | No | A comma-separated list of competitors of your brands. |
| `brand` | `str` | No | A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarCitedDomainsData]`

| Field | Type | Description |
|-------|------|-------------|
| `domain` | `str` | The cited domain name. |
| `mentions` | `list[dict[str, Any] \| None]` | Deprecated on 2026-02-10. |
| `pages` | `int` | The number of unique pages from the domain that were cited in the responses. |
| `responses` | `int` | The number of responses that cited the domain. |
| `volume` | `int` | (10 units) Estimated monthly searches that cited the domain. Based on the average monthly number of searches for the query on Google over the latest known 12 months of data. |

### `brand_radar_cited_pages()`

Cited Pages.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `limit` | `int` | No | The number of results to return. |
| `date` | `DateStr` | No | The date to search for in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (brand, competitors, market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `competitors` | `str` | No | A comma-separated list of competitors of your brands. |
| `brand` | `str` | No | A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarCitedPagesData]`

| Field | Type | Description |
|-------|------|-------------|
| `mentions` | `list[dict[str, Any] \| None]` | Deprecated on 2026-02-10. |
| `responses` | `int` | The number of responses that cited the page. |
| `url` | `str` | The URL of the cited page. |
| `volume` | `int` | (10 units) Estimated monthly searches that cited the page. Based on the average monthly number of searches for the query on Google over the latest known 12 months of data. |

### `brand_radar_impressions_history()`

Overview history - Impressions.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `brand` | `str` | Yes | The brand to search for. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarImpressionsHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `impressions` | `int` | Estimated impressions from responses mentioning the brand. |

### `brand_radar_impressions_overview()`

Overview - Impressions.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (brand, competitors, market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `competitors` | `str` | No | A comma-separated list of competitors of your brands. |
| `brand` | `str` | No | A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarImpressionsOverviewData]`

| Field | Type | Description |
|-------|------|-------------|
| `brand` | `str` | Brand name (either your brand or a competitor provided in the request). |
| `no_tracked_brands` | `int` | Estimated impressions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified). |
| `only_competitors_brands` | `int` | Estimated impressions from responses mentioning only competitor brands. |
| `only_target_brand` | `int` | Estimated impressions from responses mentioning only your brand. |
| `target_and_competitors_brands` | `int` | Estimated impressions from responses mentioning both your and competitor brands. |
| `total` | `int` | Total estimated impressions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`). |

### `brand_radar_mentions_history()`

Overview history - Mentions.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `brand` | `str` | Yes | The brand to search for. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarMentionsHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `mentions` | `int` | Estimated mentions from responses mentioning the brand. |

### `brand_radar_mentions_overview()`

Overview - Mentions.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (brand, competitors, market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `competitors` | `str` | No | A comma-separated list of competitors of your brands. |
| `brand` | `str` | No | A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarMentionsOverviewData]`

| Field | Type | Description |
|-------|------|-------------|
| `brand` | `str` | Brand name (either your brand or a competitor provided in the request). |
| `no_tracked_brands` | `int` | Estimated mentions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified). |
| `only_competitors_brands` | `int` | Estimated mentions from responses mentioning only competitor brands. |
| `only_target_brand` | `int` | Estimated mentions from responses mentioning only your brand. |
| `target_and_competitors_brands` | `int` | Estimated mentions from responses mentioning both your and competitor brands. |
| `total` | `int` | Total estimated mentions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`). |

### `brand_radar_sov_history()`

Overview history - Share of Voice.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (brand, competitors, market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `competitors` | `str` | No | A comma-separated list of competitors of your brands. |
| `brand` | `str` | No | A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarSovHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `share_of_voice` | `list[dict[str, Any] \| None]` | (1 unit per brand) Estimated share of voice for the brand. |

### `brand_radar_sov_overview()`

Overview - Share of Voice.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `report_id` | `str` | No | The ID of the report to use. If one is given, other parameters are taken from the report (brand, competitors, market, country, filters). If country or filters are provided, they override the ones in the report. You can find it in the URL of your Brand Radar report in Ahrefs: `https://app.ahrefs.com/brand-radar/reports/#report_id#/...` |
| `prompts` | `PromptsEnum` | No | The type of prompts to use. If not specified, both will be used. Custom prompts require a report_id to be provided. |
| `data_source` | `DataSourceEnum` | Yes | The chatbot model to use. |
| `market` | `str` | No | A comma-separated list of the niche markets of your brands. |
| `competitors` | `str` | No | A comma-separated list of competitors of your brands. |
| `brand` | `str` | No | A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty. |

<details>
<summary>Filterable fields (7 fields)</summary>

- `cited_domain` (domain)
- `cited_domain_subdomains` (string)
- `cited_url_exact` (string)
- `cited_url_prefix` (string)
- `question` (string)
- `response` (string)
- `topic` (string)

</details>

**Returns:** `list[BrandRadarSovOverviewData]`

| Field | Type | Description |
|-------|------|-------------|
| `brand` | `str` | Brand name (either your brand or a competitor provided in the request). |
| `share_of_voice` | `float` | Estimated share of voice for your brand. |

______________________________________________________________________

## Keywords Explorer

### `keywords_explorer_matching_terms()`

Matching terms.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `search_engine` | `SearchEngineEnum` | No | [Deprecated on 5 Aug 2024]. |
| `keywords` | `str` | No | A comma-separated list of keywords to show metrics for. |
| `keyword_list_id` | `int` | No | The id of an existing keyword list to show metrics for. |
| `match_mode` | `MatchModeEnum` | No | Keyword ideas contain the words from your query in any order (terms mode) or in the exact order they are written (phrase mode). |
| `terms` | `TermsEnum` | No | All keywords ideas or keywords ideas phrased as questions. |

<details>
<summary>Filterable fields (17 fields)</summary>

- `cpc` (integer)
- `cps` (float)
- `difficulty` (integer)
- `first_seen` (datetime)
- `global_volume` (integer)
- `intents` (object)
- `keyword` (string)
- `parent_topic` (string)
- `serp_domain_rating_top10_min` (float)
- `serp_domain_rating_top5_min` (float)
- `serp_features` (array(string))
- `serp_last_update` (datetime)
- `traffic_potential` (integer)
- `volume` (integer)
- `volume_desktop_pct` (float)
- `volume_mobile_pct` (float)
- `word_count` (integer)

</details>

**Returns:** `list[KeywordsExplorerMatchingTermsData]`

| Field | Type | Description |
|-------|------|-------------|
| `cpc` | `int \| None` | Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents. |
| `cps` | `float \| None` | Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country. |
| `difficulty` | `int \| None` | (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale. |
| `first_seen` | `str \| None` | The date when we first checked search engine results for a keyword. |
| `global_volume` | `int \| None` | (10 units) How many times per month, on average, people search for the target keyword across all countries in our database. |
| `intents` | `dict[str, Any] \| None` | (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`. |
| `keyword` | `str` | |
| `parent_topic` | `str \| None` | Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page. |
| `serp_features` | `list[SerpFeaturesItemEnum \| None]` | The enriched results on a search engine results page (SERP) that are not traditional organic results. |
| `serp_last_update` | `str \| None` | The date when we last checked search engine results for a keyword. |
| `traffic_potential` | `int \| None` | (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for. |
| `volume` | `int \| None` | (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data. |
| `volume_desktop_pct` | `float \| None` | The percentage of searches for a keyword performed on desktop devices. |
| `volume_mobile_pct` | `float \| None` | The percentage of searches for a keyword performed on mobile devices. |
| `volume_monthly` | `int \| None` | (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter |

### `keywords_explorer_overview()`

Overview.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `volume_monthly_date_to` | `DateStr` | No | The end date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested. |
| `volume_monthly_date_from` | `DateStr` | No | The start date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested. |
| `target_mode` | `ModeEnum` | No | The scope of the target URL you specified. |
| `target` | `str` | No | The target of the search: a domain or a URL. |
| `target_position` | `TargetPositionEnum` | No | Filters keywords based on the ranking position of the specified `target`. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `search_engine` | `SearchEngineEnum` | No | [Deprecated on 5 Aug 2024]. |
| `keywords` | `str` | No | A comma-separated list of keywords to show metrics for. |
| `keyword_list_id` | `int` | No | The id of an existing keyword list to show metrics for. |

<details>
<summary>Filterable fields (19 fields)</summary>

- `clicks` (integer)
- `cpc` (integer)
- `cps` (float)
- `difficulty` (integer)
- `first_seen` (datetime)
- `global_volume` (integer)
- `intents` (object)
- `keyword` (string)
- `parent_topic` (string)
- `parent_volume` (integer)
- `serp_domain_rating_top10_min` (float)
- `serp_domain_rating_top5_min` (float)
- `serp_features` (array(string))
- `serp_last_update` (datetime)
- `traffic_potential` (integer)
- `volume` (integer)
- `volume_desktop_pct` (float)
- `volume_mobile_pct` (float)
- `word_count` (integer)

</details>

**Returns:** `list[KeywordsExplorerOverviewData]`

| Field | Type | Description |
|-------|------|-------------|
| `clicks` | `int \| None` | The average monthly number of clicks on the search results that people make while searching for the target keyword. |
| `cpc` | `int \| None` | Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents. |
| `cps` | `float \| None` | Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country. |
| `difficulty` | `int \| None` | (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale. |
| `first_seen` | `str \| None` | The date when we first checked search engine results for a keyword. |
| `global_volume` | `int \| None` | (10 units) How many times per month, on average, people search for the target keyword across all countries in our database. |
| `intents` | `dict[str, Any] \| None` | (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`. |
| `keyword` | `str` | |
| `parent_topic` | `str \| None` | Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page. |
| `parent_volume` | `int \| None` | (10 units) The search volume of the parent topic. |
| `searches_pct_clicks_organic_and_paid` | `float \| None` | The average monthly percentage of people who clicked on both organic and paid results while searching for the target keyword. |
| `searches_pct_clicks_organic_only` | `float \| None` | The average monthly percentage of people who clicked only on organic results while searching for the target keyword. |
| `searches_pct_clicks_paid_only` | `float \| None` | The average monthly percentage of people who clicked only on paid results while searching for the target keyword. |
| `serp_features` | `list[SerpFeaturesItemEnum \| None]` | The enriched results on a search engine results page (SERP) that are not traditional organic results. |
| `serp_last_update` | `str \| None` | The date when we last checked search engine results for a keyword. |
| `traffic_potential` | `int \| None` | (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for. |
| `volume` | `int \| None` | (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data. |
| `volume_desktop_pct` | `float \| None` | The percentage of searches for a keyword performed on desktop devices. |
| `volume_mobile_pct` | `float \| None` | The percentage of searches for a keyword performed on mobile devices. |
| `volume_monthly` | `int \| None` | (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter |
| `volume_monthly_history` | `list[dict[str, Any] \| None]` | (2 units per historical month, with a minimum of 50 units) Historical monthly search volume estimates of a keyword for the period set by the `volume_monthly_date_from` and `volume_monthly_date_to` parameters. |

### `keywords_explorer_related_terms()`

Related terms.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `keywords` | `str` | No | A comma-separated list of keywords to show metrics for. |
| `keyword_list_id` | `int` | No | The id of an existing keyword list to show metrics for. |
| `view_for` | `ViewForEnum` | No | View keywords for the top 10 or top 100 ranking pages. |
| `terms` | `TermsEnum1` | No | Related keywords which top-ranking pages also rank for (`also_rank_for`), additional keywords frequently mentioned in top-ranking pages (`also_talk_about`), or combination of both (`all`). |

<details>
<summary>Filterable fields (17 fields)</summary>

- `cpc` (integer)
- `cps` (float)
- `difficulty` (integer)
- `first_seen` (datetime)
- `global_volume` (integer)
- `intents` (object)
- `keyword` (string)
- `parent_topic` (string)
- `serp_domain_rating_top10_min` (float)
- `serp_domain_rating_top5_min` (float)
- `serp_features` (array(string))
- `serp_last_update` (datetime)
- `traffic_potential` (integer)
- `volume` (integer)
- `volume_desktop_pct` (float)
- `volume_mobile_pct` (float)
- `word_count` (integer)

</details>

**Returns:** `list[KeywordsExplorerRelatedTermsData]`

| Field | Type | Description |
|-------|------|-------------|
| `cpc` | `int \| None` | Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents. |
| `cps` | `float \| None` | Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country. |
| `difficulty` | `int \| None` | (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale. |
| `first_seen` | `str \| None` | The date when we first checked search engine results for a keyword. |
| `global_volume` | `int \| None` | (10 units) How many times per month, on average, people search for the target keyword across all countries in our database. |
| `intents` | `dict[str, Any] \| None` | (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`. |
| `keyword` | `str` | |
| `parent_topic` | `str \| None` | Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page. |
| `serp_features` | `list[SerpFeaturesItemEnum \| None]` | The enriched results on a search engine results page (SERP) that are not traditional organic results. |
| `serp_last_update` | `str \| None` | The date when we last checked search engine results for a keyword. |
| `traffic_potential` | `int \| None` | (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for. |
| `volume` | `int \| None` | (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data. |
| `volume_desktop_pct` | `float \| None` | The percentage of searches for a keyword performed on desktop devices. |
| `volume_mobile_pct` | `float \| None` | The percentage of searches for a keyword performed on mobile devices. |
| `volume_monthly` | `int \| None` | (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter |

### `keywords_explorer_search_suggestions()`

Search suggestions.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `search_engine` | `SearchEngineEnum` | No | [Deprecated on 5 Aug 2024]. |
| `keywords` | `str` | No | A comma-separated list of keywords to show metrics for. |
| `keyword_list_id` | `int` | No | The id of an existing keyword list to show metrics for. |

<details>
<summary>Filterable fields (17 fields)</summary>

- `cpc` (integer)
- `cps` (float)
- `difficulty` (integer)
- `first_seen` (datetime)
- `global_volume` (integer)
- `intents` (object)
- `keyword` (string)
- `parent_topic` (string)
- `serp_domain_rating_top10_min` (float)
- `serp_domain_rating_top5_min` (float)
- `serp_features` (array(string))
- `serp_last_update` (datetime)
- `traffic_potential` (integer)
- `volume` (integer)
- `volume_desktop_pct` (float)
- `volume_mobile_pct` (float)
- `word_count` (integer)

</details>

**Returns:** `list[KeywordsExplorerSearchSuggestionsData]`

| Field | Type | Description |
|-------|------|-------------|
| `cpc` | `int \| None` | Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents. |
| `cps` | `float \| None` | Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country. |
| `difficulty` | `int \| None` | (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale. |
| `first_seen` | `str \| None` | The date when we first checked search engine results for a keyword. |
| `global_volume` | `int \| None` | (10 units) How many times per month, on average, people search for the target keyword across all countries in our database. |
| `intents` | `dict[str, Any] \| None` | (10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`. |
| `keyword` | `str` | |
| `parent_topic` | `str \| None` | Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page. |
| `serp_features` | `list[SerpFeaturesItemEnum \| None]` | The enriched results on a search engine results page (SERP) that are not traditional organic results. |
| `serp_last_update` | `str \| None` | The date when we last checked search engine results for a keyword. |
| `traffic_potential` | `int \| None` | (10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for. |
| `volume` | `int \| None` | (10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data. |
| `volume_desktop_pct` | `float \| None` | The percentage of searches for a keyword performed on desktop devices. |
| `volume_mobile_pct` | `float \| None` | The percentage of searches for a keyword performed on mobile devices. |
| `volume_monthly` | `int \| None` | (10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter |

### `keywords_explorer_volume_by_country()`

Volume by country.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `limit` | `int` | No | The number of results to return. |
| `search_engine` | `SearchEngineEnum` | No | [Deprecated on 5 Aug 2024]. |
| `keyword` | `str` | Yes | The keyword to show metrics for. |

**Returns:** `list[KeywordsExplorerVolumeByCountryData]`

| Field | Type | Description |
|-------|------|-------------|
| `country` | `str` | |
| `volume` | `int` | (10 units) An estimation of the average monthly number of searches for a keyword in a given country. |

### `keywords_explorer_volume_history()`

Volume history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | No | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `keyword` | `str` | Yes | The keyword to show metrics for. |

**Returns:** `list[KeywordsExplorerVolumeHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `volume` | `int` | An estimation of the number of searches for a keyword over a given month. |

______________________________________________________________________

## Rank Tracker

### `rank_tracker_competitors_overview()`

Competitors overview.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `date_compared` | `DateStr` | No | A date to compare metrics with in YYYY-MM-DD format. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `device` | `DeviceEnum` | Yes | Choose between mobile and desktop rankings. |
| `project_id` | `int` | Yes | The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#` |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

<details>
<summary>Filterable fields (14 fields)</summary>

- `country` (string)
- `is_main_position` (boolean)
- `is_main_position_prev` (boolean)
- `keyword` (string)
- `keyword_difficulty` (integer)
- `keyword_has_data` (boolean)
- `keyword_is_frozen` (boolean)
- `language` (string)
- `location` (string)
- `serp_features` (array(string))
- `serp_updated` (datetime)
- `serp_updated_prev` (datetime)
- `tags` (array(string))
- `volume` (integer)

</details>

**Returns:** `list[RankTrackerCompetitorsOverviewData]`

| Field | Type | Description |
|-------|------|-------------|
| `competitors_list` | `list[dict[str, Any] \| None]` | Competitors information for a given keyword. The following fields are included: `url`, `url_prev`, `position`, `position_prev`, `best_position_kind`, `best_position_kind`, `traffic`, `traffic_prev`, `value`, `value_prev`. Fields ending in `prev` are included only in the compared view. |
| `country` | `CountryEnum1` | The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2). |
| `keyword` | `str` | The keyword your target ranks for. |
| `keyword_difficulty` | `int \| None` | An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale. |
| `keyword_has_data` | `bool` | Will return `false` if the keyword is still processing and no SERP has been fetched yet. |
| `keyword_is_frozen` | `bool` | Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are "frozen", meaning they do not have their rankings updated. |
| `language` | `str` | The SERP language that a given keyword is being tracked for. |
| `location` | `str` | The location (country, state/province, or city) that a given keyword is being tracked in. |
| `serp_features` | `list[SerpFeaturesItemEnum1 \| None]` | The SERP features that appear in search results for a keyword. |
| `serp_updated` | `str \| None` | The date when we last checked search engine results for a keyword. |
| `serp_updated_prev` | `str \| None` | The date when we checked search engine results up to the comparison date. |
| `tags` | `list[str \| None]` | A list of tags assigned to a given keyword. |
| `volume` | `int \| None` | An estimation of the average monthly number of searches for a keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter. |

### `rank_tracker_competitors_pages()`

Competitors pages.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `target_and_tracked_competitors_only` | `bool` | No | Restrict pages to target and tracked competitors |
| `date_compared` | `DateStr` | No | A date to compare metrics with in YYYY-MM-DD format. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `device` | `DeviceEnum` | Yes | Choose between mobile and desktop rankings. |
| `project_id` | `int` | Yes | The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#` |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

<details>
<summary>Filterable fields (10 fields)</summary>

- `country` (string)
- `country_prev` (string)
- `domain` (string)
- `language` (string)
- `language_prev` (string)
- `location` (string)
- `location_prev` (string)
- `tags` (array(string))
- `tags_prev` (array(string))
- `url` (string)

</details>

**Returns:** `list[RankTrackerCompetitorsPagesData]`

| Field | Type | Description |
|-------|------|-------------|
| `keywords` | `int` | The total number of keywords that your target ranks for in the top 100 organic search results. |
| `share_of_traffic_value` | `float` | The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords. |
| `share_of_traffic_value_prev` | `float` | The share of traffic value on the comparison date. |
| `share_of_voice` | `float` | The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords. |
| `share_of_voice_prev` | `float` | The share of voice on the comparison date. |
| `status` | `StatusEnum` | The status of a page: the new page that just started to rank ("left"), the lost page that disappeared from search results ("right"), or no change ("both"). |
| `title` | `str \| None` | The title displayed for the page in its top keyword's SERP. |
| `title_prev` | `str \| None` | The title on the comparison date. |
| `traffic` | `int` | An estimation of the number of monthly visits that a page gets from organic search. |
| `traffic_prev` | `int` | The traffic on the comparison date. |
| `traffic_value` | `int \| None` | The estimated value of a page’s monthly organic search traffic, in USD cents. |
| `traffic_value_prev` | `int \| None` | The traffic value on the comparison date. |
| `url` | `str` | The page URL. |

### `rank_tracker_competitors_stats()`

Competitors metrics.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `device` | `DeviceEnum` | Yes | Choose between mobile and desktop rankings. |
| `project_id` | `int` | Yes | The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#` |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

**Returns:** `list[RankTrackerCompetitorsStatsData]`

| Field | Type | Description |
|-------|------|-------------|
| `ai_overview_count` | `int` | The total number of tracked keywords for which your target ranks in an AI Overview. |
| `average_position` | `float \| None` | The average of your target's top organic positions across all tracked keywords. |
| `competitor` | `str` | Competitor's URL. |
| `discussions_count` | `int` | The total number of tracked keywords for which your target ranks in Discussions and forums. |
| `featured_snippet_count` | `int` | The total number of tracked keywords for which your target ranks in a Featured snippet. |
| `image_pack_count` | `int` | The total number of tracked keywords for which your target ranks in an Image pack. |
| `knowledge_card_count` | `int` | The total number of tracked keywords for which your target ranks in a Knowledge card. |
| `knowledge_panel_count` | `int` | The total number of tracked keywords for which your target ranks in a Knowledge panel. |
| `pos_11_20` | `int` | The total number of tracked keywords for which your target's top organic position is within the 11th to 20th results. |
| `pos_1_3` | `int` | The total number of tracked keywords for which your target's top organic position is within the top 3 results. |
| `pos_21_50` | `int` | The total number of tracked keywords for which your target's top organic position is within the 21st to 50th results. |
| `pos_4_10` | `int` | The total number of tracked keywords for which your target's top organic position is within the 4th to 10th results. |
| `pos_51_plus` | `int` | The total number of tracked keywords for which your target's top organic position is the 51st or higher. |
| `pos_no_rank` | `int` | The total number of tracked keywords where your target doesn't rank. |
| `share_of_traffic_value` | `float` | The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords. |
| `share_of_voice` | `float` | The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords. |
| `sitelinks_count` | `int` | The total number of tracked keywords for which your target ranks in Sitelinks. |
| `thumbnail_count` | `int` | The total number of tracked keywords for which your target ranks in a Thumbnail. |
| `top_stories_count` | `int` | The total number of tracked keywords for which your target ranks in Top stories. |
| `traffic` | `int \| None` | The estimated number of monthly visits that your target gets from organic search for all tracked keywords. |
| `traffic_value` | `int \| None` | The estimated value of your target's monthly organic search traffic for all tracked keywords. |
| `video_preview_count` | `int` | The total number of tracked keywords for which your target ranks in a Video preview. |
| `videos_count` | `int` | The total number of tracked keywords for which your target ranks in Videos. |
| `x_count` | `int` | The total number of tracked keywords for which your target ranks in an X (Twitter) widget. |

### `rank_tracker_overview()`

Overview.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `date_compared` | `DateStr` | No | A date to compare metrics with in YYYY-MM-DD format. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `device` | `DeviceEnum` | Yes | Choose between mobile and desktop rankings. |
| `project_id` | `int` | Yes | The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#` |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

<details>
<summary>Filterable fields (54 fields)</summary>

- `best_position_has_thumbnail` (boolean)
- `best_position_has_thumbnail_previous` (boolean)
- `best_position_has_video_preview` (boolean)
- `best_position_has_video_preview_previous` (boolean)
- `best_position_kind` (string)
- `best_position_kind_previous` (string)
- `clicks` (integer)
- `clicks_per_search` (float)
- `cost_per_click` (integer)
- `country` (string)
- `country_prev` (string)
- `created_at` (datetime)
- `is_branded` (boolean)
- `is_commercial` (boolean)
- `is_informational` (boolean)
- `is_local` (boolean)
- `is_main_position` (boolean)
- `is_main_position_prev` (boolean)
- `is_navigational` (boolean)
- `is_transactional` (boolean)
- `keyword` (string)
- `keyword_difficulty` (integer)
- `keyword_has_data` (boolean)
- `keyword_is_frozen` (boolean)
- `keyword_prev` (string)
- `keyword_words` (integer)
- `keyword_words_prev` (integer)
- `language` (string)
- `language_prev` (string)
- `location` (string)
- `location_prev` (string)
- `parent_topic` (string)
- `position` (integer)
- `position_diff` (integer)
- `position_prev` (integer)
- `search_type_image` (float)
- `search_type_news` (float)
- `search_type_video` (float)
- `search_type_web` (float)
- `serp_features` (array(string))
- `serp_features_prev` (array(string))
- `serp_updated` (datetime)
- `serp_updated_prev` (datetime)
- `tags` (array(string))
- `tags_prev` (array(string))
- `target_positions_count` (integer)
- `traffic` (integer)
- `traffic_diff` (integer)
- `traffic_prev` (integer)
- `url` (string)
- `url_prev` (string)
- `volume` (integer)
- `volume_desktop_pct` (float)
- `volume_mobile_pct` (float)

</details>

**Returns:** `list[RankTrackerOverviewData]`

<details>
<summary>50 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `best_position_has_thumbnail` | `bool \| None` | The top position (or target URL’s, if set) has a thumbnail. |
| `best_position_has_thumbnail_previous` | `bool \| None` | The top position (or target URL’s, if set) has a thumbnail on the comparison date. |
| `best_position_has_video_preview` | `bool \| None` | The top position (or target URL’s, if set) has a video preview. |
| `best_position_has_video_preview_previous` | `bool \| None` | The top position (or target URL’s, if set) has a video preview on the comparison date. |
| `best_position_kind` | `BestPositionKindEnum \| None` | The kind of top position (or target URL’s, if set): organic, paid, or a SERP feature. |
| `best_position_kind_previous` | `BestPositionKindEnum \| None` | The kind of top position (or target URL’s, if set) on the comparison date. |
| `clicks` | `int \| None` | Clicks metric refers to the average monthly number of clicks on the search results that people make while searching for the target keyword. Some searches generate clicks on multiple results, while others might not end in any clicks at all. |
| `clicks_per_search` | `float \| None` | Clicks Per Search is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country. |
| `cost_per_click` | `int \| None` | Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword. |
| `country` | `CountryEnum1` | The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2). |
| `country_prev` | `CountryEnum1` | The country that a given keyword is being tracked in on the comparison date. A two-letter country code (ISO 3166-1 alpha-2). |
| `created_at` | `str` | The date when a keyword was added to the project. |
| `is_branded` | `bool` | User intent: branded. The user is searching for a specific brand or company name. |
| `is_commercial` | `bool` | User intent: commercial. The user is comparing products or services before making a purchase decision. |
| `is_informational` | `bool` | User intent: informational. The user is looking for information or an answer to a specific question. |
| `is_local` | `bool` | User intent: local. The user is looking for information relevant to a specific location or nearby services. |
| `is_navigational` | `bool` | User intent: navigational. The user is searching for a specific website or web page. |
| `is_transactional` | `bool` | User intent: transactional. The user is ready to complete an action, often a purchase. |
| `keyword` | `str` | The keyword your target ranks for. |
| `keyword_difficulty` | `int \| None` | An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale. |
| `keyword_has_data` | `bool` | Will return `false` if the keyword is still processing and no SERP has been fetched yet. |
| `keyword_is_frozen` | `bool` | Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are "frozen", meaning they do not have their rankings updated. |
| `keyword_prev` | `str` | The keyword your target ranks for on the comparison date. |
| `language` | `str` | The SERP language that a given keyword is being tracked for. |
| `language_prev` | `str` | The SERP language on the comparison date. |
| `location` | `str` | The location (country, state/province, or city) that a given keyword is being tracked in. |
| `location_prev` | `str` | The location (country, state/province, or city) that a given keyword is being tracked in on the comparison date. |
| `parent_topic` | `str \| None` | Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page. |
| `position` | `int \| None` | The top position (or target URL’s, if set) in organic search. |
| `position_diff` | `int \| None` | The change in top position (or target URL’s, if set) between selected dates. |
| `position_prev` | `int \| None` | The top position (or target URL’s, if set) on the comparison date. |
| `search_type_image` | `float \| None` | Search type Image shows the percentage of searches for a keyword made for images, highlighting interest in visual content. |
| `search_type_news` | `float \| None` | Search type News shows the percentage of searches for a keyword made for news articles. |
| `search_type_video` | `float \| None` | Search type Video shows the percentage of searches for a keyword made for video, reflecting interest in video content. |
| `search_type_web` | `float \| None` | Search type Web shows the percentage of searches for a keyword made for general web content, indicating interest in a wide range of information. |
| `serp_features` | `list[SerpFeaturesItemEnum1 \| None]` | The SERP features that appear in search results for a keyword. |
| `serp_features_prev` | `list[SerpFeaturesItemEnum1 \| None]` | The SERP features that appear in search results for a keyword on the comparison date. |
| `serp_updated` | `str \| None` | The date when we last checked search engine results for a keyword. |
| `serp_updated_prev` | `str \| None` | The date when we checked search engine results up to the comparison date. |
| `tags` | `list[str \| None]` | A list of tags assigned to a given keyword. |
| `tags_prev` | `list[str \| None]` | A list of tags assigned to a given keyword on the comparison date. |
| `target_positions_count` | `int` | The number of target URLs ranking for a keyword. |
| `traffic` | `int \| None` | An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter. |
| `traffic_diff` | `int \| None` | The change in traffic between your selected dates. |
| `traffic_prev` | `int \| None` | An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter. |
| `url` | `str \| None` | The top-ranking URL (or target URL, if set) in organic search. |
| `url_prev` | `str \| None` | The top-ranking URL (or target URL, if set) on the comparison date. |
| `volume` | `int \| None` | An estimation of the average monthly number of searches for a keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter. |
| `volume_desktop_pct` | `float \| None` | The percentage of the total search volume that comes from desktop devices. |
| `volume_mobile_pct` | `float \| None` | The percentage of the total search volume that comes from mobile devices. |

</details>

### `rank_tracker_serp_overview()`

SERP Overview.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `top_positions` | `int` | No | The number of top organic SERP positions to return. If not specified, all available positions will be returned. |
| `device` | `DeviceEnum` | Yes | Choose between mobile and desktop rankings. |
| `date` | `str` | No | A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned. |
| `location_id` | `int` | No | The location ID of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `language_code` | `str` | No | The language code of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords. |
| `keyword` | `str` | Yes | The keyword to return SERP Overview for. |
| `project_id` | `int` | Yes | The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#` |

**Returns:** `list[RankTrackerSerpOverviewData]`

| Field | Type | Description |
|-------|------|-------------|
| `position` | `int` | The position of the search result in SERP. |
| `title` | `str \| None` | The title of a ranking page. |
| `url` | `str \| None` | The URL of a ranking page. |
| `type` | `list[str \| None]` | The kind of the position: organic, paid, or a SERP feature. Allowed values: `ai_overview`, `ai_overview_sitelink`, `discussion`, `image`, `image_th`, `knowledge_card`, `knowledge_panel`, `local_pack`, `organic`, `organic_shopping`, `paid_top`, `paid_bottom`, `paid_right`, `question`, `sitelink`, `snippet`, `top_story`, `tweet`, `video`, `video_th`. |
| `update_date` | `str` | The date when we checked search engine results for a keyword. |
| `nr_words` | `int \| None` | The total number of words present in the HTML of a web page. |
| `domain_rating` | `float \| None` | The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale. |
| `url_rating` | `float \| None` | The strength of a page's backlink profile on a 100-point logarithmic scale. |
| `ahrefs_rank` | `int \| None` | The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |
| `backlinks` | `int \| None` | The total number of links from other websites pointing to a search result. |
| `refdomains` | `int \| None` | The total number of unique domains linking to a search result. |
| `traffic` | `int \| None` | An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for. |
| `value` | `int \| None` | The estimated value of a page’s monthly organic search traffic, in USD cents. |
| `keywords` | `int \| None` | The total number of keywords that a search result ranks for in the top 100 organic positions. |
| `top_keyword` | `str \| None` | The keyword that brings the most organic traffic to a search result. |
| `top_keyword_volume` | `int \| None` | An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data. |
| `page_type` | `str \| None` | Comma-separated list of AI-predicted hierarchical page type paths for the ranking page. Each value is a slash-prefixed path (e.g. /Article/How_to). |

______________________________________________________________________

## Serp Overview

### `serp_overview()`

SERP Overview.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `top_positions` | `int` | No | The number of top organic SERP positions to return. If not specified, all available positions will be returned. |
| `date` | `str` | No | A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `keyword` | `str` | Yes | The keyword to return SERP Overview for. |

**Returns:** `list[SerpOverviewData]`

| Field | Type | Description |
|-------|------|-------------|
| `ahrefs_rank` | `int \| None` | The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |
| `backlinks` | `int \| None` | The total number of links from other websites pointing to a search result. |
| `domain_rating` | `float \| None` | The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale. |
| `keywords` | `int \| None` | The total number of keywords that a search result ranks for in the top 100 organic positions. |
| `page_type` | `str \| None` | Comma-separated list of AI-predicted hierarchical page type paths for the ranking page. Each value is a slash-prefixed path (e.g. /Article/How_to). |
| `position` | `int` | The position of the search result in SERP. |
| `refdomains` | `int \| None` | (5 units) The total number of unique domains linking to a search result. |
| `title` | `str \| None` | The title of a ranking page. |
| `top_keyword` | `str \| None` | The keyword that brings the most organic traffic to a search result. |
| `top_keyword_volume` | `int \| None` | (10 units) An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data. |
| `traffic` | `int \| None` | (10 units) An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for. |
| `type` | `list[SerpFeaturesItemEnum1 \| None]` | The kind of the position: organic, paid, or a SERP feature. |
| `update_date` | `str` | The date when we checked search engine results for a keyword. |
| `url` | `str \| None` | The URL of a ranking page. |
| `url_rating` | `float \| None` | The strength of a page's backlink profile on a 100-point logarithmic scale. |
| `value` | `int \| None` | (10 units) The estimated value of a page’s monthly organic search traffic, in USD cents. |

______________________________________________________________________

## Site Audit

### `site_audit_issues()`

Project Issues.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date_compared` | `str` | No | A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field. |
| `date` | `str` | No | A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. |
| `project_id` | `int` | Yes | The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#` |

**Returns:** `list[SiteAuditIssuesData]`

| Field | Type | Description |
|-------|------|-------------|
| `issue_id` | `str` | The unique identifier of the issue. |
| `name` | `str` | The name of the issue. |
| `importance` | `str` | The importance of the issue. Possible values: `Error`, `Warning`, `Notice`. |
| `category` | `str` | The category of the issue. Possible values: `Internal pages`, `Indexability`, `Links`, `Redirects`, `Content`, `Social tags`, `Duplicates`, `Localization`, `Usability and performance`, `Images`, `JavaScript`, `CSS`, `Sitemaps`, `External pages`, `Other`. |
| `is_indexable` | `bool \| None` | True if the issue applies only to indexable pages. |
| `crawled` | `int` | Number of URLs currently affected by the issue. |
| `change` | `int \| None` | Difference in the number of affected URLs between the specified dates. |
| `added` | `int \| None` | Number of URLs that have the issue on the current date but did not have it on the previous date. |
| `new` | `int \| None` | Number of newly discovered URLs that have the issue on the current date. |
| `removed` | `int \| None` | Number of URLs that had the issue on the previous date but no longer have it on the current date. |
| `missing` | `int \| None` | Number of URLs that had the issue on the previous date but cannot be found on the current date. |

### `site_audit_page_content()`

Page content.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `date` | `str` | No | A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. |
| `target_url` | `str` | Yes | The URL of the page to retrieve content for. |
| `project_id` | `int` | Yes | The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#` |

**Returns:** `SiteAuditPageContentData | None`

| Field | Type | Description |
|-------|------|-------------|
| `crawl_datetime` | `str` | The timestamp when the page was crawled. |
| `page_text` | `str \| None` | The text extracted from the page content. |
| `raw_html` | `str \| None` | The raw HTML of the page. |
| `rendered_html` | `str \| None` | The rendered HTML of the page. |

### `site_audit_page_explorer()`

Page explorer.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | No | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `filter_mode` | `FilterModeEnum` | No | Indicates which pages to return compared to the previous crawl. If not specified, all URLs that match your filter conditions are returned. `added`: URLs that are a new match for your filter conditions. `new`: URLs that are newly crawled and match your filter conditions. `removed`: URLs that stopped matching your filter conditions. `missing`: URLs that weren't crawled, but previously matched your filter conditions. `no_change`: URLs that match your filter conditions in a crawl and the crawl before it. |
| `issue_id` | `str` | No | The unique identifier of an issue. When specified, only URLs affected by this issue are returned. You can get issue IDs by querying the `site-audit/issues` endpoint. |
| `date_compared` | `str` | No | A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field. |
| `date` | `str` | No | A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. |
| `project_id` | `int` | Yes | The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#` |

<details>
<summary>Filterable fields (605 fields)</summary>

- `ai_content_level` (string)
- `ai_content_status` (string)
- `alternate` (integer)
- `alternate_diff` (integer)
- `alternate_prev` (integer)
- `backlinks` (integer)
- `backlinks_diff` (integer)
- `backlinks_prev` (integer)
- `canonical` (url)
- `canonical_code` (integer)
- `canonical_counts` (integer)
- `canonical_counts_diff` (integer)
- `canonical_counts_prev` (integer)
- `canonical_group_hash` (integer)
- `canonical_is_canonical` (boolean)
- `canonical_is_canonical_prev` (boolean)
- `canonical_no_crawl_reason` (string)
- `canonical_no_crawl_reason_prev` (string)
- `canonical_prev` (url)
- `canonical_scheme` (string)
- `canonical_scheme_prev` (string)
- `compliant` (boolean)
- `compliant_prev` (boolean)
- `compression` (string)
- `compression_prev` (string)
- `content_encoding` (string)
- `content_encoding_prev` (string)
- `content_length` (integer)
- `content_length_diff` (integer)
- `content_length_prev` (integer)
- `content_nr_word` (integer)
- `content_nr_word_diff` (integer)
- `content_nr_word_prev` (integer)
- `content_type` (string)
- `content_type_prev` (string)
- `css_no_crawl_reason` (array(null))
- `css_no_crawl_reason_prev` (array(null))
- `curl_code` (integer)
- `depth` (integer)
- `depth_diff` (integer)
- `depth_prev` (integer)
- `dofollow` (integer)
- `dofollow_prev` (integer)
- `domain` (domain)
- `duplicate_content` (integer)
- `duplicate_content_canonical_hreflang` (integer)
- `duplicate_content_canonical_hreflang_diff` (integer)
- `duplicate_content_canonical_hreflang_prev` (integer)
- `duplicate_content_diff` (integer)
- `duplicate_content_prev` (integer)
- `duplicate_description` (integer)
- `duplicate_description_canonical_hreflang` (integer)
- `duplicate_description_canonical_hreflang_diff` (integer)
- `duplicate_description_canonical_hreflang_prev` (integer)
- `duplicate_description_diff` (integer)
- `duplicate_description_prev` (integer)
- `duplicate_group_identifier` (integer)
- `duplicate_h1` (integer)
- `duplicate_h1_diff` (integer)
- `duplicate_h1_prev` (integer)
- `duplicate_h1canonical_hreflang` (integer)
- `duplicate_h1canonical_hreflang_diff` (integer)
- `duplicate_h1canonical_hreflang_prev` (integer)
- `duplicate_title` (integer)
- `duplicate_title_canonical_hreflang` (integer)
- `duplicate_title_canonical_hreflang_diff` (integer)
- `duplicate_title_canonical_hreflang_prev` (integer)
- `duplicate_title_diff` (integer)
- `duplicate_title_prev` (integer)
- `edu` (integer)
- `edu_diff` (integer)
- `edu_prev` (integer)
- `external_code` (array(null))
- `external_link_anchor` (array(null))
- `external_link_anchor_prev` (array(null))
- `external_link_domain` (array(domain))
- `external_link_domain_prev` (array(domain))
- `external_links` (array(url))
- `external_links_is_canonical` (array(null))
- `external_links_is_canonical_prev` (array(null))
- `external_links_prev` (array(url))
- `external_no_crawl_reason` (array(null))
- `external_no_crawl_reason_prev` (array(null))
- `external_scheme` (array(string))
- `external_scheme_prev` (array(string))
- `final_redirect` (url)
- `final_redirect_code` (integer)
- `final_redirect_no_crawl_reason` (string)
- `final_redirect_no_crawl_reason_prev` (string)
- `final_redirect_prev` (url)
- `found_in_sitemaps` (array(url))
- `found_in_sitemaps_length` (integer)
- `found_in_sitemaps_prev` (array(url))
- `gov` (integer)
- `gov_diff` (integer)
- `gov_prev` (integer)
- `h1` (array(string))
- `h1_prev` (array(string))
- `h1length` (array(integer))
- `h1length_prev` (array(integer))
- `h2` (array(string))
- `h2_prev` (array(string))
- `hash_content` (integer)
- `hash_descriptions` (array(integer))
- `hash_h1` (array(integer))
- `hash_text` (integer)
- `hash_titles` (array(integer))
- `hreflang` (array(null))
- `hreflang_code_is_valid` (array(null))
- `hreflang_code_is_valid_prev` (array(null))
- `hreflang_country` (array(null))
- `hreflang_country_prev` (array(null))
- `hreflang_group_hash` (integer)
- `hreflang_inlink_urls` (array(url))
- `hreflang_inlink_urls_prev` (array(url))
- `hreflang_issues` (array(string))
- `hreflang_issues_prev` (array(string))
- `hreflang_language` (array(null))
- `hreflang_language_prev` (array(null))
- `hreflang_link` (array(url))
- `hreflang_link_is_canonical` (array(null))
- `hreflang_link_is_canonical_prev` (array(null))
- `hreflang_link_prev` (array(url))
- `hreflang_no_crawl_reason` (array(null))
- `hreflang_no_crawl_reason_prev` (array(null))
- `hreflang_pages_urls` (array(url))
- `hreflang_pages_urls_count` (integer)
- `hreflang_pages_urls_count_diff` (integer)
- `hreflang_pages_urls_count_prev` (integer)
- `hreflang_pages_urls_prev` (array(url))
- `hreflang_prev` (array(null))
- `html_lang` (string)
- `html_lang_code_is_valid` (boolean)
- `html_lang_code_is_valid_prev` (boolean)
- `html_lang_country` (string)
- `html_lang_country_prev` (string)
- `html_lang_language` (string)
- `html_lang_language_prev` (string)
- `html_lang_prev` (string)
- `http_code` (integer)
- `http_header` (array(string))
- `http_header_prev` (array(string))
- `http_header_robots` (array(string))
- `http_header_robots_prev` (array(string))
- `http_headers_size` (integer)
- `http_headers_size_diff` (integer)
- `http_headers_size_prev` (integer)
- `images_no_crawl_reason` (array(null))
- `images_no_crawl_reason_prev` (array(null))
- `incoming_all_links` (integer)
- `incoming_all_links_diff` (integer)
- `incoming_all_links_prev` (integer)
- `incoming_canonical` (integer)
- `incoming_canonical_diff` (integer)
- `incoming_canonical_prev` (integer)
- `incoming_css` (integer)
- `incoming_css_diff` (integer)
- `incoming_css_prev` (integer)
- `incoming_follow` (integer)
- `incoming_follow_diff` (integer)
- `incoming_follow_prev` (integer)
- `incoming_hreflang` (integer)
- `incoming_hreflang_diff` (integer)
- `incoming_hreflang_prev` (integer)
- `incoming_image` (integer)
- `incoming_image_diff` (integer)
- `incoming_image_prev` (integer)
- `incoming_js` (integer)
- `incoming_js_diff` (integer)
- `incoming_js_prev` (integer)
- `incoming_links` (integer)
- `incoming_links_diff` (integer)
- `incoming_links_prev` (integer)
- `incoming_nofollow` (integer)
- `incoming_nofollow_diff` (integer)
- `incoming_nofollow_prev` (integer)
- `incoming_pagination` (integer)
- `incoming_pagination_diff` (integer)
- `incoming_pagination_prev` (integer)
- `incoming_redirect` (integer)
- `incoming_redirect_diff` (integer)
- `incoming_redirect_prev` (integer)
- `indexnow_error` (string)
- `indexnow_error_prev` (string)
- `indexnow_reason` (string)
- `indexnow_reason_prev` (string)
- `indexnow_status` (string)
- `indexnow_status_prev` (string)
- `indexnow_submitted_at` (date)
- `indexnow_submitted_at_prev` (date)
- `internal_code` (array(null))
- `internal_inlink_urls` (array(url))
- `internal_inlink_urls_prev` (array(url))
- `internal_link_anchor` (array(null))
- `internal_link_anchor_prev` (array(null))
- `internal_link_domain` (array(domain))
- `internal_link_domain_prev` (array(domain))
- `internal_links` (array(url))
- `internal_links_is_canonical` (array(null))
- `internal_links_is_canonical_prev` (array(null))
- `internal_links_prev` (array(url))
- `internal_no_crawl_reason` (array(null))
- `internal_no_crawl_reason_prev` (array(null))
- `internal_scheme` (array(string))
- `internal_scheme_prev` (array(string))
- `is_html` (boolean)
- `is_in_sitemap` (boolean)
- `is_in_sitemap_prev` (boolean)
- `is_page_title_used_in_serp` (boolean)
- `is_redirect_loop` (boolean)
- `is_redirect_loop_prev` (boolean)
- `is_rendered` (boolean)
- `is_rendered_prev` (boolean)
- `is_valid_internal_html` (boolean)
- `is_valid_internal_html_prev` (boolean)
- `js_no_crawl_reason` (array(null))
- `js_no_crawl_reason_prev` (array(null))
- `jsonld_attributes` (array(string))
- `jsonld_attributes_prev` (array(string))
- `jsonld_schema_types` (array(string))
- `jsonld_schema_types_prev` (array(string))
- `jsonld_validation_kinds` (array(string))
- `jsonld_validation_kinds_prev` (array(string))
- `jsonld_values` (array(string))
- `jsonld_values_prev` (array(string))
- `keywords` (array(string))
- `keywords_prev` (array(string))
- `length` (integer)
- `links_count_css` (integer)
- `links_count_css_prev` (integer)
- `links_count_external` (integer)
- `links_count_external3xx` (integer)
- `links_count_external3xx_diff` (integer)
- `links_count_external3xx_prev` (integer)
- `links_count_external4xx` (integer)
- `links_count_external4xx_diff` (integer)
- `links_count_external4xx_prev` (integer)
- `links_count_external5xx` (integer)
- `links_count_external5xx_diff` (integer)
- `links_count_external5xx_prev` (integer)
- `links_count_external_diff` (integer)
- `links_count_external_follow` (integer)
- `links_count_external_follow_diff` (integer)
- `links_count_external_follow_prev` (integer)
- `links_count_external_nofollow` (integer)
- `links_count_external_nofollow_diff` (integer)
- `links_count_external_nofollow_prev` (integer)
- `links_count_external_non_canonical` (integer)
- `links_count_external_non_canonical_diff` (integer)
- `links_count_external_non_canonical_prev` (integer)
- `links_count_external_prev` (integer)
- `links_count_external_xxx` (integer)
- `links_count_external_xxx_diff` (integer)
- `links_count_external_xxx_prev` (integer)
- `links_count_images` (integer)
- `links_count_images_diff` (integer)
- `links_count_images_prev` (integer)
- `links_count_images_with_alt` (integer)
- `links_count_images_with_alt_diff` (integer)
- `links_count_images_with_alt_prev` (integer)
- `links_count_images_without_alt` (integer)
- `links_count_images_without_alt_diff` (integer)
- `links_count_images_without_alt_prev` (integer)
- `links_count_internal` (integer)
- `links_count_internal3xx` (integer)
- `links_count_internal3xx_diff` (integer)
- `links_count_internal3xx_prev` (integer)
- `links_count_internal4xx` (integer)
- `links_count_internal4xx_diff` (integer)
- `links_count_internal4xx_prev` (integer)
- `links_count_internal5xx` (integer)
- `links_count_internal5xx_diff` (integer)
- `links_count_internal5xx_prev` (integer)
- `links_count_internal_diff` (integer)
- `links_count_internal_follow` (integer)
- `links_count_internal_follow_diff` (integer)
- `links_count_internal_follow_prev` (integer)
- `links_count_internal_nofollow` (integer)
- `links_count_internal_nofollow_diff` (integer)
- `links_count_internal_nofollow_prev` (integer)
- `links_count_internal_non_canonical` (integer)
- `links_count_internal_non_canonical_diff` (integer)
- `links_count_internal_non_canonical_prev` (integer)
- `links_count_internal_prev` (integer)
- `links_count_internal_xxx` (integer)
- `links_count_internal_xxx_diff` (integer)
- `links_count_internal_xxx_prev` (integer)
- `links_count_js` (integer)
- `links_count_js_diff` (integer)
- `links_count_js_prev` (integer)
- `links_css` (array(url))
- `links_css_code` (array(null))
- `links_css_domain` (array(domain))
- `links_css_domain_prev` (array(domain))
- `links_css_prev` (array(url))
- `links_css_scheme` (array(string))
- `links_css_scheme_prev` (array(string))
- `links_external3xx` (array(url))
- `links_external3xx_prev` (array(url))
- `links_external4xx` (array(url))
- `links_external4xx_prev` (array(url))
- `links_external5xx` (array(url))
- `links_external5xx_prev` (array(url))
- `links_external_follow` (array(url))
- `links_external_follow_prev` (array(url))
- `links_external_nofollow` (array(url))
- `links_external_nofollow_prev` (array(url))
- `links_external_non_canonical` (array(url))
- `links_external_non_canonical_prev` (array(url))
- `links_external_xxx` (array(url))
- `links_external_xxx_prev` (array(url))
- `links_hreflang_code` (array(null))
- `links_images` (array(url))
- `links_images_alt` (array(null))
- `links_images_alt_prev` (array(null))
- `links_images_code` (array(null))
- `links_images_domain` (array(domain))
- `links_images_domain_prev` (array(domain))
- `links_images_prev` (array(url))
- `links_images_scheme` (array(string))
- `links_images_scheme_prev` (array(string))
- `links_images_with_alt` (array(url))
- `links_images_with_alt_prev` (array(url))
- `links_images_without_alt` (array(url))
- `links_images_without_alt_prev` (array(url))
- `links_internal3xx` (array(url))
- `links_internal3xx_prev` (array(url))
- `links_internal4xx` (array(url))
- `links_internal4xx_prev` (array(url))
- `links_internal5xx` (array(url))
- `links_internal5xx_prev` (array(url))
- `links_internal_follow` (array(url))
- `links_internal_follow_prev` (array(url))
- `links_internal_nofollow` (array(url))
- `links_internal_nofollow_prev` (array(url))
- `links_internal_non_canonical` (array(url))
- `links_internal_non_canonical_prev` (array(url))
- `links_internal_xxx` (array(url))
- `links_internal_xxx_prev` (array(url))
- `links_js` (array(url))
- `links_js_code` (array(null))
- `links_js_domain` (array(domain))
- `links_js_domain_prev` (array(domain))
- `links_js_prev` (array(url))
- `links_js_scheme` (array(string))
- `links_js_scheme_prev` (array(string))
- `loading_time` (integer)
- `loading_time_diff` (integer)
- `loading_time_prev` (integer)
- `meta_description` (array(string))
- `meta_description_length` (array(integer))
- `meta_description_length_prev` (array(integer))
- `meta_description_prev` (array(string))
- `meta_refresh` (array(string))
- `meta_refresh_prev` (array(string))
- `meta_robots` (array(string))
- `meta_robots_prev` (array(string))
- `meta_twitter_tags_app_google_play` (string)
- `meta_twitter_tags_app_google_play_prev` (string)
- `meta_twitter_tags_app_ipad` (string)
- `meta_twitter_tags_app_ipad_prev` (string)
- `meta_twitter_tags_app_iphone` (string)
- `meta_twitter_tags_app_iphone_prev` (string)
- `meta_twitter_tags_attributes` (array(string))
- `meta_twitter_tags_attributes_prev` (array(string))
- `meta_twitter_tags_card` (string)
- `meta_twitter_tags_card_prev` (string)
- `meta_twitter_tags_description` (string)
- `meta_twitter_tags_description_prev` (string)
- `meta_twitter_tags_image` (string)
- `meta_twitter_tags_image_prev` (string)
- `meta_twitter_tags_image_url_invalid` (boolean)
- `meta_twitter_tags_image_url_invalid_prev` (boolean)
- `meta_twitter_tags_player` (string)
- `meta_twitter_tags_player_height` (integer)
- `meta_twitter_tags_player_height_diff` (integer)
- `meta_twitter_tags_player_height_prev` (integer)
- `meta_twitter_tags_player_prev` (string)
- `meta_twitter_tags_player_width` (integer)
- `meta_twitter_tags_player_width_diff` (integer)
- `meta_twitter_tags_player_width_prev` (integer)
- `meta_twitter_tags_site` (string)
- `meta_twitter_tags_site_prev` (string)
- `meta_twitter_tags_title` (string)
- `meta_twitter_tags_title_prev` (string)
- `meta_twitter_tags_valid` (boolean)
- `meta_twitter_tags_valid_prev` (boolean)
- `meta_twitter_tags_values` (array(string))
- `meta_twitter_tags_values_prev` (array(string))
- `navigation_next` (url)
- `navigation_next_code` (integer)
- `navigation_next_no_crawl_reason` (string)
- `navigation_next_no_crawl_reason_prev` (string)
- `navigation_next_prev` (url)
- `navigation_prev_code` (integer)
- `navigation_prev_no_crawl_reason` (string)
- `navigation_prev_no_crawl_reason_prev` (string)
- `no_crawl_reason` (string)
- `no_crawl_reason_prev` (string)
- `nofollow` (integer)
- `nofollow_diff` (integer)
- `nofollow_prev` (integer)
- `nr_h1` (integer)
- `nr_h1_prev` (integer)
- `nr_meta_description` (integer)
- `nr_meta_description_diff` (integer)
- `nr_meta_description_prev` (integer)
- `nr_redirect_chain_urls` (integer)
- `nr_redirect_chain_urls_diff` (integer)
- `nr_redirect_chain_urls_prev` (integer)
- `nr_titles` (integer)
- `nr_titles_diff` (integer)
- `nr_titles_prev` (integer)
- `og_tags_attributes` (array(string))
- `og_tags_attributes_prev` (array(string))
- `og_tags_image` (string)
- `og_tags_image_prev` (string)
- `og_tags_image_url_invalid` (boolean)
- `og_tags_image_url_invalid_prev` (boolean)
- `og_tags_inconsistent_canonical` (boolean)
- `og_tags_inconsistent_canonical_prev` (boolean)
- `og_tags_title` (string)
- `og_tags_title_prev` (string)
- `og_tags_type` (string)
- `og_tags_type_prev` (string)
- `og_tags_url` (string)
- `og_tags_url_prev` (string)
- `og_tags_url_valid` (boolean)
- `og_tags_url_valid_prev` (boolean)
- `og_tags_valid` (boolean)
- `og_tags_valid_prev` (boolean)
- `og_tags_value` (array(string))
- `og_tags_value_prev` (array(string))
- `origin` (url)
- `origin_prev` (url)
- `page_is_nofollow` (boolean)
- `page_is_nofollow_prev` (boolean)
- `page_is_noindex` (boolean)
- `page_is_noindex_prev` (boolean)
- `page_rating` (integer)
- `page_raw_ur` (integer)
- `page_raw_ur_diff` (integer)
- `page_raw_ur_prev` (integer)
- `page_type` (array(string))
- `page_type_prev` (array(string))
- `pagination_group` (integer)
- `pagination_group_prev` (integer)
- `positions` (integer)
- `positions_diff` (integer)
- `positions_prev` (integer)
- `positions_top10` (integer)
- `positions_top10_diff` (integer)
- `positions_top10_prev` (integer)
- `positions_top3` (integer)
- `positions_top3_diff` (integer)
- `positions_top3_prev` (integer)
- `psi_crux_cls_category` (string)
- `psi_crux_cls_category_prev` (string)
- `psi_crux_cls_distributions_proportion` (array(null))
- `psi_crux_cls_distributions_proportion_prev` (array(null))
- `psi_crux_cls_percentile` (float)
- `psi_crux_cls_percentile_diff` (integer)
- `psi_crux_cls_percentile_prev` (float)
- `psi_crux_fid_category` (string)
- `psi_crux_fid_category_prev` (string)
- `psi_crux_fid_distributions_proportion` (array(null))
- `psi_crux_fid_distributions_proportion_prev` (array(null))
- `psi_crux_fid_percentile` (float)
- `psi_crux_fid_percentile_diff` (integer)
- `psi_crux_fid_percentile_prev` (float)
- `psi_crux_inp_category` (string)
- `psi_crux_inp_category_prev` (string)
- `psi_crux_inp_distributions_proportion` (array(null))
- `psi_crux_inp_distributions_proportion_prev` (array(null))
- `psi_crux_inp_percentile` (float)
- `psi_crux_inp_percentile_diff` (integer)
- `psi_crux_inp_percentile_prev` (float)
- `psi_crux_lcp_category` (string)
- `psi_crux_lcp_category_prev` (string)
- `psi_crux_lcp_distributions_proportion` (array(null))
- `psi_crux_lcp_distributions_proportion_prev` (array(null))
- `psi_crux_lcp_percentile` (float)
- `psi_crux_lcp_percentile_diff` (integer)
- `psi_crux_lcp_percentile_prev` (float)
- `psi_lighthouse_cls_error_message` (string)
- `psi_lighthouse_cls_error_message_prev` (string)
- `psi_lighthouse_cls_value` (float)
- `psi_lighthouse_cls_value_diff` (integer)
- `psi_lighthouse_cls_value_prev` (float)
- `psi_lighthouse_lcp_error_message` (string)
- `psi_lighthouse_lcp_error_message_prev` (string)
- `psi_lighthouse_lcp_value` (float)
- `psi_lighthouse_lcp_value_diff` (integer)
- `psi_lighthouse_lcp_value_prev` (float)
- `psi_lighthouse_score` (integer)
- `psi_lighthouse_score_diff` (integer)
- `psi_lighthouse_score_prev` (integer)
- `psi_lighthouse_tbt_error_message` (string)
- `psi_lighthouse_tbt_error_message_prev` (string)
- `psi_lighthouse_tbt_value` (float)
- `psi_lighthouse_tbt_value_diff` (integer)
- `psi_lighthouse_tbt_value_prev` (float)
- `psi_mobile_issues` (array(string))
- `psi_mobile_issues_explanations` (array(string))
- `psi_mobile_issues_explanations_prev` (array(string))
- `psi_mobile_issues_prev` (array(string))
- `psi_request_error_message` (string)
- `psi_request_error_message_prev` (string)
- `psi_request_status` (string)
- `psi_request_status_prev` (string)
- `redirect` (url)
- `redirect_chain_urls` (array(url))
- `redirect_chain_urls_code` (array(null))
- `redirect_chain_urls_no_crawl_reason` (array(null))
- `redirect_chain_urls_no_crawl_reason_prev` (array(null))
- `redirect_chain_urls_prev` (array(url))
- `redirect_code` (integer)
- `redirect_counts` (integer)
- `redirect_counts_diff` (integer)
- `redirect_counts_prev` (integer)
- `redirect_is_canonical` (boolean)
- `redirect_is_canonical_prev` (boolean)
- `redirect_no_crawl_reason` (string)
- `redirect_no_crawl_reason_prev` (string)
- `redirect_prev` (url)
- `redirect_scheme` (string)
- `redirect_scheme_prev` (string)
- `refclass_c` (integer)
- `refclass_c_diff` (integer)
- `refclass_c_prev` (integer)
- `refhosts` (integer)
- `refhosts_diff` (integer)
- `refhosts_prev` (integer)
- `refips` (integer)
- `refips_prev` (integer)
- `refpages` (integer)
- `refpages_diff` (integer)
- `refpages_prev` (integer)
- `robots_allow_rules` (array(null))
- `robots_allow_rules_prev` (array(null))
- `robots_crawl_delay` (integer)
- `robots_crawl_delay_prev` (integer)
- `robots_disallow_rules` (array(null))
- `robots_disallow_rules_prev` (array(null))
- `robots_error` (string)
- `robots_error_prev` (string)
- `robots_error_text` (string)
- `robots_error_text_prev` (string)
- `robots_redirect_loop` (array(null))
- `robots_redirect_loop_prev` (array(null))
- `robots_sitemaps` (array(null))
- `robots_sitemaps_prev` (array(null))
- `rss` (integer)
- `rss_diff` (integer)
- `rss_prev` (integer)
- `scheme` (string)
- `self_canonical` (boolean)
- `self_canonical_prev` (boolean)
- `self_hreflang` (array(null))
- `self_hreflang_code_is_valid` (array(null))
- `self_hreflang_code_is_valid_prev` (array(null))
- `self_hreflang_country` (array(null))
- `self_hreflang_country_prev` (array(null))
- `self_hreflang_language` (array(null))
- `self_hreflang_language_prev` (array(null))
- `self_hreflang_prev` (array(null))
- `serp_title` (string)
- `serp_title_prev` (string)
- `sitemap_error` (string)
- `sitemap_error_prev` (string)
- `sitemap_error_text` (string)
- `sitemap_error_text_prev` (string)
- `sitemap_is_index` (boolean)
- `sitemap_is_index_prev` (boolean)
- `sitemap_nr_urls` (integer)
- `sitemap_nr_urls_prev` (integer)
- `sitemap_save_max_size` (integer)
- `sitemap_save_max_size_diff` (integer)
- `sitemap_save_max_size_prev` (integer)
- `sitemap_unzipped_size` (integer)
- `sitemap_unzipped_size_diff` (integer)
- `sitemap_unzipped_size_prev` (integer)
- `size` (integer)
- `size_diff` (integer)
- `size_prev` (integer)
- `source` (array(string))
- `source_prev` (array(string))
- `stamp` (date)
- `stamp_prev` (date)
- `time_to_first_byte` (integer)
- `time_to_first_byte_prev` (integer)
- `title` (array(string))
- `title_prev` (array(string))
- `titles_length` (array(integer))
- `titles_length_prev` (array(integer))
- `top_keyword` (string)
- `top_keyword_position` (integer)
- `top_keyword_position_diff` (integer)
- `top_keyword_position_prev` (integer)
- `top_keyword_prev` (string)
- `traffic` (float)
- `traffic_diff` (float)
- `traffic_prev` (float)
- `url` (url)
- `url_prev` (url)

</details>

**Returns:** `list[SiteAuditPageExplorerData]`

<details>
<summary>605 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `ai_content_level` | `str \| None` | The estimated percentage of AI-generated text on the page. Possible values: `None`, `Low`, `Moderate`, `High`, `Very High` |
| `ai_content_status` | `str \| None` | AI detection status for each page. Possible values: - `Success`: Content analyzed successfully - `Content_too_short`: Not enough text for reliable detection - `Not_eligible`: URL isn't an internal HTML page - `Failed`: Internal issue prevented detection - `Detection_off`: Disabled in Crawl settings |
| `alternate` | `int \| None` | The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database) |
| `alternate_diff` | `int \| None` | The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database) |
| `alternate_prev` | `int \| None` | The number of incoming external links from rel="alternate" attributes on the pages (data from Ahrefs' Site Explorer database) |
| `backlinks` | `int \| None` | The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `backlinks_diff` | `int \| None` | The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `backlinks_prev` | `int \| None` | The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `canonical` | `str \| None` | The URL of the canonical version of the page |
| `canonical_code` | `int \| None` | The HTTP status code of the canonical URL |
| `canonical_counts` | `int \| None` | The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `canonical_counts_diff` | `int \| None` | The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `canonical_counts_prev` | `int \| None` | The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `canonical_group_hash` | `int \| None` | The ID of the group of pages that have the same canonical URL |
| `canonical_is_canonical` | `bool \| None` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `canonical_is_canonical_prev` | `bool \| None` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `canonical_no_crawl_reason` | `str \| None` | The reason why the canonical version of the page was not crawled |
| `canonical_no_crawl_reason_prev` | `str \| None` | The reason why the canonical version of the page was not crawled |
| `canonical_prev` | `str \| None` | The URL of the canonical version of the page |
| `canonical_scheme` | `str \| None` | The protocol of the canonical URL |
| `canonical_scheme_prev` | `str \| None` | The protocol of the canonical URL |
| `compliant` | `bool \| None` | Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the "rel=canonical" tag pointing to a different URL nor the "noindex" directive |
| `compliant_prev` | `bool \| None` | Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the "rel=canonical" tag pointing to a different URL nor the "noindex" directive |
| `compression` | `str \| None` | The data compression scheme |
| `compression_prev` | `str \| None` | The data compression scheme |
| `content_encoding` | `str \| None` | The Content-Encoding HTTP response header field |
| `content_encoding_prev` | `str \| None` | The Content-Encoding HTTP response header field |
| `content_length` | `int \| None` | The character length of content displayed on the page |
| `content_length_diff` | `int \| None` | The character length of content displayed on the page |
| `content_length_prev` | `int \| None` | The character length of content displayed on the page |
| `content_nr_word` | `int \| None` | The word count of content displayed on the page |
| `content_nr_word_diff` | `int \| None` | The word count of content displayed on the page |
| `content_nr_word_prev` | `int \| None` | The word count of content displayed on the page |
| `content_type` | `str \| None` | The Content-Type HTTP header of the page or resource. You can find the full list of content types [here](https://www.iana.org/assignments/media-types/media-types.xhtml) |
| `content_type_prev` | `str \| None` | The Content-Type HTTP header of the page or resource. You can find the full list of content types [here](https://www.iana.org/assignments/media-types/media-types.xhtml) |
| `css_no_crawl_reason` | `list[dict[str, Any] \| None]` | The reasons why CSS files linked from the page were not crawled |
| `css_no_crawl_reason_prev` | `list[dict[str, Any] \| None]` | The reasons why CSS files linked from the page were not crawled |
| `curl_code` | `int` | CURLcode return code. You can find the full list of CURL codes [here](https://curl.haxx.se/libcurl/c/libcurl-errors.html) |
| `depth` | `int \| None` | The minimum number of clicks required for our crawler to reach the URL from the starting point of a crawl (seed page). Please note that redirects are also counted as a level |
| `depth_diff` | `int \| None` | The minimum number of clicks required for our crawler to reach the URL from the starting point of a crawl (seed page). Please note that redirects are also counted as a level |
| `depth_prev` | `int \| None` | The minimum number of clicks required for our crawler to reach the URL from the starting point of a crawl (seed page). Please note that redirects are also counted as a level |
| `dofollow` | `int \| None` | The number of incoming external dofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `dofollow_prev` | `int \| None` | The number of incoming external dofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `domain` | `str` | The domain name part of the URL |
| `duplicate_content` | `int \| None` | The number of pages with matching or appreciably similar content |
| `duplicate_content_canonical_hreflang` | `int \| None` | The number of page groups with matching or appreciably similar content. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_content_canonical_hreflang_diff` | `int \| None` | The number of page groups with matching or appreciably similar content. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_content_canonical_hreflang_prev` | `int \| None` | The number of page groups with matching or appreciably similar content. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_content_diff` | `int \| None` | The number of pages with matching or appreciably similar content |
| `duplicate_content_prev` | `int \| None` | The number of pages with matching or appreciably similar content |
| `duplicate_description` | `int \| None` | The number of pages that have the same meta description. If the page has more than one meta description, each will be checked for duplicates |
| `duplicate_description_canonical_hreflang` | `int \| None` | The number of page groups that have the same meta description. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_description_canonical_hreflang_diff` | `int \| None` | The number of page groups that have the same meta description. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_description_canonical_hreflang_prev` | `int \| None` | The number of page groups that have the same meta description. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_description_diff` | `int \| None` | The number of pages that have the same meta description. If the page has more than one meta description, each will be checked for duplicates |
| `duplicate_description_prev` | `int \| None` | The number of pages that have the same meta description. If the page has more than one meta description, each will be checked for duplicates |
| `duplicate_group_identifier` | `int \| None` | The ID of the group of pages that are interconnected via a common canonical URL, hreflang or pagination tags |
| `duplicate_h1` | `int \| None` | The number of pages that have the same H1 subheader. If the page has more than one H1 subheader, each will be checked for duplicates |
| `duplicate_h1_diff` | `int \| None` | The number of pages that have the same H1 subheader. If the page has more than one H1 subheader, each will be checked for duplicates |
| `duplicate_h1_prev` | `int \| None` | The number of pages that have the same H1 subheader. If the page has more than one H1 subheader, each will be checked for duplicates |
| `duplicate_h1canonical_hreflang` | `int \| None` | The number of page groups sharing the same H1 subheader. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_h1canonical_hreflang_diff` | `int \| None` | The number of page groups sharing the same H1 subheader. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_h1canonical_hreflang_prev` | `int \| None` | The number of page groups sharing the same H1 subheader. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_title` | `int \| None` | The number of pages that have the same title. If the page has more than one title, each will be checked for duplicates |
| `duplicate_title_canonical_hreflang` | `int \| None` | The number of page groups that have the same title. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_title_canonical_hreflang_diff` | `int \| None` | The number of page groups that have the same title. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_title_canonical_hreflang_prev` | `int \| None` | The number of page groups that have the same title. A group includes pages united by a common canonical URL, hreflang or pagination tags |
| `duplicate_title_diff` | `int \| None` | The number of pages that have the same title. If the page has more than one title, each will be checked for duplicates |
| `duplicate_title_prev` | `int \| None` | The number of pages that have the same title. If the page has more than one title, each will be checked for duplicates |
| `edu` | `int \| None` | The number of incoming external links from .edu domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `edu_diff` | `int \| None` | The number of incoming external links from .edu domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `edu_prev` | `int \| None` | The number of incoming external links from .edu domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `external_code` | `list[dict[str, Any] \| None]` | The list of HTTP status codes returned by the external URLs linked from the page |
| `external_link_anchor` | `list[dict[str, Any] \| None]` | The list of anchor texts used in external outgoing links on the page |
| `external_link_anchor_prev` | `list[dict[str, Any] \| None]` | The list of anchor texts used in external outgoing links on the page |
| `external_link_domain` | `list[str \| None]` | The list of external domains linked to from the page |
| `external_link_domain_prev` | `list[str \| None]` | The list of external domains linked to from the page |
| `external_links` | `list[str \| None]` | The list of external outgoing links on the page |
| `external_links_is_canonical` | `list[dict[str, Any] \| None]` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `external_links_is_canonical_prev` | `list[dict[str, Any] \| None]` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `external_links_prev` | `list[str \| None]` | The list of external outgoing links on the page |
| `external_no_crawl_reason` | `list[dict[str, Any] \| None]` | The reasons why the external URLs linked from the page were not crawled |
| `external_no_crawl_reason_prev` | `list[dict[str, Any] \| None]` | The reasons why the external URLs linked from the page were not crawled |
| `external_scheme` | `list[str \| None]` | The protocols of the external outgoing links on the page |
| `external_scheme_prev` | `list[str \| None]` | The protocols of the external outgoing links on the page |
| `final_redirect` | `str \| None` | The destination of the final redirecting URL |
| `final_redirect_code` | `int \| None` | The HTTP status code of the destination of the final redirecting URL |
| `final_redirect_no_crawl_reason` | `str \| None` | The reason why the destination of the final redirecting URL was not crawled |
| `final_redirect_no_crawl_reason_prev` | `str \| None` | The reason why the destination of the final redirecting URL was not crawled |
| `final_redirect_prev` | `str \| None` | The destination of the final redirecting URL |
| `found_in_sitemaps` | `list[str \| None]` | The list of sitemaps that reference the URL |
| `found_in_sitemaps_length` | `int` | The number of sitemaps that reference the URL |
| `found_in_sitemaps_prev` | `list[str \| None]` | The list of sitemaps that reference the URL |
| `gov` | `int \| None` | The total number of incoming external links from .gov domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `gov_diff` | `int \| None` | The total number of incoming external links from .gov domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `gov_prev` | `int \| None` | The total number of incoming external links from .gov domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `h1` | `list[str \| None]` | The page H1 subheader |
| `h1_prev` | `list[str \| None]` | The page H1 subheader |
| `h1length` | `list[int \| None]` | The character length of the page H1 subheader |
| `h1length_prev` | `list[int \| None]` | The character length of the page H1 subheader |
| `h2` | `list[str \| None]` | The page H2 subheader |
| `h2_prev` | `list[str \| None]` | The page H2 subheader |
| `hash_content` | `int \| None` | The page content fingerprint. Pages with matching or appreciably similar content have the same content hash |
| `hash_descriptions` | `list[int \| None]` | meta_descriptions.hash |
| `hash_h1` | `list[int \| None]` | The page H1 subheader fingerprint. Pages with matching H1 tags have the same H1 hash |
| `hash_text` | `int \| None` | The page text fingerprint. Pages with matching content have the same text hash |
| `hash_titles` | `list[int \| None]` | The page title fingerprint. Pages with matching title tags have the same title hash |
| `hreflang` | `list[dict[str, Any] \| None]` | Data from hreflang attributes |
| `hreflang_code_is_valid` | `list[dict[str, Any] \| None]` | Indicates that hreflang data is specified properly in the hreflang tags on the page. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| `hreflang_code_is_valid_prev` | `list[dict[str, Any] \| None]` | Indicates that hreflang data is specified properly in the hreflang tags on the page. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| `hreflang_country` | `list[dict[str, Any] \| None]` | The list of regions specified in the hreflang tags on the page |
| `hreflang_country_prev` | `list[dict[str, Any] \| None]` | The list of regions specified in the hreflang tags on the page |
| `hreflang_group_hash` | `int \| None` | The ID of the group of pages that have the same set of hreflang attributes with the same set of URLs in them |
| `hreflang_inlink_urls` | `list[str \| None]` | The list of incoming URLs with hreflang attribute |
| `hreflang_inlink_urls_prev` | `list[str \| None]` | The list of incoming URLs with hreflang attribute |
| `hreflang_issues` | `list[str \| None]` | The list of hreflang-related issues a page has |
| `hreflang_issues_prev` | `list[str \| None]` | The list of hreflang-related issues a page has |
| `hreflang_language` | `list[dict[str, Any] \| None]` | The list of languages specified in the hreflang tags on the page |
| `hreflang_language_prev` | `list[dict[str, Any] \| None]` | The list of languages specified in the hreflang tags on the page |
| `hreflang_link` | `list[str \| None]` | The list of URLs specified in the hreflang tags on the page |
| `hreflang_link_is_canonical` | `list[dict[str, Any] \| None]` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `hreflang_link_is_canonical_prev` | `list[dict[str, Any] \| None]` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `hreflang_link_prev` | `list[str \| None]` | The list of URLs specified in the hreflang tags on the page |
| `hreflang_no_crawl_reason` | `list[dict[str, Any] \| None]` | The reasons why URLs specified in the hreflang tags on the page were not crawled |
| `hreflang_no_crawl_reason_prev` | `list[dict[str, Any] \| None]` | The reasons why URLs specified in the hreflang tags on the page were not crawled |
| `hreflang_pages_urls` | `list[str \| None]` | List of hreflang-linked pages URLs the page belongs to |
| `hreflang_pages_urls_count` | `int \| None` | Count of hreflang-linked pages URLs the page belongs to |
| `hreflang_pages_urls_count_diff` | `int \| None` | Count of hreflang-linked pages URLs the page belongs to |
| `hreflang_pages_urls_count_prev` | `int \| None` | Count of hreflang-linked pages URLs the page belongs to |
| `hreflang_pages_urls_prev` | `list[str \| None]` | List of hreflang-linked pages URLs the page belongs to |
| `hreflang_prev` | `list[dict[str, Any] \| None]` | Data from hreflang attributes |
| `html_lang` | `str \| None` | Data from the page's HTML lang tag |
| `html_lang_code_is_valid` | `bool \| None` | Indicates that the language (or language-region) code is specified properly in the HTML lang tag. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| `html_lang_code_is_valid_prev` | `bool \| None` | Indicates that the language (or language-region) code is specified properly in the HTML lang tag. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| `html_lang_country` | `str \| None` | The region code specified in the page's HTML lang tag |
| `html_lang_country_prev` | `str \| None` | The region code specified in the page's HTML lang tag |
| `html_lang_language` | `str \| None` | The language code specified in the page's HTML lang tag |
| `html_lang_language_prev` | `str \| None` | The language code specified in the page's HTML lang tag |
| `html_lang_prev` | `str \| None` | Data from the page's HTML lang tag |
| `http_code` | `int` | The HTTP status code returned by the URL |
| `http_header` | `list[str \| None]` | The HTTP headers that the web server returns |
| `http_header_prev` | `list[str \| None]` | The HTTP headers that the web server returns |
| `http_header_robots` | `list[str \| None]` | Instructions for web crawlers specified in HTTP headers |
| `http_header_robots_prev` | `list[str \| None]` | Instructions for web crawlers specified in HTTP headers |
| `http_headers_size` | `int` | The size of the HTTP headers that the web server returns, measured in bytes |
| `http_headers_size_diff` | `int \| None` | The size of the HTTP headers that the web server returns, measured in bytes |
| `http_headers_size_prev` | `int \| None` | The size of the HTTP headers that the web server returns, measured in bytes |
| `images_no_crawl_reason` | `list[dict[str, Any] \| None]` | The reasons why images linked from the page were not crawled |
| `images_no_crawl_reason_prev` | `list[dict[str, Any] \| None]` | The reasons why images linked from the page were not crawled |
| `incoming_all_links` | `int \| None` | The number of incoming links to the URL of all types |
| `incoming_all_links_diff` | `int \| None` | The number of incoming links to the URL of all types |
| `incoming_all_links_prev` | `int \| None` | The number of incoming links to the URL of all types |
| `incoming_canonical` | `int \| None` | Shows how many times the URL is linked to from a rel="canonical" element |
| `incoming_canonical_diff` | `int \| None` | Shows how many times the URL is linked to from a rel="canonical" element |
| `incoming_canonical_prev` | `int \| None` | Shows how many times the URL is linked to from a rel="canonical" element |
| `incoming_css` | `int \| None` | The number of incoming links to the CSS file |
| `incoming_css_diff` | `int \| None` | The number of incoming links to the CSS file |
| `incoming_css_prev` | `int \| None` | The number of incoming links to the CSS file |
| `incoming_follow` | `int \| None` | The number of incoming dofollow links to the URL from hyperlinks |
| `incoming_follow_diff` | `int \| None` | The number of incoming dofollow links to the URL from hyperlinks |
| `incoming_follow_prev` | `int \| None` | The number of incoming dofollow links to the URL from hyperlinks |
| `incoming_hreflang` | `int \| None` | Shows how many times the URL is linked to from a rel="alternate" hreflang="x" attribute |
| `incoming_hreflang_diff` | `int \| None` | Shows how many times the URL is linked to from a rel="alternate" hreflang="x" attribute |
| `incoming_hreflang_prev` | `int \| None` | Shows how many times the URL is linked to from a rel="alternate" hreflang="x" attribute |
| `incoming_image` | `int \| None` | The number of incoming links to the image file |
| `incoming_image_diff` | `int \| None` | The number of incoming links to the image file |
| `incoming_image_prev` | `int \| None` | The number of incoming links to the image file |
| `incoming_js` | `int \| None` | The number of incoming links to the JS file |
| `incoming_js_diff` | `int \| None` | The number of incoming links to the JS file |
| `incoming_js_prev` | `int \| None` | The number of incoming links to the JS file |
| `incoming_links` | `int \| None` | The number of incoming links to the URL from hyperlinks |
| `incoming_links_diff` | `int \| None` | The number of incoming links to the URL from hyperlinks |
| `incoming_links_prev` | `int \| None` | The number of incoming links to the URL from hyperlinks |
| `incoming_nofollow` | `int \| None` | The number of incoming nofollow links to the URL from hyperlinks |
| `incoming_nofollow_diff` | `int \| None` | The number of incoming nofollow links to the URL from hyperlinks |
| `incoming_nofollow_prev` | `int \| None` | The number of incoming nofollow links to the URL from hyperlinks |
| `incoming_pagination` | `int \| None` | Shows how many times the URL is linked to from rel="prev" or rel="next" elements on pages |
| `incoming_pagination_diff` | `int \| None` | Shows how many times the URL is linked to from rel="prev" or rel="next" elements on pages |
| `incoming_pagination_prev` | `int \| None` | Shows how many times the URL is linked to from rel="prev" or rel="next" elements on pages |
| `incoming_redirect` | `int \| None` | The number of incoming redirecting links to the URL |
| `incoming_redirect_diff` | `int \| None` | The number of incoming redirecting links to the URL |
| `incoming_redirect_prev` | `int \| None` | The number of incoming redirecting links to the URL |
| `indexnow_error` | `str \| None` | The error description for a failed auto-submission |
| `indexnow_error_prev` | `str \| None` | The error description for a failed auto-submission |
| `indexnow_reason` | `str \| None` | The reason the page was considered for auto-submission to IndexNow |
| `indexnow_reason_prev` | `str \| None` | The reason the page was considered for auto-submission to IndexNow |
| `indexnow_status` | `str \| None` | The status of IndexNow auto-submission. Possible values: - **Success:** The page was successfully submitted to IndexNow. - **No changes detected:** No changes were detected on the page; submission was not required. - **Not eligible:** The URL isn't eligible for submission, e.g., it's not an indexable HTML page. - **Invalid API key:** IndexNow submission failed due to an invalid API key. - **Failed:** Submission to IndexNow failed; see details for the reason. - **Auto-submission is off:** Automatic submission is disabled in Crawl settings |
| `indexnow_status_prev` | `str \| None` | The status of IndexNow auto-submission. Possible values: - **Success:** The page was successfully submitted to IndexNow. - **No changes detected:** No changes were detected on the page; submission was not required. - **Not eligible:** The URL isn't eligible for submission, e.g., it's not an indexable HTML page. - **Invalid API key:** IndexNow submission failed due to an invalid API key. - **Failed:** Submission to IndexNow failed; see details for the reason. - **Auto-submission is off:** Automatic submission is disabled in Crawl settings |
| `indexnow_submitted_at` | `str \| None` | The date and time when the URL was auto-submitted to IndexNow |
| `indexnow_submitted_at_prev` | `str \| None` | The date and time when the URL was auto-submitted to IndexNow |
| `internal_code` | `list[dict[str, Any] \| None]` | The list of HTTP status codes returned by the internal URLs linked to from the page |
| `internal_inlink_urls` | `list[str \| None]` | The list of URLs for incoming internal links |
| `internal_inlink_urls_prev` | `list[str \| None]` | The list of URLs for incoming internal links |
| `internal_link_anchor` | `list[dict[str, Any] \| None]` | The list of anchor texts used in internal outgoing links on the page |
| `internal_link_anchor_prev` | `list[dict[str, Any] \| None]` | The list of anchor texts used in internal outgoing links on the page |
| `internal_link_domain` | `list[str \| None]` | The domain (or its subdomains, depending on the scope of the crawl) linked to from internal outgoing links on the page |
| `internal_link_domain_prev` | `list[str \| None]` | The domain (or its subdomains, depending on the scope of the crawl) linked to from internal outgoing links on the page |
| `internal_links` | `list[str \| None]` | The list of internal outgoing links on the page |
| `internal_links_is_canonical` | `list[dict[str, Any] \| None]` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `internal_links_is_canonical_prev` | `list[dict[str, Any] \| None]` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `internal_links_prev` | `list[str \| None]` | The list of internal outgoing links on the page |
| `internal_no_crawl_reason` | `list[dict[str, Any] \| None]` | The reasons why the internal URLs linked to from the page were not crawled |
| `internal_no_crawl_reason_prev` | `list[dict[str, Any] \| None]` | The reasons why the internal URLs linked to from the page were not crawled |
| `internal_scheme` | `list[str \| None]` | The protocols of the internal outgoing links on the page |
| `internal_scheme_prev` | `list[str \| None]` | The protocols of the internal outgoing links on the page |
| `is_html` | `bool` | Indicates that the content type of the web document is HTML |
| `is_in_sitemap` | `bool \| None` | Indicates that the URL is included in the website's sitemap file |
| `is_in_sitemap_prev` | `bool \| None` | Indicates that the URL is included in the website's sitemap file |
| `is_page_title_used_in_serp` | `bool \| None` | Indicates that the page and SERP titles match |
| `is_redirect_loop` | `bool \| None` | Checks if the URL has a redirect loop |
| `is_redirect_loop_prev` | `bool \| None` | Checks if the URL has a redirect loop |
| `is_rendered` | `bool \| None` | Indicates that the crawler had executed JavaScript on the page to generate content |
| `is_rendered_prev` | `bool \| None` | Indicates that the crawler had executed JavaScript on the page to generate content |
| `is_valid_internal_html` | `bool` | The HTML page on the crawled domain or its subdomain that returns a 200 HTTP status code |
| `is_valid_internal_html_prev` | `bool \| None` | The HTML page on the crawled domain or its subdomain that returns a 200 HTTP status code |
| `js_no_crawl_reason` | `list[dict[str, Any] \| None]` | The reasons why JavaScript files linked from the page were not crawled |
| `js_no_crawl_reason_prev` | `list[dict[str, Any] \| None]` | The reasons why JavaScript files linked from the page were not crawled |
| `jsonld_attributes` | `list[str \| None]` | Names of the schema properties found on the page (with indices) |
| `jsonld_attributes_prev` | `list[str \| None]` | Names of the schema properties found on the page (with indices) |
| `jsonld_schema_types` | `list[str \| None]` | Schema objects found on the page |
| `jsonld_schema_types_prev` | `list[str \| None]` | Schema objects found on the page |
| `jsonld_validation_kinds` | `list[str \| None]` | Issues with the structured data found on the page |
| `jsonld_validation_kinds_prev` | `list[str \| None]` | Issues with the structured data found on the page |
| `jsonld_values` | `list[str \| None]` | Values of the schema properties found on the page |
| `jsonld_values_prev` | `list[str \| None]` | Values of the schema properties found on the page |
| `keywords` | `list[str \| None]` | The page meta keywords |
| `keywords_prev` | `list[str \| None]` | The page meta keywords |
| `length` | `int` | The character length of the URL |
| `links_count_css` | `int \| None` | The number of CSS files linked from the page |
| `links_count_css_prev` | `int \| None` | The number of CSS files linked from the page |
| `links_count_external` | `int \| None` | The number of external outgoing links on the page |
| `links_count_external3xx` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_count_external3xx_diff` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_count_external3xx_prev` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_count_external4xx` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_count_external4xx_diff` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_count_external4xx_prev` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_count_external5xx` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_count_external5xx_diff` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_count_external5xx_prev` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_count_external_diff` | `int \| None` | The number of external outgoing links on the page |
| `links_count_external_follow` | `int \| None` | The number of external outgoing dofollow links on the page |
| `links_count_external_follow_diff` | `int \| None` | The number of external outgoing dofollow links on the page |
| `links_count_external_follow_prev` | `int \| None` | The number of external outgoing dofollow links on the page |
| `links_count_external_nofollow` | `int \| None` | The number of external outgoing nofollow links on the page |
| `links_count_external_nofollow_diff` | `int \| None` | The number of external outgoing nofollow links on the page |
| `links_count_external_nofollow_prev` | `int \| None` | The number of external outgoing nofollow links on the page |
| `links_count_external_non_canonical` | `int \| None` | The number of external outgoing links on the page that point to non-canonical pages |
| `links_count_external_non_canonical_diff` | `int \| None` | The number of external outgoing links on the page that point to non-canonical pages |
| `links_count_external_non_canonical_prev` | `int \| None` | The number of external outgoing links on the page that point to non-canonical pages |
| `links_count_external_prev` | `int \| None` | The number of external outgoing links on the page |
| `links_count_external_xxx` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_count_external_xxx_diff` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_count_external_xxx_prev` | `int \| None` | The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_count_images` | `int \| None` | The number of images linked from the page |
| `links_count_images_diff` | `int \| None` | The number of images linked from the page |
| `links_count_images_prev` | `int \| None` | The number of images linked from the page |
| `links_count_images_with_alt` | `int \| None` | The number of images linked from the page that have an alt attribute (alternate text) |
| `links_count_images_with_alt_diff` | `int \| None` | The number of images linked from the page that have an alt attribute (alternate text) |
| `links_count_images_with_alt_prev` | `int \| None` | The number of images linked from the page that have an alt attribute (alternate text) |
| `links_count_images_without_alt` | `int \| None` | The number of images linked from the page that have no alt attribute (alternate text) |
| `links_count_images_without_alt_diff` | `int \| None` | The number of images linked from the page that have no alt attribute (alternate text) |
| `links_count_images_without_alt_prev` | `int \| None` | The number of images linked from the page that have no alt attribute (alternate text) |
| `links_count_internal` | `int \| None` | The number of internal outgoing links on the page |
| `links_count_internal3xx` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_count_internal3xx_diff` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_count_internal3xx_prev` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_count_internal4xx` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_count_internal4xx_diff` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_count_internal4xx_prev` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_count_internal5xx` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_count_internal5xx_diff` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_count_internal5xx_prev` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_count_internal_diff` | `int \| None` | The number of internal outgoing links on the page |
| `links_count_internal_follow` | `int \| None` | The number of internal outgoing dofollow links on the page |
| `links_count_internal_follow_diff` | `int \| None` | The number of internal outgoing dofollow links on the page |
| `links_count_internal_follow_prev` | `int \| None` | The number of internal outgoing dofollow links on the page |
| `links_count_internal_nofollow` | `int \| None` | The number of internal outgoing nofollow links on the page |
| `links_count_internal_nofollow_diff` | `int \| None` | The number of internal outgoing nofollow links on the page |
| `links_count_internal_nofollow_prev` | `int \| None` | The number of internal outgoing nofollow links on the page |
| `links_count_internal_non_canonical` | `int \| None` | The number of internal outgoing links on the page that point to non-canonical pages |
| `links_count_internal_non_canonical_diff` | `int \| None` | The number of internal outgoing links on the page that point to non-canonical pages |
| `links_count_internal_non_canonical_prev` | `int \| None` | The number of internal outgoing links on the page that point to non-canonical pages |
| `links_count_internal_prev` | `int \| None` | The number of internal outgoing links on the page |
| `links_count_internal_xxx` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_count_internal_xxx_diff` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_count_internal_xxx_prev` | `int \| None` | The number of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_count_js` | `int \| None` | The number of JavaScript files linked from the page |
| `links_count_js_diff` | `int \| None` | The number of JavaScript files linked from the page |
| `links_count_js_prev` | `int \| None` | The number of JavaScript files linked from the page |
| `links_css` | `list[str \| None]` | The list of CSS files linked from the page |
| `links_css_code` | `list[dict[str, Any] \| None]` | The list of HTTP status codes returned by CSS files linked from the page |
| `links_css_domain` | `list[str \| None]` | The list of domains that contain CSS files linked from the page |
| `links_css_domain_prev` | `list[str \| None]` | The list of domains that contain CSS files linked from the page |
| `links_css_prev` | `list[str \| None]` | The list of CSS files linked from the page |
| `links_css_scheme` | `list[str \| None]` | The protocols of CSS files linked from the page |
| `links_css_scheme_prev` | `list[str \| None]` | The protocols of CSS files linked from the page |
| `links_external3xx` | `list[str \| None]` | The list of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_external3xx_prev` | `list[str \| None]` | The list of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_external4xx` | `list[str \| None]` | The list of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_external4xx_prev` | `list[str \| None]` | The list of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_external5xx` | `list[str \| None]` | The list of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_external5xx_prev` | `list[str \| None]` | The list of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_external_follow` | `list[str \| None]` | The list of external outgoing dofollow links on the page |
| `links_external_follow_prev` | `list[str \| None]` | The list of external outgoing dofollow links on the page |
| `links_external_nofollow` | `list[str \| None]` | The list of external outgoing nofollow links on the page |
| `links_external_nofollow_prev` | `list[str \| None]` | The list of external outgoing nofollow links on the page |
| `links_external_non_canonical` | `list[str \| None]` | The list of external outgoing links on the page that point to non-canonical pages |
| `links_external_non_canonical_prev` | `list[str \| None]` | The list of external outgoing links on the page that point to non-canonical pages |
| `links_external_xxx` | `list[str \| None]` | The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_external_xxx_prev` | `list[str \| None]` | The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_hreflang_code` | `list[dict[str, Any] \| None]` | The list of HTTP status codes returned by the URLs specified in hreflang tags on the page |
| `links_images` | `list[str \| None]` | The list of images linked from the page |
| `links_images_alt` | `list[dict[str, Any] \| None]` | The list of alternate texts of images linked from the page |
| `links_images_alt_prev` | `list[dict[str, Any] \| None]` | The list of alternate texts of images linked from the page |
| `links_images_code` | `list[dict[str, Any] \| None]` | The list of HTTP status codes returned by images linked from the page |
| `links_images_domain` | `list[str \| None]` | The list of domains that contain images linked from the page |
| `links_images_domain_prev` | `list[str \| None]` | The list of domains that contain images linked from the page |
| `links_images_prev` | `list[str \| None]` | The list of images linked from the page |
| `links_images_scheme` | `list[str \| None]` | The protocols of images linked from the page |
| `links_images_scheme_prev` | `list[str \| None]` | The protocols of images linked from the page |
| `links_images_with_alt` | `list[str \| None]` | The list of images linked from the page that have an alt attribute (alternate text) |
| `links_images_with_alt_prev` | `list[str \| None]` | The list of images linked from the page that have an alt attribute (alternate text) |
| `links_images_without_alt` | `list[str \| None]` | The list of images linked from the page that have no alt attribute (alternate text) |
| `links_images_without_alt_prev` | `list[str \| None]` | The list of images linked from the page that have no alt attribute (alternate text) |
| `links_internal3xx` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_internal3xx_prev` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes |
| `links_internal4xx` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_internal4xx_prev` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes |
| `links_internal5xx` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_internal5xx_prev` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes |
| `links_internal_follow` | `list[str \| None]` | The list of internal outgoing dofollow links on the page |
| `links_internal_follow_prev` | `list[str \| None]` | The list of internal outgoing dofollow links on the page |
| `links_internal_nofollow` | `list[str \| None]` | The list of internal outgoing nofollow links on the page |
| `links_internal_nofollow_prev` | `list[str \| None]` | The list of internal outgoing nofollow links on the page |
| `links_internal_non_canonical` | `list[str \| None]` | The list of internal outgoing links on the page that point to non-canonical pages |
| `links_internal_non_canonical_prev` | `list[str \| None]` | The list of internal outgoing links on the page that point to non-canonical pages |
| `links_internal_xxx` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_internal_xxx_prev` | `list[str \| None]` | The list of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code |
| `links_js` | `list[str \| None]` | The list of JavaScript files linked from the page |
| `links_js_code` | `list[dict[str, Any] \| None]` | The list of HTTP status codes returned by JavaScript files linked from the page |
| `links_js_domain` | `list[str \| None]` | The list of domains that contain JavaScript files linked from the page |
| `links_js_domain_prev` | `list[str \| None]` | The list of domains that contain JavaScript files linked from the page |
| `links_js_prev` | `list[str \| None]` | The list of JavaScript files linked from the page |
| `links_js_scheme` | `list[str \| None]` | The protocols of JavaScript files linked from the page |
| `links_js_scheme_prev` | `list[str \| None]` | The protocols of JavaScript files linked from the page |
| `loading_time` | `int` | The time it takes for the crawler to load the full content of the document, measured in milliseconds |
| `loading_time_diff` | `int \| None` | The time it takes for the crawler to load the full content of the document, measured in milliseconds |
| `loading_time_prev` | `int \| None` | The time it takes for the crawler to load the full content of the document, measured in milliseconds |
| `meta_description` | `list[str \| None]` | Meta description |
| `meta_description_length` | `list[int \| None]` | Meta description length |
| `meta_description_length_prev` | `list[int \| None]` | Meta description length |
| `meta_description_prev` | `list[str \| None]` | Meta description |
| `meta_refresh` | `list[str \| None]` | The time set in a meta refresh tag, in seconds |
| `meta_refresh_prev` | `list[str \| None]` | The time set in a meta refresh tag, in seconds |
| `meta_robots` | `list[str \| None]` | Instructions for web crawlers specified in HTML robots meta tags on the page |
| `meta_robots_prev` | `list[str \| None]` | Instructions for web crawlers specified in HTML robots meta tags on the page |
| `meta_twitter_tags_app_google_play` | `str \| None` | The app ID in the Google Play Store specified in the twitter:app:id:ipad meta property |
| `meta_twitter_tags_app_google_play_prev` | `str \| None` | The app ID in the Google Play Store specified in the twitter:app:id:ipad meta property |
| `meta_twitter_tags_app_ipad` | `str \| None` | The app ID in the iTunes App Store specified in the twitter:app:id:ipad meta property |
| `meta_twitter_tags_app_ipad_prev` | `str \| None` | The app ID in the iTunes App Store specified in the twitter:app:id:ipad meta property |
| `meta_twitter_tags_app_iphone` | `str \| None` | The app ID in the iTunes App Store specified in the twitter:app:id:iphone meta property |
| `meta_twitter_tags_app_iphone_prev` | `str \| None` | The app ID in the iTunes App Store specified in the twitter:app:id:iphone meta property |
| `meta_twitter_tags_attributes` | `list[str \| None]` | The list of X (Twitter) Card properties on the page |
| `meta_twitter_tags_attributes_prev` | `list[str \| None]` | The list of X (Twitter) Card properties on the page |
| `meta_twitter_tags_card` | `str \| None` | The X (Twitter) Card type can be "summary", "summary_large_image", "app", or "player" |
| `meta_twitter_tags_card_prev` | `str \| None` | The X (Twitter) Card type can be "summary", "summary_large_image", "app", or "player" |
| `meta_twitter_tags_description` | `str \| None` | meta_twitter_tags.description |
| `meta_twitter_tags_description_prev` | `str \| None` | meta_twitter_tags.description |
| `meta_twitter_tags_image` | `str \| None` | The image URL specified in the twitter:image meta property |
| `meta_twitter_tags_image_prev` | `str \| None` | The image URL specified in the twitter:image meta property |
| `meta_twitter_tags_image_url_invalid` | `bool \| None` | Indicates that the URL specified in the twitter:image meta property is a valid absolute URL |
| `meta_twitter_tags_image_url_invalid_prev` | `bool \| None` | Indicates that the URL specified in the twitter:image meta property is a valid absolute URL |
| `meta_twitter_tags_player` | `str \| None` | The HTTPS URL of player iframe specified in the twitter:player meta property |
| `meta_twitter_tags_player_height` | `int \| None` | The height of iframe in pixels specified in the twitter:player:width meta property |
| `meta_twitter_tags_player_height_diff` | `int \| None` | The height of iframe in pixels specified in the twitter:player:width meta property |
| `meta_twitter_tags_player_height_prev` | `int \| None` | The height of iframe in pixels specified in the twitter:player:width meta property |
| `meta_twitter_tags_player_prev` | `str \| None` | The HTTPS URL of player iframe specified in the twitter:player meta property |
| `meta_twitter_tags_player_width` | `int \| None` | The width of iframe in pixels specified in the twitter:player:width meta property |
| `meta_twitter_tags_player_width_diff` | `int \| None` | The width of iframe in pixels specified in the twitter:player:width meta property |
| `meta_twitter_tags_player_width_prev` | `int \| None` | The width of iframe in pixels specified in the twitter:player:width meta property |
| `meta_twitter_tags_site` | `str \| None` | The X (Twitter) handle specified in the twitter:site meta property |
| `meta_twitter_tags_site_prev` | `str \| None` | The X (Twitter) handle specified in the twitter:site meta property |
| `meta_twitter_tags_title` | `str \| None` | The title text specified in the twitter:title meta property |
| `meta_twitter_tags_title_prev` | `str \| None` | The title text specified in the twitter:title meta property |
| `meta_twitter_tags_valid` | `bool \| None` | Indicates that the page has all the necessary tags required in a X (Twitter) Card |
| `meta_twitter_tags_valid_prev` | `bool \| None` | Indicates that the page has all the necessary tags required in a X (Twitter) Card |
| `meta_twitter_tags_values` | `list[str \| None]` | Data from the X (Twitter) Card properties on the page |
| `meta_twitter_tags_values_prev` | `list[str \| None]` | Data from the X (Twitter) Card properties on the page |
| `navigation_next` | `str \| None` | The URL specified in the rel="next" element on the page |
| `navigation_next_code` | `int \| None` | The HTTP status code returned by the URL specified in the rel="next" element on a page |
| `navigation_next_no_crawl_reason` | `str \| None` | The reason why the URL specified in the rel="next" element on a page was not crawled |
| `navigation_next_no_crawl_reason_prev` | `str \| None` | The reason why the URL specified in the rel="next" element on a page was not crawled |
| `navigation_next_prev` | `str \| None` | The URL specified in the rel="next" element on the page |
| `navigation_prev_code` | `int \| None` | The HTTP status code returned by the URL specified in the rel="prev" element on a page |
| `navigation_prev_no_crawl_reason` | `str \| None` | The reason why the URL specified in the rel="prev" element on a page was not crawled |
| `navigation_prev_no_crawl_reason_prev` | `str \| None` | The reason why the URL specified in the rel="prev" element on a page was not crawled |
| `no_crawl_reason` | `str \| None` | The reason why the URL was not crawled |
| `no_crawl_reason_prev` | `str \| None` | The reason why the URL was not crawled |
| `nofollow` | `int \| None` | The number of incoming external nofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `nofollow_diff` | `int \| None` | The number of incoming external nofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `nofollow_prev` | `int \| None` | The number of incoming external nofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `nr_h1` | `int` | The number of H1 subheaders on the page |
| `nr_h1_prev` | `int \| None` | The number of H1 subheaders on the page |
| `nr_meta_description` | `int` | Number of Meta descriptions |
| `nr_meta_description_diff` | `int \| None` | Number of Meta descriptions |
| `nr_meta_description_prev` | `int \| None` | Number of Meta descriptions |
| `nr_redirect_chain_urls` | `int \| None` | The number of redirect chain URLs |
| `nr_redirect_chain_urls_diff` | `int \| None` | The number of redirect chain URLs |
| `nr_redirect_chain_urls_prev` | `int \| None` | The number of redirect chain URLs |
| `nr_titles` | `int` | The number of title tags on the page |
| `nr_titles_diff` | `int \| None` | The number of title tags on the page |
| `nr_titles_prev` | `int \| None` | The number of title tags on the page |
| `og_tags_attributes` | `list[str \| None]` | The list of Open Graph properties on a page |
| `og_tags_attributes_prev` | `list[str \| None]` | The list of Open Graph properties on a page |
| `og_tags_image` | `str \| None` | The image URL specified in the og:image meta property |
| `og_tags_image_prev` | `str \| None` | The image URL specified in the og:image meta property |
| `og_tags_image_url_invalid` | `bool \| None` | Indicates that the URL specified in the og:image meta property is a valid absolute URL |
| `og_tags_image_url_invalid_prev` | `bool \| None` | Indicates that the URL specified in the og:image meta property is a valid absolute URL |
| `og_tags_inconsistent_canonical` | `bool \| None` | Indicates that the URL specified in the og:url meta property matches the URL specified as the canonical version of the page |
| `og_tags_inconsistent_canonical_prev` | `bool \| None` | Indicates that the URL specified in the og:url meta property matches the URL specified as the canonical version of the page |
| `og_tags_title` | `str \| None` | The title text specified in the og:title meta property |
| `og_tags_title_prev` | `str \| None` | The title text specified in the og:title meta property |
| `og_tags_type` | `str \| None` | The object type specified in the og:type meta property |
| `og_tags_type_prev` | `str \| None` | The object type specified in the og:type meta property |
| `og_tags_url` | `str \| None` | The URL specified in the og:url meta property |
| `og_tags_url_prev` | `str \| None` | The URL specified in the og:url meta property |
| `og_tags_url_valid` | `bool \| None` | Indicates that the URL specified in the og:url meta property is a valid absolute URL |
| `og_tags_url_valid_prev` | `bool \| None` | Indicates that the URL specified in the og:url meta property is a valid absolute URL |
| `og_tags_valid` | `bool \| None` | Indicates that the page has all four required Open Graph properties: og:title, og:type, og:image, and og:url |
| `og_tags_valid_prev` | `bool \| None` | Indicates that the page has all four required Open Graph properties: og:title, og:type, og:image, and og:url |
| `og_tags_value` | `list[str \| None]` | Data from Open Graph properties on a page |
| `og_tags_value_prev` | `list[str \| None]` | Data from Open Graph properties on a page |
| `origin` | `str \| None` | Shows where the URL was originally found during the crawl |
| `origin_prev` | `str \| None` | Shows where the URL was originally found during the crawl |
| `page_is_nofollow` | `bool \| None` | Check if the page is nofollow, based on http header and meta robots instructions |
| `page_is_nofollow_prev` | `bool \| None` | Check if the page is nofollow, based on http header and meta robots instructions |
| `page_is_noindex` | `bool \| None` | Check if the page is noindex, based on http header and meta robots instructions |
| `page_is_noindex_prev` | `bool \| None` | Check if the page is noindex, based on http header and meta robots instructions |
| `page_rating` | `int \| None` | Page Rating (PR) shows the URL's internal and external backlink profile strength relative to other URLs included in the crawl |
| `page_raw_ur` | `int \| None` | URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. [Learn more](https://help.ahrefs.com/en/articles/72658-what-is-url-rating-ur) |
| `page_raw_ur_diff` | `int \| None` | URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. [Learn more](https://help.ahrefs.com/en/articles/72658-what-is-url-rating-ur) |
| `page_raw_ur_prev` | `int \| None` | URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. [Learn more](https://help.ahrefs.com/en/articles/72658-what-is-url-rating-ur) |
| `page_type` | `list[str \| None]` | Site Audit categorizes URLs as HTML Pages, Resource files (image, CSS or JavaScript), XML Sitemaps and Robots.txt. If a page doesn't return status code 200 or has a content type that isn't covered by the categories above, it's considered as "Other". Since we can't determine what these pages are, we further classify them based on how incoming links reference them: as resources (receive resource incoming links) or as pages (receive non-resource incoming links) |
| `page_type_prev` | `list[str \| None]` | Site Audit categorizes URLs as HTML Pages, Resource files (image, CSS or JavaScript), XML Sitemaps and Robots.txt. If a page doesn't return status code 200 or has a content type that isn't covered by the categories above, it's considered as "Other". Since we can't determine what these pages are, we further classify them based on how incoming links reference them: as resources (receive resource incoming links) or as pages (receive non-resource incoming links) |
| `pagination_group` | `int \| None` | The ID of the group of pages interconnected via their rel="next" and rel="prev" links |
| `pagination_group_prev` | `int \| None` | The ID of the group of pages interconnected via their rel="next" and rel="prev" links |
| `positions` | `int \| None` | The number of keywords the page is ranking for in top 100 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_diff` | `int \| None` | The number of keywords the page is ranking for in top 100 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_prev` | `int \| None` | The number of keywords the page is ranking for in top 100 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_top10` | `int \| None` | The number of keywords the page is ranking for in top 10 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_top10_diff` | `int \| None` | The number of keywords the page is ranking for in top 10 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_top10_prev` | `int \| None` | The number of keywords the page is ranking for in top 10 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_top3` | `int \| None` | The number of keywords the page is ranking for in top 3 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_top3_diff` | `int \| None` | The number of keywords the page is ranking for in top 3 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `positions_top3_prev` | `int \| None` | The number of keywords the page is ranking for in top 3 organic search results worldwide (data from Ahrefs' Site Explorer) |
| `psi_crux_cls_category` | `str \| None` | Your CLS category will be either Good (\<0.1), Needs Improvement (0.1 - 0.25), or Poor (>0.25). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_cls_category_prev` | `str \| None` | Your CLS category will be either Good (\<0.1), Needs Improvement (0.1 - 0.25), or Poor (>0.25). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_cls_distributions_proportion` | `list[dict[str, Any] \| None]` | What % of collected CLS metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_cls_distributions_proportion_prev` | `list[dict[str, Any] \| None]` | What % of collected CLS metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_cls_percentile` | `float \| None` | Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_cls_percentile_diff` | `int \| None` | Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_cls_percentile_prev` | `float \| None` | Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_fid_category` | `str \| None` | Your FID category will be either Good (\<100 ms), Needs Improvement (100 ms - 300 ms), or Poor (>300 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_fid_category_prev` | `str \| None` | Your FID category will be either Good (\<100 ms), Needs Improvement (100 ms - 300 ms), or Poor (>300 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_fid_distributions_proportion` | `list[dict[str, Any] \| None]` | What % of collected FID metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_fid_distributions_proportion_prev` | `list[dict[str, Any] \| None]` | What % of collected FID metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_fid_percentile` | `float \| None` | First Input Delay measures interactivity. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_fid_percentile_diff` | `int \| None` | First Input Delay measures interactivity. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_fid_percentile_prev` | `float \| None` | First Input Delay measures interactivity. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_inp_category` | `str \| None` | Your INP category will be either Good (\<200 ms), Needs Improvement (200 ms - 500 ms), or Poor (>500 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://web.dev/inp/) |
| `psi_crux_inp_category_prev` | `str \| None` | Your INP category will be either Good (\<200 ms), Needs Improvement (200 ms - 500 ms), or Poor (>500 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://web.dev/inp/) |
| `psi_crux_inp_distributions_proportion` | `list[dict[str, Any] \| None]` | What % of collected INP metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://web.dev/inp/) |
| `psi_crux_inp_distributions_proportion_prev` | `list[dict[str, Any] \| None]` | What % of collected INP metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://web.dev/inp/) |
| `psi_crux_inp_percentile` | `float \| None` | Interaction to Next Paint measure overall responsiveness of a page to user interactions. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://web.dev/inp/) |
| `psi_crux_inp_percentile_diff` | `int \| None` | Interaction to Next Paint measure overall responsiveness of a page to user interactions. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://web.dev/inp/) |
| `psi_crux_inp_percentile_prev` | `float \| None` | Interaction to Next Paint measure overall responsiveness of a page to user interactions. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://web.dev/inp/) |
| `psi_crux_lcp_category` | `str \| None` | Your LCP category will be either Good (\<2.5 sec), Needs Improvement (2.5 sec - 4.0 sec), or Poor (>4.0 sec). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_lcp_category_prev` | `str \| None` | Your LCP category will be either Good (\<2.5 sec), Needs Improvement (2.5 sec - 4.0 sec), or Poor (>4.0 sec). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_lcp_distributions_proportion` | `list[dict[str, Any] \| None]` | What % of collected LCP metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_lcp_distributions_proportion_prev` | `list[dict[str, Any] \| None]` | What % of collected LCP metrics are in each associated threshold, which categorize performance as either "Good", "Needs Improvement", or "Poor". [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_lcp_percentile` | `float \| None` | Largest Contentful Paint measures visual loading performance. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_lcp_percentile_diff` | `int \| None` | Largest Contentful Paint measures visual loading performance. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_crux_lcp_percentile_prev` | `float \| None` | Largest Contentful Paint measures visual loading performance. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_cls_error_message` | `str \| None` | The message returned by Lighthouse if there is an error when measuring CLS |
| `psi_lighthouse_cls_error_message_prev` | `str \| None` | The message returned by Lighthouse if there is an error when measuring CLS |
| `psi_lighthouse_cls_value` | `float \| None` | Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_cls_value_diff` | `int \| None` | Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_cls_value_prev` | `float \| None` | Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_lcp_error_message` | `str \| None` | The message returned by Lighthouse if there is an error when measuring LCP |
| `psi_lighthouse_lcp_error_message_prev` | `str \| None` | The message returned by Lighthouse if there is an error when measuring LCP |
| `psi_lighthouse_lcp_value` | `float \| None` | Largest Contentful Paint measures visual loading performance. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_lcp_value_diff` | `int \| None` | Largest Contentful Paint measures visual loading performance. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_lcp_value_prev` | `float \| None` | Largest Contentful Paint measures visual loading performance. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_score` | `int \| None` | This score uses multiple Lighthouse speed metrics to create a summary of the page's performance and use of best practices. Scores will be considered Good (>90), Needs Improvement (50-90), or Poor (\<50). [Learn more](https://web.dev/performance-scoring/) |
| `psi_lighthouse_score_diff` | `int \| None` | This score uses multiple Lighthouse speed metrics to create a summary of the page's performance and use of best practices. Scores will be considered Good (>90), Needs Improvement (50-90), or Poor (\<50). [Learn more](https://web.dev/performance-scoring/) |
| `psi_lighthouse_score_prev` | `int \| None` | This score uses multiple Lighthouse speed metrics to create a summary of the page's performance and use of best practices. Scores will be considered Good (>90), Needs Improvement (50-90), or Poor (\<50). [Learn more](https://web.dev/performance-scoring/) |
| `psi_lighthouse_tbt_error_message` | `str \| None` | The message returned by Lighthouse if there is an error when measuring TBT |
| `psi_lighthouse_tbt_error_message_prev` | `str \| None` | The message returned by Lighthouse if there is an error when measuring TBT |
| `psi_lighthouse_tbt_value` | `float \| None` | Total Blocking Time measures the total amount of time that a page is blocked from responding to user interactions. This score comes from Lighthouse in a simulated test environment. TBT is the recommended alternative to FID for lab tests. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_tbt_value_diff` | `int \| None` | Total Blocking Time measures the total amount of time that a page is blocked from responding to user interactions. This score comes from Lighthouse in a simulated test environment. TBT is the recommended alternative to FID for lab tests. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_lighthouse_tbt_value_prev` | `float \| None` | Total Blocking Time measures the total amount of time that a page is blocked from responding to user interactions. This score comes from Lighthouse in a simulated test environment. TBT is the recommended alternative to FID for lab tests. [Learn more](https://ahrefs.com/blog/core-web-vitals/) |
| `psi_mobile_issues` | `list[str \| None]` | List of mobile-related issues on the page detected by Lighthouse |
| `psi_mobile_issues_explanations` | `list[str \| None]` | Details about the mobile issues detected by Lighthouse |
| `psi_mobile_issues_explanations_prev` | `list[str \| None]` | Details about the mobile issues detected by Lighthouse |
| `psi_mobile_issues_prev` | `list[str \| None]` | List of mobile-related issues on the page detected by Lighthouse |
| `psi_request_error_message` | `str \| None` | The message returned by PageSpeed Insights API if there is an error. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool) |
| `psi_request_error_message_prev` | `str \| None` | The message returned by PageSpeed Insights API if there is an error. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool) |
| `psi_request_status` | `str \| None` | The result of a request to PageSpeed Insights API. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool) |
| `psi_request_status_prev` | `str \| None` | The result of a request to PageSpeed Insights API. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool) |
| `redirect` | `str \| None` | The destination of the redirecting URL |
| `redirect_chain_urls` | `list[str \| None]` | The list of redirect chain URLs |
| `redirect_chain_urls_code` | `list[dict[str, Any] \| None]` | The list of HTTP status codes returned by the redirect chain URLs |
| `redirect_chain_urls_no_crawl_reason` | `list[dict[str, Any] \| None]` | The reasons why the redirect chain URLs were not crawled |
| `redirect_chain_urls_no_crawl_reason_prev` | `list[dict[str, Any] \| None]` | The reasons why the redirect chain URLs were not crawled |
| `redirect_chain_urls_prev` | `list[str \| None]` | The list of redirect chain URLs |
| `redirect_code` | `int \| None` | The HTTP status code of the destination of the redirecting URL |
| `redirect_counts` | `int \| None` | The number of incoming external links pointing to the URL via a redirect. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `redirect_counts_diff` | `int \| None` | The number of incoming external links pointing to the URL via a redirect. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `redirect_counts_prev` | `int \| None` | The number of incoming external links pointing to the URL via a redirect. Not to be confused with the number of linking pages, as one page can contain multiple backlinks |
| `redirect_is_canonical` | `bool \| None` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `redirect_is_canonical_prev` | `bool \| None` | Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical |
| `redirect_no_crawl_reason` | `str \| None` | The reason why the destination of the redirecting URL was not crawled |
| `redirect_no_crawl_reason_prev` | `str \| None` | The reason why the destination of the redirecting URL was not crawled |
| `redirect_prev` | `str \| None` | The destination of the redirecting URL |
| `redirect_scheme` | `str \| None` | The protocol of the redirecting URL |
| `redirect_scheme_prev` | `str \| None` | The protocol of the redirecting URL |
| `refclass_c` | `int \| None` | The number of IP networks that have websites with at least 1 link pointing to the URL. An IP network consists of IP addresses sharing the first three numbers of their numerical label. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the IP network |
| `refclass_c_diff` | `int \| None` | The number of IP networks that have websites with at least 1 link pointing to the URL. An IP network consists of IP addresses sharing the first three numbers of their numerical label. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the IP network |
| `refclass_c_prev` | `int \| None` | The number of IP networks that have websites with at least 1 link pointing to the URL. An IP network consists of IP addresses sharing the first three numbers of their numerical label. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the IP network |
| `refhosts` | `int \| None` | The number of unique external domains that have at least 1 link pointing to the URL (data from Ahrefs' Site Explorer database) |
| `refhosts_diff` | `int \| None` | The number of unique external domains that have at least 1 link pointing to the URL (data from Ahrefs' Site Explorer database) |
| `refhosts_prev` | `int \| None` | The number of unique external domains that have at least 1 link pointing to the URL (data from Ahrefs' Site Explorer database) |
| `refips` | `int \| None` | The number of unique external IP addresses that incorporate websites with at least 1 link pointing to the URL. Several domains can share one IP address |
| `refips_prev` | `int \| None` | The number of unique external IP addresses that incorporate websites with at least 1 link pointing to the URL. Several domains can share one IP address |
| `refpages` | `int \| None` | The number of unique external pages linking to the URL (data from Ahrefs' Site Explorer database) |
| `refpages_diff` | `int \| None` | The number of unique external pages linking to the URL (data from Ahrefs' Site Explorer database) |
| `refpages_prev` | `int \| None` | The number of unique external pages linking to the URL (data from Ahrefs' Site Explorer database) |
| `robots_allow_rules` | `list[dict[str, Any] \| None]` | Allow: rules |
| `robots_allow_rules_prev` | `list[dict[str, Any] \| None]` | Allow: rules |
| `robots_crawl_delay` | `int \| None` | Crawl-delay: |
| `robots_crawl_delay_prev` | `int \| None` | Crawl-delay: |
| `robots_disallow_rules` | `list[dict[str, Any] \| None]` | Disallow: rules |
| `robots_disallow_rules_prev` | `list[dict[str, Any] \| None]` | Disallow: rules |
| `robots_error` | `str \| None` | The error occurred while crawling the robots.txt file |
| `robots_error_prev` | `str \| None` | The error occurred while crawling the robots.txt file |
| `robots_error_text` | `str \| None` | Robots.txt error text |
| `robots_error_text_prev` | `str \| None` | Robots.txt error text |
| `robots_redirect_loop` | `list[dict[str, Any] \| None]` | Robots.txt error redirect loop |
| `robots_redirect_loop_prev` | `list[dict[str, Any] \| None]` | Robots.txt error redirect loop |
| `robots_sitemaps` | `list[dict[str, Any] \| None]` | The list of sitemaps referenced in the robots.txt file |
| `robots_sitemaps_prev` | `list[dict[str, Any] \| None]` | The list of sitemaps referenced in the robots.txt file |
| `rss` | `int \| None` | The number of incoming external links from RSS feeds (data from Ahrefs' Site Explorer database) |
| `rss_diff` | `int \| None` | The number of incoming external links from RSS feeds (data from Ahrefs' Site Explorer database) |
| `rss_prev` | `int \| None` | The number of incoming external links from RSS feeds (data from Ahrefs' Site Explorer database) |
| `scheme` | `str` | Hypertext Transfer Protocol of the URL (HTTP or HTTPS) |
| `self_canonical` | `bool \| None` | Indicates that the page has a self-referential canonical URL |
| `self_canonical_prev` | `bool \| None` | Indicates that the page has a self-referential canonical URL |
| `self_hreflang` | `list[dict[str, Any] \| None]` | Data from hreflang tag with a self-referential URL |
| `self_hreflang_code_is_valid` | `list[dict[str, Any] \| None]` | Indicates that hreflang data is specified properly in hreflang tag with a self-referential URL. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| `self_hreflang_code_is_valid_prev` | `list[dict[str, Any] \| None]` | Indicates that hreflang data is specified properly in hreflang tag with a self-referential URL. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| `self_hreflang_country` | `list[dict[str, Any] \| None]` | The region specified in the hreflang tag with a self-referential URL |
| `self_hreflang_country_prev` | `list[dict[str, Any] \| None]` | The region specified in the hreflang tag with a self-referential URL |
| `self_hreflang_language` | `list[dict[str, Any] \| None]` | The language specified in the hreflang tag with a self-referential URL |
| `self_hreflang_language_prev` | `list[dict[str, Any] \| None]` | The language specified in the hreflang tag with a self-referential URL |
| `self_hreflang_prev` | `list[dict[str, Any] \| None]` | Data from hreflang tag with a self-referential URL |
| `serp_title` | `str \| None` | The title displayed for the page in its top keyword's SERP on desktop |
| `serp_title_prev` | `str \| None` | The title displayed for the page in its top keyword's SERP on desktop |
| `sitemap_error` | `str \| None` | The error occurred while crawling the sitemap |
| `sitemap_error_prev` | `str \| None` | The error occurred while crawling the sitemap |
| `sitemap_error_text` | `str \| None` | Sitemap error text |
| `sitemap_error_text_prev` | `str \| None` | Sitemap error text |
| `sitemap_is_index` | `bool \| None` | Indicates that the sitemap is a sitemap index file |
| `sitemap_is_index_prev` | `bool \| None` | Indicates that the sitemap is a sitemap index file |
| `sitemap_nr_urls` | `int \| None` | The number of URLs referenced in the sitemap |
| `sitemap_nr_urls_prev` | `int \| None` | The number of URLs referenced in the sitemap |
| `sitemap_save_max_size` | `int \| None` | Max size of sitemap allows content to be saved |
| `sitemap_save_max_size_diff` | `int \| None` | Max size of sitemap allows content to be saved |
| `sitemap_save_max_size_prev` | `int \| None` | Max size of sitemap allows content to be saved |
| `sitemap_unzipped_size` | `int \| None` | Sitemap size (uncompressed) |
| `sitemap_unzipped_size_diff` | `int \| None` | Sitemap size (uncompressed) |
| `sitemap_unzipped_size_prev` | `int \| None` | Sitemap size (uncompressed) |
| `size` | `int` | The size of the page or resource, measured in bytes |
| `size_diff` | `int \| None` | The size of the page or resource, measured in bytes |
| `size_prev` | `int \| None` | The size of the page or resource, measured in bytes |
| `source` | `list[str \| None]` | Source from which the URL can be reached |
| `source_prev` | `list[str \| None]` | Source from which the URL can be reached |
| `stamp` | `str` | The time and date when the URL was crawled |
| `stamp_prev` | `str \| None` | The time and date when the URL was crawled |
| `time_to_first_byte` | `int` | The time it takes for the crawler to receive the first byte of the response from a web server, measured in milliseconds |
| `time_to_first_byte_prev` | `int \| None` | The time it takes for the crawler to receive the first byte of the response from a web server, measured in milliseconds |
| `title` | `list[str \| None]` | The page title |
| `title_prev` | `list[str \| None]` | The page title |
| `titles_length` | `list[int \| None]` | The character length of the page title |
| `titles_length_prev` | `list[int \| None]` | The character length of the page title |
| `top_keyword` | `str \| None` | The keyword that brings the page the most organic traffic across all countries |
| `top_keyword_position` | `int \| None` | The position that the page holds for its top keyword |
| `top_keyword_position_diff` | `int \| None` | The position that the page holds for its top keyword |
| `top_keyword_position_prev` | `int \| None` | The position that the page holds for its top keyword |
| `top_keyword_prev` | `str \| None` | The keyword that brings the page the most organic traffic across all countries |
| `traffic` | `float \| None` | Our estimate of monthly organic search traffic coming to the URL (data from Ahrefs Site Explorer). Calculations are based on a mixture of clickstream data, the estimated monthly search volumes of keywords for which the page ranks, and the current ranking position for the URL in the search results. You can learn more [here](https://ahrefs.com/blog/ahrefs-seo-metrics/#organictraffic) |
| `traffic_diff` | `float \| None` | Our estimate of monthly organic search traffic coming to the URL (data from Ahrefs Site Explorer). Calculations are based on a mixture of clickstream data, the estimated monthly search volumes of keywords for which the page ranks, and the current ranking position for the URL in the search results. You can learn more [here](https://ahrefs.com/blog/ahrefs-seo-metrics/#organictraffic) |
| `traffic_prev` | `float \| None` | Our estimate of monthly organic search traffic coming to the URL (data from Ahrefs Site Explorer). Calculations are based on a mixture of clickstream data, the estimated monthly search volumes of keywords for which the page ranks, and the current ranking position for the URL in the search results. You can learn more [here](https://ahrefs.com/blog/ahrefs-seo-metrics/#organictraffic) |
| `url` | `str` | The web address of the page or resource |
| `url_prev` | `str \| None` | The web address of the page or resource |

</details>

### `site_audit_projects()`

Project Health Scores.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `date` | `str` | No | A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC. |
| `project_id` | `int` | No | The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#` |

**Returns:** `list[SiteAuditProjectsData]`

| Field | Type | Description |
|-------|------|-------------|
| `project_id` | `str` | The unique identifier of the project. |
| `project_name` | `str` | The project name. |
| `target_protocol` | `str` | The protocol of the target. Possible values: `both`, `http`, `https`. |
| `target_url` | `str` | The URL of the project's target. |
| `target_mode` | `str` | The scope of the target. Possible values: `exact`, `prefix`, `domain`, `subdomains`. |
| `date` | `str \| None` | The finish date and time of the last finished crawl, in GMT time zone. |
| `status` | `str \| None` | The status of the most recent finished crawl. Possible values: `Completed`, `Stopped`, `Error`, `In_progress`. |
| `health_score` | `int \| None` | Reflects the proportion of internal URLs on your site that do not have errors, based on the last finished crawl. Excludes crawls that are starting, in progress, finalizing, or were skipped. |
| `urls_with_errors` | `int \| None` | Number of internal URLs with errors |
| `urls_with_warnings` | `int \| None` | Number of internal URLs with warnings |
| `urls_with_notices` | `int \| None` | Number of internal URLs with notices |
| `total` | `int \| None` | Number of total crawled internal URLs |

______________________________________________________________________

## Site Explorer

### `site_explorer_all_backlinks()`

Backlinks.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `link_group_count`, which is not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `aggregation` | `AggregationEnum` | No | The backlinks grouping mode. |
| `history` | `str` | No | A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. |

<details>
<summary>Filterable fields (86 fields)</summary>

- `ahrefs_rank_source` (integer)
- `ahrefs_rank_target` (integer)
- `alt` (string)
- `anchor` (string)
- `broken_redirect_new_target` (string)
- `broken_redirect_reason` (string)
- `broken_redirect_source` (string)
- `class_c` (integer)
- `discovered_status` (string)
- `domain_rating_source` (float)
- `domain_rating_target` (float)
- `drop_reason` (string)
- `encoding` (string)
- `first_seen` (datetime)
- `first_seen_link` (datetime)
- `http_code` (integer)
- `http_crawl` (boolean)
- `ip_source` (string)
- `is_alternate` (boolean)
- `is_canonical` (boolean)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_form` (boolean)
- `is_frame` (boolean)
- `is_homepage_link` (boolean)
- `is_image` (boolean)
- `is_lost` (boolean)
- `is_new` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_redirect` (boolean)
- `is_redirect_lost` (boolean)
- `is_root_source` (boolean)
- `is_root_target` (boolean)
- `is_rss` (boolean)
- `is_spam` (boolean)
- `is_sponsored` (boolean)
- `is_text` (boolean)
- `is_ugc` (boolean)
- `js_crawl` (boolean)
- `languages` (array(string))
- `last_seen` (datetime)
- `last_visited` (datetime)
- `len_url_redirect` (integer)
- `link_group_count` (integer)
- `link_type` (string)
- `linked_domains_source_domain` (integer)
- `linked_domains_source_page` (integer)
- `linked_domains_target_domain` (integer)
- `links_external` (integer)
- `links_internal` (integer)
- `lost_reason` (string)
- `name_source` (string)
- `name_target` (string)
- `noindex` (boolean)
- `page_category_source` (string)
- `page_size` (integer)
- `page_type_source` (string)
- `port_source` (integer)
- `port_target` (integer)
- `positions` (integer)
- `positions_source_domain` (integer)
- `powered_by` (array(string))
- `redirect_code` (integer)
- `redirect_kind` (array(integer))
- `refdomains_source` (integer)
- `refdomains_source_domain` (integer)
- `refdomains_target_domain` (integer)
- `root_name_source` (string)
- `root_name_target` (string)
- `snippet_left` (string)
- `snippet_right` (string)
- `source_page_author` (string)
- `source_page_publish_date` (date)
- `title` (string)
- `tld_class_source` (string)
- `tld_class_target` (string)
- `traffic` (integer)
- `traffic_domain` (integer)
- `url_from` (string)
- `url_from_plain` (string)
- `url_rating_source` (float)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)
- `url_to_plain` (string)

</details>

**Returns:** `list[SiteExplorerAllBacklinksData]`

<details>
<summary>82 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `ahrefs_rank_source` | `int` | The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |
| `ahrefs_rank_target` | `int` | The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |
| `alt` | `str \| None` | The alt attribute of the link. |
| `anchor` | `str` | The clickable words in a link that point to a URL. |
| `broken_redirect_new_target` | `str \| None` | The new destination of a modified redirect. |
| `broken_redirect_reason` | `BrokenRedirectReasonEnum \| None` | The reason the redirect was considered broken during the last crawl. |
| `broken_redirect_source` | `str \| None` | The redirecting URL that was modified, causing the redirect to become broken. |
| `class_c` | `int` | (5 units) The number of unique class_c subnets linking to the referring page. |
| `discovered_status` | `DiscoveredStatusEnum \| None` | The reason the link was discovered during the last crawl: the page was crawled for the first time, the link was added to the page, or the link re-appeared after being removed. |
| `domain_rating_source` | `float` | The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale. |
| `domain_rating_target` | `float` | The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale. |
| `drop_reason` | `DropReasonEnum \| None` | The reason we removed the link from our index. |
| `encoding` | `str` | The character set encoding of the referring page HTML. |
| `first_seen` | `str` | The date the referring page URL was first discovered. |
| `first_seen_link` | `str` | The date we first found a backlink to your target on a given referring page. |
| `http_code` | `int` | The return code from HTTP protocol returned during the referring page crawl. |
| `http_crawl` | `bool` | The link was discovered without executing javascript and rendering the page. |
| `ip_source` | `str \| None` | The referring domain IP address. |
| `is_alternate` | `bool` | The link with the rel=“alternate” attribute. |
| `is_canonical` | `bool` | The link with the rel=“canonical” attribute. |
| `is_content` | `bool` | The link was found in the biggest piece of content on the page. |
| `is_dofollow` | `bool` | The link has no special nofollow attribute. |
| `is_form` | `bool` | The link was found in a form HTML tag. |
| `is_frame` | `bool` | The link was found in an iframe HTML tag. |
| `is_image` | `bool` | The link is a regular link that has an image inside their href attribute. |
| `is_lost` | `bool` | The link currently does not exist anymore. |
| `is_new` | `bool` | The link was discovered on the last crawl. |
| `is_nofollow` | `bool` | The link or the referring page has the nofollow attribute set. |
| `is_redirect` | `bool` | The link pointing to your target via a redirect. |
| `is_redirect_lost` | `bool` | The redirected link currently does not exist anymore. |
| `is_root_source` | `bool` | The referring domain name is a root domain name. |
| `is_root_target` | `bool` | The target domain name is a root domain name. |
| `is_rss` | `bool` | The link was found in an RSS feed. |
| `is_spam` | `bool` | Indicates whether the backlink comes from a known spammy domain. |
| `is_sponsored` | `bool` | The link has the Sponsored attribute set in the referring page HTML. |
| `is_text` | `bool` | The link is a standard href hyperlink. |
| `is_ugc` | `bool` | The link has the User Generated Content attribute set in the referring page HTML. |
| `js_crawl` | `bool` | The link was discovered after executing javascript and rendering the page. |
| `languages` | `list[str \| None]` | The languages listed in the referring page metadata or detected by the crawler to appear in the HTML. |
| `last_seen` | `str \| None` | The date we discovered that the link was lost. |
| `last_visited` | `str` | The date we last verified a live link to your target page. |
| `link_group_count` | `int` | The number of backlinks that were grouped together based on the aggregation parameter. This field cannot be used with aggregation 'all'. |
| `link_type` | `LinkTypeEnum` | The kind of the backlink. |
| `linked_domains_source_domain` | `int` | The number of unique root domains linked from the referring domain. |
| `linked_domains_source_page` | `int` | The number of unique root domains linked from the referring page. |
| `linked_domains_target_domain` | `int` | The number of unique root domains linked from the target domain. |
| `links_external` | `int` | The number of external links from the referring page. |
| `links_internal` | `int` | The number of internal links from the referring page. |
| `lost_reason` | `LostReasonEnum \| None` | The reason the link was lost during the last crawl. |
| `name_source` | `str` | The complete referring domain name, including subdomains. |
| `name_target` | `str` | The complete target domain name, including subdomains. |
| `noindex` | `bool` | The referring page has the noindex meta attribute. |
| `page_category_source` | `str \| None` | Comma-separated list of AI-predicted hierarchical category paths for the referring page. Each value is a slash-prefixed path (e.g. /Business_and_Industrial/Advertising_and_Marketing/Marketing). |
| `page_size` | `int` | The size in bytes of the referring page content. |
| `page_type_source` | `str \| None` | Comma-separated list of AI-predicted hierarchical page type paths for the referring page. Each value is a slash-prefixed path (e.g. /Article/How_to). |
| `port_source` | `int` | The network port of the referring page URL. |
| `port_target` | `int` | The network port of the target page URL. |
| `positions` | `int` | The number of keywords that the referring page ranks for in the top 100 positions. |
| `powered_by` | `list[str \| None]` | Web technologies used to build and serve the referring page content. |
| `redirect_code` | `int \| None` | The HTTP status code of a referring page pointing to your target via a redirect. |
| `redirect_kind` | `list[int \| None]` | The HTTP status codes returned by the target redirecting URL or redirect chain. |
| `refdomains_source` | `int` | (5 units) The number of unique referring domains linking to the referring page. |
| `refdomains_source_domain` | `int` | (5 units) The number of unique referring domains linking to the referring domain. |
| `refdomains_target_domain` | `int` | (5 units) The number of unique referring domains linking to the target domain. |
| `root_name_source` | `str` | The root domain name of the referring domain, not including subdomains. |
| `root_name_target` | `str` | The root domain name of the target domain, not including subdomains. |
| `snippet_left` | `str` | The snippet of text appearing just before the link. |
| `snippet_right` | `str` | The snippet of text appearing just after the link. |
| `source_page_author` | `str \| None` | The author of the referring page. |
| `source_page_publish_date` | `str \| None` | the date we identified the page was published |
| `title` | `str` | The html title of the referring page. |
| `tld_class_source` | `TldClassSourceEnum` | The top level domain class of the referring domain. |
| `tld_class_target` | `TldClassSourceEnum` | The top level domain class of the target domain. |
| `traffic` | `int` | (10 units) The referring page's estimated monthly organic traffic from search. |
| `traffic_domain` | `int` | (10 units) The referring domain's estimated monthly organic traffic from search. |
| `url_from` | `str` | The URL of the page containing a link to your target. |
| `url_from_plain` | `str` | The referring page URL optimized for use as a filter. |
| `url_rating_source` | `float` | The strength of the referring page's backlink profile compared to the others in our database on a 100-point scale. |
| `url_redirect` | `list[str \| None]` | A redirect chain the target URL of the link points to. |
| `url_redirect_with_target` | `list[str \| None]` | The target URL of the link with its redirect chain. |
| `url_to` | `str` | The URL the backlink points to. |
| `url_to_plain` | `str` | The target page URL optimized for use as a filter. |

</details>

### `site_explorer_anchors()`

Anchors.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `history` | `str` | No | A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. |

<details>
<summary>Filterable fields (44 fields)</summary>

- `anchor` (string)
- `discovered_status` (string)
- `dofollow_links` (integer)
- `domain_rating` (float)
- `drop_reason` (string)
- `first_seen` (datetime)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_homepage_link` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_root_domain` (boolean)
- `is_spam` (boolean)
- `is_sponsored` (boolean)
- `is_ugc` (boolean)
- `languages` (array(string))
- `last_seen` (datetime)
- `len_url_redirect` (integer)
- `link_type` (string)
- `linked_domains` (integer)
- `links_external` (integer)
- `links_to_target` (integer)
- `lost_links` (integer)
- `lost_reason` (string)
- `new_links` (integer)
- `noindex` (boolean)
- `positions` (integer)
- `positions_source_domain` (integer)
- `powered_by` (array(string))
- `refdomains` (integer)
- `refdomains_source` (integer)
- `refpages` (integer)
- `root_domain_name` (string)
- `snippet_left` (string)
- `snippet_right` (string)
- `source_page_author` (string)
- `title` (string)
- `top_domain_rating` (float)
- `traffic_domain` (integer)
- `traffic_page` (integer)
- `url_from` (string)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)

</details>

**Returns:** `list[SiteExplorerAnchorsData]`

| Field | Type | Description |
|-------|------|-------------|
| `anchor` | `str` | The clickable words in a link that point to a URL. |
| `dofollow_links` | `int` | The number of links with a given anchor to your target that don’t have the “nofollow” attribute. |
| `first_seen` | `str` | The date we first found a link with a given anchor to your target. |
| `is_spam` | `bool` | Indicates whether the backlink comes from a known spammy domain. |
| `last_seen` | `str \| None` | The date we discovered the last backlink with a given anchor was lost. |
| `links_to_target` | `int` | The number of inbound backlinks your target has with a given anchor. |
| `lost_links` | `int` | The number of backlinks with a given anchor lost during the selected time period. |
| `new_links` | `int` | The number of new backlinks with a given anchor found during the selected time period. |
| `refdomains` | `int` | (5 units) The number of unique domains linking to your target with a given anchor. |
| `refpages` | `int` | The number of pages containing a link with a given anchor to your target. |
| `top_domain_rating` | `float` | The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale. |

### `site_explorer_backlinks_stats()`

Backlinks stats.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |

**Returns:** `SiteExplorerBacklinksStatsData | None`

| Field | Type | Description |
|-------|------|-------------|
| `live` | `int` | The total number of links from other websites pointing to your target. |
| `all_time` | `int` | The total number of links from other websites pointing to your target for all time. |
| `live_refdomains` | `int` | (5 units) The total number of unique domains linking to your target. |
| `all_time_refdomains` | `int` | (5 units) The total number of unique domains linking to your target for all time. |

### `site_explorer_best_by_external_links()`

Best by External Links.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `http_code_target`, `languages_target`, `last_visited_target`, `powered_by_target`, `target_redirect`, `title_target`, `url_rating_target`, which are not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `history` | `str` | No | A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. |

<details>
<summary>Filterable fields (54 fields)</summary>

- `anchor` (string)
- `dofollow_to_target` (integer)
- `domain_rating_source` (float)
- `first_seen_link` (datetime)
- `http_code_source` (integer)
- `http_code_target` (integer)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_homepage_link` (boolean)
- `is_lost` (boolean)
- `is_new` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_root_source` (boolean)
- `is_spam` (boolean)
- `is_sponsored` (boolean)
- `is_ugc` (boolean)
- `languages_source` (array(string))
- `languages_target` (array(string))
- `last_seen` (datetime)
- `last_visited_source` (datetime)
- `last_visited_target` (datetime)
- `len_url_redirect` (integer)
- `link_type` (string)
- `linked_domains_source` (integer)
- `links_external_source` (integer)
- `links_to_target` (integer)
- `lost_links_to_target` (integer)
- `new_links_to_target` (integer)
- `nofollow_to_target` (integer)
- `positions_source` (integer)
- `positions_source_domain` (integer)
- `powered_by_source` (array(string))
- `powered_by_target` (array(string))
- `redirects_to_target` (integer)
- `refdomains_source` (integer)
- `refdomains_target` (integer)
- `root_name_source` (string)
- `snippet_left` (string)
- `snippet_right` (string)
- `source_page_author` (string)
- `target_redirect` (string)
- `title_source` (string)
- `title_target` (string)
- `top_domain_rating_source` (float)
- `traffic_domain_source` (integer)
- `traffic_source` (integer)
- `url_from_plain` (string)
- `url_rating_source` (float)
- `url_rating_target` (float)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)
- `url_to_plain` (string)

</details>

**Returns:** `list[SiteExplorerBestByExternalLinksData]`

| Field | Type | Description |
|-------|------|-------------|
| `dofollow_to_target` | `int` | The number of links to your target page that don’t have the “nofollow” attribute. |
| `first_seen_link` | `str` | The date we first found a link to your target. |
| `http_code_target` | `int \| None` | The return code from HTTP protocol returned during the target page crawl. |
| `is_spam` | `bool` | Indicates whether the backlink comes from a known spammy domain. |
| `languages_target` | `list[str \| None]` | The languages listed in the target page metadata or detected by the crawler to appear in the HTML. |
| `last_seen` | `str \| None` | The date your target page lost its last live link. |
| `last_visited_source` | `str` | The date we last verified a live link to your target page. |
| `last_visited_target` | `str \| None` | The date we last crawled your target page. |
| `links_to_target` | `int` | The number of inbound backlinks the target page has. |
| `lost_links_to_target` | `int` | The number of backlinks lost during the selected time period. |
| `new_links_to_target` | `int` | The number of new backlinks found during the selected time period. |
| `nofollow_to_target` | `int` | The number of links to your target page that have the “nofollow” attribute. |
| `powered_by_target` | `list[str \| None]` | Web technologies used to build and serve the target page content. |
| `redirects_to_target` | `int` | The number of inbound redirects to your target page. |
| `refdomains_target` | `int` | (5 units) The number of unique referring domains linking to the target page. |
| `target_redirect` | `str \| None` | The target's redirect if any. |
| `title_target` | `str \| None` | The html title of the target page. |
| `top_domain_rating_source` | `float` | The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale. |
| `url_rating_target` | `float \| None` | The strength of the target page's backlink profile compared to the others in our database on a 100-point scale. |
| `url_to` | `str` | The URL the backlink points to. |
| `url_to_plain` | `str` | The target page URL optimized for use as a filter. |

### `site_explorer_best_by_internal_links()`

Best by Internal Links.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `http_code_target`, `languages_target`, `last_visited_target`, `powered_by_target`, `target_redirect`, `title_target`, `url_rating_target`, which are not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

<details>
<summary>Filterable fields (48 fields)</summary>

- `anchor` (string)
- `canonical_to_target` (integer)
- `dofollow_to_target` (integer)
- `domain_rating_source` (float)
- `first_seen_link` (datetime)
- `http_code_source` (integer)
- `http_code_target` (integer)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_homepage_link` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_root_source` (boolean)
- `is_sponsored` (boolean)
- `is_ugc` (boolean)
- `languages_source` (array(string))
- `languages_target` (array(string))
- `last_seen` (datetime)
- `last_visited_source` (datetime)
- `last_visited_target` (datetime)
- `len_url_redirect` (integer)
- `link_type` (string)
- `linked_domains_source` (integer)
- `links_external_source` (integer)
- `links_to_target` (integer)
- `nofollow_to_target` (integer)
- `positions_source` (integer)
- `positions_source_domain` (integer)
- `powered_by_source` (array(string))
- `powered_by_target` (array(string))
- `redirects_to_target` (integer)
- `refdomains_source` (integer)
- `root_name_source` (string)
- `snippet_left` (string)
- `snippet_right` (string)
- `source_page_author` (string)
- `target_redirect` (string)
- `title_source` (string)
- `title_target` (string)
- `traffic_domain_source` (integer)
- `traffic_source` (integer)
- `url_from_plain` (string)
- `url_rating_source` (float)
- `url_rating_target` (float)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)
- `url_to_plain` (string)

</details>

**Returns:** `list[SiteExplorerBestByInternalLinksData]`

| Field | Type | Description |
|-------|------|-------------|
| `canonical_to_target` | `int` | The number of inbound canonical links to your target page. |
| `dofollow_to_target` | `int` | The number of links to your target page that don’t have the “nofollow” attribute. |
| `first_seen_link` | `str` | The date we first found a link to your target. |
| `http_code_target` | `int \| None` | The return code from HTTP protocol returned during the target page crawl. |
| `languages_target` | `list[str \| None]` | The languages listed in the target page metadata or detected by the crawler to appear in the HTML. |
| `last_seen` | `str \| None` | The date your target page lost its last live link. |
| `last_visited_source` | `str` | The date we last verified a live link to your target page. |
| `last_visited_target` | `str \| None` | The date we last crawled your target page. |
| `links_to_target` | `int` | The number of inbound backlinks the target page has. |
| `nofollow_to_target` | `int` | The number of links to your target page that have the “nofollow” attribute. |
| `powered_by_target` | `list[str \| None]` | Web technologies used to build and serve the target page content. |
| `redirects_to_target` | `int` | The number of inbound redirects to your target page. |
| `target_redirect` | `str \| None` | The target's redirect if any. |
| `title_target` | `str \| None` | The html title of the target page. |
| `url_rating_target` | `float \| None` | The strength of the target page's backlink profile compared to the others in our database on a 100-point scale. |
| `url_to` | `str` | The URL the backlink points to. |
| `url_to_plain` | `str` | The target page URL optimized for use as a filter. |

### `site_explorer_broken_backlinks()`

Broken Backlinks.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See the response schema for valid column identifiers, except for `http_code_target`, `last_visited_target`, `link_group_count`, which are not supported in `order_by` for this endpoint. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `aggregation` | `AggregationEnum` | No | The backlinks grouping mode. |

<details>
<summary>Filterable fields (77 fields)</summary>

- `ahrefs_rank_source` (integer)
- `ahrefs_rank_target` (integer)
- `alt` (string)
- `anchor` (string)
- `class_c` (integer)
- `domain_rating_source` (float)
- `domain_rating_target` (float)
- `encoding` (string)
- `first_seen` (datetime)
- `first_seen_link` (datetime)
- `http_code` (integer)
- `http_code_target` (integer)
- `http_crawl` (boolean)
- `ip_source` (string)
- `is_alternate` (boolean)
- `is_canonical` (boolean)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_form` (boolean)
- `is_frame` (boolean)
- `is_homepage_link` (boolean)
- `is_image` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_redirect` (boolean)
- `is_root_source` (boolean)
- `is_root_target` (boolean)
- `is_rss` (boolean)
- `is_spam` (boolean)
- `is_sponsored` (boolean)
- `is_text` (boolean)
- `is_ugc` (boolean)
- `js_crawl` (boolean)
- `languages` (array(string))
- `last_seen` (datetime)
- `last_visited` (datetime)
- `last_visited_target` (datetime)
- `len_url_redirect` (integer)
- `link_group_count` (integer)
- `link_type` (string)
- `linked_domains_source_domain` (integer)
- `linked_domains_source_page` (integer)
- `linked_domains_target_domain` (integer)
- `links_external` (integer)
- `links_internal` (integer)
- `name_source` (string)
- `name_target` (string)
- `page_category_source` (string)
- `page_size` (integer)
- `page_type_source` (string)
- `port_source` (integer)
- `port_target` (integer)
- `positions` (integer)
- `positions_source_domain` (integer)
- `powered_by` (array(string))
- `redirect_code` (integer)
- `redirect_kind` (array(integer))
- `refdomains_source` (integer)
- `refdomains_source_domain` (integer)
- `refdomains_target_domain` (integer)
- `root_name_source` (string)
- `root_name_target` (string)
- `snippet_left` (string)
- `snippet_right` (string)
- `source_page_author` (string)
- `title` (string)
- `tld_class_source` (string)
- `tld_class_target` (string)
- `traffic` (integer)
- `traffic_domain` (integer)
- `url_from` (string)
- `url_from_plain` (string)
- `url_rating_source` (float)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)
- `url_to_plain` (string)

</details>

**Returns:** `list[SiteExplorerBrokenBacklinksData]`

<details>
<summary>73 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `ahrefs_rank_source` | `int` | The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |
| `ahrefs_rank_target` | `int` | The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |
| `alt` | `str \| None` | The alt attribute of the link. |
| `anchor` | `str` | The clickable words in a link that point to a URL. |
| `class_c` | `int` | (5 units) The number of unique class_c subnets linking to the referring page. |
| `domain_rating_source` | `float` | The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale. |
| `domain_rating_target` | `float` | The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale. |
| `encoding` | `str` | The character set encoding of the referring page HTML. |
| `first_seen` | `str` | The date the referring page URL was first discovered. |
| `first_seen_link` | `str` | The date we first found a backlink to your target on a given referring page. |
| `http_code` | `int` | The return code from HTTP protocol returned during the referring page crawl. |
| `http_code_target` | `int \| None` | The return code from HTTP protocol returned during the target page crawl. |
| `http_crawl` | `bool` | The link was discovered without executing javascript and rendering the page. |
| `ip_source` | `str \| None` | The referring domain IP address. |
| `is_alternate` | `bool` | The link with the rel=“alternate” attribute. |
| `is_canonical` | `bool` | The link with the rel=“canonical” attribute. |
| `is_content` | `bool` | The link was found in the biggest piece of content on the page. |
| `is_dofollow` | `bool` | The link has no special nofollow attribute. |
| `is_form` | `bool` | The link was found in a form HTML tag. |
| `is_frame` | `bool` | The link was found in an iframe HTML tag. |
| `is_image` | `bool` | The link is a regular link that has an image inside their href attribute. |
| `is_nofollow` | `bool` | The link or the referring page has the nofollow attribute set. |
| `is_redirect` | `bool` | The link pointing to your target via a redirect. |
| `is_root_source` | `bool` | The referring domain name is a root domain name. |
| `is_root_target` | `bool` | The target domain name is a root domain name. |
| `is_rss` | `bool` | The link was found in an RSS feed. |
| `is_spam` | `bool` | Indicates whether the backlink comes from a known spammy domain. |
| `is_sponsored` | `bool` | The link has the Sponsored attribute set in the referring page HTML. |
| `is_text` | `bool` | The link is a standard href hyperlink. |
| `is_ugc` | `bool` | The link has the User Generated Content attribute set in the referring page HTML. |
| `js_crawl` | `bool` | The link was discovered after executing javascript and rendering the page. |
| `languages` | `list[str \| None]` | The languages listed in the referring page metadata or detected by the crawler to appear in the HTML. |
| `last_seen` | `str \| None` | The date we discovered that the link was lost. |
| `last_visited` | `str` | The date we last re-crawled the referring page to verify the backlink is alive. |
| `last_visited_target` | `str \| None` | The date we last re-crawled the target page to verify that it is broken. |
| `link_group_count` | `int` | The number of backlinks that were grouped together based on the aggregation parameter. This field cannot be used with aggregation 'all'. |
| `link_type` | `LinkTypeEnum` | The kind of the backlink. |
| `linked_domains_source_domain` | `int` | The number of unique root domains linked from the referring domain. |
| `linked_domains_source_page` | `int` | The number of unique root domains linked from the referring page. |
| `linked_domains_target_domain` | `int` | The number of unique root domains linked from the target domain. |
| `links_external` | `int` | The number of external links from the referring page. |
| `links_internal` | `int` | The number of internal links from the referring page. |
| `name_source` | `str` | The complete referring domain name, including subdomains. |
| `name_target` | `str` | The complete target domain name, including subdomains. |
| `page_category_source` | `str \| None` | Comma-separated list of AI-predicted hierarchical category paths for the referring page. Each value is a slash-prefixed path (e.g. /Business_and_Industrial/Advertising_and_Marketing/Marketing). |
| `page_size` | `int` | The size in bytes of the referring page content. |
| `page_type_source` | `str \| None` | Comma-separated list of AI-predicted hierarchical page type paths for the referring page. Each value is a slash-prefixed path (e.g. /Article/How_to). |
| `port_source` | `int` | The network port of the referring page URL. |
| `port_target` | `int` | The network port of the target page URL. |
| `positions` | `int` | The number of keywords that the referring page ranks for in the top 100 positions. |
| `powered_by` | `list[str \| None]` | Web technologies used to build and serve the referring page content. |
| `redirect_code` | `int \| None` | The HTTP status code of a referring page pointing to your target via a redirect. |
| `redirect_kind` | `list[int \| None]` | The HTTP status codes returned by the target redirecting URL or redirect chain. |
| `refdomains_source` | `int` | (5 units) The number of unique referring domains linking to the referring page. |
| `refdomains_source_domain` | `int` | (5 units) The number of unique referring domains linking to the referring domain. |
| `refdomains_target_domain` | `int` | (5 units) The number of unique referring domains linking to the target domain. |
| `root_name_source` | `str` | The root domain name of the referring domain, not including subdomains. |
| `root_name_target` | `str` | The root domain name of the target domain, not including subdomains. |
| `snippet_left` | `str` | The snippet of text appearing just before the link. |
| `snippet_right` | `str` | The snippet of text appearing just after the link. |
| `source_page_author` | `str \| None` | The author of the referring page. |
| `title` | `str` | The html title of the referring page. |
| `tld_class_source` | `TldClassSourceEnum` | The top level domain class of the referring domain. |
| `tld_class_target` | `TldClassSourceEnum` | The top level domain class of the target domain. |
| `traffic` | `int` | (10 units) The referring page's estimated monthly organic traffic from search. |
| `traffic_domain` | `int` | (10 units) The referring domain's estimated monthly organic traffic from search. |
| `url_from` | `str` | The URL of the page containing a link to your target. |
| `url_from_plain` | `str` | The referring page URL optimized for use as a filter. |
| `url_rating_source` | `float` | The strength of the referring page's backlink profile compared to the others in our database on a 100-point scale. |
| `url_redirect` | `list[str \| None]` | A redirect chain the target URL of the link points to. |
| `url_redirect_with_target` | `list[str \| None]` | The target URL of the link with its redirect chain. |
| `url_to` | `str` | The URL the backlink points to. |
| `url_to_plain` | `str` | The target page URL optimized for use as a filter. |

</details>

### `site_explorer_domain_rating()`

Domain rating.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |

**Returns:** `SiteExplorerDomainRatingData | None`

| Field | Type | Description |
|-------|------|-------------|
| `domain_rating` | `float` | The strength of your target's backlink profile compared to the other websites in our database on a 100-point logarithmic scale. |
| `ahrefs_rank` | `int \| None` | The strength of your target's backlink profile compared to the other websites in our database, with rank #1 being the strongest. |

### `site_explorer_domain_rating_history()`

Domain Rating history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `history_grouping` | `HistoryGroupingEnum` | No | The time interval used to group historical data. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |

**Returns:** `list[SiteExplorerDomainRatingHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `domain_rating` | `float` | The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale. |

### `site_explorer_keywords_history()`

Keywords history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `select` | `SelectStr` | No | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `history_grouping` | `HistoryGroupingEnum` | No | The time interval used to group historical data. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

**Returns:** `list[SiteExplorerKeywordsHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `top11_20` | `int` | The total number of keywords that your target ranks for in the top 11-20 organic search results. |
| `top11_plus` | `int` | The total number of keywords that your target ranks for in the top 11+ organic search results. |
| `top21_50` | `int` | The total number of keywords that your target ranks for in the top 21-50 organic search results. |
| `top3` | `int` | The total number of keywords that your target ranks for in the top 3 organic search results. |
| `top4_10` | `int` | The total number of keywords that your target ranks for in the top 4-10 organic search results. |
| `top51_plus` | `int` | The total number of keywords that your target ranks for in the top 51+ organic search results. |

### `site_explorer_linked_anchors_external()`

Outgoing external anchors.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

<details>
<summary>Filterable fields (32 fields)</summary>

- `anchor` (string)
- `dofollow_links` (integer)
- `domain` (string)
- `domain_rating` (float)
- `first_seen` (datetime)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_sponsored` (boolean)
- `is_ugc` (boolean)
- `languages` (array(string))
- `len_url_redirect` (integer)
- `link_type` (string)
- `linked_domains` (integer)
- `linked_domains_source` (integer)
- `linked_pages` (integer)
- `links_external` (integer)
- `links_from_target` (integer)
- `port_source` (integer)
- `port_target` (integer)
- `positions` (integer)
- `powered_by` (array(string))
- `refdomains_source` (integer)
- `snippet_left` (string)
- `snippet_right` (string)
- `title` (string)
- `traffic_page` (integer)
- `url_from` (string)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)

</details>

**Returns:** `list[SiteExplorerLinkedAnchorsExternalData]`

| Field | Type | Description |
|-------|------|-------------|
| `anchor` | `str` | The clickable words in a link that point to a URL. |
| `dofollow_links` | `int` | The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute. |
| `first_seen` | `str` | The date we first found a link with a given anchor on your target. |
| `linked_domains` | `int` | The number of unique domains linked from your target with a given anchor. |
| `linked_pages` | `int` | The number of unique pages linked from your target with a given anchor. |
| `links_from_target` | `int` | The number of outbound links your target has with a given anchor. |

### `site_explorer_linked_anchors_internal()`

Outgoing internal anchors.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

<details>
<summary>Filterable fields (31 fields)</summary>

- `anchor` (string)
- `dofollow_links` (integer)
- `domain` (string)
- `domain_rating` (float)
- `first_seen` (datetime)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_sponsored` (boolean)
- `is_ugc` (boolean)
- `languages` (array(string))
- `len_url_redirect` (integer)
- `link_type` (string)
- `linked_domains_source` (integer)
- `linked_pages` (integer)
- `links_external` (integer)
- `links_from_target` (integer)
- `port_source` (integer)
- `port_target` (integer)
- `positions` (integer)
- `powered_by` (array(string))
- `refdomains_source` (integer)
- `snippet_left` (string)
- `snippet_right` (string)
- `title` (string)
- `traffic_page` (integer)
- `url_from` (string)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)

</details>

**Returns:** `list[SiteExplorerLinkedAnchorsInternalData]`

| Field | Type | Description |
|-------|------|-------------|
| `anchor` | `str` | The clickable words in a link that point to a URL. |
| `dofollow_links` | `int` | The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute. |
| `first_seen` | `str` | The date we first found a link with a given anchor on your target. |
| `linked_pages` | `int` | The number of unique pages linked from your target with a given anchor. |
| `links_from_target` | `int` | The number of outbound links your target has with a given anchor. |

### `site_explorer_linkeddomains()`

Linked Domains.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

<details>
<summary>Filterable fields (36 fields)</summary>

- `anchor` (string)
- `dofollow_linked_domains` (integer)
- `dofollow_links` (integer)
- `dofollow_refdomains` (integer)
- `domain` (string)
- `domain_rating` (float)
- `first_seen` (datetime)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_root_domain` (boolean)
- `is_sponsored` (boolean)
- `is_ugc` (boolean)
- `languages` (array(string))
- `len_url_redirect` (integer)
- `link_type` (string)
- `linked_domain_traffic` (integer)
- `linked_domains` (integer)
- `linked_pages` (integer)
- `links_external` (integer)
- `links_from_target` (integer)
- `port_source` (integer)
- `port_target` (integer)
- `positions` (integer)
- `powered_by` (array(string))
- `refdomains` (integer)
- `root_domain_name` (string)
- `snippet_left` (string)
- `snippet_right` (string)
- `title` (string)
- `traffic_page` (integer)
- `url_from` (string)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)

</details>

**Returns:** `list[SiteExplorerLinkeddomainsData]`

| Field | Type | Description |
|-------|------|-------------|
| `dofollow_linked_domains` | `int` | The number of unique root domains with dofollow links linked from the linked domain. |
| `dofollow_links` | `int` | The number of links from your target to the linked domain that don’t have the “nofollow” attribute. |
| `dofollow_refdomains` | `int` | (5 units) The number of unique domains with dofollow links to the linked domain. |
| `domain` | `str` | A linked domain that has at least one link from your target. |
| `domain_rating` | `float` | The strength of a domain's backlink profile compared to the others in our database on a 100-point scale. |
| `first_seen` | `str` | The date we first found a link to the linked domain from your target. |
| `is_root_domain` | `bool` | The domain name is a root domain name. |
| `linked_domain_traffic` | `int` | (10 units) The linked domain’s estimated monthly organic traffic from search |
| `linked_pages` | `int` | The number of the domain's pages linked from your target. |
| `links_from_target` | `int` | The number of links to the linked domain from your target. |

### `site_explorer_metrics()`

Metrics.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |

**Returns:** `SiteExplorerMetricsData | None`

| Field | Type | Description |
|-------|------|-------------|
| `org_keywords` | `int` | The total number of keywords that your target ranks for in the top 100 organic search results. |
| `paid_keywords` | `int` | The total number of keywords that your target ranks for in paid search results. |
| `org_keywords_1_3` | `int` | The total number of keywords that your target ranks for in the top 3 organic search results. |
| `org_traffic` | `int` | (10 units) The estimated number of monthly visitors that your target gets from organic search. |
| `org_cost` | `int \| None` | (10 units) The estimated value of your target's monthly organic search traffic, in USD cents. |
| `paid_traffic` | `int` | (10 units) The estimated number of monthly visitors that your target gets from paid search. |
| `paid_cost` | `int \| None` | (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents. |
| `paid_pages` | `int` | The total number of pages from a target ranking in paid search results. |

### `site_explorer_metrics_by_country()`

Metrics by country.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `select` | `SelectStr` | No | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |

**Returns:** `list[SiteExplorerMetricsByCountryData]`

| Field | Type | Description |
|-------|------|-------------|
| `country` | `CountryEnum1` | |
| `org_cost` | `int \| None` | (10 units) The estimated value of your target's monthly organic search traffic, in USD cents. |
| `org_keywords` | `int` | The total number of keywords that your target ranks for in the top 100 organic search results. |
| `org_keywords_1_3` | `int` | The total number of keywords that your target ranks for in the top 3 organic search results. |
| `org_traffic` | `int` | (10 units) The estimated number of monthly visitors that your target gets from organic search. |
| `paid_cost` | `int \| None` | (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents. |
| `paid_keywords` | `int` | The total number of keywords that your target ranks for in paid search results. |
| `paid_pages` | `int` | The total number of pages from a target ranking in the top 100 paid search results. |
| `paid_traffic` | `int` | (10 units) The estimated number of monthly visitors that your target gets from paid search. |

### `site_explorer_metrics_history()`

Metrics history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `select` | `SelectStr` | No | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |
| `history_grouping` | `HistoryGroupingEnum` | No | The time interval used to group historical data. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

**Returns:** `list[SiteExplorerMetricsHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `org_cost` | `int` | (10 units) The estimated cost of your target's monthly organic search traffic, in USD cents. |
| `org_traffic` | `int` | (10 units) The estimated number of monthly visitors that your target gets from organic search. |
| `paid_cost` | `int` | (10 units) The estimated cost of your target's monthly paid search traffic, in USD cents. |
| `paid_traffic` | `int` | (10 units) The estimated number of monthly visitors that your target gets from paid search. |

### `site_explorer_organic_competitors()`

Organic competitors.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `country` | `CountryEnum` | Yes | A two-letter country code (ISO 3166-1 alpha-2). |
| `date_compared` | `DateStr` | No | A date to compare metrics with in YYYY-MM-DD format. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

<details>
<summary>Filterable fields (28 fields)</summary>

- `competitor_domain` (domain)
- `competitor_url` (url)
- `cpc_competitor` (integer)
- `cpc_target` (integer)
- `domain_rating` (float)
- `group_mode` (string)
- `keyword_difficulty_competitor` (integer)
- `keyword_difficulty_target` (integer)
- `keywords_common` (integer)
- `keywords_competitor` (integer)
- `keywords_target` (integer)
- `pages` (integer)
- `pages_diff` (integer)
- `pages_merged` (integer)
- `pages_prev` (integer)
- `share` (float)
- `traffic` (integer)
- `traffic_diff` (integer)
- `traffic_merged` (integer)
- `traffic_prev` (integer)
- `value` (integer)
- `value_diff` (integer)
- `value_merged` (integer)
- `value_prev` (integer)
- `volume_competitor` (integer)
- `volume_target` (integer)
- `words_competitor` (integer)
- `words_target` (integer)

</details>

**Returns:** `list[SiteExplorerOrganicCompetitorsData]`

| Field | Type | Description |
|-------|------|-------------|
| `competitor_domain` | `str \| None` | A competitor's domain of your target in “domains" group mode. |
| `competitor_url` | `str \| None` | A competitor's URL of your target in pages" group mode. |
| `domain_rating` | `float` | The strength of a domain's backlink profile compared to the others in our database on a 100-point scale. |
| `group_mode` | `GroupModeEnum` | To see competing pages instead, use the “exact URL” target mode or “path” target mode if your target doesn't have multiple pages. |
| `keywords_common` | `int` | Organic keywords that both your target and a competitor are ranking for. |
| `keywords_competitor` | `int` | Organic keywords that a competitor is ranking for, but your target isn't. |
| `keywords_target` | `int` | Organic keywords that your target is ranking for, but a competitor isn't. |
| `pages` | `int \| None` | The total number of pages from a target ranking in search results. |
| `pages_diff` | `int` | The change in pages between your selected dates. |
| `pages_merged` | `int` | The pages field optimized for sorting. |
| `pages_prev` | `int \| None` | The total number of pages from a target ranking in search results on the comparison date. |
| `share` | `float` | The percentage of common keywords out of the total number of keywords that your target and a competitor both rank for. |
| `traffic` | `int \| None` | (10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter. |
| `traffic_diff` | `int` | The change in traffic between your selected dates. |
| `traffic_merged` | `int` | (10 units) The traffic field optimized for sorting. |
| `traffic_prev` | `int \| None` | (10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter on the comparison date. |
| `value` | `int \| None` | (10 units) The estimated value of a page's monthly organic search traffic, in USD cents. |
| `value_diff` | `int` | The change in value between your selected dates. |
| `value_merged` | `int \| None` | (10 units) The value field optimized for sorting. |
| `value_prev` | `int \| None` | (10 units) The estimated value of a page's monthly organic search traffic, in USD cents on the comparison date. |

### `site_explorer_organic_keywords()`

Organic keywords.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `date_compared` | `DateStr` | No | A date to compare metrics with in YYYY-MM-DD format. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

<details>
<summary>Filterable fields (82 fields)</summary>

- `best_position` (integer)
- `best_position_diff` (integer)
- `best_position_has_thumbnail` (boolean)
- `best_position_has_thumbnail_prev` (boolean)
- `best_position_has_video` (boolean)
- `best_position_has_video_prev` (boolean)
- `best_position_kind` (string)
- `best_position_kind_merged` (string)
- `best_position_kind_prev` (string)
- `best_position_prev` (integer)
- `best_position_set` (string)
- `best_position_set_prev` (string)
- `best_position_url` (string)
- `best_position_url_prev` (string)
- `best_position_url_raw` (string)
- `best_position_url_raw_prev` (string)
- `cpc` (integer)
- `cpc_merged` (integer)
- `cpc_prev` (integer)
- `entities` (array(object))
- `event_entities` (array(string))
- `is_best_position_set_top_11_50` (boolean)
- `is_best_position_set_top_11_50_prev` (boolean)
- `is_best_position_set_top_3` (boolean)
- `is_best_position_set_top_3_prev` (boolean)
- `is_best_position_set_top_4_10` (boolean)
- `is_best_position_set_top_4_10_prev` (boolean)
- `is_branded` (boolean)
- `is_commercial` (boolean)
- `is_informational` (boolean)
- `is_local` (boolean)
- `is_main_position` (boolean)
- `is_main_position_prev` (boolean)
- `is_navigational` (boolean)
- `is_transactional` (boolean)
- `keyword` (string)
- `keyword_country` (string)
- `keyword_difficulty` (integer)
- `keyword_difficulty_merged` (integer)
- `keyword_difficulty_prev` (integer)
- `keyword_language` (array(string))
- `keyword_merged` (string)
- `keyword_prev` (string)
- `language` (string)
- `language_prev` (string)
- `last_update` (datetime)
- `last_update_prev` (datetime)
- `location_entities` (array(string))
- `organisation_entities` (array(string))
- `person_entities` (array(string))
- `position_kind` (string)
- `position_kind_prev` (string)
- `positions_kinds` (array(string))
- `positions_kinds_prev` (array(string))
- `product_entities` (array(string))
- `serp_features` (array(string))
- `serp_features_count` (integer)
- `serp_features_count_prev` (integer)
- `serp_features_merged` (array(string))
- `serp_features_prev` (array(string))
- `serp_target_main_positions_count` (integer)
- `serp_target_main_positions_count_prev` (integer)
- `serp_target_positions_count` (integer)
- `serp_target_positions_count_prev` (integer)
- `status` (string)
- `sum_paid_traffic` (integer)
- `sum_paid_traffic_merged` (integer)
- `sum_paid_traffic_prev` (integer)
- `sum_traffic` (integer)
- `sum_traffic_merged` (integer)
- `sum_traffic_prev` (integer)
- `title` (string)
- `title_prev` (string)
- `volume` (integer)
- `volume_desktop_pct` (float)
- `volume_merged` (integer)
- `volume_mobile_pct` (float)
- `volume_prev` (integer)
- `words` (integer)
- `words_merged` (integer)
- `words_prev` (integer)
- `work_entities` (array(string))

</details>

**Returns:** `list[SiteExplorerOrganicKeywordsData]`

<details>
<summary>68 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `all_positions` | `list[dict[str, Any] \| None]` | (5 units) The list of all positions for a keyword. |
| `all_positions_prev` | `list[dict[str, Any] \| None]` | (5 units) The list of all positions for a keyword on the comparison date. |
| `best_position` | `int \| None` | The top position your target ranks for in the organic search results for a keyword. |
| `best_position_diff` | `int \| None` | The change in position between your selected dates. |
| `best_position_has_thumbnail` | `bool \| None` | The top position has a thumbnail. |
| `best_position_has_thumbnail_prev` | `bool \| None` | The top position has a thumbnail on the comparison date. |
| `best_position_has_video` | `bool \| None` | The top position has a video. |
| `best_position_has_video_prev` | `bool \| None` | The top position has a video on the comparison date. |
| `best_position_kind` | `BestPositionKindEnum \| None` | The kind of the top position: organic, paid, or a SERP feature. |
| `best_position_kind_merged` | `BestPositionKindEnum` | The kind of the top position optimized for sorting. |
| `best_position_kind_prev` | `BestPositionKindEnum \| None` | The kind of the top position on the comparison date. |
| `best_position_prev` | `int \| None` | The top position on the comparison date. |
| `best_position_set` | `BestPositionSetEnum` | The ranking group of the top position. |
| `best_position_set_prev` | `BestPositionSetEnum \| None` | The ranking group of the top position on the comparison date. |
| `best_position_url` | `str \| None` | The ranking URL in organic search results. |
| `best_position_url_prev` | `str \| None` | The ranking URL on the comparison date. |
| `cpc` | `int \| None` | Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents. |
| `cpc_merged` | `int \| None` | The CPC field optimized for sorting. |
| `cpc_prev` | `int \| None` | The CPC metric on the comparison date. |
| `entities` | `list[dict[str, Any] \| None]` | Organizations, products, persons, works, events, and locations found in a keyword. |
| `is_best_position_set_top_11_50` | `bool` | The ranking group of the top position is 11-50. |
| `is_best_position_set_top_11_50_prev` | `bool \| None` | The ranking group of the top position was 11-50 on the comparison date. |
| `is_best_position_set_top_3` | `bool` | The ranking group of the top position is Top 3. |
| `is_best_position_set_top_3_prev` | `bool \| None` | The ranking group of the top position was Top 3 on the comparison date. |
| `is_best_position_set_top_4_10` | `bool` | The ranking group of the top position is 4-10. |
| `is_best_position_set_top_4_10_prev` | `bool \| None` | The ranking group of the top position was 4-10 on the comparison date. |
| `is_branded` | `bool` | User intent: branded. The user is searching for a specific brand or company name. |
| `is_commercial` | `bool` | User intent: commercial. The user is comparing products or services before making a purchase decision. |
| `is_informational` | `bool` | User intent: informational. The user is looking for information or an answer to a specific question. |
| `is_local` | `bool` | User intent: local. The user is looking for information relevant to a specific location or nearby services. |
| `is_navigational` | `bool` | User intent: navigational. The user is searching for a specific website or web page. |
| `is_transactional` | `bool` | User intent: transactional. The user is ready to complete an action, often a purchase. |
| `keyword` | `str \| None` | The keyword your target ranks for. |
| `keyword_country` | `CountryEnum1` | The country of a keyword your target ranks for. |
| `keyword_difficulty` | `int \| None` | (10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale. |
| `keyword_difficulty_merged` | `int \| None` | (10 units) The keyword difficulty field optimized for sorting. |
| `keyword_difficulty_prev` | `int \| None` | (10 units) The keyword difficulty on the comparison date. |
| `keyword_language` | `list[str \| None]` | The language of the search query |
| `keyword_merged` | `str` | The keyword field optimized for sorting. |
| `keyword_prev` | `str \| None` | The keyword your target ranks for on the comparison date. |
| `language` | `str` | The SERP language. |
| `language_prev` | `str \| None` | The SERP language on the comparison date. |
| `last_update` | `str` | The date when we last checked search engine results for a keyword. |
| `last_update_prev` | `str \| None` | The date when we checked search engine results up to the comparison date. |
| `serp_features` | `list[SerpFeaturesItemEnum1 \| None]` | The SERP features that appear in search results for a keyword. |
| `serp_features_count` | `int` | The number of SERP features that appear in search results for a keyword. |
| `serp_features_count_prev` | `int \| None` | The number of SERP features on the comparison date. |
| `serp_features_merged` | `list[SerpFeaturesItemEnum1 \| None]` | The SERP features field optimized for sorting. |
| `serp_features_prev` | `list[SerpFeaturesItemEnum1 \| None]` | The SERP features that appear in search results for a keyword on the comparison date. |
| `serp_target_main_positions_count` | `int` | The number of target URLs ranking for a keyword excluding positions in Sitelinks, Top stories, Image packs, and posts on X (Twitter). |
| `serp_target_main_positions_count_prev` | `int \| None` | The number of target URLs ranking for a keyword excluding positions in Sitelinks, Top stories, Image packs, and posts on X (Twitter) on the comparison date. |
| `serp_target_positions_count` | `int` | The number of target URLs ranking for a keyword. |
| `serp_target_positions_count_prev` | `int \| None` | The number of target URLs ranking for a keyword on the comparison date. |
| `status` | `StatusEnum` | The status of a page: the new page that just started to rank ("left"), the lost page that disappeared from search results ("right"), or no change ("both"). |
| `sum_paid_traffic` | `int \| None` | (10 units) An estimation of the number of monthly visits that your target gets from paid search for a keyword. |
| `sum_paid_traffic_merged` | `int` | (10 units) The paid traffic field optimized for sorting. |
| `sum_paid_traffic_prev` | `int \| None` | (10 units) The paid traffic on the comparison date. |
| `sum_traffic` | `int \| None` | (10 units) An estimation of the number of monthly visitors that your target gets from organic search for a keyword. |
| `sum_traffic_merged` | `int` | (10 units) The traffic field optimized for sorting. |
| `sum_traffic_prev` | `int \| None` | (10 units) The traffic on the comparison date. |
| `volume` | `int \| None` | (10 units) An estimation of the number of searches for a keyword over the latest month. |
| `volume_desktop_pct` | `float \| None` | The percentage of the total search volume that comes from desktop devices. |
| `volume_merged` | `int \| None` | (10 units) The search volume field optimized for sorting. |
| `volume_mobile_pct` | `float \| None` | The percentage of the total search volume that comes from mobile devices. |
| `volume_prev` | `int \| None` | (10 units) The search volume on the comparison date. |
| `words` | `int \| None` | The number of words in a keyword. |
| `words_merged` | `int` | The number of words in a keyword optimized for sorting. |
| `words_prev` | `int \| None` | The number of words in a keyword on the comparison date. |

</details>

### `site_explorer_outlinks_stats()`

Outlinks stats.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |

**Returns:** `SiteExplorerOutlinksStatsData | None`

| Field | Type | Description |
|-------|------|-------------|
| `outgoing_links` | `int` | The number of external links from the target. |
| `outgoing_links_dofollow` | `int` | The number of external dofollow links from the target. |
| `linked_domains` | `int` | The number of unique root domains linked from the target. |
| `linked_domains_dofollow` | `int` | The number of unique root domains linked via dofollow links from the target. |

### `site_explorer_pages_by_traffic()`

Pages by traffic.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

**Returns:** `SiteExplorerPagesByTrafficData | None`

| Field | Type | Description |
|-------|------|-------------|
| `range0_pages` | `int` | The total number of pages with 0 traffic. |
| `range100_traffic` | `int` | (10 units) The total traffic from pages with 1-100 traffic. |
| `range100_pages` | `int` | The total number of pages with 1-100 traffic. |
| `range1k_traffic` | `int` | (10 units) The total traffic from pages with 101-1K traffic. |
| `range1k_pages` | `int` | The total number of pages with 101-1K traffic. |
| `range5k_traffic` | `int` | (10 units) The total traffic from pages with 1K-5K traffic. |
| `range5k_pages` | `int` | The total number of pages with 1K-5K traffic. |
| `range10k_traffic` | `int` | (10 units) The total traffic from pages with 5K-10K traffic. |
| `range10k_pages` | `int` | The total number of pages with 5K-10K traffic. |
| `range10k_plus_traffic` | `int` | (10 units) The total traffic from pages with 10K+ traffic. |
| `range10k_plus_pages` | `int` | The total number of pages with 10K+ traffic. |

### `site_explorer_pages_history()`

Pages history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `history_grouping` | `HistoryGroupingEnum` | No | The time interval used to group historical data. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

**Returns:** `list[SiteExplorerPagesHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `pages` | `int` | The total number of pages from a target ranking in the top 100 organic search results. |

### `site_explorer_paid_pages()`

Paid pages.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `date_compared` | `DateStr` | No | A date to compare metrics with in YYYY-MM-DD format. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

<details>
<summary>Filterable fields (66 fields)</summary>

- `ads_count` (integer)
- `ads_count_diff` (integer)
- `ads_count_prev` (integer)
- `cpc` (integer)
- `cpc_prev` (integer)
- `description` (string)
- `description_prev` (string)
- `has_thumbnail` (boolean)
- `has_thumbnail_prev` (boolean)
- `has_video` (boolean)
- `has_video_prev` (boolean)
- `keyword` (string)
- `keyword_difficulty` (integer)
- `keyword_difficulty_prev` (integer)
- `keyword_prev` (string)
- `keywords` (integer)
- `keywords_diff` (integer)
- `keywords_diff_percent` (integer)
- `keywords_merged` (integer)
- `keywords_prev` (integer)
- `position` (integer)
- `position_kind` (string)
- `position_kind_prev` (string)
- `position_prev` (integer)
- `raw_url` (string)
- `raw_url_prev` (string)
- `referring_domains` (integer)
- `serp_features` (array(string))
- `serp_features_prev` (array(string))
- `status` (string)
- `sum_traffic` (integer)
- `sum_traffic_merged` (integer)
- `sum_traffic_prev` (integer)
- `title` (string)
- `title_prev` (string)
- `top_keyword` (string)
- `top_keyword_best_position` (integer)
- `top_keyword_best_position_diff` (integer)
- `top_keyword_best_position_kind` (string)
- `top_keyword_best_position_kind_prev` (string)
- `top_keyword_best_position_prev` (integer)
- `top_keyword_best_position_title` (string)
- `top_keyword_best_position_title_prev` (string)
- `top_keyword_country` (string)
- `top_keyword_country_prev` (string)
- `top_keyword_prev` (string)
- `top_keyword_volume` (integer)
- `top_keyword_volume_prev` (integer)
- `traffic` (integer)
- `traffic_diff` (integer)
- `traffic_diff_percent` (integer)
- `traffic_prev` (integer)
- `ur` (float)
- `url` (url)
- `url_prev` (url)
- `url_visual` (string)
- `url_visual_prev` (string)
- `value` (integer)
- `value_diff` (integer)
- `value_diff_percent` (integer)
- `value_merged` (integer)
- `value_prev` (integer)
- `volume` (integer)
- `volume_prev` (integer)
- `words` (integer)
- `words_prev` (integer)

</details>

**Returns:** `list[SiteExplorerPaidPagesData]`

<details>
<summary>38 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `ads_count` | `int \| None` | The number of unique ads with a page. |
| `ads_count_diff` | `int` | The change in ads between your selected dates. |
| `ads_count_prev` | `int \| None` | The number of ads on the comparison date. |
| `keywords` | `int \| None` | The total number of keywords that your target ranks for in paid search results. |
| `keywords_diff` | `int` | The change in keywords between your selected dates. |
| `keywords_diff_percent` | `int` | The change in keywords between your selected dates, in percents. |
| `keywords_merged` | `int` | The total number of keywords optimized for sorting. |
| `keywords_prev` | `int \| None` | The keyword your target ranks for on the comparison date. |
| `raw_url` | `str` | The ranking page URL in encoded format. |
| `raw_url_prev` | `str \| None` | The ranking page URL on the comparison date in encoded format. |
| `referring_domains` | `int \| None` | (5 units) The number of unique domains linking to a page. |
| `status` | `StatusEnum` | The status of a page: the new page that just started to rank in paid results ("left"), the lost page that disappeared from paid results ("right"), or no change ("both"). |
| `sum_traffic` | `int \| None` | (10 units) An estimation of the monthly paid search traffic that a page gets from all the keywords that it ranks for. |
| `sum_traffic_merged` | `int` | (10 units) The paid traffic field optimized for sorting. |
| `sum_traffic_prev` | `int \| None` | (10 units) The paid traffic on the comparison date. |
| `top_keyword` | `str \| None` | The keyword that brings the most paid traffic to a page. |
| `top_keyword_best_position` | `int \| None` | The ranking position that a page holds for its top keyword. |
| `top_keyword_best_position_diff` | `int \| None` | The change in the top position between your selected dates. |
| `top_keyword_best_position_kind` | `BestPositionKindEnum \| None` | The kind of the top position: organic, paid or a SERP feature. |
| `top_keyword_best_position_kind_prev` | `BestPositionKindEnum \| None` | The kind of the top position on the comparison date. |
| `top_keyword_best_position_prev` | `int \| None` | The top position on the comparison date. |
| `top_keyword_best_position_title` | `str \| None` | The title displayed for the page in its top keyword's SERP. |
| `top_keyword_best_position_title_prev` | `str \| None` | The title displayed for the page in its top keyword's SERP on the comparison date. |
| `top_keyword_country` | `CountryEnum1 \| None` | The country in which a page ranks for its top keyword. |
| `top_keyword_country_prev` | `CountryEnum1 \| None` | The country in which a page ranks for its top keyword on the comparison date. |
| `top_keyword_prev` | `str \| None` | The keyword that brings the most paid traffic to a page on the comparison date. |
| `top_keyword_volume` | `int \| None` | (10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter. |
| `top_keyword_volume_prev` | `int \| None` | (10 units) The search volume on the comparison date. |
| `traffic_diff` | `int` | The change in traffic between your selected dates. |
| `traffic_diff_percent` | `int` | The change in traffic between your selected dates, in percents. |
| `ur` | `float \| None` | URL Rating (UR) shows the strength of your target page’s backlink profile on a 100-point logarithmic scale. |
| `url` | `str \| None` | The ranking page URL. |
| `url_prev` | `str \| None` | The ranking page URL on the comparison date. |
| `value` | `int \| None` | (10 units) The estimated cost of a page's monthly paid search traffic, in USD cents. |
| `value_diff` | `int` | The change in traffic value between your selected dates. |
| `value_diff_percent` | `int` | The change in traffic value between your selected dates, in percents. |
| `value_merged` | `int \| None` | (10 units) The traffic value field optimized for sorting. |
| `value_prev` | `int \| None` | (10 units) The traffic value on the comparison date. |

</details>

### `site_explorer_refdomains()`

Refdomains.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `history` | `str` | No | A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format. |

<details>
<summary>Filterable fields (47 fields)</summary>

- `anchor` (string)
- `discovered_status` (string)
- `dofollow_linked_domains` (integer)
- `dofollow_links` (integer)
- `dofollow_refdomains` (integer)
- `domain` (string)
- `domain_rating` (float)
- `drop_reason` (string)
- `first_seen` (datetime)
- `ip_source` (string)
- `is_content` (boolean)
- `is_dofollow` (boolean)
- `is_homepage_link` (boolean)
- `is_nofollow` (boolean)
- `is_non_html` (boolean)
- `is_root_domain` (boolean)
- `is_spam` (boolean)
- `is_sponsored` (boolean)
- `is_ugc` (boolean)
- `languages` (array(string))
- `last_seen` (datetime)
- `len_url_redirect` (integer)
- `link_type` (string)
- `linked_domains` (integer)
- `links_external` (integer)
- `links_to_target` (integer)
- `lost_links` (integer)
- `lost_reason` (string)
- `new_links` (integer)
- `noindex` (boolean)
- `port_source` (integer)
- `port_target` (integer)
- `positions` (integer)
- `positions_source_domain` (integer)
- `powered_by` (array(string))
- `refdomains` (integer)
- `root_domain_name` (string)
- `snippet_left` (string)
- `snippet_right` (string)
- `source_page_author` (string)
- `title` (string)
- `traffic_domain` (integer)
- `traffic_page` (integer)
- `url_from` (string)
- `url_redirect` (array(url))
- `url_redirect_with_target` (array(string))
- `url_to` (string)

</details>

**Returns:** `list[SiteExplorerRefdomainsData]`

| Field | Type | Description |
|-------|------|-------------|
| `dofollow_linked_domains` | `int` | The number of unique root domains with dofollow links linked from the referring domain. |
| `dofollow_links` | `int` | The number of links from the referring domain to your target that don't have the “nofollow” attribute. |
| `dofollow_refdomains` | `int` | (5 units) The number of unique domains with dofollow links to the referring domain. |
| `domain` | `str` | A referring domain that has at least one link to your target. |
| `domain_rating` | `float` | The strength of a domain's backlink profile compared to the others in our database on a 100-point scale. |
| `first_seen` | `str` | The date we first found a backlink to your target from the referring domain. |
| `ip_source` | `str \| None` | The referring domain IP address. |
| `is_root_domain` | `bool` | The domain name is a root domain name. |
| `is_spam` | `bool` | Indicates whether the backlink comes from a known spammy domain. |
| `last_seen` | `str \| None` | The date your target lost its last live backlink for the referring domain. |
| `links_to_target` | `int` | The number of backlinks from the referring domain to your target. |
| `lost_links` | `int` | The number of backlinks lost from the referring domain for the selected time period. |
| `new_links` | `int` | The number of new backlinks found from the referring domain for the selected time period. |
| `positions_source_domain` | `int` | The number of keywords that the referring domain ranks for in the top 100 positions. |
| `traffic_domain` | `int` | (10 units) The referring domain's estimated monthly organic traffic from search. |

### `site_explorer_refdomains_history()`

Refdomains history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `history_grouping` | `HistoryGroupingEnum` | No | The time interval used to group historical data. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

**Returns:** `list[SiteExplorerRefdomainsHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `refdomains` | `int` | (5 units) The total number of unique domains linking to your target. |

### `site_explorer_top_pages()`

Top pages.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `int` | No | A manual timeout duration in seconds. |
| `limit` | `int` | No | The number of results to return. |
| `order_by` | `str` | No | A column to order results by. See response schema for valid column identifiers. |
| `where` | `str` | No | Filter expression ([syntax](filter-syntax.md)). Filterable fields listed below. |
| `select` | `SelectStr` | Yes | A comma-separated list of columns to return. See response schema for valid column identifiers. |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `date_compared` | `DateStr` | No | A date to compare metrics with in YYYY-MM-DD format. |
| `date` | `DateStr` | Yes | A date to report metrics on in YYYY-MM-DD format. |
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |

<details>
<summary>Filterable fields (58 fields)</summary>

- `cpc` (integer)
- `cpc_prev` (integer)
- `has_thumbnail` (boolean)
- `has_thumbnail_prev` (boolean)
- `has_video` (boolean)
- `has_video_prev` (boolean)
- `keyword` (string)
- `keyword_difficulty` (integer)
- `keyword_difficulty_prev` (integer)
- `keyword_prev` (string)
- `keywords` (integer)
- `keywords_diff` (integer)
- `keywords_diff_percent` (integer)
- `keywords_merged` (integer)
- `keywords_prev` (integer)
- `page_type` (string)
- `position` (integer)
- `position_kind` (string)
- `position_kind_prev` (string)
- `position_prev` (integer)
- `raw_url` (string)
- `raw_url_prev` (string)
- `referring_domains` (integer)
- `serp_features` (array(string))
- `serp_features_prev` (array(string))
- `status` (string)
- `sum_traffic` (integer)
- `sum_traffic_merged` (integer)
- `sum_traffic_prev` (integer)
- `top_keyword` (string)
- `top_keyword_best_position` (integer)
- `top_keyword_best_position_diff` (integer)
- `top_keyword_best_position_kind` (string)
- `top_keyword_best_position_kind_prev` (string)
- `top_keyword_best_position_prev` (integer)
- `top_keyword_best_position_title` (string)
- `top_keyword_best_position_title_prev` (string)
- `top_keyword_country` (string)
- `top_keyword_country_prev` (string)
- `top_keyword_prev` (string)
- `top_keyword_volume` (integer)
- `top_keyword_volume_prev` (integer)
- `traffic` (integer)
- `traffic_diff` (integer)
- `traffic_diff_percent` (integer)
- `traffic_prev` (integer)
- `ur` (float)
- `url` (url)
- `url_prev` (url)
- `value` (integer)
- `value_diff` (integer)
- `value_diff_percent` (integer)
- `value_merged` (integer)
- `value_prev` (integer)
- `volume` (integer)
- `volume_prev` (integer)
- `words` (integer)
- `words_prev` (integer)

</details>

**Returns:** `list[SiteExplorerTopPagesData]`

<details>
<summary>36 fields</summary>

| Field | Type | Description |
|-------|------|-------------|
| `keywords` | `int \| None` | The total number of keywords that your target ranks for in the top 100 organic search results. |
| `keywords_diff` | `int` | The change in keywords between your selected dates. |
| `keywords_diff_percent` | `int` | The change in keywords between your selected dates, in percents. |
| `keywords_merged` | `int` | The total number of keywords optimized for sorting. |
| `keywords_prev` | `int \| None` | The keyword your target ranks for on the comparison date. |
| `page_type` | `str \| None` | Comma-separated list of AI-predicted hierarchical page type paths. Each value is a slash-prefixed path (e.g. /Article/How_to). |
| `raw_url` | `str` | The ranking page URL in encoded format. |
| `raw_url_prev` | `str \| None` | The ranking page URL on the comparison date in encoded format. |
| `referring_domains` | `int \| None` | (5 units) The number of unique domains linking to a page. |
| `status` | `StatusEnum` | The status of a page: the new page that just started to rank ("left"), the lost page that disappeared from search results ("right"), or no change ("both"). |
| `sum_traffic` | `int \| None` | (10 units) An estimation of the monthly organic search traffic that a page gets from all the keywords that it ranks for. |
| `sum_traffic_merged` | `int` | (10 units) The traffic field optimized for sorting. |
| `sum_traffic_prev` | `int \| None` | (10 units) The traffic on the comparison date. |
| `top_keyword` | `str \| None` | The keyword that brings the most organic traffic to a page. |
| `top_keyword_best_position` | `int \| None` | The ranking position that a page holds for its top keyword. |
| `top_keyword_best_position_diff` | `int \| None` | The change in the top position between your selected dates. |
| `top_keyword_best_position_kind` | `BestPositionKindEnum \| None` | The kind of the top position: organic, paid or a SERP feature. |
| `top_keyword_best_position_kind_prev` | `BestPositionKindEnum \| None` | The kind of the top position on the comparison date. |
| `top_keyword_best_position_prev` | `int \| None` | The top position on the comparison date. |
| `top_keyword_best_position_title` | `str \| None` | The title displayed for the page in its top keyword's SERP. |
| `top_keyword_best_position_title_prev` | `str \| None` | The title displayed for the page in its top keyword's SERP on the comparison date. |
| `top_keyword_country` | `CountryEnum1 \| None` | The country in which a page ranks for its top keyword. |
| `top_keyword_country_prev` | `CountryEnum1 \| None` | The country in which a page ranks for its top keyword on the comparison date. |
| `top_keyword_prev` | `str \| None` | The keyword that brings the most organic traffic to a page on the comparison date. |
| `top_keyword_volume` | `int \| None` | (10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the "volume_mode" parameter. |
| `top_keyword_volume_prev` | `int \| None` | (10 units) The search volume on the comparison date. |
| `traffic_diff` | `int` | The change in traffic between your selected dates. |
| `traffic_diff_percent` | `int` | The change in traffic between your selected dates, in percents. |
| `ur` | `float \| None` | URL Rating (UR) shows the strength of your target page’s backlink profile on a 100-point logarithmic scale. |
| `url` | `str \| None` | The ranking page URL. |
| `url_prev` | `str \| None` | The ranking page URL on the comparison date. |
| `value` | `int \| None` | (10 units) The estimated value of a page's monthly organic search traffic, in USD cents. |
| `value_diff` | `int` | The change in traffic value between your selected dates. |
| `value_diff_percent` | `int` | The change in traffic value between your selected dates, in percents. |
| `value_merged` | `int \| None` | (10 units) The traffic value field optimized for sorting. |
| `value_prev` | `int \| None` | (10 units) The traffic value on the comparison date. |

</details>

### `site_explorer_total_search_volume_history()`

Total search volume history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `volume_mode` | `VolumeModeEnum` | No | The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. |
| `top_positions` | `ViewForEnum` | No | The number of top organic search positions to consider when calculating total search volume. |
| `history_grouping` | `HistoryGroupingEnum` | No | The time interval used to group historical data. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `country` | `CountryEnum` | No | A two-letter country code (ISO 3166-1 alpha-2). |
| `protocol` | `ProtocolEnum` | No | The protocol of your target. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |
| `mode` | `ModeEnum` | No | The scope of the search based on the target you entered. |

**Returns:** `list[SiteExplorerTotalSearchVolumeHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `total_search_volume` | `int` | (10 units) The total search volume of keywords for which your target ranks within the specified `top_positions` in the search results. |

### `site_explorer_url_rating_history()`

URL Rating history.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `history_grouping` | `HistoryGroupingEnum` | No | The time interval used to group historical data. |
| `date_to` | `DateStr` | No | The end date of the historical period in YYYY-MM-DD format. |
| `date_from` | `DateStr` | Yes | The start date of the historical period in YYYY-MM-DD format. |
| `target` | `str` | Yes | The target of the search: a domain or a URL. |

**Returns:** `list[SiteExplorerUrlRatingHistoryData]`

| Field | Type | Description |
|-------|------|-------------|
| `date` | `str` | |
| `url_rating` | `float` | The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale. |
