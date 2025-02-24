---
_db_id:
content_type: topic
ready: true
title: KM-02-KT07: Operator Precedence
---

## Learning Outcomes
1. **KT0701: Definition and Terminology**
Understand what operator precedence means and how it affects the evaluation of expressions.
2. **KT0702: Purpose and Use**
Recognize the purpose of operator precedence and how it affects computations.
3. **KT0703: Order of Operations (Left to Right)**
Comprehend the standard order of operations for various operators.
4. **KT0704: Apply Precedence**
Apply operator precedence to solve expressions, including the use of parentheses, multiplication/division, and addition/subtraction.
5. **KT0705: Use of PEMDAS in Programming**
Understand and apply the concept of PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) in programming languages.

## KT0701: Definition and Terminology
- **Operator Precedence** refers to the rules that govern the order in which operations are performed in an expression. Higher-precedence operators are executed before lower-precedence ones.
  - Example: In the expression 1+5×31 + 5 \times 3, multiplication (×\times) has higher precedence than addition (+), so the multiplication is performed first: 1+(5×3)=1+15=161 + (5 \times 3) = 1 + 15 = 16
  - **Precedence with Example**: In C, the multiplication (×\times) operator has a higher precedence than subtraction (−-): x=5−(17×6)x = 5 - (17 \times 6)
  - Here, multiplication is performed first.
## KT0702: Purpose and Use
- The **purpose** of operator precedence is to ensure that expressions are evaluated in the correct order. Without operator precedence, mathematical expressions could lead to incorrect results.
- **Associativity**: Operators of the same precedence are evaluated based on their associativity (left-to-right or right-to-left).
  - Example: Multiplication and division are left-to-right, meaning 5×3÷25 \times 3 \div 2 is evaluated as: (5×3)÷2=15÷2=7.5(5 \times 3) \div 2 = 15 \div 2 = 7.5

## KT0703: Order of Operations (Left to Right)
The general **order of precedence** for operators is:
1. **Exponentiation and root extraction** (highest precedence)
2. **Multiplication and division**
3. **Addition and subtraction** (lowest precedence)

In mathematical and programming contexts:
   - **Exponents** are calculated first.
   - Then, **multiplication** and **division** (from left to right).
   - Lastly, **addition** and **subtraction** (from left to right).

This ensures that mixed operations follow a standard order to avoid ambiguity.
## KT0704: Apply Precedence
- In expressions with mixed operators, parentheses can be used to explicitly set precedence. For example:
  - Without parentheses: 1+5×31 + 5 \times 3, the result is 1616.
  - With parentheses: (1+5)×3(1 + 5) \times 3, the result is 1818.

In networking and IP packet prioritization, **precedence** values determine the priority of different packets, with precedence types ranging from 0 to 7. This is used in network policies to manage packet transmission priorities.

## KT0705: Use of PEMDAS in Programming
- **PEMDAS** (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) is a mnemonic used to remember the order of operations:
  - **P**arentheses: Solve expressions inside parentheses first.
  - **E**xponents: Evaluate powers and roots.
  - **MD:** Multiplication and Division (left-to-right).
  - **AS:** Addition and Subtraction (left-to-right).

Some programming languages may handle operations differently, but the basic idea remains consistent.
