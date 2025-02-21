---
_db_id:
content_type: topic
prerequisites:
  hard:
    - topics/solo-learn/python/intro-to-python/1-getting-started-with-python-project/
ready: true
title: 10-PM-02-PS10 Code Loops (Tailored to a Specific Tool or Platform)
---

#### Overview

In this section, we will explore loops, which are essential programming structures that allow you to repeat a set of instructions multiple times. Loops help automate repetitive tasks and make your code more efficient. Understanding how to work with different types of loops—such as while loops, iterating loops, and nested loops—is crucial for writing effective code that can handle large datasets or repeated operations.

Applied Knowledge

By completing this section, you will gain an understanding of:

- **Types of loops**—familiarity with different loop structures (e.g., while, for, do-while).
- **Checking conditions**—how loops rely on conditions to continue or stop iterating.
- **Initializer, condition, iterator**—understanding the components that define a loop's execution flow.
- **Sequence**—how loops follow a specific sequence to repeat tasks.

#### Instructions

Given a problem statement and access to a suitable PC or device with software toolkit/platform, the learner must be able to:

### PA1001: Use and Apply Different Types of Loops

1. **While Loop**

   - A `while` loop repeats a block of code as long as a specified condition is `true`.  
     It’s important to ensure that the condition eventually becomes `false` to prevent an infinite loop.

   **Syntax**:

   ```javascript
   while (condition) {
     // code to be executed
   }
   ```

   **Example**:

   ```javascript
   let count = 1;

   while (count <= 5) {
     console.log(count);
     count++; // Increment count
   }

   // Output:
   // 1
   // 2
   // 3
   // 4
   // 5
   ```

2. In this example, the loop continues to execute as long as count is less than or equal to 5. After each iteration, the value of count increases by 1.

3. **Iterating Loops (For Loops)**

   - A `for` is commonly used when the number of iterations is known. It’s structured with three parts: initialization, condition, and iterator.

   **Syntax**:

   ```javascript
   for (initializer; condition; iterator) {
     // code to be executed
   }
   ```

   **Example**:

   ```javascript
   for (let i = 1; i <= 5; i++) {
     console.log(i);
   }

   // Output:
   // 1
   // 2
   // 3
   // 4
   // 5
   ```

4. In this case, the loop starts by initializing `i` to 1, checks the condition (`i <= 5`), and increments i after each iteration. The loop stops when the condition evaluates to `false`.

5. **Nested Loops**

   - A **nested loop** is a loop inside another loop. It’s useful when working with multi-dimensional data structures (e.g., matrices or tables) and allows you to iterate through each element.

   **Syntax**:

   ```javascript
   for (let i = 0; i < rows; i++) {
     for (let j = 0; j < columns; j++) {
       // code to be executed
     }
   }
   ```

   **Example**:

   ```javascript
   for (let i = 1; i <= 3; i++) {
     for (let j = 1; j <= 3; j++) {
       console.log(`Row ${i}, Column ${j}`);
     }
   }

   // Output:
   // Row 1, Column 1
   // Row 1, Column 2
   // Row 1, Column 3
   // Row 2, Column 1
   // Row 2, Column 2
   // Row 2, Column 3
   // Row 3, Column 1
   // Row 3, Column 2
   // Row 3, Column 3
   ```

6. In this example, the outer loop runs three times, and for each iteration, the inner loop runs three times as well, resulting in a total of nine outputs.

#### Key Concepts

- **Initializer**: In loops like for, the initializer sets the starting value of the loop variable (e.g., let i = 0;).
- **Condition**: The condition defines the logic that determines whether the loop continues (e.g., i < 10;).
- **Iterator**: The iterator updates the loop variable after each iteration (e.g., i++).

#### Best Practices for Using Loops

- **Avoid Infinite Loops**: Ensure the condition of the loop is eventually met to avoid infinite looping.
- **Efficient Use**: Use loops for repetitive tasks to avoid redundant code.
- **Readability**: Make sure loops are simple and easy to understand. For complex logic, consider adding comments.

#### Assessment

Your supervisor, facilitator, or mentor will assess you based on the following:

- Correct **use of loops**: The ability to choose and implement the appropriate type of loop for different tasks (e.g., while, for, nested).
- **Loop structure**: Proper initialization, condition checking, and iteration to ensure loops run as expected.
- **Control flow**: Ensuring loops execute correctly based on conditions and that they terminate as intended.

---

#### Example Problem

**Task:**  
Write a program that prints the multiplication table for a number (e.g., 5) using a loop.

#### Solution:

```javascript
let number = 5;
for (let i = 1; i <= 10; i++) {
  console.log(`${number} x ${i} = ${number * i}`);
}
//5 x 1 = 5
//5 x 2 = 10
//...
//5 x 10 = 50
```

By completing this section, you will have developed a clear understanding of how to code loops, use them effectively, and ensure your code is both efficient and easy to maintain.
