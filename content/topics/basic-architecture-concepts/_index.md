---
_db_id: 182
content_type: topic
ready: true
title: Intro to software architecture
---

Software architecture is a pretty vast topic. This here is just scratching the surface.

## Separate display logic from data logic

If your data and your gui get all mixed up then things get very hard to test. Here's an approach you might consider:

1. Think what your data should look like. What is the shape of it? These things shouldn't know about HTML. For example, if you were writing a game server (with no front-end at all) then these data structures should be valid. Of course you would be setting up these structures and interactions in a TDD manner
2. Figure out how your data will change. What are the inputs? What are the effects on the data? At this point we still haven't considered drawing any pictures.
3. Now for some display code. Here's a pretty good example adapted from one of your predecessors. This code comes from a project to do with a 10-pin bowling scoring system:

```
function drawPlayerDetails(player) {
    document.getElementById("showDetails").innerHTML =
        "<strong>Player Name: </strong>" + player.name +
        "<br><strong>Points: </strong>" + player.totalScore +
        "<br><strong>Position: </strong>" + player.pos +
        "<br><strong>scores: </strong> [" + player.score + "]";
}
```

This function does one thing, and it does that thing well and intuitively.

### Some oop resources

- https://stackoverflow.com/questions/226977/what-is-loose-coupling-please-provide-examples
- https://medium.com/clarityhub/low-coupling-high-cohesion-3610e35ac4a6
- SOLID: https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design