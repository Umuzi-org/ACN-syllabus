---
_db_id: 53
content_type: topic
ready: true
title: TDD Horrors
---

These are all the most common TDD problems recruits tend to come across, read and make sure you didn't make any of these or any mistakes at all.

- **Write tests**. Recruits in the past have done the mistake of not writing tests for TDD assignments, make sure you avoid this weird mistake. Always write tests for your TDD projects.
- Please make sure you understand .gitignore, please don't add your node_modules to git.
- Name your files according to what is inside them
- Avoid making tests depend on each other. Making test dependent on each other is the perfect path to pain, expense, fragility, and complication.
- Pay attention to failure messages. Make each failure message as helpful for diagnosis as you can.
- Do not skimp on the refactoring. It is the refactoring that will keep your code (including the tests) easy to understand and change
- Naming conventions: in general, be careful with your naming conventions. make sure your naming convention consistent, names should be more descriptive. Name your files properly and according to what's inside them.
- Keep good directory structure and delete all junk files.
- Avoid messy indentation (install prettier).
- Test for errors/exception, sometimes code is supposed to throw an error or raise an exception. In these cases your tests should make sure that the error happens as it should, your tests need to use the following syntax:

  Javascript:

  ```js
  expect(...).toThrow()
  ```

  Python:

  ```py
  with pytest.raises([ErrorType])...
  ```

- _Python peeps_ DO NOT Define a test case(testing function) inside a function.

```py
def test_something():

  def totally_valid_test():
    assert add(1,20,5) == 26

  def another_test():
    assert add(1,23,5) == 29

```

_Note:_
Nice thing about the `pytest` module is that it removes the need for boilerplate code. so the following code would work:

```py
  from module import add

  # tests start here.
  def test_add_two_values():
    assert add(1,2) == 3

  def test_add_multiple_values():
    assert add(1,2,3,4) == 10
```

---

- Test cases should focus on one functionality and one functionality only.

**Python example:**

Do not do this:

```py
    def test(self):
      assert add(1,2,3,4) == 10
      assert multiply(1,2,3) == 6
```

Do this instead:

```py
# test add function.
  def test_add_two_values(self):
    assert add(1,2) == 3

  def test_add_multiple_values(self):
    assert add(1,2,3,4,5,6) == 21
    assert add(2,3,4,5) == 14

  def test_multiply_two_values(self):
    assert multiply(1,2) == 2

  def test_multiply_multiple_values(self):
    assert multiply(1,2,4) == 8
```

**Javascript example:**

Don't do this:

```js
describe("Test one", () => {
  it("Should add", () => {
    let sum = add(1, 23, 5);
    expect(sum).toBe(29);
  });
  it("Should multiply", () => {
    let prod = multiply(1, 23);
    expect(prod).toBe(23);
  });
});
```

Each Function should have it's own describe object\_

Do this:

```js
describe("add()", () => {
  it("Should add [what exactly?]", () => {
    let sum = add(1, 23, 5);
    expect(sum).toBe(29);
  });
});
describe("multiply()", () => {
  it("Should multiply [what exactly?]", () => {
    let prod = multiply(1, 23);
    expect(prod).toBe(23);
  });
});
```

---

- Javascript: Test strings are there to be descriptive:

  - eg:

    Do: `it("can/should multiply [what exactly?]")`

    Don't: `it("multiply")`

- Incomplete projects:

  - Always make sure that your projects are complete. Submitting Incomplete projects looks, BAD! to both an employer and Code reviewers, so don't submit incomplete projects, it's bad for your reputation. If you do not have tests, for your TDD project, then your project is incomplete.

- TDD tests fail:

  - Failing tests aren't bad during development, but make sure your **all** tests pass when you submit your project.

- Documentation on how to setup and test the code:

  - Make use of README.md, requirements.txt files, collaborators shouldn't guess/remember how to setup all the dependencies for your project, document all the necessary processes please.

- Clean code base. Need I say more?

  1. Dirty.

  Javascript:

  ```js
  // Testing if the Error Checks throw
  //var sixSided = new Dice(6,[1,"gdfdf"]);
  var sixSided = new Dice(6, [1, 6, 5, -16]);
  //console.log(sixSided.rollDice());
  ```

  Python:

  ```py
    # I was thinnking about This
    # Then I did this but it didn't work. so I left
    # And then, it came to me, eureka!
    die6 = Dice(6)
    # Since it works, there's no need to clean it.
  ```

2. Clean.

   Javascript:

   ```js
   var sixSided = new Dice(6, [1, 6, 5, -16]);
   ```

   Python:

   ```py
     die6 = Dice(6)
   ```

Remove useless stuff, it serves no purpose. so get rid of it.

- One test: writing one test to test everything is a bad idea, you need to separate it into multiple tests that test one and thing only.

### Some useful Readings

1. [Common mistakes in TDD](https://cmatskas.com/common-mistakes-in-tdd/)
2. {{% contentlink path="/topics/unit-testing/" %}}
3. {{% contentlink path="/topics/clean-code/" %}}