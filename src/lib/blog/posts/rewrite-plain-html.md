---
title: Launching my Personal Website
date: 2025-01-28
published: true
---

Thanks to finding [this repo](https://github.com/arnath/vijayp.dev) I was finally able to publish a personal website and blog.
I'm not a big fan of Javascript frameworks as they added bloat to the code and provided much more functionality
than I needed. I had been looking for a way to create a site without writing too much html/css and forking this repo is an
easy way to get there.

### Basic Parts

[This repo](https://github.com/dflaten/dflaten.dev) contains all the
things needed to build the static resources. I plan on having this hosted on Cloudfare Pages with a custom domain.

### Problems Encountered
The only problem that I encountered when setting this up was getting the code into Cloudfare Pages. Ultimately
I first tried to create the Pages project through the UI in Cloudfare and execute the Build commands in the makefile to
build the website. This didn't work due to Pages not having `uv` installed.

After doing some research on other options I tried using Github actions to publish the resources and that the
repo had a `.yaml` file with the action defined but when I forked the repo Github disabled the workflow. I had to
activate the workflow but things still weren't working correctly because the Cloudfare Pages project
needed to be created first. After creating a base placeholder project in Cloudfare things worked as expected.
