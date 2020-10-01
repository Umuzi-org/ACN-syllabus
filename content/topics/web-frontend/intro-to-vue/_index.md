---
_db_id: 74
content_type: topic
ready: true
title: Intro to Vue
---

#### What is? ####

[Vue.js](https://vuejs.org/v2/guide/index.html) is an [Model View viewmodel](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel) [javascript framework](https://en.wikipedia.org/wiki/JavaScript_framework) that has different optional tools for building user interfaces and [single page applications](https://en.wikipedia.org/wiki/Single-page_application). Vue.js allow you to extend basic HTML with html attributes called [directives](https://012.vuejs.org/guide/directives.html) which adds extra functionality to the html. This directives are provided by Vue.js by default or can be defined by user.

_Vue.js Directives_

In Vue.js a directive is a type of token/indentifier that tells vue.js code to do something to the [DOM/Documet Object Model](https://en.wikipedia.org/wiki/Document_Object_Model). 

Directive simple syntax :

{{< highlight go "linenos=table,linenostart=1" >}}

 <html-element prefix-directive="expression"></html-element>

{{< / highlight >}}

_Usage example_

{{< highlight go "linenos=table,linenostart=1" >}}

 <h1 id='heading1' v-text='heading_1'></h1>

{{< / highlight >}}
This can also be written using double braces as placeholders for output data like :
{{< highlight go "linenos=table,linenostart=1" >}}

 <h1 id='heading1'>
    {{ heading_1 }}
 </h1>

{{< / highlight >}}
In the first example looking at [ v-text='heading_1' ], the prefix 'v' is default similar to [AngularJS](https://www.w3schools.com/angular/angular_directives.asp) 'ng' its purpose is to tell Vue.js library that the [HTML attribute](https://en.wikipedia.org/wiki/HTML_attribute) is Vue.js attribute. The 'text' part of the ['v-text'](https://012.vuejs.org/api/directives.html) is the directive and its meant to tell Vue.js that it should change textContent of the HTML element, with what 'heading_1' expression presents/contains.
The same goes for the second example except for example 2 'heading_1' is directly defined whithin HTML heading attribute textContent area. Some of the directives are [v-if, v-el, v-pre, v-on, v-ref, v-transition, etc](https://012.vuejs.org/api/directives.html).

#### Comparison ####
Simple examples to show usage of Vue.js and normal html alternative.

_1) Add text to heading 1 :_

{{< highlight go "linenos=table,linenostart=1" >}}
<!-- Vue.js -->

<html>
  <script src="https://cdn.jsdelivr.net/npm/vue"></script>
  <body>


    <h1 id='heading1'>{{ heading_1 }}</h1>

    <script>
    
      new Vue({
        el: '#heading1',
        data: {heading_1: 'Vue.js'}
      })

    </script>

  </body>
</html>

{{< / highlight >}}
[new](https://www.freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8/) Vue() creates an instance of a Vue.js object. 'el' object key expects its value to be an 'id' of an html element and the 'data' key, value should be data that will be applied to the specified vue.js expression whithin the html code.
{{< highlight go "linenos=table,linenostart=1" >}}
 <!-- html and javascript -->

<html>

  <body>

    <h1 id='heading1'></h1>

    <script>
    
	document.getElementById('heading1').innerHTML= 'Vue.js';
    </script>

  </body>
</html>
{{< / highlight >}}


_2) Write input box reply to the dom :_

{{< highlight go "linenos=table,linenostart=1" >}}
<!-- Vue.js -->

<html>
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
<body>

  <h2>Vue.js</h2>

  <div id="my_name">

    <p>What is your name? : {{ reply }}</p>

    <input v-model="reply">

  </div>

  <script>

    new Vue({
      el: '#my_name',
      data: {reply: ''}
    })

  </script>

  </body>
</html>

{{< / highlight >}}
The ['v-model'](https://vuejs.org/v2/guide/forms.html) directive binds the value of HTML elements to application data, and updates the dom when any changes occur. 
{{< highlight go "linenos=table,linenostart=1" >}}
 <!-- html and javascript -->

<html>

<body>

  <h2>Vue.js</h2>


    <p>What is your name? : 
    	<span id="my_name"></span>
     </p>

    <input type='text' id='reply_box' onkeyup='show_reply()'>

 

  <script>

    function show_reply(){
        
        document.getElementById('my_name').innerHTML=document.getElementById('reply_box').value;

    }

  </script>

  </body>
</html>
{{< / highlight >}}

_3) Show items list :_

{{< highlight go "linenos=table,linenostart=1" >}}
<!-- Vue.js -->

<html>
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
  <body>

    <h2>Vue.js</h2>

    <div id="app">
      <ul>

        <li v-for="ingredients in coffee_reciepe">
        
          {{ ingredients }}
          
        </li>

      </ul>

    </div>

    <script>

      new Vue({
        el: '#app',
        data: {
          coffee_reciepe: ['water','sugar','milk']
        }
      })

    </script>

  </body>
</html>
{{< / highlight >}}
The 'v-for' directive loops through array of items.
{{< highlight go "linenos=table,linenostart=1" >}}
 <!-- html and javascript -->

<html>
  <body>

    <h2>Vue.js</h2>

 
      <ul id="app"></ul>

  
    <script>
    
		var coffee_reciepe = ['water','sugar','milk'];

        var ingredient_item_list = '';
        
        coffee_reciepe.forEach(function(ingredient){
        	
            ingredient_item_list = ingredient_item_list + '<li>' + ingredient + '</li>';

        });
        
        document.getElementById('app').innerHTML = ingredient_item_list;

    </script>

  </body>
</html>
{{< / highlight >}}



#### Resorce links ####

[Vue.js Guide](https://vuejs.org/v2/guide/).

[Vue.js api](https://vuejs.org/v2/api/).

[ Components basics ](https://vuejs.org/guide/components.html).

[ Template syntax ](https://vuejs.org/v2/guide/syntax.html).

[ Vue.js cli](https://cli.vuejs.org/guide/).

[Vue.js examples ](https://vuejs.org/v2/examples/).