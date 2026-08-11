---
content_type: topic
ready: true
title: KM-02-KT08: Integer Division
---

## Learning Outcomes
- **KT0801: Definition and Terminology**
  - Understand the concept of integer division and the terminology associated with it.
- **KT0802: Purpose and Use**
  - Recognize the purpose and uses of integer division in various contexts.
- **KT0803: Rules on How to Divide Integers**
  - Learn the rules for dividing integers, including the effect of signs on the quotient.
- **KT0804: Names and Symbols for Integer Division**
  - Familiarize with the various names and symbols used to denote integer division.
- **KT0805: Software for Integer Division**
  - Understand how integer division is implemented in programming languages and how it behaves in different scenarios.

## KT0801: Definition and Terminology
- **Integer Division** refers to division where the remainder is discarded, and the result is an integer.
  - Example: In Python 2.7, the expression 3÷23 \div 2 would return 11 (discarding the remainder), whereas in Python 3, the same operation would return 1.51.5.
  - Integer division can be represented by symbols such as // in Python or / in Java when both operands are integers.

## KT0802: Purpose and Use
- The **purpose of division** is to share a quantity into equal groups.
  - Example: To divide 16 balls into 4 equal groups, you would use 16÷4=416 \div 4 = 4, meaning each group contains 4 balls.
  - Division is the inverse operation of multiplication. If 3×4=123 \times 4 = 12, then 12÷4=312 \div 4 = 3.
  - **Special Names:**
    - Dividend: The number being divided.
    - Divisor: The number by which the dividend is divided.
    - Quotient: The result of the division.
    - Remainder: The leftover part when division is not exact.

## KT0803: Rules on How to Divide Integers
- **Rule 1**: The quotient of a positive integer divided by a negative integer is negative.
  - Example: 8÷−4=−28 \div -4 = -2
- **Rule 2**: The quotient of two positive integers is positive.
  - Example: 8÷4=28 \div 4 = 2
- **Rule 3**: The quotient of two negative integers is positive.
  - Example: −8÷−4=2-8 \div -4 = 2
- The result’s sign depends on whether the operands are positive or negative, following these basic rules.

## KT0804: Names and Symbols for Integer Division
- **Symbols for Integer Division:**


  - `div` (mathematical notation).
  - `/` (commonly used in programming languages like Java and Python).
  - `\\` (used in some languages like Python for integer division).
  - `%` (modulus operator to get the remainder).
- Integer division can be computed using these symbols, with behavior varying based on the context (positive or negative values).


## KT0805: Software for Integer Division
- In programming:
  - **Python**: The `//` operator is used for integer division, which returns the quotient without the remainder.
    - Example: 7//3=27 // 3 = 2 (discarding the remainder).
  - **Java**: The / operator performs integer division if both operands are integers, discarding the remainder.
    - Example: 7/3=27 / 3 = 2
  - To get a real (floating-point) result, at least one operand must be of type `double`. For example, in Java, casting one of the operands to `double` would perform real division.
