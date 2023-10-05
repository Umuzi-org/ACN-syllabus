---
content_type: project
flavours:
  - java
  - javascript
  - markdown
  - python
prerequisites:
  hard:
    - error-handling/java-error-handling
    - error-handling/python-error-handling
    - error-handling/javascript-error-handling
protect_main_branch: false
ready: true
submission_type: repo
title: Error Handling Assignment
---

Please answer the following questions in markdown files and submit following the instructions below.

## Questions

1. What is the fundamental purpose of error handling?

2. What are some poor practices in error handling that developers should avoid? Provide 1 example.

3. When should developers catch and handle errors?

4. Take a look at the following code snippets:

```java
// java
try {
  // Code...
} catch (Exception error) {
  System.out.println(error);
}

try {
  // Code...
} catch (Exception error) {
  System.out.println("Error: " + error);
}

try {
  // Code...
} catch (Exception error) {
  return error;
}

try {
  // Code...
} catch (IllegalArgumentException error) {
  throw error;
}
```

```python
# python
try:
  # Code...
except Exception as error:
  print(error)

try:
  # Code...
except Exception as error:
  print(f"Error: {error}")

try:
  # Code...
except Exception as error:
  return error

try:
  # Code...
except ValueError as error:
  raise error
```

```javascript
// javascript
try {
  // Code...
} catch (error) {
  console.error(error);
}

try {
  // Code...
} catch (error) {
  console.log(`Error: ${error}`);
}

try {
  // Code...
} catch (error) {
  return error;
}

try {
  // Code...
} catch (error) {
  throw error;
}
```

please select and write one snippet that is a good example of error handling.

## How to submit your work

Please follow the following instructions to submit your work:

{{< contentlink path="project-submission-instructions/markdown-questions" >}}
