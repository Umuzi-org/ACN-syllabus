---
_db_id: 711
content_type: project
ready: true
tags:
- technical-assessment
flavours:
- any_language
submission_type: link
title: 'Assessment: Classes and objects'
---

## Note about submission format

On Tilde you'll notice that this card is asking for a link submission. **Please don't worry about submitting a link**. You will be assessed according to {{% contentlink path="specific-skill-success-criteria/introduction-to-assessments" %}}



All learners need to understand all of the following concepts:

## JS learners should know how constructors work

```
class Car {
  constructor(registrationId, color, brand){
    this._registrationId = registrationId
    this.color = color
    this.brand = brand
  }
}
```
## JS learners should know how to instantiate many objects from the same class and interact with them

```
let car1 = new Car(1, "red", "honda")
let car2 = new Car(2, "blue", "honda")
let car3 = new Car(3, "white", "ford")

car2.color = "black"
console.log(car2.color) //the color of this car is no longer blue
```
## JS learners should know how to modify and access private members of a class

```
class Car {
    ...

    editRegistration(id){ //setter
        this._registrationId = id
    }
    getRegistrationId(){ //getter
        return this._registrationId
    }
}

let car1 = new Car(1, "red", "honda")
console.log(car1.registrationId) // would this print 1?

car1.editRegistration(5)
console.log(car1.getRegistrationId())

```
## JS learners should understand inheritance and overriding and extending methods
```
class Car {
  ...

  details(){
    console.log(`Color: ${this.color}, Brand: ${this.brand}`)
  }
}

class Model extends Car {
  constructor(model){
    super()
    this.model = model
  }
  details(){
    console.log(`Model: ${this.model}`)
  }
}

let carModel = new Model("Toyota", "Corolla")
```
