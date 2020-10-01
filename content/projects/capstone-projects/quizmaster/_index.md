---
_db_id: 422
content_type: project
ready: true
submission_type: nosubmit
title: The Quizmaster
---

## Who should do this?

This will work best as a Django application.

## Spec

### Admin interface

Create an app where an administrator can set up multiple choice quizzes.
Create database models for Quiz, Question and Choice.
Questions and choices should be able to contain rich text and even images. These should be fully defined using Markdown. Questions should also have another field called “explanation” that also contains markdown text.

### Recruit Interface

Recruits can test their skills by answering the questions. They can navigate to a quiz and then they will get shown one question at a time. They will get to choose between the answers. Once they have finished the quiz they will be told their mark and a summary of what they got right and wrong. If a question was wrong then the recruit should be shown the “explanation” associated with the question.

## Resources