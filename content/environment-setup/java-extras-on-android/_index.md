---
_db_id: 635
content_type: topic
ready: true
title: Java setup for Android
---

For our Java bootcamp you will need to be able to write Java code and markdown code. And there isn't one editor that does both of these well.

ACode is great for markdown. But when it comes to writing and running Java Code you'll need something more:

This editor is your friend: https://play.google.com/store/apps/details?id=com.duy.compiler.javanide&hl=en&gl=US

Once you have installed it, open it up. It will have a funny looking form show up. 

## Try it out

Under your project name you can say "katas0" or similar. This should describe the project you are working on.

Under package name you can say `org.umuzi`. And then you can set the Main class name to `Main`.

Once that is done you can update your main class so it looks like this:

```
public class Main
{
   public static void main(String[] args)
   {
      System.out.println("weeeee");
   }
}
```

You'll see a play button at the top of the editor. Press it and your code will run.

## Starting the next project

You'll need to submit a few different projects during bootcamp. When you want to start another project do this:

- Press on File (at the top of the screen)
- Select "New"
- Select "New Java Console Project"
- fill in the form like before, just give your project a different name

## Figuring out where your projects get saved

If you choose File > Save As when one of your files is open, then you'll be able to see the directory where your stuff gets saved. This is useful because you are going to need to interact with your stuff via git.

Now open up termux and `cd` into your project directory. It'll be something like:

```
cd storage/shared/JavaNIDE/
ls # you'll see your project names here
cd katas0 # enter one of your project direcories
cd app
ls # you'll see a few directories here: build, libs and src
git init # initialise your git repo
echo "build/" >> .gitignore # tell git to ignore the build directory
```