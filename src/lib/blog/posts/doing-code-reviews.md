---
title: Doing Good Code Reviews 
date: 2025-07-13
published: true
---

Code reviews provide the reviewer and reviewee an opportunity to learn and grow. An important part of the development process on a good team code reviews provide a way for multiple devlopers be invovled in the development process.  

### What makes for a good Code Review?

* **What is the problem being solved?** - Before reviewing any of the code make sure you as the reviewer understand the original user story and problem being addressed. Without this you could have great code that solves the wrong problem or misses key parts of the solution regardless of how well the code was written.

* **Ask Questions and focus on the code.** - When providing feedback on a piece of good rather than going immediately for "This is wrong." Ask a question arround why the person chose to make the decision they did there. The coder may have context you don't. Also make sure your comments are focused on the code not the coder.

* **Provide reasoning for suggestions** - Don't just make suggesions but give the reasoning behind it. This is a teaching opportunity for the coder!

* **Call out the good stuff** - Make sure you highlight where good decisions or new things you learned take place. 

* **Prioritize major over minor** - If the pr you are reviewing has many major items in it to review it may be best to leave out the minor formatting or other issues so the coder stays focused on what is most important. 

* **Sometimes a call is needed** - If you are putting a lot of comments on a PR and think it will require some back and forth don't be afraid to setup a call. In the long run this saves time and potential misunderstanding.


### Code Review Checklist

This is a list you can use when reviewing any pull request. To be most effective you should have an agreed upon list you have created with all team members input.

#### Pull Request Checklist
- [] Does the description describe the problem being addressed?
- [] Are you clear about the problem being addressed in the code? 
- [] Is the PR focused on one and only one issue?
- [] Is the PR less than ~500 lines?
- [] Is the build passing?
- [] Unit Tests cover the majority of branches?
- [] Is Integration testing included or at least was it deployed and tested?
- [] Are the methods in the PR no bigger than a paragraph?

