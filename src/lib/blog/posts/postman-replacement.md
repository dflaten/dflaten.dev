---
title: Finding a Postman Replacement 
date: 2026-02-01
published: false 
---

Most developers at some point will need a tool to help test and program APIs (Application Programming Interfaces). In the past I've used Postman to help do this but overtime they added so many features I didn't use and pushed the need for creating an account to the point where I started looking for an alternative and saw the suggestion to just create your own. So that's what I did! 

### Python Based Api Explorer 
I do a lot in Python these days so it seemed the easiest way to go for creating my tool. Dependencies are pretty limited using the primarily the  `requests` library and `urllib3` plus a couple other related dependencies. 

Installing is simple, just requires [uv](https://docs.astral.sh/uv/) to install: `uv sync`.

You can use the tool like: `uv run api-cli my_api_config.json get_users` after defining the config file to make requests.

As I find new things I want to be able to run I'm making updates.
