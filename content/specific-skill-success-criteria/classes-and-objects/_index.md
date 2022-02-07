---
_db_id: 711
content_type: project
ready: true
flavours:
- any_language
submission_type: link
title: 'Assessment: Classes and objects'
---

## Note about submission format

On Tilde you'll notice that this card is asking for a link submission. **Please don't worry about submitting a link**. You will be assessed according to {{% contentlink path="specific-skill-success-criteria/introduction-to-assessments" %}}



All students need to probably understand all of the following concepts:

- how constructors work
- construction of multiple class instances:
  - make many objects of the same class
  - interact with them and see that they are distinct
- getters and setters
- inheritance and overriding and extending methods
- composition

# Python

## Constructors
The `__init__()` method is called the constructor and is always called when an object is created, generally used for instantiating an object.

### Default Constructor
A simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
```
class BankAccount:
  def __init__(self):
    pass
```

### Parameterized Constructor
A constructor with parameters. Takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
```
class BankAccount:
  def __init__(self, acc_no, amount):
    self.acc_no = acc_no
    self.amount = amount
```

## Instantiation
Instantiating a class is creating a copy of the class which inherits all class variables and methods. We simply call the class as if it were a function, passing the arguments that the `__init__()` method defines (except `self`).
```
saitama_acc = BankAccount("sa1234", 10000)
```

A class can have multiple instances.
```
kuroko_acc = BankAccount("ka1234", 300)
tsukasa_acc = BankAccount("ta1234", 75010)
vash_acc = BankAccount("va1234", 813650)
```


## Getters and setters

### Getters
A getter is a method that gets the value of a property.
```
  def balance(self):
    return self.amount
```

```
saitama_acc.amount
```

```
saitama_acc.balance()
```

### Setters
A setter is a method that sets the value of a property.
```
  def deposit(self, amount):
    self.amount += amount

  def withdraw(self, amount):
    self.amount -= amount
```

```
saitama_acc.deposit(500)
saitama_acc.withdraw(320)
```


## Inheritance
It enables us to create a new class from an existing class. The new class is a specialized version of the existing class and it inherits all the non-private variables and methods of the existing class.

No additional instance variable(s), `__init__()` can be left out
```
class SavingsAccount(BankAccount):
  pass
```

Additional instance variable(s), `super()` is used
```
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, amount, main_acc_instance):
        super().__init__(acc_no, amount)
        self.main_acc_instance = main_acc_instance
```

```
saitama_savings_acc = SavingsAccount('ssa1234', 0, saitama_acc)
```

```
saitama_acc.deposit(500)
saitama_acc.withdraw(320)
```

```
saitama_savings_acc.deposit(500)
saitama_savings_acc.withdraw(320)
```

## Overriding
Defining in the child class a method with the same name of a method in the parent class. If a method is overridden the implementation of the parent class is not considered at all.
```
    def deposit(self, amount):
        self.main_acc_instance.amount -= amount
        self.amount += amount

    def withdraw(self, amount):
        self.main_acc_instance.amount += amount
        self.amount -= amount
```
