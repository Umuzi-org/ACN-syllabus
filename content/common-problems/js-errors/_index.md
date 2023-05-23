---
_db_id: 842
content_type: topic
title: Javascript Error handling
---

## Thoughtlessly squashing errors

If you ever see this kind of thing then it's probably wrong:

```
try {
    // stuff
} catch(err) {
    console.log(err);
}
```

Basically that says: Squash the error, log it, and move on. There are situations where that is the right thing to do. 99% of the time it's the wrong thing to do. 

Did you know that errors were implemented by very clever people? They were implemented in Javascript, Python, C#, Java, Clojure, Go and basically all languages because they are actually really useful. Always imagine how the code might be used in a larger application. If you are logging your errors to the console then any calling code would need to monitor the console logs in order to know if there was an error and figure out what to do about it. This would be insane.

There are a lot of really terrible JS tutorials out there that that just squash errors with no explanation. DO NOT blindly copy random stuff from the internet and put it in your code without thinking about the consequences.

If you aren't handling an exception then don't catch it.

## Catching an error just to raise it again

This is also fairly common:

```
try {
    stuff()
} catch(err) {
    throw err
}
```

Learners will often do this if we tell them not to squash errors.

Of course the following code does the exact same thing:

```
// try {
    stuff()   // this is the only line that is worth keeping
// } catch(err) {
//    throw err
// }
```

## Throwing errors just so you can catch them immediately

Consider the following code, there is a LOT wrong with it:

```
try {
    if(typeof number !== 'number') {
        throw new Error("Invalid input");
    } else if(fs.existsSync(filepath)) {
        const data = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
        return new Visitor(data.fullName, data.age, data.dateOfVisit, data.timeOfVisit, data.comments, data.nameOfAssistant);
    } else {
        throw new Error("File not found");
    }
} catch(err) {
    console.log(err);
}
```

First of all, we throw errors just so we can catch them and log them. So this code does pretty much the same thing:

```
if(typeof number !== 'number') {
    console.log("Invalid input");
} else if(fs.existsSync(filepath)) {
    const data = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
    return new Visitor(data.fullName, data.age, data.dateOfVisit, data.timeOfVisit, data.comments, data.nameOfAssistant);
} else {
    console.log"File not found");
}
```


## References

For more info see here:

- {{< contentlink path="topics/javascript-error-handling" >}}