---
_db_id: 84
content_type: topic
ready: true
title: Clean Code for XML
---

A XML user interface can get quite nested and complicated, which is why it is very important to write clean and easy to read code.

## Adding an element or a layout

Typically in XML you mark the end of an element in the following way:

```
<Element></Element>
```

this is however only necessary in a situation in which you want to place another element inside this element. Usually used for `layout` elements.

example:
	
	```
	<LayoutElement>
		<ViewElement /> //This now resides within the LayoutElement.
	</LayoutElement> //This is then the closing tag.
	```

When you want to add an element that does not contain any `View Elements` or `Layout Elements` it is best practise to close it in the following manner:

example:
	
	```
	<ViewElement /> //Note how it does not require a closing tag.
	```

## Adding properties to a element

When adding `properties` to an XML element, it is important to `line up each property vertically` and on a `new line`.

example:

	```		
	<ViewElement	Property1="Value1"
					Property2="Value2"
					Property3="Value3" />
	```

## Nesting elements

To assist with readability, `indentations` are used to indicate that an element is within another element. Each element is indented once when inside a `parent` element.

example:

	```
	<LayoutElement	Property1="Value1"
					Property2="Value2" >

		<ViewElement	Property1="Value1"
						Property2="Value2" />

	</LayoutElement>
	```

Note: Leave one new line between elements to assist with differentating elements.

For more information regarding XML `best practices`, you can read through this [documentation](https://docs.oracle.com/cd/E14571_01/web.1111/e13724/best.htm#XMLPG211).