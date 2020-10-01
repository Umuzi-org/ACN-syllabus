---
_db_id: 242
available_flavours:
- python
content_type: project
pre: '<b> HARD: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/dashboards/plotly_dashboards
  soft:
  - projects/data-science-specific/data-wrangling
ready: true
submission_type: repo
tags:
- webscraping
- dashboard
title: Webscraping and Live Dashboard Assignment
---

## Assignment

Use [beautifulsoup](https://pypi.org/project/beautifulsoup4/) and regular expressions (regex) to scrape the data of provincial dam levels from the [Department of Water and Sanitation](http://www.dwa.gov.za/Hydrology/Weekly/SumProvince.aspx).

Create a dashboard with graphs showing the current and previous week's dam levels by province, and compare it to the water levels from the previous year. Your dashboard should update weekly (in other words, you can't just copy and paste this week's data to your notebook).

### Think about

- What type of graph will show this information best?
- Do all graphs have clearly understandable headings, axis labels and (if applicable) legends?