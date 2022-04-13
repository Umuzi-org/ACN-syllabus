---
_db_id: 182
content_type: topic
ready: true
tags:
- architecture
title: Intro to software architecture
---

Software architecture is a pretty vast topic. This here is just scratching the surface. One good rule of thumb when you are starting is:

**Architect your code so that it is testable.**

If your code is easy to test then that has a bunch of benefits:
- of course, your code works, because you tested it
- your code is broken down into small testable units so that you can test one thing at a time. This means that the code is reusable in different circumstances
- your code is broken down into small clear things - clear code is a big deal 

## Think about layers 

Here's an example. Imagine you are writing an app that has a user interface. The user interacts with the GUI and then the stuff drawn on the GUI gets updated.

This can be separated into multiple layers. You can think of a data layer and a GUI layer. 

If your data and your GUI get all mixed up then things get very hard to test. Here's an approach you might consider:

1. Think about what your data should look like. What is its shape of it? These things shouldn't know about HTML. For example, if you were writing a game server (with no front-end at all) then these data structures should be valid. Of course, you would be setting up these structures and interactions in a TDD manner
2. Figure out how your data will change. What are the inputs? What are the effects on the data? At this point, we still haven't considered drawing any pictures.
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
