---
_db_id: 363
content_type: topic
ncit_specific_outcomes:
- assessment_criteria:
  - The documentation design covers the format of the documents in line with industry
    conventions.
  - The documentation plan covers full program documentation components.
  outcome: 1
  title: Plan and design documentation for a computer program to agreed standards.
- assessment_criteria:
  - The documentation is created according to the design created in specific outcome
    'Plan and design documentation for a computer program to agreed standards'.
  - The documentation components created are created according to the plan specified
    in specific outcome 'Plan and design documentation for a computer program to agreed
    standards'.
  - The documentation created is structured sensibly, defining how program specifications
    have been met.
  outcome: 2
  title: Create documentation for a computer program to agreed standards.
- assessment_criteria:
  - The review identifies if documentation was created according to the design created
    in specific outcome 'Plan and design documentation for a computer program to agreed
    standards'.
  - The review identifies if documentation was created consistent with the computer
    program being documented.
  outcome: 3
  title: Review documentation for a computer program for completeness.
ncit_standards:
- 115388
prerequisites:
  hard:
  - topics/clean-code
ready: false
tags:
- ncit
- documentation
title: Pseudocode and documentation
---

### 1. Why document?

Documenting software is one of the most crucial, but often most neglected parts of the development process. Documenting your variables, functions, and entire programs is absolutely necessary if you are to succeed as a coder. Various sources will tell you to dedicate at least 10% of your development time to documentation. That is reasonable advice, and should be adopted when you are planning the development of any program or website.

After we cover some best practices for documentation, we will cover the general process for documentation (listed below). Each of these will be covered in detail in the following sections.

#### Documentation Process

1. Pseudocode

2. Convert pseudocode to comments

3. Update comments as program changes

4. Add summary/high-level instructions

5. Develop user documentation (API docs) and technical docs (for other coders and administrators)

### 2. Best practices

#### Documentation requirements

The first step of documentation should take place before you write a single line of code. If your organization follows a “Waterfall” process, there will be several planning and “vision” documents that outline all the resources needed and plans for development. However, in the Agile project management process, teams produce far fewer documents before development starts. The product owner may create a document outlining user requirements and goals for the project, but most of the documentation will come during and after development.

What are these development documents used for?

The main reasons why people need the technical design document for their work:

- Stakeholders require the reports.
- Customers need to feel more secure and at ease using the program.
- To keep track of everything on the project.
- For audit purposes.
- As a training material for new people in the team.

#### Agile documentation best practices:

**Only the relevant information**

Agile suggests that only the most necessary information should be documented.

What is the need for documenting something everyone knows? Create a vision, if it helps you get fundraising. Write only the customer documents your customers require. Document your decisions only if there are alternatives and you need a reminder of what was behind those decisions.

**Wait before documenting**

This is the best way to avoid the false information in your papers. Document later. Wait until the decision is implemented and there’s no going back until you actually put it on paper. The information is stabilized and reliable. You economize the cost, time and effort spent on redoing your documents. Note: This only applies to high-level documents that explain your program to a user. You should document your code with comments/pseudocode before you write any code.

**Be specific**

Keep in mind, that every project has its own requirements and specifications. You cannot apply the document templates for one project while working with a different one. Some fields might not even exist in a project whilst some important ones are missing.

In addition, the customers are different and what works with one is simply not enough for the other. Let the customers decide on the content and amount of your documentation. It will save you some extra work and nerves.

**Keep it all in one place**

Technical design documents have to be accessible and transparent. You need to have them available for anyone who might be in need for them. So as not to have a mess, keep all your papers in order and in one place. A real life-hack is to create your own Wiki or at least a separate folder in your GitHub repository that everyone can access.

For more info on Agile documentation can be found [here](https://easternpeak.com/blog/agile-documentation/).

### 3. Pseudocode

Once the general requirements and goals have been documented (or at least discussed and agreed upon by the team), you should start by writing pseudocode. Starting with pseudocode will help you think through all the functionality of your program without getting distracted by the technical details of how you will implement it. The added bonus of creating good pseudocode for all the functions of your program is that pseudocode is easily converted into comments.

To review the steps of how and why to write pseudocode, visit the following link:

https://www.wikihow.com/Write-Pseudocode

A quick summary (halfway down the page) with examples: https://web.archive.org/web/20210414161651/http://userpages.wittenberg.edu/bshelburne/Comp150/Algorithms.htm

A quick video description is [here](https://www.khanacademy.org/computing/computer-programming/programming/good-practices/pt/planning-with-pseudo-code)

## 4. DON'T DO THIS

```
var a = 0; // declare a variable called a
```

If you ever catch yourself rewriting your code as English sentences, you are doing it wrong and it adds no value.

Comments in your code exist to add clarity, coders read code. They don't need you to rewite things in English. 

Comments should be used to overcome confusing things. For example, you can explain *why* you are doing something. Or you could link to an external document that explains an algorithm you are implementing.

Also, if you choose good variable and function names then comments become less necessary.

For example,
```
// BAD

const myFunction = x => {
    return (5 / 9) * (x - 32);   
}

// GOOD

const fahrenheitToCelcius = fahrenheit => {
    return (5 / 9) * (fahrenheit - 32);   
}
```