---
title: world
description: Learn how to retrieve global news data using the obb.news.world API.
  This documentation covers the parameters, returns, and data structures used in the
  API, including details on how to set the limit and provider, and how to filter the
  news by date, author, channels, and more. Explore the different data fields such
  as date, title, images, text, and URL, and understand the structure of the returned
  results, warnings, chart, and metadata.
keywords:
- Global News
- global news data
- obb.news.world
- parameters
- limit
- provider
- default
- benzinga
- biztoc
- fmp
- intrinio
- display
- date
- start_date
- end_date
- updated_since
- published_since
- sort
- order
- isin
- cusip
- channels
- topics
- authors
- content_types
- returns
- results
- provider
- warnings
- chart
- metadata
- data
- date
- title
- images
- text
- url
- id
- author
- teaser
- stocks
- tags
- updated
- favicon
- score
- site
- company
- datetime
- list
- dict
---


<!-- markdownlint-disable MD012 MD031 MD033 -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Global News. Global news data.

```python wordwrap
obb.news.world(limit: int = 20, provider: Literal[str] = benzinga)
```

---

## Parameters

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| limit | int | The number of data entries to return. Here its the no. of articles to return. | 20 | True |
| provider | Literal['benzinga', 'biztoc', 'fmp', 'intrinio'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'benzinga' if there is no default. | benzinga | True |
</TabItem>

<TabItem value='benzinga' label='benzinga'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| limit | int | The number of data entries to return. Here its the no. of articles to return. | 20 | True |
| provider | Literal['benzinga', 'biztoc', 'fmp', 'intrinio'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'benzinga' if there is no default. | benzinga | True |
| display | Literal['headline', 'abstract', 'full'] | Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). | full | True |
| date | str | Date of the news to retrieve. | None | True |
| start_date | str | Start date of the news to retrieve. | None | True |
| end_date | str | End date of the news to retrieve. | None | True |
| updated_since | int | Number of seconds since the news was updated. | None | True |
| published_since | int | Number of seconds since the news was published. | None | True |
| sort | Literal['id', 'created', 'updated'] | Key to sort the news by. | created | True |
| order | Literal['asc', 'desc'] | Order to sort the news by. | desc | True |
| isin | str | The ISIN of the news to retrieve. | None | True |
| cusip | str | The CUSIP of the news to retrieve. | None | True |
| channels | str | Channels of the news to retrieve. | None | True |
| topics | str | Topics of the news to retrieve. | None | True |
| authors | str | Authors of the news to retrieve. | None | True |
| content_types | str | Content types of the news to retrieve. | None | True |
</TabItem>

<TabItem value='biztoc' label='biztoc'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| limit | int | The number of data entries to return. Here its the no. of articles to return. | 20 | True |
| provider | Literal['benzinga', 'biztoc', 'fmp', 'intrinio'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'benzinga' if there is no default. | benzinga | True |
| filter | Literal['crypto', 'hot', 'latest', 'main', 'media', 'source', 'tag'] | Filter by type of news. | latest | True |
| source | str | Filter by a specific publisher. Only valid when filter is set to source. | bloomberg | True |
| tag | str | Tag, topic, to filter articles by. Only valid when filter is set to tag. | None | True |
| term | str | Search term to filter articles by. This overrides all other filters. | None | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : List[GlobalNews]
        Serializable results.

    provider : Optional[Literal['benzinga', 'biztoc', 'fmp', 'intrinio']]
        Provider name.

    warnings : Optional[List[Warning_]]
        List of warnings.

    chart : Optional[Chart]
        Chart object.

    metadata: Optional[Metadata]
        Metadata info about the command execution.
```

---

## Data

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | datetime | The date of the data. Here it is the published date of the news. |
| title | str | Title of the news. |
| images | List[Dict[str, str]] | Images associated with the news. |
| text | str | Text/body of the news. |
| url | str | URL of the news. |
</TabItem>

<TabItem value='benzinga' label='benzinga'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | datetime | The date of the data. Here it is the published date of the news. |
| title | str | Title of the news. |
| images | List[Dict[str, str]] | Images associated with the news. |
| text | str | Text/body of the news. |
| url | str | URL of the news. |
| id | str | ID of the news. |
| author | str | Author of the news. |
| teaser | str | Teaser of the news. |
| channels | str | Channels associated with the news. |
| stocks | str | Stocks associated with the news. |
| tags | str | Tags associated with the news. |
| updated | datetime | None |
</TabItem>

<TabItem value='biztoc' label='biztoc'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | datetime | The date of the data. Here it is the published date of the news. |
| title | str | Title of the news. |
| images | List[Dict[str, str]] | Images associated with the news. |
| text | str | Text/body of the news. |
| url | str | URL of the news. |
| favicon | str | Icon image for the source of the article. |
| tags | List[str] | Tags for the article. |
| id | str | Unique Article ID. |
| score | float | Search relevance score for the article. |
</TabItem>

<TabItem value='fmp' label='fmp'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | datetime | The date of the data. Here it is the published date of the news. |
| title | str | Title of the news. |
| images | List[Dict[str, str]] | Images associated with the news. |
| text | str | Text/body of the news. |
| url | str | URL of the news. |
| site | str | Site of the news. |
</TabItem>

<TabItem value='intrinio' label='intrinio'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| date | datetime | The date of the data. Here it is the published date of the news. |
| title | str | Title of the news. |
| images | List[Dict[str, str]] | Images associated with the news. |
| text | str | Text/body of the news. |
| url | str | URL of the news. |
| id | str | Article ID. |
| company | Dict[str, Any] | Company details related to the news article. |
</TabItem>

</Tabs>

