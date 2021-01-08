---
_db_id: 636
content_type: topic
ready: true
title: Getting set up to write Javascript on your computer
---

## Install VSCode and plugins

https://code.visualstudio.com/ 

This is a really wonderful code editer, it works on any operating system and has a few features we like a lot. [Here] (https://www.youtube.com/watch?v=liy7kSdLB7s) is a video that shows you some vscode features. The video talks about JavaScript but it is relevant to other languages as well.

VSCode has a rich ecosystem of plugins. There are a few that will make your life better:

- dbaeumer.vscode-eslint: this highlights problems in your code so you can spot problems and fix them quickly
- esbenp.prettier-vscode: this can be set up to reformat your code every time you hit save. Your code will be beautiful forever more

## Install Node

https://nodejs.org/en/download/

Node gives you a way to run JavaScript code without having to use a web page.

In a command line you can then do things like `node my_script.js`. This is good because then you wont need to worry about html and browsers and devtools and all that stuff. You can just save your script, open a terminal, cd into the right place and then use node to execute it whenever you want. 

## Try it out

You don't need to hand this in or anything. It's just for you to check that stuff is running correctly.

Use VSCode to create a new file.

Inside the file, type in

```
console.log("Winning")
```

Now save the file. You can just call it `winning.js` or something. The `.js` at the end is really important. Whenever you save a JavaScript file you need to add .js to the end.

You can open up a terminal right in VSCode using the menu at the top of the screen. Alternatively use the keyboard shortcut: "Ctrl+`".

Now if you type in `node winning.js` your code will run.

If you get an error like 
```
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

it just means you saved your file somewhere unexpected. Right click on your file name in vscode (the file name can be seen in the tab control at the top of the screen, and also in the file explorer on the left if you have it open). You'll see a context menu pop up. Choose to "Copy Path". Then use this command in the terminal:

```
node [the path you just copied]
```

For example this is how it would look on my computer:

```
node /home/sheena/workspace/temp/winning.js
```