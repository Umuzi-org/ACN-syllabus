---
_db_id: 704
content_type: project
flavours:
- any_language
ready: true
submission_type: repo
title: Understanding map reduce
---

Many programming languages have map and reduce functions. In this project you'll learn about why that stuff is cool and you'll do some katas to get your heads around it.

The first thing to know is that map reduce is hella useful when it comes to processing big data. If you wanted to chug through 1TB of stuff, and distribute that processing across a fleet of computers like a boss, then you'll need a solid understanding of map-reduce.

## Big data 

MapReduce became popular because of a tool called Hadoop. You can read about how Hadoop does it here: https://www.guru99.com/introduction-to-mapreduce.html 


## Project instructions

Please use git feature branching. Use a separate branch for each task here. 

### Word-count

Write a well architected command line utility that:

- takes in a url as a command-line parameter. Assume the url points to a page of this syllabus site
- grabs the text from the web page
- uses your languages map and reduce functions in order to get the number of times each word appears in the text 
- this should be case insensitive. For example in the sentence "The ninja wrote the code", the word "the" appears twice
 
Please pretend that you are running something like Hadoop. Imagine that your data gets split across 50 computers and your map and reduce functions need to run on those machines, and that the results of those operations are combined on one machine right at the end.

That means you cant have a mapper or reducer function that has knowledge of anything except its direct inputs and outputs.  

Eg you MUST NOT do this:

```
// pseudocode

words = text.split()
word_counts = {}

words.map((word)=>{
    if (word_counts.get(word)){
        word_counts[word] = word_counts[word] + 1
    }
    else{
        word_counts[word] = 1
    }
})

```

Because the mapper function needs to know about stuff outside the mapper function.

### word count over many pages

Make use of the work you did in the previous task to make a command-line utility that:

- gets a list of urls as command line parameters
- grabs the text from each of those
- prints a list of the top 10 most uncommon words and where they are found

For example, this page has the word hippopotamus. It is incredibly unlikely that any other syllabus page has the word hippopotamus.

So if this page's url is an input for your script, then part of your output would be:

```
hippopotamus:
- {this url}

second most common word
- {some other url}
- {maybe another one}
```