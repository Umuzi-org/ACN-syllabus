---
_db_id: 302
content_type: topic
prerequisites:
  hard:
  - topics/kotlin/set-up
  soft: []
ready: true
title: Basic Syntax & Types
---

### [var us val:](https://www.youtube.com/watch?v=Nz-lMqxfUUs)

- **val and var** both are used to declare a variable.
- **var** is like general variable and it&#39;s known as a **mutable** variable in **Kotlin** and can be assigned multiple times.
- **val** is like Final variable and it&#39;s known as **immutable** in **Kotlin** and can be initialized only single time., after it become read only. The IllegalAccessorError will occur when you try to reassign the value.
- You can enforce a type called [strongtyping](https://whatis.techtarget.com/definition/strongly-typed). This is the opposite of statically typed.

Syntaxt : var book:String = &quot;Maths&quot; // This should only be used when necessary.

### Numbers:

- Kotlin handles numbers in a way close to Java, but not exactly the same.
- Kotlin provides the following built in types representing numbers (this is close to Java):

| **Type** | **Bit** [**Width**](https://www.youtube.com/watch?v=_SkpnG571z8) |
| --- | --- |
| Double | 64 |
| Float | 32 |
| Long | 64 |
| Int(Default data type in Kotlin) | 32 |
| Short | 16 |
| Byte | 8 |

### Characters:

- Note that characters are not numbers in Kotlin.
- Characters are represented by the type Char.
- They cannot be treated directly as number.
- [In Java](https://www.youtube.com/watch?v=LBQrD2nkKQg) they are stored as numbers internally.
  - [https://www.youtube.com/watch?v=LBQrD2nkKQg](https://www.youtube.com/watch?v=LBQrD2nkKQg)


```
Fun check(c: Char){

If (c == 1) {

// Error : incomaptable types will occur

}

}
```


### Booleans:

The type Boolean represents booleans, has a **true** or **false** value.

**Arrays:**

Arrays in Kotlin are represented by the array class, that has get and set functions (that turn into [] by operator overloading conventions), and size property, along with a few other useful member functions:


```
Class Array private constructor() {

val size: int

operator fun get (index : Int) T

operator fun set(index : Int, value: T ) : Unit

}
```


### Strings

Strings represented by the type String. Strings are immutable.

They are immutable in nature.

Should be written in double quotes.

Elements of a string are characters that can be accessed by the indexing operation:


```
s[I]

A string can be iterated over with a for loop:

for (c in str){

prinln(c)

}
```

### Defining packages
Package specification should be at the top of the source file:
```
package my.demo

import java.util.*

// ...
```
It is not required to match directories and packages: source files can be placed arbitrarily in the file system.

### Defining functions
Function having two Int parameters with Int return type:
```
//sampleStart
fun sum(a: Int, b: Int): Int {
    return a + b
}
//sampleEnd

fun main(args: Array<String>) {
    print("sum of 3 and 5 is ")
    println(sum(3, 5))
}
```
Function with an expression body and inferred return type:
```
//sampleStart
fun sum(a: Int, b: Int) = a + b
//sampleEnd

fun main(args: Array<String>) {
    println("sum of 19 and 23 is ${sum(19, 23)}")
}

```
Function returning no meaningful value:
```
//sampleStart
fun printSum(a: Int, b: Int): Unit {
    println("sum of $a and $b is ${a + b}")
}
//sampleEnd

fun main(args: Array<String>) {
    printSum(-1, 8)
}
```
Unit return type can be omitted:
```
//sampleStart
fun printSum(a: Int, b: Int) {
    println("sum of $a and $b is ${a + b}")
}
//sampleEnd

fun main(args: Array<String>) {
    printSum(-1, 8)
}
```
### Defining local variables
Assign-once (read-only) local variable:
```
fun main(args: Array<String>) {
//sampleStart
    val a: Int = 1  // immediate assignment
    val b = 2   // `Int` type is inferred
    val c: Int  // Type required when no initializer is provided
    c = 3       // deferred assignment
//sampleEnd
    println("a = $a, b = $b, c = $c")
}
```
Mutable variable:
```
fun main(args: Array<String>) {
//sampleStart
    var x = 5 // `Int` type is inferred
    x += 1
//sampleEnd
    println("x = $x")
}
```
### Comments
Just like Java and JavaScript, Kotlin supports end-of-line and block comments.
```
// This is an end-of-line comment

/* This is a block comment
   on multiple lines. */
```
Unlike Java, block comments in Kotlin can be nested.

### Using string templates
```
fun main(args: Array<String>) {
//sampleStart
    var a = 1
    // simple name in template:
    val s1 = "a is $a"

    a = 2
    // arbitrary expression in template:
    val s2 = "${s1.replace("is", "was")}, but now is $a"
//sampleEnd
    println(s2)
}
```
### Using conditional expressions
```
//sampleStart
fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}
//sampleEnd

fun main(args: Array<String>) {
    println("max of 0 and 42 is ${maxOf(0, 42)}")
}
```
Using if as an expression:
```
//sampleStart
fun maxOf(a: Int, b: Int) = if (a > b) a else b
//sampleEnd

fun main(args: Array<String>) {
    println("max of 0 and 42 is ${maxOf(0, 42)}")
}
```
### Using nullable values and checking for null
A reference must be explicitly marked as nullable when null value is possible.

Return null if str does not hold an integer:
```
fun parseInt(str: String): Int? {
    // ...
}
Use a function returning nullable value:

fun parseInt(str: String): Int? {
    return str.toIntOrNull()
}

//sampleStart
fun printProduct(arg1: String, arg2: String) {
    val x = parseInt(arg1)
    val y = parseInt(arg2)

    // Using `x * y` yields error because they may hold nulls.
    if (x != null && y != null) {
        // x and y are automatically cast to non-nullable after null check
        println(x * y)
    }
    else {
        println("either '$arg1' or '$arg2' is not a number")
    }
}
//sampleEnd


fun main(args: Array<String>) {
    printProduct("6", "7")
    printProduct("a", "7")
    printProduct("a", "b")
}
```
or
```
fun parseInt(str: String): Int? {
    return str.toIntOrNull()
}

fun printProduct(arg1: String, arg2: String) {
    val x = parseInt(arg1)
    val y = parseInt(arg2)

//sampleStart
    // ...
    if (x == null) {
        println("Wrong number format in arg1: '${arg1}'")
        return
    }
    if (y == null) {
        println("Wrong number format in arg2: '${arg2}'")
        return
    }

    // x and y are automatically cast to non-nullable after null check
    println(x * y)
//sampleEnd
}

fun main(args: Array<String>) {
    printProduct("6", "7")
    printProduct("a", "7")
    printProduct("99", "b")
}
```
### Using type checks and automatic casts
The is operator checks if an expression is an instance of a type. If an immutable local variable or property is checked for a specific type, there's no need to cast it explicitly:
```
//sampleStart
fun getStringLength(obj: Any): Int? {
    if (obj is String) {
        // `obj` is automatically cast to `String` in this branch
        return obj.length
    }

    // `obj` is still of type `Any` outside of the type-checked branch
    return null
}
//sampleEnd


fun main(args: Array<String>) {
    fun printLength(obj: Any) {
        println("'$obj' string length is ${getStringLength(obj) ?: "... err, not a string"} ")
    }
    printLength("Incomprehensibilities")
    printLength(1000)
    printLength(listOf(Any()))
}
```
or
```
//sampleStart
fun getStringLength(obj: Any): Int? {
    if (obj !is String) return null

    // `obj` is automatically cast to `String` in this branch
    return obj.length
}
//sampleEnd


fun main(args: Array<String>) {
    fun printLength(obj: Any) {
        println("'$obj' string length is ${getStringLength(obj) ?: "... err, not a string"} ")
    }
    printLength("Incomprehensibilities")
    printLength(1000)
    printLength(listOf(Any()))
}
```
or even
```
//sampleStart
fun getStringLength(obj: Any): Int? {
    // `obj` is automatically cast to `String` on the right-hand side of `&&`
    if (obj is String && obj.length > 0) {
        return obj.length
    }

    return null
}
//sampleEnd


fun main(args: Array<String>) {
    fun printLength(obj: Any) {
        println("'$obj' string length is ${getStringLength(obj) ?: "... err, is empty or not a string at all"} ")
    }
    printLength("Incomprehensibilities")
    printLength("")
    printLength(1000)
}
```
### Using a for loop
```
fun main(args: Array<String>) {
//sampleStart
    val items = listOf("apple", "banana", "kiwi")
    for (item in items) {
        println(item)
    }
//sampleEnd
}
```
or
```
fun main(args: Array<String>) {
//sampleStart
    val items = listOf("apple", "banana", "kiwi")
    for (index in items.indices) {
        println("item at $index is ${items[index]}")
    }
//sampleEnd
}
```
### Using a while loop
```
fun main(args: Array<String>) {
//sampleStart
    val items = listOf("apple", "banana", "kiwi")
    var index = 0
    while (index < items.size) {
        println("item at $index is ${items[index]}")
        index++
    }
//sampleEnd
}
```
### Using when expression
```
//sampleStart
fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }
//sampleEnd

fun main(args: Array<String>) {
    println(describe(1))
    println(describe("Hello"))
    println(describe(1000L))
    println(describe(2))
    println(describe("other"))
}
```
### Using ranges
Check if a number is within a range using in operator:
```
fun main(args: Array<String>) {
//sampleStart
    val x = 10
    val y = 9
    if (x in 1..y+1) {
        println("fits in range")
    }
//sampleEnd
}
```
Check if a number is out of range:
```
fun main(args: Array<String>) {
//sampleStart
    val list = listOf("a", "b", "c")

    if (-1 !in 0..list.lastIndex) {
        println("-1 is out of range")
    }
    if (list.size !in list.indices) {
        println("list size is out of valid list indices range too")
    }
//sampleEnd
}
```
Iterating over a range:
```
fun main(args: Array<String>) {
//sampleStart
    for (x in 1..5) {
        print(x)
    }
//sampleEnd
}
or over a progression:

fun main(args: Array<String>) {
//sampleStart
    for (x in 1..10 step 2) {
        print(x)
    }
    for (x in 9 downTo 0 step 3) {
        print(x)
    }
//sampleEnd
}
```
### Using collections
Iterating over a collection:
```
fun main(args: Array<String>) {
    val items = listOf("apple", "banana", "kiwi")
//sampleStart
    for (item in items) {
        println(item)
    }
//sampleEnd
}
```
Checking if a collection contains an object using in operator:
```
fun main(args: Array<String>) {
    val items = setOf("apple", "banana", "kiwi")
//sampleStart
    when {
        "orange" in items -> println("juicy")
        "apple" in items -> println("apple is fine too")
    }
//sampleEnd
}
```
Using lambda expressions to filter and map collections:
```
fun main(args: Array<String>) {
    val fruits = listOf("banana", "avocado", "apple", "kiwi")
//sampleStart
    fruits
        .filter { it.startsWith("a") }
        .sortedBy { it }
        .map { it.toUpperCase() }
        .forEach { println(it) }
//sampleEnd
}
```