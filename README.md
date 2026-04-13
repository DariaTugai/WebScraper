# WebScraper
## Project implementation steps
### Stages 1-3
1. Provide url address of product's opinions webpage
2. Send the request to provided url adress
3. If status code is OK, fetch all opinions from requested webpage
4. For all fetched opinions, parse them to extract relevant data 
5. Check if there is next page with opinions
6. For all remaining pages repeat steps 2-5
7. Save obtained opinions

## Project inputs
### Products codes
- 100714868
- 34935197
- 174881911
- 105022684
### Product structure
|component|name|selector|
|---------|----|--------|
|opinion ID|opinion_id|[data-entry-id]|
|opinion's author|author|span.user-post__author-name|
|author's recommendation|recommendation|span.user-post__author-recommendation>em|
|score expressed in number of stars|score|span.user-post__score-count|
|opinion’s content|content|div.user-post__text|
|list of product advantages|pros|div.review-feature__item--positive|
|list of product disadvantages|cons|div.review-feature__item--negattive|
| how many users think that opinion was helpful|like|button.vote.yes > span|
| how many users think that opinion was unhelpful|dislike|button.vote.no > span|
| publishing date|publishing_date|span.user-post__published > time:nth-child(1)[datetime]|
| purchase date|purchase_date|span.user-post__published > time:nth-child(2)[datetime]|
