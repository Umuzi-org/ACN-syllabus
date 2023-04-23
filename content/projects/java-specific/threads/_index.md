---
content_type: project
flavours:
- java
prerequisites:
  hard:
  - topics/java-specific/concurrency
  - topics/java-specific/functional-interface
  soft:
  - projects/java-specific/functional-interface
ready: true
submission_type: repo
title: Java Threads
---

## The Chicken and the Farmer

In this project you are going to create a `Chicken` function and a `Farmer` function each following these rules

1. Have the Chicken and the Farmer run on different threads

2. The Chicken should put eggs in a Basket ***(static array/list of size 1)*** and the Farmer should take eggs from the basket

3. The Farmer cannot take from an empty basket

4. The Chicken cannot add to a full basket

5. The basket is full if it has 1 egg


We kept the instructions open-ended on purpose. This is meant to have a bit of room for interpretation, there is no one perfect solution to this. We are very interested to see how you structure your solution.

Oh yeah, and remember to test your work. Always.



