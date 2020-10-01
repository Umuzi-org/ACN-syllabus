---
_db_id: 554
content_type: topic
ready: true
title: Django and Javascript
---

As you now know, you can write Django views that generate HTML responses. What ends up running in the user's browser is a plain ol website. And so you can do whatever you would usually do with HTML.

The following tutorial shows how to incorperate js into your Django frontend. Pretty cool.

It shows how to use javascript and HighChart.js to draw some useful charts.

https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html

## Notes on static resources

This tutorial shows how to use `<script>` tags to include your js right in your template. While this can be convenient and possibly even appropriate for short scripts, it's not always the est thing to do.

If your script is long, then you might want to put it in a seperate file and refer to it as a static resource. This also of course adds to the reussability and testability of your javascript code. If everything is all jumbled together then your code can be very hard to unit test.

To learn about how Django allows you to manage static files, take a look here: https://docs.djangoproject.com/en/3.1/howto/static-files/

## Notes on ajax and apis

the `chart_data` view can be called a JSON API endpoint. Your frontend sends a request to that endpoint to fech the data.

Can you imagine how you would add a button to your frontend that re-fetches the chart data without reloading the page?

You can make other api endpoints to perform different actions and wire your frontend right to those. By doing this you can add a lot of functionality to a frontend through ajax.