---
_db_id:
content_type: topic
ready: true
title: KM-02-KT01: Conversion Between Decimal and Binary Systems
---

## Learning Outcomes

- **KT0201:** Introduction to binary numbers
- **KT0202:** Performing addition and subtraction of positive whole numbers in binary
- **KT0203:** Binary arithmetic
- **KT0204:** Use of BODMAS

## KT0201: Introduction to Binary Numbers

**What is Binary?**

  Binary is a base-2 number system that uses only two digits: **`0`** and **`1`**. It is foundational to digital computing, enabling devices to encode information, perform arithmetic operations, and execute logical control processes.

 Binary is advantageous because it directly corresponds to the **on** and **off** states of electronic circuits, making it simple to implement in hardware.

Binary vs. Decimal

- **Decimal System:** Uses ten digits (0–9), each place value represents a power of 10.
- **Binary System:** Uses two digits (0 and 1), each place value represents a power of 2.


| Binary | Decimal Calculation                                 | Decimal Value |
|--------|------------------------------------------------------|---------------|
| 100    | 1×221 \times 2^2                                                | 4             |
| 101    | 1×22 + 0×21 + 1×201 \times 2^2 + 0 \times 2^1 + 1 \times 2^0                               | 5             |
| 10011  | 1×24 + 0×23 + 0×22 + 1×21 + 1×201 \times 2^4 + 0 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0                | 19            |

## KT0202: Performing Addition and Subtraction in Binary

**Binary Basics**
Each digit (or **bit**) in binary represents an increasing power of 2, starting from `202^0` at the rightmost digit.

| **Bit Position** | 232^3 | 222^2 | 212^1 | 202^0 |
|--------------|-----|-----|-----|-----|
| Decimal  | 8   | 4   | 2   | 1   |

Example: Converting Binary `11001100` to Decimal

- `1 × 23 + 1 × 22 + 0 × 21 + 0 × 201 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 0 \times 2^0`  
- `8 + 4 + 0 +0= 128 + 4 + 0 + 0 = 12`

**Binary Addition**
The rules for binary addition are:
- **Rules:**
  - `0 + 0 = 00 + 0 = 0`
  - `0 + 1 = 10 + 1 = 1`
  - `1 + 0 = 11 + 0 = 1`
  - `1 + 1 = 101 + 1 = 10` (write `0`, carry `1`)

**Example:**
```
101
+ 011
-----
1000
```

**Binary Subtraction**

Binary subtraction follows the borrowing rules:
1. `0−0=00 - 0 = 0`
2. `1−0=11 - 0 = 1`
3. `1−1=01 - 1 = 0`
4. `0−1=10 - 1 = 1` (borrow 1 from the next column)

**Example:**

```
 1010
-  011
------
   0111
```

## KT0203: Binary Arithmetic

Binary Multiplication

Similar to decimal multiplication but simpler since it only involves 00 and 11.
 Rules:
1. `0×0=00 \times 0 = 0`
2. `1×0=01 \times 0 = 0`
3. `0×1=00 \times 1 = 0`
4. `1×1=11 \times 1 = 1`
   
**Example:**
```
  101
×   11
------
   101
+ 1010
------
  1111
```

**Binary Division**

Binary division resembles long division in decimals. The result is expressed in binary with remainders.

## KT0204: Use of BODMAS

**What is BODMAS?**

BODMAS is an acronym to guide the order of operations in calculations:

- **B**: Brackets
- **O**: Order (e.g., powers and roots)
- **D**: Division
- **M**: Multiplication
- **A**: Addition
- **S**: Subtraction
  
Operations should be performed **left-to-right** for Division/Multiplication and Addition/Subtraction.

**Example:**

 Calculate (3+5)×22−4÷2(3 + 5) \times 2^2 - 4 \div 2:

1. Brackets: (3+5)=8(3 + 5) = 8
2. Order: 22=42^2 = 4
3. Multiplication: 8×4=328 \times 4 = 32
4. Division: 4÷2=24 \div 2 = 2
5. Subtraction: 32−2=3032 - 2 = 30
