---
content_type: topic
ready: true
title: KM-02-KT11: Mixing Types
---

## Learning Outcomes
1. **KT1101: Definition and Terminology**
   - Understand the concept of mixing types in mathematical and programming contexts.
2. **KT1102: Purpose and Use**
   - Recognize the purpose and applications of mixing types in various scenarios.
3. **KT1103: Apply an Operator**
   - Learn how to apply operators, particularly in queries involving table-valued functions.
4. **KT1104: Combination with the Order of Operations**
   - Understand how mixed operations work in combination with the order of operations.
5. **KT1105: The Order in Which an Expression is Written**
   - Grasp how the order of operations impacts the evaluation of mathematical and programming expressions.
6. **KT1106: How a Computer Would Evaluate Some Expressions that Combine Types**
   - Learn how a computer evaluates expressions that mix different data types.

## KT1101: Definition and Terminology
- **Mixing** in a general context refers to combining different elements (like liquids, solutions, or substances) to form a new mixture.
  - **Example**: Mixing water and a solution with a ratio of 8:1 (8 parts water, 1 part solution) results in a mixture of 9 parts.
  - **Mixing Solutions**: You can calculate dilution or mixing ratios using formulas such as **C1V1 = C2V2**, where C is the concentration and V is the volume.
    - **Example**: To dilute 95% ethanol to 70%, use the formula to determine the volume of 95% ethanol required for a final volume of 100 ml at 70% concentration.


## KT1102: Purpose and Use
- **Purpose of Mixing**: In various fields (e.g., music, chemistry, programming), mixing is used to combine components in a way that optimizes the result. For example:
  - In **audio mixing**, adjusting levels and adding effects to multiple tracks creates a cohesive sound.
  - Mix **Ratios and Percentages**: If you know the mix ratio (e.g., 8:1), you can calculate the percentage by dividing 1 by the total number of parts (9 in this case) to get 11.1%.
  - Conversely, if you know the percentage (e.g., 4%), you can calculate the ratio (96:4, simplified to 24:1).

## KT1103: Apply an Operator
- **The APPLY Operator** in SQL is used to invoke a table-valued function for each row returned by an outer table expression.
  - **Syntax**: The APPLY operator is used when combining two tables or functions:

```
Example:
SELECT a.*, b.*
FROM tableA a
CROSS APPLY dbo.fn_tablefunction(a.id) b
```

  - The APPLY operator evaluates the right input (the function) for each row in the left input (the table), combining them in the final output.
  
## KT1104: Combination with the Order of Operations
- The **Order of Operations** (PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) is the sequence in which mathematical operations are performed.
- **Example**: In `3 × (2 + 4)`, parentheses are handled first: `2 + 4 = 6`, and then `3 × 6 = 18`.
- **Combined Operations**: When combining operations like addition and multiplication, ensure to follow the correct order to avoid mistakes.
  
## KT1105: The Order in Which an Expression is Written
- **Order of Operations in Programming**: Similar to mathematical expressions, programming languages follow a specific order when evaluating expressions, which helps prevent ambiguity.
  - **Example**: In the expression `1 + 2 × 3`, the multiplication is done first, resulting in `1 + 6 = 7`, not `(1 + 2) × 3 = 9`.
  - **Use of Parentheses**: Parentheses can override the default order of operations. For example, `(2 + 3) × 4 = 20` forces the addition to be done first.
  - **Nested Parentheses**: Use different brackets (`[ ]`, `{ }`) to avoid confusion when multiple pairs are involved.

## KT1106: How a Computer Would Evaluate Some Expressions that Combine Types
- **Evaluating Expressions**: To evaluate an expression in programming or mathematics, a variable is substituted with a specific value, and the expression is simplified step by step following the order of operations.
  - **Example**: To evaluate the expression `3 + 5 × 2`, first calculate `5 × 2 = 10`, then `3 + 10 = 13`.
