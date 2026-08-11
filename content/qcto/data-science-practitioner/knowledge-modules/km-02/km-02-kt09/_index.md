---
content_type: topic
ready: true
title: KM-02-KT09: Modulus
---

## Learning Outcomes
1. **KT0901: Definition and Terminology**
   - Understand the concept of modulus and related terminology.
2. **KT0902: Purpose and Use**
   - Recognize the purpose and applications of modulus in mathematics and programming.
3. **KT0903: Modulus Abbreviated as “mod”**
   - Learn the abbreviation "mod" and how it is used to represent the modulus operation.
4. **KT0904: % Application**
   - Understand the application of the percent symbol (%) in modulus operations.
5. **KT0905: (==) Application**
   - Explore how the equality operator (==) is used in modulus-related contexts.
6. **KT0906: Modulus in Programming**
   - Understand how modulus is implemented in programming languages and its practical uses.

## KT0901: Definition and Terminology
- **Modulus** refers to the remainder of a division operation. Specifically, when dividing one number by another, the modulus is the leftover part after performing integer division.
  - Example: 100mod  9=1100 \mod 9 = 1 because 100 divided by 9 gives a quotient of 11 with a remainder of 1.
  - Modulus can also be seen as "wrapping around" once it reaches the modulus value.

## KT0902: Purpose and Use
- **Modulus** is commonly used in many practical applications, particularly in fields like programming, time calculations, and physics.
  - **In Programming:** The modulus operator (%) is widely used to handle periodic events, such as in clock arithmetic (calculating hours, minutes, seconds), or for pattern matching.
  - **In Time Calculations:** The modulus helps convert seconds to minutes, days, or other units.
  - **In Physics:** The modulus is used in concepts like Young's Modulus, which measures the elasticity of materials.

## KT0903: Modulus Abbreviated as “mod”
- **Modulo (or "mod")** is the operation that finds the remainder of a division of one integer by another.
  - Mathematical Notation: amod  b=ra \mod b = r, where:
    - aa is the dividend,
    - bb is the divisor (or modulus),
    - rr is the remainder.
  - Example:
    - 11mod  4=311 \mod 4 = 3 (since 11 divided by 4 gives a remainder of 3),
    - 25mod  5=025 \mod 5 = 0 (since 25 is exactly divisible by 5).

## KT0904: % Application
  - The percent sign (%) is used in programming languages to denote the modulus operator.
    - In Programming: It returns the remainder after dividing two numbers.
    - Example: 11%4=311 \% 4 = 3, because 11 divided by 4 leaves a remainder of 3.
    - The percent sign can also represent percentages (i.e., parts per hundred), but in modulus operations, it computes the remainder of division.

## KT0905: (==) Application
- **The equality operator** (==) checks whether two values are equal.
  - **In Modulus Contexts**: The equality operator can be used to compare the result of a modulus operation with a specific value.
  - Example: In the condition (a%b)==c(a \% b) == c, the program checks whether the remainder of dividing aa by bb equals cc.

## KT0906: Modulus in Programming
- **Modulus in Programming:** The modulus operator (%) is used to obtain the remainder from dividing two integers.
  - **Behavior**: If yy divides xx completely, the result is 0. Otherwise, the result is the remainder of the division.
  - **Example**:
    - 9%3=09 \% 3 = 0 (no remainder),
    - 5%2=15 \% 2 = 1 (remainder of 1).
  - In programming, modulus is essential for working with periodic cycles, such as calculating the day of the week or managing loops with a fixed number of iterations.
