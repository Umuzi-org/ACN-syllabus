---
_db_id: 769
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

#### Do you think you've got it? 

Based on the above guidelines, which of the following is a good way to name a Java directory?
```
  > ajavadirectory
  
  > a_java_directory
  
  > a-java-directory
  
  > AJAVADIRECTORY
  
  > AjavaDirectory
```

We are curious as to what your answer was!
See below for some tips in naming your directories.
```
  > gooddirectoryname
  
  > bad-directory-name
  
  > AnotherBadDirectoryName
  
  > AVERYBADDIRECTORYNAME
  
  > never_name_you_directory_like_this
```

### File names
File names should be in CamelCase (also known as Upper CamelCase), this is where each new word begins with a capital letter. Eg `SimpleCalculator`

#### Do you think you've got it?

Test yourself again - do any of the examples below follow the recommended Java file naming guidelines?

```
 > myfile.Java
 
 > my-file.java
 
 > myfile.java
 
 > Myfile.java
 
 > MyFile.java
```
In case you found the above a bit tricky, see a few more rule abiding file names below.

```
 > MyFile.py
 
 > GoodJavaFilename.py
 
 > KeepItShort
 
 > MustBeMeangingful.py

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
