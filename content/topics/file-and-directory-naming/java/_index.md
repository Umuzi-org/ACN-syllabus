---
_db_id: 835
content_type: topic
prerequisites:
  hard:
  - topics/file-and-directory-naming/general
ready: true
tags:
- File and directory naming
- java
title: File and directory naming in Java
---

## How should I name my Java files and directories?
When you think about how to name files and directories in Java, you should know that different Java programmers can have different styles and approaches to the way they program. When naming stuff you must use Java standard conventions that are readable and meaningful to yourself and other programmers.


### Directories
Directory names in Java should be in lower case which means that you only use small letters. Eg `src` or `main`

See below for examples of naming your directories.

```

 > src

 > main 
 
```

### File names
File names should be in CamelCase (also known as Upper CamelCase), this is where each new word begins with a capital letter. Eg `SimpleCalculator`

See below for some tips in naming your files.

```

 > MyFile.java
 
 > GoodJavaFilename.java
 
 > KeepItShort.java
 
 > MustBeMeangingful.java

```


### Example of what's expected

```

├── src
    └── main
    |   └── java
    |       └── StringCalculator.java
    |       └── Main.java    
    └── test
        └── java
           └── StringCalculatorTest.java 

```