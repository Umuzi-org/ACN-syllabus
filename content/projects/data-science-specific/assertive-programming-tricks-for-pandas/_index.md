---
content_type: project
submission_type: repo
title: Assertive programming helpers for Pandas
prerequisites:
  hard: 
  - topics/intro-to-assertive-programming
---

Data-science is a bit of a funny thing because even though data scientists write a lot of code, they typically aren't expected to follow all the software engineering best practices other kinds of developers would need to follow. 

This can be a really good thing because a data-scientist's job is usually to answer hard questions based on data, and make those answers clear to other people. A lot of the time, writing beautiful production-ready code is actually a bit of a waste of time.

But there is a problem - because data-scientists typically don't follow "software development best practices" then they don't get the benefits of those best practices.  For example, it's pretty rare for a data-scientist to write unit tests for a Jupyter notebook.

Data-scientists are human (usually) and so they are prone to human-error (like everyone else). So it's useful for data-scientists to have some way of at least doing some sanity-checking while they are writing code. 

That's where assertive programming comes in.

If you write good assertions in your code then:

1. You will have confidence that nothing insane is happening
2. Your code will be clearer to read since the assertions would make your thought-process more clear to anyone reading your code 

## Instructions

Please create a single file named `assertions.py`.  Inside this file you will write a number of functions that will make use of `assert` statements to raise errors with useful error messages if things are not as expected.

Here is an example of a pretty trivial assertion function:

```
def assert_equal(a,b):
    assert a == b , f"{a} {type(a)} != {b} {type(b)}"
```

Take note of:
- the use of the `assert` keyword
- how much useful information is included in the error message
- what happens if the assertion passes



Please implement the following functions:

```
def assert_df_dimensions_equal(df, height, width):

def assert_df_columns_equal(df,column_names):

def assert_no_duplicate_rows(df):

def assert_no_null_values(df):

def assert_all_values_positive(df):
```

## Think about

What other assertions are you likely to use in future? Maybe you would want to check if a specific column or row meets a specific condition.
