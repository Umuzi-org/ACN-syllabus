---
_db_id: 374
content_type: topic
nqf: ncit
ready: false
tags:
- agile
title: Managing the Software Development Process
unit_standards:
- 115392
---

## 1. Understand the problem


The first step to developing any new solution (whether the final “product” will be software, hardware, or a new process) is to understand the issues and problems faced by the user. You’ve had practice with the process with Human-Centered Design. HCD is a great tool for gaining insight into the needs and problems of a user. It should be your first choice whenever you are working on a new project.

### User Stories
Once you’ve empathised with the user, a useful method to get closer to developing a solution is to write User Stories. User stories are short, simple descriptions of a feature told from the perspective of the person who desires the new capability, usually a user or customer of the system. User Stories are an Agile method, and they take the following form:


` “As a <type of user>, I want <some goal>, so that <some benefit/value>” `


For example:


`As a basic customer, I want a way to backup specific folders on my computer, so that I know my data is secure.`

`As a movie-goer, I want to be able to search the movies that are playing at nearby cinemas, so that I can easily know which cinema to go to.`

`As a video game player, I want to see when my friends log on, so that I can start a new game with them.`


User stories are used to determine the functionality you must include in any software you develop. The more detail you can add to a user story, the easier it is to know exactly what it is you’ll design and implement. Detail can be added to user stories in two ways:


 - By splitting a user story into multiple, smaller user stories.

 - By adding “conditions of satisfaction.”


The conditions of satisfaction is simply a high-level acceptance test that will be true after the agile user story is complete. These conditions are all of the little details you must pay attention to to make sure the user is satisfied in all cases.


User stories are written throughout the development process. However most of the stories will be written near the beginning when you and your team are figuring out the user requirements for the product. It’s best to do the user stories together with many team members, writing all the stories on index cards/post-it notes so you can easily categories them.


The written list of user stories you develop serves as a pointer to the real requirement. User stories could point to a diagram depicting a workflow, a spreadsheet showing how to perform a calculation, or any other document the product owner or team desires.


