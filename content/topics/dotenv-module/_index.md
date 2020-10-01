---
_db_id: 62
content_type: topic
ready: true
title: Introduction to Dotenv module
---

## Description

> [Dotenv](https://www.npmjs.com/package/dotenv) is a zero-dependency module that loads environment variables from a .env file into [process.env](https://codeburst.io/process-env-what-it-is-and-why-when-how-to-use-it-effectively-505d0b2831e7).

- We can either set the environment through application code, or we can use a tool to set an environment for us.
- A common application level tool is dotenv which allows us to load environment variables from a file named ```.env```.
- Configs should have a separate file of their own and not hosted within the code repository. Having a separate config file makes it easy to update the config values without touching the actual code base.
- Having separate file eliminates the need for re-deployment of your applications when you change certain values in your config files.
- In other words, configs belong in the environment as variables, not in the application, you should be able to move it to another environment without having to touch the source code.

## How do I use dotenv?

- Create project directory and name it whatever you want.
- cd into the directory you created and run
```
npm init -y
npm install dotenv

``` 
- Create a .env file and add your configurations.

```
//.env

BASE_URL=https://umuzi.org
API_KEY=000FBAA4558FF565851A3E104017AB1A
SERVER_PORT=3000
USER=umuziadmin
OBJ={key1:"value1", key2:"value2",key3:"value3",key4:"value4"}
BOOL=true
NUM=123456
STRING= Dumela Lefatshe
ARRAY=[1,2,3,4,5,6]

```

#### &nbsp; Usage

- You can access your configuration from your code like this.
```
//index.js

require('dotenv').config();

const url = process.env.BASE_URL;
const apiKey = process.env.API_KEY;
const port = process.env.SERVER_PORT;
const user = process.env.USER;
const obj = process.env.OBJ;
const boolean = process.env.BOOL;
const number = process.env.NUM;
const string = process.env.STRING;
const null1 = process.env.NULL; //be careful with reserved words
const undefined1 = process.env.UNDEFINED;
const array = process.env.ARRAY;

console.log(url);
console.log(apiKey);
console.log(port);
console.log(user); //lol, this one seems to return the name of pc owners.
console.log(obj);
console.log(number);
console.log(string);
console.log(boolean);
console.log(null1 == null ? true : false);
console.log(array);

```

What if you need this environment variables in multiple places? If you do reference the variables everywhere that you need them it could make refactoring and maintenance more difficult than if they are in one place. 

#### &nbsp; You can use a Javascript config file to get around this.

```
//config.js

require('dotenv').config();

module.exports = {
    url : process.env.BASE_URL,
    apiKey : process.env.API_KEY,
    port : process.env.SERVER_PORT,
    user : process.env.USER,
    obj : process.env.OBJ,
    boolean : process.env.BOOL,
    number : process.env.NUM,
    string : process.env.STRING,
    null1 : process.env.NULL,
    undefined1 : process.env.UNDEFINED,
    array : process.env.ARRAY
};

```

Now you can import this configs from any place in your code.

```
//index.js, doSomething.js, anotherJsFile.js, etc

const configs = require('/path/to/js/config/file');

console.log(configs.url);
console.log(configs.apiKey);
console.log(configs.user);
console.log(configs.obj);

```
##### What’s the value in this technique?

- it is easy
- clarity on how all environment variables are being mapped
- you can rename variables to more readable properties
- you can add other configuration properties from non-environment variables


## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OR

Dotenv has the option of preloading the environment variables outside your code. Preload your variables and eliminate the code that reads the .env file from your code  base. Less code is fewer lines that could break or be maintained.
![alt text](https://imgflip.com/s/meme/Roll-Safe-Think-About-It.jpg)

This technique removes any need for code that uses require on dotenv. This includes the ``` dotenv.config()``` or  ``` require('dotenv').config() ``` code mentioned previously in this article. You can run your node app using the — require ( -r ) command line option to preload dotenv. The following command will preload all environment variables from the file .env using dotenv and make them available in your app.


```
node -r dotenv/config server.js

```
Now you can access all environment variables in the .env without requiring dotenv in your code, use  ```process.env.NAME_OF_VARAIBLE``` to access the variables.

## Best practices

> Be careful to add .env to your .gitignore file and commit that change before you add your .env. Otherwise, you run the risk of committing an early version of your .env to source control. Your .env file contains very sensitive information (your app key at the very least). You do not want this in version control where everybody can see this information and possibly use it to attack your site.
Think about database information which might be stored in there or email keys or passwords. Furthermore it is likely that the information which you use in your .env file also needs to change between environments so you will need to change values anyways. 

```
//.gitignore

.env

```

#### Sharing your .env file

The best practice on this matter is add a ```.env-example``` file in your repo to give a general outline of configuration available to developers but using dummy data as values to your variables.


```
//.env-example

BASE_URL=https://dummy.url.com
API_KEY=dummyApiKeyHere
SERVER_PORT=dummyPort
USER=dummyAdminName
OBJ={dummyKey1:"dummyvalue1", dummyKey2:"dummyValue2",dummyKey3:"dummyValue3",dummyKey4:"dummyValue4"}
BOOL=true
NUM=123456
STRING=DummyString
ARRAY=["dummy","dummy","dummy","dummy","dummy"]

```
**Do not include this file in ```.gitignore```**

## Resources 

https://www.npmjs.com/package/dotenv

https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa

https://medium.com/chingu/protect-application-assets-how-to-secure-your-secrets-a4165550c5fb

https://projectricochet.com/blog/importance-code-separation-and-why-we-use-git-workflow-managing-different-environments