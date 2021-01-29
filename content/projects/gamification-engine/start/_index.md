---
_db_id: 643
content_type: project
flavours:
- any_unit_testing
- any_language
submission_type: repo
tags:
- tdd
- oop
title: Gamification engine
---

In this project you'll be demonstrating your knowledge of unit testing and oop. In order for your code to be acceptable, you'll need to make sure you follow best practices. NAme your stuff properly, write clean code, write clear small functions. All that stuff.

## What is gamification

Gamification refers to taking game mechanisms and applying them to things that aren't usually considered games. The most obvious game mechanisms are points and leaderboards.

For example, imagine you own an online magazine. You have a bunch of journalists working for you and you want to give them an idea of how well they are doing and motivate them to take certain actions. So you start counting the following things:

1. Every time an article gets read
2. Every time an article gets a complaint (for being inaccurate or clickbait)
3. Every time an article gets shared
4. Every time a reader comments on an article

By tracking this stuff you can do some cool things like create leaderboards for different categories. You can do simple things like "Top 10 most read journalists". You can also combine scored in different ways, eg: "Most shared and accurate journalists" can be derived from combining 2 and 3.

I'm sure you can think af many other things that points and leaderboards can be used for. It could even be used for games.

## What is a gamification engine

This would be a general purpose piece of code that can be used to keep track of different kinds of points and generate different leaderboards. Basically it will contain the mechanisms we need to make a game, but it wont know what game we are playing.

## KISS

Google it.

## RTFQ

Google that too!

If we say "write a function named gobbles" then that is exactly what is expected. Coders pay close attention to detail. Coders check their work. Coders do not jump to conclusions. Well... good coders anyway.

## TDD

We want very thorough testing. The best way to get this right is with a TDD approach.

## Naming conventions

Please follow the naming conventions of the language you are doing this project in. Python's naming conventions are different from JavaScript and Java.

## Specification

Alright. Here's what you need to do:

Write a class galled `GameEngine`.

### Constructing an instance

The constructor of the game engine should accept a list or array of strings. These are the names of the different kinds of scores we want to keep track of.

For example if we were using the engine to track performance of journalists we might want to instantiate the engine like this:

```
GameEngine(["reads","shares","comments","complaints"])
```

If we wanted to use the `GameEngine` to get an idea of a developer's productivity then we might want to initiate it a bit differently. Developer productivity is kinda a difficult thing to measure in real life, but there are some very obvious things worth tracking:

```
GameEngine(["pull_request_reviews_done","acceptance_reviews_done","pull_requests_made","pull_requests_merged"])
```

The game engine needs to sore these score types.

### Querying a user's score

The game engine's main job is to keep track of the scores of different people. So there needs to be a way to fetch those scores.

Write a function called `get_score` or `getScore`. It needs to accept 2 strings. NB choose the correct naming convention for your language please.


```
get_score(player,score_type)
```

Player represents the person or entity who we are trying to get the score for.

eg if we want to get the number of pull request reviews done by Tshepo we would call:

```
engine.get_score("tshepo@whatever.org","pull_request_reviews_done")
```

If Tshepo does not yet have any points there, then the funciton will return 0.

### Updating a user's score

We also need to be able to give people points for their stuff

This will give Tshepo 1 point:

```
engine.add_points("tshepo@whatever.org","pull_request_reviews_done",1)
```

This will remove 1 point:

```
engine.add_points("tshepo@whatever.org","pull_request_reviews_done",-1)
```

### A complete example

Note, this is pseudocode.

Hint: It would be very useful to incorporate this kind of logic into your unit tests

```
engine = GameEngine(["pull_request_reviews_done","acceptance_reviews_done","pull_requests_made","pull_requests_merged"])

engine.get_score("tshepo@whatever.org","pull_request_reviews_done")  // returns 0
engine.get_score("bob@whatever.org","pull_request_reviews_done")  // returns 0

engine.add_points("tshepo@whatever.org","pull_request_reviews_done",1)
engine.get_score("tshepo@whatever.org","pull_request_reviews_done")  // returns 1
engine.get_score("tshepo@whatever.org","pull_requests_made")  // returns 0

engine.add_points("tshepo@whatever.org","pull_request_reviews_done",10)
engine.get_score("tshepo@whatever.org","pull_request_reviews_done")  // returns 11
engine.get_score("tshepo@whatever.org","pull_requests_made")  // returns 0

engine.add_points("tshepo@whatever.org","pull_request_reviews_done",-1)
engine.get_score("tshepo@whatever.org","pull_request_reviews_done")  // returns 10
engine.get_score("tshepo@whatever.org","pull_requests_made")  // returns 0

engine.get_score("bob@whatever.org","pull_request_reviews_done")  // returns 0 since we never gave bob any points
```