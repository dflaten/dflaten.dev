
---
title: The place for IDEs when Agents do most of the coding 
date: 2026-11-25
published: true 
---

As I use agents like Claude or Codex to do development work I find less and less of a reason to use my IDE. I've been able to get Agents to take over almost all the "hands on keyboard" part of coding very effectively. It takes me much less time to create a similar or better version of features with the Agent doing the coding than when I did the coding in the past. Due to this I've found I need a tool centered more around the management of my Agents than the management of code which is something IDEs have done in the past. I still need an IDE or at least text editor to easily make small edits, review changes and explore the code but most of my time is spent managing the Agents. What has been helpful for me is finding an Agent Development Environment or ADE.

Of course Agents are still getting better and some of the things which were once very helpful to have are less helpful as Agents have obtained better capabilities. Managing agents requires you to be able to get visibility into the choices being made so you can redirect as needed. For now I'm not convinced that a totally automated "Software Factory" is currently possible so you can go from prompt to production without any human intervention though for some changes this is probably coming soon. At least until then we need the ability to look into the Agent as they are building and redirect when poor decisions have been made.

## What are you looking for in an Agent Development Environment
In one line - The ability to easily manage multiple agents at one time, including the ability to have multiple Agents developing on the same project. 

## Agent Management Options
In the past year many options have been released for managing work done by Agents. [Orca](https://orca.dev/), [T3 Code](https://t3.codes/), [Paseo](https://paseo.sh/) are currently some of the most popular options. I haven't had much experience with them but they bring an easy way to get into running multiple agents on a code base using git worktrees to get work done in parallel.

## My Personal Setup
I created [my own ADE](https://github.com/dflaten/dux) forked from an existing one. My ADE is terminal based and doesn't have all the extras you might see in the others like a mobile app integrated with it. Thanks to Agents I've been able to add a lot of features to it as tools have improved and I've found gaps in what I have versus what I want.

<img src="./dux-multi-repo.png" alt="Dux Multi Repo Screenshot" width="320" />

