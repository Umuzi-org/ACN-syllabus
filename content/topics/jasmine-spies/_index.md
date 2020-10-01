---
_db_id: 69
content_type: topic
ready: true
title: Jasmine Spies
---

### Spying on JavaScirpt Methods using Jasmine

Jasmine is made for unit testing. Unit tests are supposed to test only one component of your application. A component can be a function, an object, a module, basically everything self-contained that acts like a black box to the outside world. You usually want to avoid that your unit tests fail because another component failed. That’s why you want to test your components in isolation as much as possible.

For example, you may not want to send data to another server in your unit tests or you don’t want to manipulate a page’s DOM. But you want to make sure that the components which are responsible for these tasks get called correctly. How do we do this?

One of the primary aims of unit testing is to isolate a method or component that you want to test and see how it behaves under a variety of circumstances. These might include calls with various arguments - or even none at all, - or whether it calls other methods as it should. Unfortunately, many methods and/or objects have dependencies on other methods and/or objects, such as network connections, data sources, files, and even previously executed methods. This is where mocks come in. A mock is a fake object that poses as the real McCoy in order to satisfy the inherent dependency(ies) without having to go through the overhead of creating the real object.

In Jasmine, mocks are referred to as spies. There are two ways to create a spy in Jasmine: *spyOn()* can only be used when the method already exists on the object, whereas *jasmine.createSpy()* will return a brand new function:

```
//spyOn(object, methodName) where object.method() is a function
spyOn(obj, 'myMethod')
 
//jasmine.createSpy(stubName);
var myMockMethod = jasmine.createSpy('My Method');

```

#### Using the *SpyOn()* method

As mentioned above, __*spyOn()*__ can only be used when the method already exists on the object.  
For simple tests, this is your best bet.

The test cases all feature the following __Person class__. It has a couple of attributes,   
a getter and setter for the name, and two public methods:

```
class Person {

    //default variables
    let _age = 0, 
        _name = 'John Doe';
    
    constructor(name, age) {

        this._name = name | _name;
        this._age = age | _age;
    }

    //Getters and setters
    this.getName = function() { return this._name; }
    this.setName = function( name ) { this._name = name; }

    this.getAge = function() { return this._age; }
    this.setAge = function( age ) { this._age = age; }

    //Public methods
    this.addBirthday = function() { this_age++; } 
    this.toString    = function() { 
    
        return 'My name is " + this.getName() + " and I am " + this.getAge() + " years old.'; 
    }
}

```

Say that we want to verify that the __*toString()*__ method was calling __*getName()*__. We would instantiate the __Person__ as usual, but before calling __*toString()*__, we would call __*spyOn()*__, passing in the *person* instance and the name of the method that we want to spy on __('getName')__.   
We can then call jasmine matchers to see what happened. The simplest test is to check that __*getName()*__ was in fact called:

```
describe("Person toString() Test", function() {

    it("calls the getName() function", function() {
        //Creating person instance
        var testPerson = new Person();

        //Creating a spy to test on
        spyOn(testPerson, "getName");

        //Calling the function and the using matchers to check whether it has been called
        testPerson.toString();
        expect(testPerson.getName).toHaveBeenCalled();
    });
});
```

But that's just the beginning. We can run other tests on our spied function, such as what arguments it was called with. 

A spy only exists in the describe or it block in which it is defined, and will be removed after each spec.

There are special matchers for interacting with spies. __This syntax has changed for Jasmine 2.0__. The __*toHaveBeenCalled()*__ matcher will return true if the spy was called. The __*toHaveBeenCalledWith()*__ matcher will return true if the argument list matches any of the recorded calls to the spy.

Conversely, we can test that the function was called without any parameters by calling __*toHaveBeenCalledWith()*__ without a value:

```
describe("Person toString() Test", function() {
    var testPerson;
    beforeEach( function() { 
        
        testPerson = new Person(); 

        foo = {

            setBar: function(value) {
                        
                        bar = value;
                    }
        };   
    } );   
    afterEach ( function() { testPerson = undefined;    } );
     
    it("calls the getName() function", function() {

        spyOn(testPerson, "getName");

        testPerson.toString();
        expect(testPerson.getName).toHaveBeenCalled();
    });
     
    it("Method getName() was called with zero arguments", function() {
        
        // Ensure the spy was called with the correct number of arguments
        // In this case, no arguments
        expect(testPerson.getName).toHaveBeenCalledWith();
    });

    it("tracks that the spy was called", function() {
        
        spyOn(foo, 'setBar');

        foo.setBar(123); 
        expect(foo.setBar).toHaveBeenCalled();
    });

    it("tracks all the arguments of its calls", function() {
        
        spyOn(foo, 'setBar');

        foo.setBar(123);
        expect(foo.setBar).toHaveBeenCalledWith(123);
    });
});
```

#### Creating Our Own Spy Method

Sometimes, it may be beneficial to completely replace the original method with a fake one for testing. Perhaps the original method takes a long time to execute, or it depends on other objects that aren't available in the test context. Jasmine lets us handle this issue by creating a fake method using __*jasmine.createSpy()*__. Here's how to substitute a fake __*getName()*__ for the real one:

```
describe("Person toString() Test with Fake getName() Method", function() {

    it("calls the fake getName() function", function() {
        //Create new person instance
        var testPerson = new Person();

        //Create own jasmine fake methid
        testPerson.getName = jasmine.createSpy("getName spy");

        //Test if the fake method is called instead of the original being called
        testPerson.toString();
        expect(testPerson.getName).toHaveBeenCalled();
    });
});
```

Unlike __*spyOn()*__, creating a fake method circumvents the original method so that it is not called during tests.

#### Understanding Spies

By default a spy will only report if a call was done without calling through the spied function (i.e the function will stop executing), but you can change the default behavior using these method.

- [``` and.callThrough() ```]( https://jasmine.github.io/2.0/introduction.html#section-Spies:_%3Ccode%3Eand.callThrough%3C/code%3E ): call through the original function,
- [``` and.returnValue(value) ```]( https://jasmine.github.io/2.0/introduction.html#section-Spies:_%3Ccode%3Eand.returnValue%3C/code%3E ):  return the specified value,
- [``` and.callFake(fn) ```]( https://jasmine.github.io/2.0/introduction.html#section-Spies:_%3Ccode%3Eand.callFake%3C/code%3E ): call the fake function instead of the original one,
- [``` and.throwError(err) ```]( https://jasmine.github.io/2.0/introduction.html#section-Spies:_%3Ccode%3Eand.throwError%3C/code%3E ): throw an error,
- [``` and.stub() ```]( https://jasmine.github.io/2.0/introduction.html#section-Spies:_%3Ccode%3Eand.stub%3C/code%3E ): resets the default stubbing behavior.

### References

[An Introduction to Jasmine Unit Testing.]( https://www.freecodecamp.org/news/jasmine-unit-testing-tutorial-4e757c2cbf42/#Understanding%20Spies )  
[Spy on JavaScript Methods Using the Jasmine Testing Framework]( https://www.htmlgoodies.com/html5/javascript/spy-on-javascript-methods-using-the-jasmine-testing-framework.html )   
[Spies in Isolation]( https://www.htmlgoodies.com/html5/javascript/spy-on-javascript-methods-using-the-jasmine-testing-framework.html )  
[Spying On JavaScript methods using Jasmine]( https://blog.codeship.com/jasmine-spyon/ )