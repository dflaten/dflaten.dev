---
title: Building a Postman Replacement 
date: 2026-02-21
published: true 
---

Most developers at some point will need a tool to help test and program APIs (Application Programming Interfaces). In the past I've used Postman to help do this but overtime they added so many features I didn't use and pushed the need for creating an account to the point where I started looking for an alternative and saw the suggestion to just create your own. So that's what I did! 

### Python Based Api Explorer 
I do a lot in Python these days so it seemed the easiest way to go for creating my tool. Dependencies are pretty limited using the primarily the  `requests` library and `urllib3` plus a couple other related dependencies. 

Installing is simple, just requires [uv](https://docs.astral.sh/uv/) to install: `uv sync`.

You can use the tool like: `uv run api-cli my_api_config.json get_users` after defining the config file to make requests.

As I find new things I want to be able to do with it such as automatically updating the config when I'm requesting a new token I do so.

This gives me an easy way to explore an API which won't change unless I need it to. 


### In use
So here I'll outline how I used the tool to connect to `newsapi.org` which provides free keys for developers.

Config:
```json
  "base_url": "https://newsapi.org/v2/",
  "timeout": 30,
  "default_headers": {
    "Content-Type": "application/json",
    "X-API-KEY": "REDACTED"
  },
  "endpoints": {
    "top_headlines": {
      "method": "GET",
      "path": "top-headlines",
      "params": {
        "country": "us"
      }
    }
  }
```


Running: `uv run api-cli newsapi_config.json top_headlines`

Gets me a response like (I redacted most of the response to save on length): 

```json
{
  "status": "ok",
  "totalResults": 36,
  "articles": [
    {
      "source": {
        "id": "the-washington-post",
        "name": "The Washington Post"
      },
      "author": "Ben Noll",
      "title": "See where snow could be measured in inches \u2014 or feet \u2014 in the East this weekend - The Washington Post",
      "description": "A strong nor\u2019easter is expected to form near the Mid-Atlantic coast on Sunday, threatening to bring accumulating snow, strong winds and travel disruptions.",
      "url": "https://www.washingtonpost.com/weather/2026/02/20/noreaster-snow-forecast-midatlantic-northeast/",
      "urlToImage": "https://www.washingtonpost.com/wp-apps/imrs.php?src=https://cloudfront-us-east-1.images.arcpublishing.com/wapo/3YOZVIMA2RG37ELCO6NPTKXXZM.png&w=1440",
      "publishedAt": "2026-02-20T18:32:02Z",
      "content": "A strong noreaster is expected to form near the Mid-Atlantic coast on Sunday, threatening to bring accumulating snow, strong winds and travel disruptions to the densely populated corridor from D.C. t\u2026 [+20 chars]"
    },
    {
      "source": {
        "id": "cnn",
        "name": "CNN"
      },
      "author": "Abby Phillip, Manu Raju",
      "title": "House Speaker Johnson rejects request for Jesse Jackson to lie in honor at Capitol - CNN",
      "description": "House Speaker Mike Johnson has denied a request for the late Rev. Jesse Jackson Sr. to lie in honor at the United States Capitol, citing past precedent over how the deaths of other high-profile figures were handled, according to sources familiar with the matt\u2026",
      "url": "https://www.cnn.com/2026/02/20/politics/jesse-jackson-lie-in-honor-capitol-rejected",
      "urlToImage": "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2246052493.jpg?c=16x9&q=w_800,c_fill",
      "publishedAt": "2026-02-20T16:31:54Z",
      "content": "House Speaker Mike Johnson has denied a request for the late Rev. Jesse Jackson Sr. to lie in honor at the United States Capitol, citing past precedent over how the deaths of other high-profile figur\u2026 [+1690 chars]"
    },
    ...
```
