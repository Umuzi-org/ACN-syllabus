---
_db_id: 933
content_type: topic
prerequisites:
  hard:
  - tech-big-picture/how-web-applications-work/part-2
ready: true
title: Anatomy of a web app - part 3 - AJAX
---

In the last part of our story, you used the "search" function, and you were redirected to a new page containing your search results.

## Loading more 

Now let's say you are looking at the listed toasters and you aren't quite finding the one you want. So you scroll to the bottom of the page and click on the "Load more" button.

Now you don't get redirected to a new page. Instead what happens is:

- the button turns into a loading spinner
- then new toasters arrive on the bottom of the page, you can keep scrolling down

So you didn't redirect to a new page, your browser somehow fetched extra information from the server and displayed it without the need for a redirect.

## What happened?

AJAX is what happened. AJAX stands for "Asynchronous JavaScript And XML", so a lot of people think it is way more complicated than it actually is.

Here's how it works:

Your browser has the ability to send HTTP(S) requests to the Takealot server whenever it needs to. So far in this story, you have only seen these requests being triggered when new pages are visited. When you visited the Takealot home page in part 1, then your browser requested some information from the server. Then when you landed on the search results page in part 2, more information was requested.

So requests get sent to the server when you navigate to a new page. But they can also be sent in other circumstances.

If you think back to earlier in this course, you would have been introduced to the 3 languages of the web. HTML, CSS and JavaScript. 

HTML describes the content of a web page, CSS describes the looks. Javascript describes the smarts - you can use JavaScript to implement algorithms.

When you click on the "Load More" button then some Javascript functionality is triggered. The algorithm looks like this:

```
Change the Load More button to look like a spinner
Send a request to the server to fetch the next page of search results
Wait for the results
Draw the new toasters onto the screen
Change the Load More button so it no longer looks like a spinner
```

AJAX sounds fancy, but it really just means: Sending HTTP(S) requests from a browser whenever you need to (instead of just on page load).

## Some things to notice

There are a few cool things happening here:

### Pagination

Not all toasters were loaded when you accessed the search result page for the first time, you actually needed to load more. Most websites that need to display large listings of information do something similar. The technique is called paging or pagination. 

This is useful because if you fetch absolutely all the toaster information on the first page visit then:

- you'd be fetching a lot of data, much of which would be irrelevant
- the server and database would be doing extra work for nothing
- you would need to wait longer for the information, so the page would take longer to load
- the whole web page would take up extra memory and slow your computer down

Pagination is a pretty efficient way to give the user the information they need when they need it.

### Javascript can get triggered by buttons

The Load More button is defined in HTML. When a user clicks on that button then it triggers a JavaScript function.

It's possible to tie different JavaScript functions to different events as well, it's not just limited to button clicks. 

### Javascript can update HTML and CSS 

Here is the algorithm again:

```
1. Change the Load More button to look like a spinner
2. Send a request to the server to fetch the next page of search results
3. Wait for the results
4. Draw the new toasters onto the screen
5. Change the Load More button so it no longer looks like a spinner
```

Can you see how JavaScript was used to manipulate the HTML and CSS of the website?

A possible point of confusion is that, even though HTML and CSS are being manipulated, Javascript isn't actually changing any of the original files. 

When a browser receives HTML and CSS files then it draws a picture called the DOM (Document Object Model). When you use Javascript to make changes to what is displayed then you are not changing the original files, you are editing the DOM.

This technique is referred to as DOM manipulation. 

## In conclusion 

You have now seen how JavaScript fits into the picture, and you've been introduced to AJAX and DOM Manipulation.

Next up, we're going to learn about authentication and authorization.