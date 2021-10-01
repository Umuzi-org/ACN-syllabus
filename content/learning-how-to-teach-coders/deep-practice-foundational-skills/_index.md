---
_db_id: 650
content_type: topic
ready: true
title: Deep practice of foundational skills
---

## When

This is most effective early in the program. 

Also, if another session reveals some kind of misunderstanding or lack of knowledge then it would be useful to zoom in on the difficulty and revert to a deep practice mechanism. Generally if someone is struggling to leverage a concept in a complicated context then it is good to break that context down and make sure the learner understands each piece of the puzzle.

## Procedure

- Pick a concept
- The leader shares their screen 
- The leader writes some dead simple code that demonstrates the concept in one way and asks "what does this code print?"
- If the follower gets things right:
  - make the code more complex and ask the question again
- If the follower gets things wrong
  - try to figure out what they are misunderstanding and zoom in on that until they understand it then go back to the things they were getting wrong
- If significant progress is made during the session, make sure you tell the learner. Eg: "when this session started you were getting all the answers wrong, now you're rocking it and only 15 minutes has passed. You leveled up! Try to do this kind of thing on your own when you are learning a new thing"
- Try to get the follower to see that they can do this kind of work on their own

## Example code

Let's say you want to make sure a learner understands the difference between return and print. This is a common issue.

The following code samples show the use of return in increasingly complicated situations and can be used to demonstrate that understanding:

```[javascript]
function foo(){
    console.log("hello")
}

bar = foo()
console.log(bar)
```

```[javascript]
function foo(){
    console.log("hello")
    return 1;
}

bar = foo()
console.log(bar)
```

```[javascript]
function foo(){
    return 1;
    console.log("hello")
}

bar = foo()
console.log(bar)
```

```[javascript]
function foo(x){
    console.log("hello")
    return x;
}

bar = foo("blue")
bar = foo("red")
console.log(bar)
```

etc...

Get a bit creative:

- put the return inside a loop
- have multiple returns
- have multiple function calls
- etc

## List of common coding problems to get across to recruits

1. return versus print
2. for loops and 2d arrays
3. function calls and the order of execution of code
4. classes and object instantiation
5. tdd

## Why should the leader do the typing?

Often the follower types more slowly and mishears things and then the conversation becomes a lot more like pulling teeth. Allowing the leader to type keeps things quick and focused. It also shows the learner how to use their code editor effectively for rapid exploration of new concepts.