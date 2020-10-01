---
_db_id: 178
content_type: topic
prerequisites:
  hard:
  - topics/unit-testing
  soft: []
ready: true
tags:
- tdd
title: Test Driven Development
---

By now you should know a bit about what a unit test is and why we do them. The next question is: when should we do them? Do we write our unit tests after we write our code or before?

Test driven development is a methodology in which tests are written before the code. This probably seems a little bit strange. Because it is. But it has a lot of advantages.

The basic algoorithm you follow in TDD is the same no matter what language you are writing in. Here it is:

RED -> GREEN -> REFACTOR -> repeat until victory!

- RED means: Step 1 is to write a test. The test should fail
- GREEN means: Write some code so that your test passes
- REFACTOR means: Look critically at your code. Is it DRY and cohesive? do the names make sense? Is it kak or is is lekker. Make it lekker and make sure your tests still pass.
- VICTORY: Beautiful code that works

There's a lot more to be said about it than that. And there are a lot of intricacies and frustrations that you are going to bump into. YOu're going to be doing a lot of this.

## Resources

- https://www.guru99.com/test-driven-development.html This is really good. But it glosses over the REFACTOR phase of TDD. ALways refactor. Always.
- https://www.youtube.com/watch?v=H4Hf3pji7Fw
- https://www.youtube.com/watch?v=3vuW4lFdAxc

This video is about BDD. Which is even cooler than tdd. https://www.youtube.com/watch?v=VS6EEUVZGLE

# Example

This is written in Java. But if you aren't learning Java, eg if you are writing Python or JS instead, don't be scared! Once you know one language then many others are pretty straight-forward to pick up.

https://technologyconversations.com/2013/12/20/test-driven-development-tdd-example-walkthrough/