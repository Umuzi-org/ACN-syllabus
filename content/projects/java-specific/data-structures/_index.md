---
_db_id: 209
available_flavours:
- java
content_type: project
prerequisites:
  hard:
  - projects/java-specific/collections
  - topics/java-specific/collections-and-datastructures
  soft: []
ready: true
submission_type: repo
title: Java data structures
---

**Game Time**

In this project we are going to create a GAME!!! fun right, its called [Conway Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

**How This game works**

Initially, there is a grid (yours should be 10 \* 10) with some cells which may be alive or dead. Our task is to generate the next generation of cells based on the following rules:

1. Any live cell with fewer than two live neighbors dies, as if caused by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

You will need to show in your console the initial state (input) and next generation

(+) - Dead Cell

(#) - Alive Cell

**Input**

/ + + # + + +

/ + + # # # +

/ + + + + + +

**Next generation**

/ + + # + + +

/ + + # # + +

/ + + + # + +

You should have a test for all the rules above but you can also add more test if you want.