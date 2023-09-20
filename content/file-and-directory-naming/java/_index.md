---
_db_id: 835
content_type: topic
prerequisites:
  hard:
  - file-and-directory-naming/general
ready: true
tags:
- File and directory naming
- java
title: File and directory naming in Java
---

## How should I name my Java files and directories?



### Directories

Directory names in Java should consistently use lowercase letters to maintain uniformity and adhere to Java conventions. This practice ensures that your project's directory structure is clean and easy to work with. Additionally, when using tools like Gradle or Maven to set up your project, it's advisable to follow the conventions they establish for directory structure, as they are designed to simplify project management and align with best practices.

See below for examples of naming your directories.

```

 > src

 > main 
 
```

### Class names

Java class names should be written in CamelCase, starting with an uppercase letter. Use meaningful and descriptive names that indicate the purpose of the class. For example: `CarRentalSystem`, `EmployeeManager`, `StudentRecord`.

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
