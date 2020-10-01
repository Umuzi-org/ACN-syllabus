---
_db_id: 116
content_type: topic
ready: true
title: Java OOP basics resources and readings
---

One thing a lot of programmers really struggle with is Object Orientated Programming. Once you get your head around it it can be pretty fun. And it is a super powerful tool. Read and understand this

- [What is Object Oriented Programming?](https://medium.com/learn-how-to-program/chapter-3-what-is-object-oriented-programming-d0a6ec0a7615)
- [Beginners guide to OOP]https://dev.to/charanrajgolla/beginners-guide---object-oriented-programming

## Four main OOP priciples in java

OOP is really powerful. There's a lot worth knowing. Make sure that you understand these foundational concepts and everything else will come pretty easily.

### Abstraction == focusing on the necessary details

In Object-oriented programming, abstraction is a process of hiding the implementation details from the user, only the functionality will be provided to the user. In other words, the user will have the information on what the object does instead of how it does it.

An every day example of abstraction is driving a car. When you turn on the ignition you just turn a key, the car does a whole lot of things under the hood. The starter motor and carberator is abstracted. You don't need to know how that stuff works in order to work a car.

In Java there is a thing called an Abstract Class. This is not to be confused with the principle of abstraction. You can achieve abstraction without using abstract classes. A lot of people get these concepts mixed up.

- abstraction = hiding implementation details
- abstract classes = classes that are not meant to be instantiated

Abstraction can be achieved through use of abstract classes. Or just regular classes.

Take a look at (this discussion)[https://softwareengineering.stackexchange.com/questions/230401/confused-about-the-definition-of-abstraction-in-oop] for a bit more info

### Encapsulation == hiding details

Encapsulation is known as data-hiding. Basically in OOP in Java you can choose what parts of your objects are exposed for use, and which are under the hood. If we think about cars again, the steering wheel and gear lever are exposed to you, but then the fuel injection system is hidden away.

In coding terms this means that objects may be able to communicate with one another but are restricted to access some of the object's components directly.
Publicly accessible methods are generally provided in the class so-called [accessors and mutators.](https://www.cs.colostate.edu/~cs161/Fall12/labs/lab2/bookgetset.html))

[Read more on encapsulation.](https://www.geeksforgeeks.org/encapsulation-in-java/)

The following Java code shows how Encapsulation can be implemented:

```
class Employee{

    //private data member
    private String name;   // you can't just access this whenever you want.

    public void setName(String employeeName){
        // this is the only way to update the name. Yo can put validation logic in here if you want. Eg if the employeeName has naughty words in it then raise an exception.
        this.name  = employeeName;
    }

    //getter method for name
    public String getName(){
        return name;
    }

}

class Main{
    public static void main(String args[]) {
        //creating instance of the encapsulated class
        Employee e = new Employee();
        //setting value in the name member
        e.setName("Mbali");
        //getting value of the name member
        System.out.println(e.getName());

    }
}
```

[Abstraction vs Encapsulation](https://1.bp.blogspot.com/-ECYNAUTGGMk/WPQeY4EpFtI/AAAAAAAAIX8/j-Ji8N_mDz8-d72SasgNPnQD-nIlw-kiACLcB/s1600/Abstraction%2Bvs%2BEncapsulation%2B2.jpg)

### Inheritance

Inheritance can be thought of an an "is a" relationship.

The following Java code shows how Inheritance can be implemented. In this example we have a superclass called `Vehicle`. a `Bakkie` is a `Vehicle`, and a `Beatle` is a `Vehicle`. So both these child classes do vehivle things and have vehicle attributes, but layer on a bit of extra behavior.

```
//superclass
class Vehicle {
    void printType(){
        System.out.println("I am a Vehicle");
    }
}

class Beatle extends  Vehicle {
    //Override method
    @Override
    void printType() {
        //call method in super class
        super.printType();
        System.out.println("I am a Beatle");
    }
}

class Bakkie extends  Vehicle {
    //Override method
    @Override
    void printType() {
        //call method in super class
        super.printType();
        System.out.println("I am a Bakkie");
    }
}

class Main{
    public static void main(String[] args) {
        //Create a car object
        Beatle beatle = new Beatle();
        //call method
        beatle.printType();
    }
}

```

To learn how `@Override` actually works, check (this)[https://www.baeldung.com/java-override] out

### Polymorphism

Polymorphism in Java is a concept by which we can perform a single action in different ways. Polymorphism is derived from 2 Greek words: poly and morphs. The word "poly" means many and "morphs" means forms. So polymorphism means many forms.

There are two types of polymorphism in Java: compile-time polymorphism and run-time polymorphism. We can perform polymorphism in java by method overloading and method overriding. [Read more.](https://stackify.com/oop-concept-polymorphism/)

#### Method overriding

Refer back to the `inheritance` stuff above. We used overriding there.

Overriding a method is when a method in the subclass has the same name and method signature as a method in the superclass. When overriding a method you are not allowed to make the method more private.

The following Java code shows how overriding can be implemented:

```
public class Fruit {
    public void print() {
        System.out.println("I am a fruit");
    }
}

class Apple extends Fruit {

    //Override method
    @Override
    public void print() {
        System.out.println("I am an Apple");
    }

}

class Main{
    public static void main(String[] args) {
        //Create an animal object
        Fruit fruit = new Fruit();
        //Create horse object
        Apple apple = new Apple()
        fruit.print();
        //call method
        apple.print();
    }
}

```

#### Method overloading

Overloading a method is when a method in the subclass has the same name but the method signature is different from the method in the superclass.[Read more](https://beginnersbook.com/2013/05/method-overloading/)

The following Java code shows how overloading can be implemented:

```
class Calculate{

    public int product (int x, int y) {
        return (x * y);
    }

    // Overloaded. This product method  takes three int parameters
    public int product(int x, int y, int z) {
        return (x * y * z);
    }

    // Overloaded. This product method takes two double parameters
    public double product(double x, double y) {
        return (x * y);
    }
}

class Main {
    public static void main(String args[]) {
        Calculate prod_object = new Calculate();
        System.out.println(prod_object.product(10, 20));
        System.out.println(prod_object.product(10, 20, 30));
        System.out.println(prod_object.product(10.5, 20.5));
    }
}
```

#### The danger of accidental overloading

```
public class Machine {
    public boolean equals(Machine obj){
        return true;
    }
}

public class MainProgram {
    public static void main(String[] args){

        Object first = new Machine();
        Object second = new Machine();
        Machine third = new Machine();
        Machine fourth = new Machine();

        System.out.println(first.equals(second)); // returns false
        System.out.println(third.equals(fourth)); // returns true
    }
}
```

This is because every class in Java inherits from a base Object class. And so a `Machine` is an `Object`. And `Object.equals` means something very specific.

## Important links

- Read more to gain further understanding on [OOP concepts](https://beginnersbook.com/2013/04/oops-concepts/).
- [Here](https://stackify.com/oops-concepts-in-java/) is another useful link.
- [Java oops concepts](https://www.javatpoint.com/java-oops-concepts) by Java T Point.
- [Access modifiers explained](https://stackoverflow.com/questions/215497/what-is-the-difference-between-public-protected-package-private-and-private-in)
- [Implements veresus Extends](https://stackoverflow.com/questions/10839131/implements-vs-extends-when-to-use-whats-the-difference)
- [More on overloading versus overriding](https://www.baeldung.com/java-method-overload-override)

## Super cool advanced stuff

The true power of OOP comes from the interaction between objects. There are some pretty common patterns to how OOP gets used in industry. These patterns are called "Design Patterns". Take a look at [this](https://www.javatpoint.com/design-patterns-in-java).