For more on user stories, [read through this short article](https://www.mountaingoatsoftware.com/agile/user-stories).

### From stories to plan
Old development processes require the team to create something called the [Software Requirements Specification (SRS)](https://en.wikipedia.org/wiki/Software_requirements_specification) which lists every requirement a piece of software must fulfill. This can be a tedious document to create, which is why agile methods prefer creating user stories. One advantage of user stories is that they can be used readily in project planning. User stories are written so that each can be given an estimate of how difficult or time-consuming it will be to develop. Also a story is implemented all in a single iteration of an agile project. So you only need to focus in on the specific details of a requirement during that one iteration, instead of trying to list every detail you might need at the beginning of a project.

## 2. From plan to design

Once your team has completed writing user stories, you should have a good sense of the features the program should have (obviously these features might change some as you go along -- that’s okay). Creating these user stories will also help you figure out the best design for your program. You can group the stories so you can see which features interact with each other.


Once you’ve grouped the stories, it’s time to sketch out the proposed design for you program. You don’t have to decide everything right at the start, but it will be helpful to think through the overall goals of the program so you can create a design that accommodates these goals. This is when you and your team should gather around a whiteboard and decide what architecture you need.


In most cases, you’ll want to use object-oriented programming. So that means the first design step, after grouping the features together, is brainstorming the possible classes you might need. Then you and your team will identify which classes will be best to use. During this stage, it is also helpful to discuss the possible data structures you will use. Additionally, your team can decide which methods (functions) the end user will have access to. Once your team has decided on appropriate classes and the properties and methods each class will have (again, this might change as you develop), you’ll be ready to start developing.


### Design considerations
However, before you start developing -- you were planning to use test-driven development, right? -- there are a few things to keep in mind when you are initially designing a program. Creative skill, past experience, a sense of what makes “good” software, and an overall commitment to quality are critical success factors for a competent design. The design model is the equivalent of an architect’s plans for a house. It begins by representing the totality of the thing to be built (e.g., a three-dimensional rendering of the house) and slowly reﬁnes the thing to provide guidance for constructing each detail (e.g., the plumbing layout).


The design process **should not suffer from “tunnel vision.”** A good designer should consider alternative approaches, judging each based on the requirements of the problem, the resources available to do the job.


The design **should not reinvent the wheel**. Systems are constructed using a set of design patterns, many of which have likely been encountered before. These patterns should always be chosen as an alternative to reinvention.


### Other considerations for good design

**Extensibility** - New capabilities can be added to the software without major changes to the underlying architecture.

**Maintainability** - A measure of how easily bug fixes or functional modifications can be accomplished. High maintainability can be the product of modularity and extensibility.

**Modularity** - the resulting software comprises well defined, independent components. That leads to better maintainability. The components should be implemented and tested in isolation before being integrated to form a desired software system. This allows division of work in a software development project.

**Reliability** - The software is able to perform a required function under stated conditions for a specified period of time.

**Reusability** - the software is able to add further features and modification with slight or no modification.

**Robustness** - The software is able to operate under stress or tolerate unpredictable or invalid input. For example, it can be designed with a resilience to low memory conditions.

**Security** - The software is able to withstand hostile acts and influences.

**Usability** - The software user interface must be usable for its target user/audience. Default values for the parameters must be chosen so that they are a good choice for the majority of the users.

**Performance** - The software performs its tasks within a user-acceptable time. The software does not consume too much memory.

**Portability** - The usability of the same software in different environments.

**Scalability** - The software adapts well to increasing data or number of users.

## 3. Creating the program through sprints


With the planning and design stages done, it’s finally time to start coding! Well, not so fast. The next stage of creating a computer program is prioritizing which features to build first. In the agile methodology, and particularly in Scrum, you prioritize tasks with a product backlog.


The agile product backlog in Scrum is a prioritized features list, containing short descriptions of all functionality desired in the product. This list is typically derived from the user stories you created when first planning the app. Typically, a Scrum team and its product owner begin by writing down everything they can think of for agile backlog prioritization (user story creation). This agile product backlog is almost always more than enough for a first sprint. The Scrum product backlog is then allowed to grow and change as more is learned about the product and its customers.

A typical Scrum backlog comprises the following different types of items:

1. Features

2. Bugs

3. Technical work

4. Knowledge acquisition

 

As mentioned, the predominant way for a Scrum team to express features on the agile product backlog is in the form of user stories, which are short, simple descriptions of the desired functionality told from perspective of the user. An example would be, "As a shopper, I can review the items in my shopping cart before checking out so that I can see what I've already selected."


Because there's really no difference between a bug and a new feature -- each describes something different that a user wants -- bugs are also put on the Scrum product backlog.


Technical work and knowledge acquisition activities also belong on the agile backlog. An example of technical work would be, "Upgrade all developers' workstations to Windows 7." An example of knowledge acquisition could be a Scrum backlog item about researching various JavaScript libraries and making a selection.


The product owner shows up at the sprint planning meeting with the prioritized agile product backlog and describes the top items to the team. The team then determines which items they can complete during the coming sprint. The team then moves items from the product backlog to the sprint backlog. In doing so, they expand each Scrum product backlog item into one or more sprint backlog tasks so they can more effectively share work during the sprint. Trello is the recommended project management tool to manage the features in your Product and Sprint backlogs.


Now, with the prioritized list decided, and the features for the first sprint chosen, it’s time to start coding! Be sure that the features and module you code conform to any bigger design decision you and your team made during the planning and design phase.


All code you create should be pushed and committed to the team’s code repository (usually on **GitHub**). This will ensure that everyone on your team has your latest work and is informed of any changes you’ve made to functionality or important variable names. All these changes should also be discussed at your daily stand up meeting where you share what you’re working on that day.

## 4. Testing your program with TDD

As you learned in previous modules, you should tackle any software application with a test-driven development method. Remember the TDD guiding principle of “Red, Green, Refactor.”


What this means is that there's a 3-step process:

1. **Write a Failing Test** - Understand the (user) requirements/story well enough to write a test for what you expect. (the test should fail initially - hence it being "Red")

2. **Make the (failing) Test Pass** - Write (only) the code you need to make the (failing) test pass, while ensuring your existing/previous tests all still pass (no regressions).

3. **Refactor the code you wrote** - if you have time to tidy up the code you wrote to make it simpler (for your future self or colleagues to understand) before you need to ship the current feature, do it.

Using TDD means that you will be testing your program from the very beginning of development and can be relatively sure that it will perform well under the conditions you tested for. Of course that means you must write good tests -- make tests for all the various kinds of input that a function may encounter. That also means testing for unexpected input (e.g. the user is supposed to input a number but they input a string instead) and appropriately handling any errors.

### Other tests
Test-driven development will ensure that all of your specific functions work, and that all of the modules or functions work properly together. However, for large programs, there is additional testing you want to do before you deploy your software to clients or customers. Below are a few additional types of testing you should consider for your project.

**Load testing** is primarily concerned with testing that the system can continue to operate under a specific load, whether that be large quantities of data or a large number of users. This is generally referred to as software scalability. Volume is a way to test software functions even when certain components (for example a file or database) increase radically in size.

**Stress testing** is a way to test reliability under unexpected or rare workloads. Stability testing (often referred to as load or endurance testing) checks to see if the software can continuously function well in or above an acceptable period.

**Usability testing** is to check if the user interface is easy to use and understand. It is concerned mainly with the use of the application.

**Security testing** is essential for software that processes confidential data to prevent system intrusion by hackers.

## 5. Delivering the program

When you follow the agile method, you’ll usually have a basic functioning product after one or two sprints. One of the main purposes of Agile is to be very user focused and get a working solution into your users hands as quickly as possible. Obviously, you’ll add more features and fix any issues as you do more sprints and add new items to your sprint backlog. But the first priority is to get the software in the hands of users and get feedback.


With good user stories and continually communicating with the client, you’ll be sure that the program you are building conforms to their expectations. If, for some reason, those expectations change or they would prefer something to function a little differently, you can simply add those features to future sprints.


In addition to good communication and early delivery of a product to users, you may need to provide more thorough tutorials to make sure users know how to do everything they want to do with your software.


**Video tutorials** are a great, user-friendly way to teach users how to use a program. Make sure your team dedicates time to producing video/screencast tutorials that demonstrate and explain how the program works.


Alternatively, **written walkthroughs** with good screenshots/photos of how to accomplish tasks in the program will be useful to users (especially for users who want more details or don’t like watching videos).


Finally, if your software or program requires the user to install something on their local machine, make sure this process is very well documented and explained with step-by-step instructions and photos to accompany each step. You want it to be as easy as possible for your clients to use your program. All of these extra touches make your work user-friendly and will keep customers coming back for more.

## 6. Documenting the program

In addition to providing video tutorial and walkthroughs for your users, you’ll need to provide more extensive documentation that explains all of the capabilities of your program. This will include some overview documents that explain the purpose and design of the program, as well as user docs that provide examples of how each feature/function works.


Review the section on “User Docs” to recall the important parts of user documentation.


Of course, you’ll also want extensive documentation within the source files of your program. This includes comments which explain each function and important variables, as well as high-level summaries of each source file which describes its functionality, content, and last update time. Review the sections on “comments as documentation” and “high-level summaries” for the key points.

