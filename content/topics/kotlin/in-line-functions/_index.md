---
_db_id: 385
content_type: topic
prerequisites:
  hard:
  - topics/kotlin/functions
  soft: []
ready: true
title: In Line Functions
---

Using __higher-order functions__ imposes certain runtime penalties: each function is an object, and it captures a closure, i.e. those variables that are accessed in the body of the function. Memory allocations (both for function objects and classes) and virtual calls introduce runtime overhead.

But it appears that in many cases this kind of overhead can be eliminated by inlining the lambda expressions. The functions shown below are good examples of this situation. I.e., the lock() function could be easily inlined at call-sites. Consider the following case:
```
lock(l) { foo() }
```
Instead of creating a function object for the parameter and generating a call, the compiler could emit the following code
```
l.lock()
try {
    foo()
}
finally {
    l.unlock()
}
```
Isn't it what we wanted from the very beginning?

To make the compiler do this, we need to mark the __lock()__ function with the __inline__ modifier:
```
inline fun lock<T>(lock: Lock, body: () -> T): T {
    // ...
}
```
The __inline__ modifier affects both the function itself and the lambdas passed to it: all of those will be inlined into the call site.

Inlining may cause the generated code to grow, but if we do it in a reasonable way (do not inline big functions) it will pay off in performance, especially at "megamorphic" call-sites inside loops.

### noinline
In case you want only some of the lambdas passed to an inline function to be inlined, you can mark some of your function parameters with the __noinline__ modifier:
```
inline fun foo(inlined: () -> Unit, noinline notInlined: () -> Unit) {
    // ...
}
```
Inlinable lambdas can only be called inside the inline functions or passed as inlinable arguments, but noinline ones can be manipulated in any way we like: stored in fields, passed around etc.

Note that if an inline function has no inlinable function parameters and no reified type parameters, the compiler will issue a warning, since inlining such functions is very unlikely to be beneficial (you can suppress the warning if you are sure the inlining is needed).

### Non-local returns
In Kotlin, we can only use a normal, unqualified return to exit a named function or an anonymous function. This means that to exit a lambda, we have to use a label, and a bare return is forbidden inside a lambda, because a lambda can not make the enclosing function return:
```
fun foo() {
    ordinaryFunction {
        return // ERROR: can not make `foo` return here
    }
}
```
But if the function the lambda is passed to is inlined, the return can be inlined as well, so it is allowed:
```
fun foo() {
    inlineFunction {
        return // OK: the lambda is inlined
    }
}
```
Such returns (located in a lambda, but exiting the enclosing function) are called non-local returns. We are used to this sort of constructs in loops, which inline functions often enclose:
```
fun hasZeros(ints: List<Int>): Boolean {
    ints.forEach {
        if (it == 0) return true // returns from hasZeros
    }
    return false
}
```
Note that some inline functions may call the lambdas passed to them as parameters not directly from the function body, but from another execution context, such as a local object or a nested function. In such cases, non-local control flow is also not allowed in the lambdas. To indicate that, the lambda parameter needs to be marked with the crossinline modifier:
```
inline fun f(crossinline body: () -> Unit) {
    val f = object: Runnable {
        override fun run() = body()
    }
    // ...
}
```
__break__ and __continue__ are not yet available in inlined lambdas, but we are planning to support them too

### Reified type parameters
Sometimes we need to access a type passed to us as a parameter:
```
fun <T> TreeNode.findParentOfType(clazz: Class<T>): T? {
    var p = parent
    while (p != null && !clazz.isInstance(p)) {
        p = p.parent
    }
    @Suppress("UNCHECKED_CAST")
    return p as T?
}
```
Here, we walk up a tree and use reflection to check if a node has a certain type. It’s all fine, but the call site is not very pretty:
```
treeNode.findParentOfType(MyTreeNode::class.java)
What we actually want is simply pass a type to this function, i.e. call it like this:
```
```
treeNode.findParentOfType<MyTreeNode>()
```
To enable this, inline functions support reified type parameters, so we can write something like this:
```
inline fun <reified T> TreeNode.findParentOfType(): T? {
    var p = parent
    while (p != null && p !is T) {
        p = p.parent
    }
    return p as T?
}
```
We qualified the type parameter with the reified modifier, now it’s accessible inside the function, almost as if it were a normal class. Since the function is inlined, no reflection is needed, normal operators like !is and as are working now. Also, we can call it as mentioned above: myTree.findParentOfType<MyTreeNodeType>().

Though reflection may not be needed in many cases, we can still use it with a reified type parameter:
```
inline fun <reified T> membersOf() = T::class.members

fun main(s: Array<String>) {
    println(membersOf<StringBuilder>().joinToString("\n"))
}
```
Normal functions (not marked as inline) can not have reified parameters. A type that does not have a run-time representation (e.g. a non-reified type parameter or a fictitious type like Nothing) can not be used as an argument for a reified type parameter.

### Inline properties (since 1.1)
The inline modifier can be used on accessors of properties that don't have a backing field. You can annotate individual property accessors:
```
val foo: Foo
    inline get() = Foo()

var bar: Bar
    get() = ...
    inline set(v) { ... }
```
You can also annotate an entire property, which marks both of its accessors as inline:
```
inline var bar: Bar
    get() = ...
    set(v) { ... }
```
At the call site, inline accessors are inlined as regular inline functions.