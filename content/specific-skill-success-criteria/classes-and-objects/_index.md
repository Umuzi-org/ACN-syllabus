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

```
class BankAccount:
  def __init__(self):
    pass
```

```
class BankAccount:
  def __init__(self, acc_no, amount):
    self.acc_no = acc_no
    self.amount = amount
```

## Instantiation

```
saitama_acc = BankAccount("sa1234", 10000)
```

```
kuroko_acc = BankAccount("ka1234", 300)
tsukasa_acc = BankAccount("ta1234", 75010)
vash_acc = BankAccount("va1234", 813650)
```


## Getters and setters

### Getters

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
