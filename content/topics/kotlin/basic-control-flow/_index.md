---
_db_id: 291
content_type: topic
prerequisites:
  hard:
  - topics/kotlin/basic-syntax-types
  soft: []
ready: true
title: Basic Control Flow
---

### "If" Expression

In Kotlin, "if" is an expression, i.e. it returns a value. Therefore there is no ternary operator (condition ? then : else), because ordinary if works fine in this role.

```
// Traditional usage

var max = a

if (a \&lt; b) max = b

// With else

var max: Int

if (a >; b) {

max = a

} else {

max = b

}

// As expression

val max = if (a > b) a else b 
```
"if" branches can be blocks, and the last expression is the value of a block: 
```

val max = if (a > b) { 

    print("Choose a") 

    a 

} else { 

    print("Choose b") 

    b 

}
```



If you're using "if" as an expression rather than a statement (for example, returning its value or assigning it to a variable), the expression is required to have an else branch.

### When Expression

when replaces the switch operator of C-like languages. In the simplest form it looks like this


```
when (x) {

 1 -> print("x == 1") 

    2 -> print("x == 2") 

    else -> { // Note the block 

        print("x is neither 1 nor 2") 
}

}
```
when matches its argument against all branches sequentially until some branch condition is satisfied. when can be used either as an expression or as a statement. If it is used as an expression, the value of the satisfied branch becomes the value of the overall expression. If it is used as a statement, the values of individual branches are ignored. (Just like with if, each branch can be a block, and its value is the value of the last expression in the block.)

The else branch is evaluated if none of the other branch conditions are satisfied. If when is used as an expression, the else branch is mandatory, unless the compiler can prove that all possible cases are covered with branch conditions.

If many cases should be handled in the same way, the branch conditions may be combined with a comma:
```
when (x) {

 0, 1 -> print("x == 0 or x == 1") 

    else -> print("otherwise") 

}
```
We can use arbitrary expressions (not only constants) as branch conditions
```
when (x) {
arseInt(s) -> print("s encodes x") 

    else -> print("s does not encode x") 

}
```
We can also check a value for being in or !in a range or a collection:
```
when (x) {

 in 1..10 -> print("x is in the range") 

    in validNumbers -> print("x is valid") 

    !in 10..20 -> print("x is outside the range") 

    else -> print("none of the above") 
}
```
Another possibility is to check that a value is or !is of a particular type. Note that, due to smart casts, you can access the methods and properties of the type without any extra checks.
```
fun hasPrefix(x: Any) = when(x) { 
 
     is String -> x.startsWith("prefix") 
 
     else -> false 

}
```
when can also be used as a replacement for an if-else if chain. If no argument is supplied, the branch conditions are simply boolean expressions, and a branch is executed when its condition is true:
```
when {

  x.isOdd() -> print("x is odd") 

    x.isEven() -> print("x is even") 

    else -> print("x is funny") 
}
```
### For Loops
```
for loop iterates through anything that provides an iterator. The syntax is as follows:

for (item in collection) print(item)

The body can be a block.

for (item: Int in ints) {

// ...

}
```
As mentioned before, for iterates through anything that provides an iterator, i.e.

has a member- or extension-function iterator(), whose return type

has a member- or extension-function next(), and

has a member- or extension-function hasNext() that returns Boolean.

All of these three functions need to be marked as operator.

A for loop over an array compiled to an index-based loop that does not create an iterator object.

If you want to iterate through an array or a list with an index, you can do it this way:
```
for (i in array.indices) {

print(array[i])

}
```
Note that this &quot;iteration through a range&quot; is compiled down to optimal implementation with no extra objects created.

Alternatively, you can use the withIndex library function:
```
for ((index, value) in array.withIndex()) { 

    println("the element at $index is $value") 

} 
```
### While Loops

while and do..while work as usual
```
while (x > 0) {

x--

}

do {

val y = retrieveData()

} while (y != null) // y is visible here!
```
### Break and continue in loops

Kotlin supports traditional break and continue operators in loops.

Returns and Jumps
Kotlin has three structural jump expressions:

return. By default returns from the nearest enclosing function or anonymous function.
break. Terminates the nearest enclosing loop.
continue. Proceeds to the next step of the nearest enclosing loop.
All of these expressions can be used as part of larger expressions:

```
val s = person.name ?: return
```

The type of these expressions is the Nothing type.

### Break and Continue Labels
Any expression in Kotlin may be marked with a label. Labels have the form of an identifier followed by the @ sign, for example: abc@, fooBar@ are valid labels. To label an expression, we just put a label in front of it

```
loop@ for (i in 1..100) {
    // ...
}
```

Now, we can qualify a break or a continue with a label:

````
loop@ for (i in 1..100) {
    for (j in 1..100) {
        if (...) break@loop
    }
}

````

A break qualified with a label jumps to the execution point right after the loop marked with that label. A continue proceeds to the next iteration of that loop.

### Return at Labels
With function literals, local functions and object expression, functions can be nested in Kotlin. Qualified returns allow us to return from an outer function. The most important use case is returning from a lambda expression. Recall that when we write this:

````
fun foo() {
    ints.forEach {
        if (it == 0) return
        print(it)
    }
}
````

The return-expression returns from the nearest enclosing function, i.e. foo. (Note that such non-local returns are supported only for lambda expressions passed to inline functions.) If we need to return from a lambda expression, we have to label it and qualify the return:

````
fun foo() {
    ints.forEach lit@ {
        if (it == 0) return@lit
        print(it)
    }
}

````

Now, it returns only from the lambda expression. Oftentimes it is more convenient to use implicits labels: such a label has the same name as the function to which the lambda is passed.

````
fun foo() {
    ints.forEach {
        if (it == 0) return@forEach
        print(it)
    }
}

````

Alternatively, we can replace the lambda expression with an anonymous function. A return statement in an anomymous function will return from the anonymous function itself.

````
fun foo() {
    ints.forEach(fun(value: Int) {
        if (value == 0) return
        print(value)
    })
}
````

When returning a value, the parser gives preference to the qualified return, i.e.

return@a 1
means "return 1 at label @a" and not "return a labeled expression (@a 1)".