---
_db_id: 626
content_type: topic
ready: true
tags:
- problem solving
title: Problem solving techniques
---

As a coder, your job is to write code that solves problems. Problems that nobody has ever seen before! Problems that can't be Googled or YouTubed! Problems where the answers don't even exist on StackOverflow!

What you need is a strategy that will work on any problem. This might sound like something magical, but it exists.

Basically every problem can be broken down into smaller problems. And those problems can be broken down again and again. Eventually you end up with a bunch of tidy little problems that can be written down as simple lines of code.

It sounds simple, but it's something that takes quite a lot of practice.

## What if I don't know how to break down the problem?

Sometimes you get weird kind of problems and you simply don't know what the steps are. This is tricky. In these cases it's really nice to rely on a pencil and paper. Because there is no school like the old school.

Try to actually do the problem by hand. Or perhaps a smaller version of the problem.

For example, if you are instructed to do something interesting to an array with length 1000, see what you can manually do to an array of length 5 that is equivalent. Try solve it a few times with different inputs and see if you can find a pattern that you can break down :)

## Beware of the edge cases

Edge case is kinda a funny thing to understand. Basically you need to think of extreme values and see if your code can handle that.

For example:

- If you are writing code for a game, how do you deal with things if the players tie?
- If you need to write code that accepts an integer, what if the value is zero?
- What if you need to do some processing on an input string and the string is empty? What if it's really really long?
- What if you need to process a bunch of numbers, and they are all equal to each other?

This discussion thread has many more examples: https://www.quora.com/What-is-an-edge-case-when-programming

When writing tests for your code, it's important to test all the inputs

## Common mistakes and misconceptions

- **Don't try to write everything on one line**. A lot of geeklings try to solve absolutely everything on one line. Don't do that! Break it down. Make each step of your logic very clear and simple to follow.
- **Do follow coding best practice** Your code should be easy to read, it should make its intention clear. Choose meaningful names for your variables. Keep things DRY.
- **Do take time to plan your code** If you jump straight into writing code before planning it out and thinking it through, you'll end up wasting time. `Less haste == More speed`.
- **Don't try to show off** Some people think that making their code as fancy as possible is a good thing. Trust me, it is not. The best code is clear and readable and it works.
- **Don't write highly nested code unless you have to** If you have a loop inside a loop inside an if statement inside a loop, you ARE doing it wrong. Remember you need to write code that humans can read. Break things down into functions if you need to.

## Resources

These wonderful articles explain this stuff really well. Please read them:

- https://medium.com/@dannysmith/breaking-down-problems-its-hard-when-you-re-learning-to-code-f10269f4ccd5
- https://simpleprogrammer.com/solving-problems-breaking-it-down/
- https://hackernoon.com/how-to-approach-any-coding-problem-9230f3ad6f9

### General Problem solving

The resources above are great resources for coding related problem solving techniques. But, problem solving is not unique only to coding. It is a skill to be practiced in everyday life. Please checkout the following content from MIT:

- https://ccmit.mit.edu/problem-solving/

## Practice

Of course, reading about code and watching other people code is great. But if you personally want to get good at this stuff: Practice practice practice.

Hackerrank is a great resource.
