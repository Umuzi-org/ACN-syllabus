---
_db_id: 963
content_type: project
flavours:
  - markdown
prerequisites:
  hard:
    - topics/test-driven-development
  soft: []
protect_main_branch: false
ready: true
submission_type: repo
tags:
  - tdd
title: Test Driven Development - Questions
---

Please answer the following questions:

1. Define test-driven development

2. If you are following test-driven-development, can you ever skip the "RED" step of the process?

3. List at least 3 benefits of TDD. Each benefit should be explained in a short paragraph.

4. How can you apply a TDD approach to fixing bugs in your code?

5. How does unit testing help make a dev team more effective?

6. Take a look at the following code snippets:

```python
# python

assert warning_colour == "orange"
assert warning_colour != "blue"
```

```javascript
// javascript

expect(warningColour).toBe("orange")
expect(warningColour).not.toBe("blue")
```

```java
// java

assertEquals(warningColor,"orange");
assertNotEquals(warningColor,"blue");
```

For each language, only one of the assertions/expectations is useful and the other one adds no value. Please say which line should be removed and explain why.

## How to submit your work

Please follow the following instructions to submit your work:

{{< contentlink path="project-submission-instructions/markdown-questions" >}}
