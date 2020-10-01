---
_db_id: 126
content_type: topic
ready: true
title: Unit testing with mocks and spies
---

Unit testing is a pretty powerful thing - it lets you quickly and easily check if your code works the way it is supposed to, and acts as documentation for your code. And it stops your team mates from breaking your stuff. This is super powerful.

One thing that is special about unit tests is the concept of a "unit". A unit test tests a unit of code. A unit is supposed to be something small and specific, it should be quick to test and it should be "cheap" to run. What does that mean? If your tests take a long time to run, or actually cost money to run then that's a real problem. Your tests shouldn't have real world conseqences when you run them.

Let me show you an example.

Let's imaging that you have a program where users create accounts. Users have phone numbers and those phone numbers need to be verified using an sms. There are a lot of ways to send an sms from your program, for example [Twilio](https://www.twilio.com/docs/sms/send-messages) and [Nexmo](https://developer.nexmo.com/api/sms).

So basically when a user changes their phone number we need to send a single sms. Sending two sms's would be a problem. We need to send the sms to the right person, with the right message. Basically instead of actually sending an sms, we need to make sure that the correct sms sending api has been called with the correct arguments and the correct number of times.

For now, to Keep It Short and Simple, let's just assume we have a simple function to send sms's that looks a bit like this:

```
# python

def send_sms(to_phone_number,message):
    magic happens here
```

```
// js

def sendSms(toPhoneNumber,message):
    magic happens here
```

So our test should do something like this (pseudocode-ish):

```
# python ish
def test_validate_phone_number_sends_correct_sms():
    do_some_setup()
    change_the_user_phone_number(new_phone_numer)
    assert send_sms.call_count == 1
    assert send_sms.call_arguments["to_phone"] == new_phone_number
```

```
# js -ish

it('should send the correct sms when a user's phone number changes',()=>{
    doSomeSetup()
    changeTheUserPhoneNumber(newPhoneNumer);
    expect(sendSms.callCount).toBe(1);
    expect(sendSms.arguments.toPhone).toBe(newPhoneNumber);
})
```

Note: the above code is not strictly correct. This is just an illustration of the kind of thinking you need to do.

Differnt languages and tools have different ways to do this stuff. But you can often use the same mental models to understand how it all works.

## Python Resources

- [Real Python has a great tutorial](https://realpython.com/python-mock-library/)
- [The official docs](https://docs.python.org/3/library/unittest.mock.html)

## JS Resources

{{% contentlink path="topics/jasmine-spies" %}}