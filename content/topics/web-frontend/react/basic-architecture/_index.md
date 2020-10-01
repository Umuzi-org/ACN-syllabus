---
_db_id: 514
content_type: topic
prerequisites:
  hard:
  - topics/web-frontend/react/basic-tutorial
  soft: []
ready: true
title: 'React: Basic basic architectural guidelines'
---

React is very powerful but allows a person to write some proper spaghetti code. It's best to develop some good habits early on so that you write code that is easy to grow and maintain.

Here are a few rules worth following

## Use function based components

You have a choice of writing your components as functions or classes. Choose functions unless you are forced to use classes.

Why? The code is just smaller and cleaner. And React actually runs a little faster with function based components.

This is a class based component

```
class IconButton extends React.Component {
  [...]
  render() {
    return (
      <button onClick={this.props.onClick()}>
        <i class={this.props.iconClass}></i>
      </button>
    );
  }
}
```

But this would be better:

```
const IconButton = (props) => {
    return (
      <button onClick={this.props.onClick()}>
        <i class={this.props.iconClass}></i>
      </button>
    );
  }
```

## NameComponentsLikeThis

The standard in js is toNameYourFunctionsLikeThis. But the standard in react is to:

```
<UseYourComponentsLikeThis/>
<andNotLikeThis/>
```

If it walks like a compeont, and it quacks like a component, make sure it is accessable by a name that makes it look like a component.

If you are working on a team of devs and you say "Hey bro, just use the header menu component", then your team mate should just know that they can use `<HeaderMenu/>` in their code. Thay should not have to guess or look things up. Components just behave like components.

## Install Prettier

Seriously.

## Seperate display stuff from logic and data stuff

Unless a component is suuuuper simple it is good to seperate your display and data code. This is generally considered good practice.

Different people recommend different naming schemes. This one is pretty clear.

Have a directory hierarchy

```
MyComponent/
    index.js
    Presentation.js
```

Inside index.js we'd have something like this:

```
import React from "react";
import Presentation from "./Presentation";

// some logic and data and things

function YourComponent(props){
    // blah blah complicated stuff

    return <Presentation {presentationProps}/>
}

// etc etc more stuff

export default YourComponent;

```

And inside Presentation.js you would have something like this:

```
// imports
// styling

export default (props)=>{
    //seriously no state here. Only props!!!
    return (
        <Pretty>
            <Stuff>
                <That/>
                <Makes/>
                <Use/>
                <OfThoseProps/>
            </Stuff>
        <Pretty>
    )
}
```

Then to import your component just do:

```
import MyComponent from "path/to/MyComponent"
```

Since `MyComponent` is a directory, the import will automatically grab whatever got exported from index.js.

## Dont use a CSS pre-processor unless you are dealing with legacy code

There are loads of css pre-processors around, eg Sass and Less. But that said, these days you dont need them React does the job of a CSS pre-processor just fine. And even if you weren't using React, modern web technologies make css pre-processors into a pointless complication.

So avoid them on new projects.

If you want to know more about why, just look at how versatile React's styling system is. And you can read up on the Shadow Dom as well if you want to.