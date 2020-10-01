---
_db_id: 77
content_type: topic
ready: true
title: Intro to Angular
---

[Angular](https://angular.io/) is an opensource [Javascript Framework](https://en.wikipedia.org/wiki/JavaScript_framework) used to build [dynamic mobile and desktop web applications](https://en.wikipedia.org/wiki/Dynamic_web_page) using [TypeScript](https://en.wikipedia.org/wiki/TypeScript)/JavaScript and other languages.


## History ##

In 2012 Google introduced a new Javascript Framework called [AngularJS](https://angularjs.org/), the framework was written using pure Javascript and deloveloped using [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) concept. The framework uses HTML as a [templating language](https://en.wikipedia.org/wiki/Template_processor) by extending [HTML attributes](https://www.w3schools.com/html/html_attributes.asp) with [directives](https://www.w3schools.com/angular/angular_directives.asp) and linking the data to HTML with [expressions](https://www.w3schools.com/angular/angular_expressions.asp), this makes possible quick development of dynamic webapps with source code that is easier to read, understand and maintain.

*An example of creating a simple dynamic AngularJS web app :*

{{< highlight go "linenos=table, linenostart=1" >}}
<html>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
<body>

<div ng-app="">
 
<p>AngularJS web app</p>
<p>Name: <input type="text" ng-model="name" placeholder="What's your name?"></p>
<p ng-bind="name"></p>

</div>

</body>
</html>
{{< / highlight >}}




AngularJS is also known as Angular 1, in the following years after AngularJS was released google and the opensource community released a second version of AngularJS but they called it Angular 2, the suffix 'JS' from AngularJS was removed and this has been so even now with the [latest version](https://angular.io/guide/releases) of angular released being version 7. Angular 2 was a re-design of AngularJS not an increment of it, Angular 2 apps/code is not backward compartible to AngularJS apps/code, but they do share some of the concepts and philosophies except Angular has had more improvements and features added to it, while angularJS has remained at version 1. 

Knowledge of [NodeJS](https://nodejs.org/) and [Typescript](https://www.typescriptlang.org/) is necessary to develop Angular apps. Javascript can be used instead of Typescript but such a practice is not widely used and sometimes not recommended by some of Angular users/developers.

You can create an Angular app using this few commands below. Please ensure you have Nodjs installed on your system.

Open your CMD/Terminal and type :


{{< highlight go "linenos=table, linenostart=1" >}}

npm install -g @angular/cli  

{{< / highlight >}}
More about [NPM/Node Package Manager](https://www.npmjs.com/get-npm), [NPM commands](https://docs.npmjs.com/cli-documentation/).


{{< highlight go "linenos=table, linenostart=2" >}}

ng new my-dream-app  

{{< / highlight >}}
(a) Select (y) if you want angular to add routing and (N) if not. [Introduction to angular Routing](https://angular.io/guide/router).

(b) Select CSS or your preferred CSS preprocessor. [Introduction to different types of css preprocessor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_preprocessor).


{{< highlight go "linenos=table, linenostart=3" >}}

cd my-dream-app  

{{< / highlight >}}
List of commonly used [CLI/Command Line Interface commands](https://www.codecademy.com/articles/command-line-commands) to navigate/create/modify files in an operating system.


{{< highlight go "linenos=table, linenostart=4" >}}

ng serve

{{< / highlight >}}
Look for a line similar to this "Angular Live Development Server is listening on localhost:4200", and open your browser to url localhost/27.0.0.1 include specified port, example: for me I would open the browser and type "localhost:4200" and I will see Angular app webpage. To understand files produced, structure and their purpose look [here](https://angular.io/guide/file-structure).


*To improve the app further*

[Add new components](https://angular.io/cli/generate).

[Add Angular Material](https://material.angular.io/guide/getting-started).

[Add Angular dependancies](https://angular.io/guide/npm-packages).

[Run and watch tests](https://angular.io/guide/testing).

[Build for production](https://angular.io/guide/build).


### Angular Features and Benefits ###

- Create desktop installable app using same code for Linux, windows, Mac.

- Build native mobile apps using Cordova, Ionic, Nativescript, etc.

- Develop high perfomance Native like [Progressive web apps](https://en.wikipedia.org/wiki/Progressive_web_applications).

- More features and benefits [here](https://angular.io/features).

### Angular introductory resources ###

[Angular home](https://angular.io/).

[Angular documentation](https://angular.io/docs).

[Angular tutorial](https://angular.io/tutorial).

[Angular CLI documentation](https://angular.io/cli).