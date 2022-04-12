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

By now you should know a bit about what unit tests are and why we do them. The next question is, when should we do them? Do we write our unit tests before or after writing our code?

Test-Driven Development (TDD) is a methodology in which tests are written before the code. This probably seems a little bit strange but it has a lot of advantages.

The basic algorithm you follow in TDD is the same no matter what language you are write in. Here it is:

RED -> GREEN -> REFACTOR -> repeat until victory!

- RED means: Step 1 is to write a test. The test should fail.
- GREEN means: Write some code so that your test passes.
- REFACTOR means: Look critically at your code. Is it DRY and cohesive? Do the names make sense? Is it yay or meh. Make it awesome and make sure your tests still pass.
- VICTORY: Beautiful code that works.

There is a lot more to be said about it than that. And there are a lot of intricacies and frustrations that you are going to bump into. You are going to do a lot of this.

## Resources

- https://www.guru99.com/test-driven-development.html This is really good but it glosses over the REFACTOR phase of TDD. Always refactor, always.
- https://www.youtube.com/watch?v=H4Hf3pji7Fw
- https://www.youtube.com/watch?v=3vuW4lFdAxc

This video is about Behavior Driven Development (BDD). Which is even cooler than TDD. https://www.youtube.com/watch?v=VS6EEUVZGLE

# Example

This is written in Java but if you aren't learning Java, for example, if you are writing Python or JS instead, don't be scared! Once you know one language then many others are pretty straight-forward to pick up.

https://technologyconversations.com/2013/12/20/test-driven-development-tdd-example-walkthrough/
