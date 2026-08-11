---
_db_id: 145
content_type: topic
ready: true
tags:
- defensive-programming
- skill/combined_concept_projects
title: Introduction to Assertive Programming
---

You've all heard of "defensive driving," right? When driving a car, you do certain things if you want to stay safe. You maintain a safe following distance, check your mirrors and blind spot, and watch your speed. Why do you do that?

Because mistakes happen. Sometimes the road is bad, sometimes there's a cow in the road, and sometimes the other drivers are inattentive. Sometimes you are inattentive.

Okay, now let's talk about code. Code is written by humans for humans. Humans are prone to error. They make mistakes all the time: there will be typos, off-by-one errors, assumptions, and all sorts of weird nonsense.

Assertive programming is one way to practice defensive programming. It has loads of benefits.

First, consider the following code:

```python
# python

def refund_client(refund_amount):
    assert refund_amount > 0, f"Refund amount needs to be positive, this is invalid: {refund_amount}"
    now_do_the_actual_work()
```

```javascript
// javascript

function refundClient(refundAmount) {
    console.assert(refundAmount > 0, `Refund amount needs to be positive, this is invalid: ${refundAmount}`);
    nowDoTheActualWork();
}
```

You can see that the Python and JavaScript versions of this are really similar! Other languages have their own way of doing the same kind of stuff. Basically, what this does is raise/throw an Exception/Error when a certain condition is not met. The error message is nice and descriptive.

This is good for a few different things:

- Sanity checking around human error and input validation.
- These assertions are useful as documentation as well. If someone else is reading your code, they will see exactly how your stuff should be used.

Also, in general, the earlier you find a problem, the cheaper it is to fix. This is a fact of life. Seriously.

In terms of coding, let's talk a bit more about the `refund_amount` assertion. Imagine a piece of software that is all about shopping. Occasionally, users require refunds. What might happen if somehow a negative refund amount slips into the system? It might show up as something weird on a frontend and make the end users distrust the system. Then the backend devs will blame the frontend devs, maybe the accounting system will be negatively affected (of course the frontend devs will be blamed for this too, at least for a little while), the refund won't be paid to the user on time, and lots of other awful, nasty stuff.

That one little line of code prevents all sorts of crazy stuff from happening in the code.

Assertions save lives!

## Resources

This excellent article talks about the benefits of failing fast and loudly:
https://www.martinfowler.com/ieeeSoftware/failFast.pdf

This discussion on Stack Overflow is about where assertions are inappropriate. It makes use of heavy words like `public methods` and stuff like that. Basically, a shortcut to doing this right is thinking about who is going to see your error message and how the error message will be useful to them:
https://stackoverflow.com/questions/13832487/why-should-assertions-not-be-used-for-argument-checking-in-public-methods

And here are a few more excellent resources:
 
- [Pragmatic Paranoia](https://www.informit.com/articles/article.aspx?p=2982114&seqNum=3)
- [Benefits of Assertive Programming](https://stackoverflow.com/questions/787643/benefits-of-assertive-programming)

## Java Resources

- https://www.geeksforgeeks.org/assertions-in-java/

## JS Resources

- https://developer.mozilla.org/en-US/docs/Web/API/console/assert

## Python Resources

- https://wiki.python.org/moin/UsingAssertionsEffectively