---
_db_id: 652
content_type: topic
ready: true
title: Polishing existing projects
---

This type of intervention is a lot like industry standard pair programming. It differs in that: industry pair programming is mostly about building working code, whereas our main focus is to get the follower to understand their code.

This means that the leader should be asking questions and getting the follower to demonstrate their understanding. If it becomes clear that the follower is missing some foundational knowledge then switch to deep practice mode.

## Preparation  

If a student is getting marked as `not yet competent` on one of their projects, then that project is a good one to work on.

Make sure that you are able to do the project yourself.

Take a look at the submitted code ahead of time.

When you invite the follower to the session, make it clear that they will be sharing their screen.

## Session prioriies 

There can be a lot of things keeping a project from being marked as competent.

The following points are pretty much in the right order. This is a STRONG opinion rather than a rule. There will be reasons to do things in a different way, but this order is likely correct most of the time.  

1. Make sure that the follower understands the project specification. This step might not be required. Eg: if the the learner's code actually works fine, but is dirty as sin then they don't need to prove that they understand the spec.

2. Clean up the existing code if it is dirty. Take care of the technical debt before trying to move forward. If the code has unit tests then get the follower to run the tests often during the clean up process in order to make sure nothing is breaking.

3. Now address any missing functionality. If there are tests missing then guide them to write the correct tests. This sentence seems to work quite well on people: "When you write unit tests you should pretend that you are testing the work of your enemy and you want to prove that the bastard took shortcuts". Also if tests are insufficient then it is good to say things like "this function would pass your tests, and it really shouldn't" and then write that function.

4. Implement the features. Try to follow a TDD approach if there is testing involved.

5. If there is a bug in their code then: write a test that fails because of the bug, then make the code changes to make the test pass (this practice is commonly used on production systems and it is worth practicing)