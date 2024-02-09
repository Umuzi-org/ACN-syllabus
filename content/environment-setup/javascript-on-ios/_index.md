---
_db_id: 1029
content_type: topic
ready: true
title: javaScript setup for iOS
---

## Installing Node.js

To install Node.js on iOS, you need to use iSH. You can find instructions on how to install iSH [here](https://ish.app/).
Once you have iSH installed, you can install Node.js like so:

```bash
apk add nodejs
```

To check what version of Node.js is installed you can use the command:

```bash
node --version
```

Node gives you a way to run JavaScript code without having to use a web page.

In a command line you can then do things like `node my_script.js`. This is good because then you wont need to worry about html and browsers and devtools and all that stuff. You can just save your script, open a terminal, cd into the right place and then use node to execute it whenever you want.

## Try it out

You don't need to hand this in or anything. It's just for you to check that stuff is running correctly.

Use Koder to create a new file.

Inside the file, type in

```javascript
console.log("Winning")
```

Now save the file. You can just call it `winning.js` or something. The `.js` at the end is really important. Whenever you save a JavaScript file you need to add .js to the end.

You can open up iSH and use the `cd` command to navigate to the folder where you saved your file. Then you can use the `ls` command to check that your file is there.

Now if you type in `node winning.js` your code will run.

If you get an error like

```bash
internal/modules/cjs/loader.js:834
  throw err;
  ^

Error: Cannot find module '/home/sheena/workspace/ACN-syllabus/winning.js'
    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:831:15)
    at Function.Module._load (internal/modules/cjs/loader.js:687:27)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:60:12)
    at internal/main/run_main_module.js:17:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: []
}
```

it just means you saved your file somewhere unexpected. You can use the `pwd` command to check where you are. Then you can use the `cd` command to navigate to the right place.

```bash
node [the path you just copied]
```

For example this is how it would look on my computer:

```bash
node /home/sheena/workspace/temp/winning.js
```