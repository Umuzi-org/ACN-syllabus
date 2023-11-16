---
_db_id: 956
content_type: project
flavours:
- any_language
from_repo: projects/oop/animals/part1
prerequisites:
  hard:
  - projects/tdd/simple-calculator-part1
  - projects/oop/animals/part1
  - projects/oop/animals/part2
  soft: []
ready: true
submission_type: continue_repo
tags:
- unit-testing
- oop
- skill/combined_concept_projects
title: Animals Part 3. Adding more functionality
---

In this project you'll be revising some of your earlier work and you'll be adding more functionality.

## Remove pet function

Add a function called `remove pet` on the `Home` class. This function should take any Animal as an argument. `remove pet` should return the number of pets in the home as an integer.

If you try to remove a pet that has not been adopted then an error/exception with a suitable error message should be raised/thrown.

## Dogs can't have more than one Home, but Cats can

Extend the `adopt pet` function so that it raises/throws an Exception/Error if a home tries to adopt a dog that already has a home.

If multiple homes try to adopt the same cat then that is fine.

Here is some pseudocode:

```
home1.adoptPet(dog)  # ok
home2.adoptPet(dog) # this is not allowed since the dog already lives in home1

home1.adoptPet(cat)
home2.adoptPet(cat)
home3.adoptPet(cat) # this cat has 3 homes. That's a lucky cat
```

## Testing

Make sure you test all your functionality thoroughly