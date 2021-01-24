---
_db_id: 376
content_type: topic
nqf: ncit
ready: false
tags: []
title: Search and Sort Techniques
unit_standards:
- 115373
---

## 1. Abstract data types

**What is abstract data type?**

An abstract data type is defined as a mathematical model of the data objects that make up a data type as well as the functions that operate on these objects. There are no standard conventions for defining them. A broad division may be drawn between "imperative" and "functional" definition styles.

To manage the complexity of problems and the problem-solving process, computer scientists use abstractions to allow them to focus on the “big picture” without getting lost in the details. By creating models of a problem, we are able to utilize a better and more efficient problem-solving process.

This “big picture” idea of hiding particular details is known as abstraction. An abstract data type, sometimes abbreviated ADT, is a logical description of how we view the data and the operations that are allowed on that data without regard to how they will be implemented. This means that we are concerned only with what the data is representing and not with how it will eventually be constructed. By providing this level of abstraction, we are creating an encapsulation around the data. The idea is that by encapsulating the details of the implementation, we are hiding them from the user’s view. This is called information hiding.

The implementation of an abstract data type, often referred to as a data structure, will require that we provide a physical view of the data using some collection of programming constructs and primitive data types.



**Data Structures**

A data structure is a particular way of organizing data in a computer so that it can be used efficiently. “Used efficiently” here means according to your needs. You may need a structure that allows very fast lookup or very fast insertion. The key thing to remember is that each data structure has its own advantages and disadvantages. There isn’t any one of them that would beat all of the others, that’s the reason why it is important to know many of them.

Here’s a partial list of data structures we can implement in computer programs:

 - Array

 - Hash Table

 - Set

 - Linked List

 - Stack

 - Queue

 - Tree

 - Binary Search Tree

 - Graph

We will focus on arrays, stacks, queues and hash tables. As you develop as a programmer, you will likely use most of these data structures, so it wouldn’t hurt to read a bit about them on your own.

**Arrays**

An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index. The simplest type of data structure is a linear array, also called one-dimensional array. In some programming languages the length of an array is established when the array is created. In JavaScript, it is very easy to add elements to an array, so it grows as your program needs it.



![An array of 10 elements](array-demo.png)

Each item in an array is called an element, and each element is accessed by its numerical index. As shown in the preceding illustration, numbering begins with 0. The 9th element, for example, would therefore be accessed at index 8.

```
//An array that stores 5 numbers.
var myArray = [12,24,36,48,60];
```

In JavaScript, you can mix that types of elements you have in an array (some languages require you to only have data of one type---e.g. only integers or only strings).

```
//An array with mixed data types
var myArray = ["apple", 24];
```

An element in an array can also be another array. This is sometimes called “nesting”. It is also called a multi-dimensional array.

```
//an array that contains 3 arrays, each of which stores numbers
var myArray = [[2,4,6],[1,2,3],[10,15,20]];
```

**Stacks**

A stack is a collection of elements which has two primary operations: push and pop. “Push” adds a new element to the end of the collection. “Pop” removes the most recently added element from the collection. Stack is sometimes called “Last In, First Out”.

A useful way to think about a stack is to imagine piling up paper on a desk. You place the first sheet of paper down (you “push” it on to the stack). Now you have one element in your collection. When you add another sheet of paper, it goes on top of the first sheet and becomes the second element in your collection. As you add more sheets (also known as “pushing”) they all stack on top of the previous sheets. If you want to remove a sheet of paper, you can only take from the top of the stack. In a stack, you can’t add or remove elements from the middle. You can only remove the most recent element you added from the end: the last element in the collection is the first one to be taken out. “Last In, First Out”

```
var stack = [];
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack); //[1,2,3]
stack.pop();
console.log(stack); //[1,2];
```

**Queue**

A queue is very similar to a stack, but the way you add and remove elements from your collection differs. A queue follows the model of “First In, First Out.” This is what you might expect given its name: it is just like people standing in a queue to buy something. The first person to join the queue will be the first person who is served. So the first element you “enqueue” will be the first element removed when you want to “dequeue”. In JavaScript, the “shift” command is used to “dequeue” an element (remove the element at index 0).

 
```
var queue = [];
queue.push(1);
queue.push(2);
queue.push(3);
 
console.log(queue); //[1,2,3]
queue.shift();
console.log(queue); //[2,3]
```

The “shift” command removes an element from the beginning of your array, which is the same as “dequeue-ing.”

## 2. Sort techniques

**Sorting** is a way of arranging data, usually in ascending or descending order. A sorting algorithm is an algorithm made up of a series of instructions that takes an array as input, performs specified operations on the array, and outputs a sorted array. 

There are many methods or algorithms for sorting. A few examples:

 - Bubble sort

 - Merge sort

 - Insertion sort

 - Quick sort

 - Heap sort

One of the easiest sorting methods to understand is “Bubble sort”. Just because it’s easy to understand how it works, doesn’t mean it’s the best or fastest way to sort. You’ll see there are much faster methods.

**Bubble sort**

Bubble sort is a simple sorting algorithm that works by comparing the first pair of items in the array and swapping them if they are in the wrong order. The algorithm continues with the next pair of items in the array, then the next, and the next, until it reaches the end. Then the algorithm goes back to the beginning and repeats this process until every item is in the correct order.

It is called Bubble sort, because with each iteration the largest element in the list bubbles up towards the last place, just like a water bubble rises up to the water surface.

![](bubble-sort.png)

Watch the video at the top of this website to see bubble sort in action:

https://brilliant.org/wiki/sorting-algorithms/

**Insertion sort**

Insertion sort is a comparison-based algorithm that builds a final sorted array one element at a time. It goes through an array one element at a time, and inserts that element into the right place. By the time the algorithm gets to the last element in the array, all the elements will be sorted. It is slightly faster than bubble sort (and selection sort) because it doesn’t have to loop through the array as many times. Like bubble sort, it is efficient for small data sets, but very inefficient for larger lists.

**Merge sort**

The video on Brilliant.org also explained merge sort, and showed why it can be much faster for a computer to complete. Merge sort uses a divide and conquer technique. This means taking two pre-sorted arrays and combining them in to one resulting array that is also sorted. In merge sort the unsorted list is divided into N sublists, each having one element, because a list consisting of one element is always sorted. Then, it repeatedly merges these sublists, to produce new sorted sublists, and in the end, only one sorted list is produced.


![](merge-sort.png)

Like we can see in the above example, merge sort first breaks the unsorted list into sorted sublists, each having one element, because a list of one element is considered sorted and then it keeps merging these sublists, to finally get the complete sorted list.



Another video explaining merge sort:

https://www.youtube.com/watch?v=e5ik2UGjHBk

A video about bubble sort, insertion sort, and quick sort:

https://www.youtube.com/watch?v=WaNLJf8xzC4


A note about JavaScript ES6: If you are familiar with the features of JavaScript ES6, you'll know that there is a built-in sort() function. It is a higher-order function (meaning it expects another function as the input argument). This following video gives an overview of how the sort() function works on arrays. 


Watch this video: [16.9: Array Functions: sort() - Topics of JavaScript/ES6](https://youtu.be/MWD-iKzR2c8)

If you are unfamiliar with higher-order functions, like reduce(), map(), etc., or "arrow function" syntax, then it is recommended you watch all videos in this Coding Train series (https://www.youtube.com/watch?v=H4awPsyugS0&list=PLRqwX-V7Uu6aAEUqu96Newc-7qpuh-cxc) on YouTube.