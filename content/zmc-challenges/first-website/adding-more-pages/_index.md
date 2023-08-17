---
_db_id: 867
blurb: One of HTML's superpowers is linking. One HTML page is nice and all, but more
  is better.
content_type: project
flavours:
- none
link_example: https://your-name.github.io/your-repo-name/
link_message: Please make sure you are linking to your github page, not just your
  repo. If someone follows the link then they should see your website
link_name: Github page url
link_regex: https://.*\.github\.io/(?!.*\.html/?$).*
submission_type: link
title: Adding more pages
---

In this section, you are going to learn about making websites with multiple pages. First, you're going to need to learn about anchor tags, also known as links.

Give these a read:

- [W3Schools documentation on links](https://www.w3schools.com/html/html_links.asp)
- [MDN documentation on links](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks)

## Project instructions 

Now you are going to demonstrate your knowledge of links by adding a few to your site.

Here is what you need to do:

### 1. Create another page

On your local device create another html file and give it a nice name. Your directory structure should now look like this:

```
your-project-directory/
    images/
    index.html
    new_page.html  < You can name this whatever you want
                     Just make sure that it ends in .html
```

Your new file should have the following:

- valid `<head>` and `<body>` elements
- a single `<h1>` title 
- an unordered HTML list. It can contain whatever you want. You'll need to do a little bit of research to figure this one out :) 
- a link to your `index.html` page
- a link to another website of your choice. The `href` attribute should have an absolute URL (check the MDN docs above if you don't know what that means)

### 2. Update index.html

Create a link from your `index` page to your new page. This link should make use of a relative URL.

### 3. Check yourself

When you look at your website on your device you should be able to click/press on the different links and they should go to the right places.

If you are on the index page then you should be able to navigate to your new page.

If you are on our new page you should be able to navigate back to your index page. You should also be able to navigate to an external site.

All 3 links should work perfectly.

And, as usual, it's very important to make sure that all your HTML is valid!

### 4. Update your repo 

Once everything seems to be working fine then upload your latest changes to Github. Make sure your GitHub page shows the latest version of your website. Make sure the links on your website work.

All of your files should be in the same repo. 

Double check that everything is still working in your Github page.

### 5. Submit your project

Once you are happy that your Github page does what it is meant to, submit the link to your Github page and wait for feedback.