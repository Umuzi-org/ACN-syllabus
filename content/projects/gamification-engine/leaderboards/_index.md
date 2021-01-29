---
title: Add Leaderoard functionality
content_type: project 
submission_type: continue_repo 
prerequisites: 
    hard: 
      - projects/gamification-engine/start
from_repo:  projects/gamification-engine/start
flavours: 
  - any_unit_testing
  - any_language

tags:
  - tdd
  - oop
---
### Leaderboards

The next thing we need is to be able to see who is winning. Create a function called `leaderboard`. It needs to return a string. This is best explained through an example:

```
engine = GameEngine(["pull_request_reviews_done","acceptance_reviews_done","pull_requests_made","pull_requests_merged"])

engine.add_points("tshepo@whatever.org","pull_request_reviews_done",10)
engine.add_points("tshepo@whatever.org","acceptance_reviews_done",1)
engine.add_points("bob@whatever.org","pull_request_reviews_done",1)

engine.leaderboard("pull_request_reviews_done")
// returns:
// 1: tshepo@whatever.org [10]
// 2: bob@whatever.org [1]

engine.leaderboard("acceptance_reviews_done")
// returns:
// 1: tshepo@whatever.org [1]
// 2: bob@whatever.org [0]

engine.leaderboard("pull_requests_merged")
// returns:
// 1: bob@whatever.org [0]
// 2: tshepo@whatever.org [0]
```

- each line has the format `{position} {player} [{score}]`
- one line per player
- if two or more users are tied then arrange them alphabetically. See `engine.leaderboard("pull_requests_merged")` in the example above.
- the leaderboard contains a maximum of 10 users