---
_db_id: 141
content_type: topic
ready: true
title: Super basic intro to Node
---

Most people are introduced to JavaScript in the context of a web browser. JS adds smarts to HTML and CSS.

JS is a proper programming language so it can do a whole lot more than make a web page clever. Basically it doesn't need to interact with a website in order to work. You can use it on the "back-end". It can be used to interact with filesystems and databases and all sorts of other things.

When JS is running on the backend it's usually referred to as Node. Node is really a "runtime environmnet" that can execute JS code.

Here are instructions on how to install node: https://nodejs.org/en/download/

Try type this into a terminal:

```
node
```

Now type

```
var greeting = "hello world";
console.log(greeting);
```

So you see you can execute JavaScript code right there in your terminal and it just works.

Now save the helloworld code above to a file named `hello.js`. You can execute this whenever you want to by saying `node hello.js` in a terminal. Or rather `node /path/to/hello.js` if you are in a different location.

### package managers

There are a few different package managers. The two main ones are npm and yarn. In this course you'll be using npm.

If you know how to use npm then using a different package manager will be pretty easy.

https://docs.npmjs.com/about-npm/

## Getting started with npm

Install npm if you need to. Then follow the steps below:

- make a directory called `npm_demo`
- cd into your new directory
- type in `npm init`. Npm will ask you a bunch of questions. You can just say yes to everything.
- There is a new file inside your directory. Take a look at it. It should be fairly easy to read.
- now type in `npm install jasmine`. Jasmine is a tool used for testing your js code. When you type in this command then npm will download and install jasmine, and update a few other files in the directory. Take a look around your directory again.

**Super Important** you'll notice that npm creates a directory called `node_modules`. This is where the downloaded code gets saved. You'll see jasmine in there. **Make sure you always gitignore your node_modules directory**