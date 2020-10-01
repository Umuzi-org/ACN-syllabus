---
_db_id: 115
content_type: topic
ready: true
title: Gradle and IntelliJ project submission structure
---

When pushing your work to git it's important to be intentional about what you are pushing. When you build your java project and/or run your tests then certain files get created automatically. We don't want those files. We should be able to generate them ourselves whenever we want to.

When you commit your code to git, you can tell git which files to ignore. You can do this though use of a `.gitignore` file. We've included a seriosly verbose gitignore file at the bottom of this document. Please just copy it and save it as a file named`.gitignore` in the root of your project.

Now if you did this right from the start you should be able to do something like this:

```
git add .
git commit -m "a useful and informative message"
git push
```

Now let's see if it all worked out. Try cloning your code yourself and see what git knows about:

```
cd somewhere_nice
git clone <your github repo> temporary_copy
cd temporary_copy
tree  # you might need to: `sudo apt install tree`
```

This should output something neat and tidy. Eg from one of our many calculator projects you would see something that looks like this:

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    │   └── java
    │       └── Calculator.java
    └── test
        └── java
            └── CalculatorTest.java
```

Now you can run these commands and they should work:

```
 ./gradlew build
 ./gradlew test
```

## Troubleshooting

If the directory structure that githb is tracking is huge and crazy looking then that's because you committed things before adding `.gitignore` to your project. That's totally ok! We can fix it like so:

```
git rm -r -cached .
git add .
git status # this should tell yu about a whole big pile of deleted files. This is expected
git commit -m "cleaned up junk files"
git push
```

Now take a look at what github knows about. Everything should be looking clean and tidy and if you clone your code it should just work.

## Massive and very thorough gitignore file

Please copy this into your projects and save it as `.gitignore`:

{{% code_snippet ".gitignore" %}}