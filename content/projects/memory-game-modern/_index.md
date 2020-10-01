---
_db_id: 287
available_flavours:
- any_frontend_framework
content_type: project
submission_type: repo
title: 'Memory Game: rebuild using a modern web frontend framework'
---

Take a look at this: {{% contentlink path="projects/memory-game/part-1" %}}

## Instructions

### Part 1: MVP

Create an MVP memory game using Angular or React. Follow a TDD procedure.

- The game should draw a grid with 6 columns and 5 rows
- The cards in the game should be randomized
- When the game finishes then display a message on the screen that says "Congratulations! You are done!" There should be a button labelled "Play Again" that the player can use to restart the game

### Part 2: Count-down

- Draw a timer widget on the screen. It should start off showing 2 minutes and count down to zero
- The color of the timer should be green initially
- the timer should turn orange after one minute has passed
- the timer should turn red when there are 30 seconds left on the clock
- when the timer runs out:
  - flip all the cards over to reveal what is underneath
  - display a message saying "Sorry! You lost the game". There should be a button labelled "Play Again" that the player can use to restart the game

### Part 3: Winning stats

When the user wins the game then the congratulations message should include:

- the number of turns taken (1 turn == 2 clicks)
- the amount of time taken

### Part 4: ExpressJs

- Serve your game using ExpressJS (as static content)
- Connect a MongoDB database
- expose the following json api endpoints:
  - POST update_score: This should accept a json object like this `{name:"a string", time: number of seconds, turns: number of turns taken}`. This endpoint must update the database
  - GET leaderboard/time: This should return the top 10 fastest people to win the game
  - GET leaderboard/turns: This should return the top 10 people to win the game using the fewest clicks

### Part 5: Ajax

- When the game starts then the user will need to enter their name

- Whenever a user successfully wins the game then:

  - their score should be stored in MongoDB updated through use of the update_score endpoint
  - the two leaderboards should be fetched and displayed on the page
  - If the current user is on a leaderboard then they should be highlighted

- Whenever a player loses the game
  - display the two leaderboards