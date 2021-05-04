---
_db_id: 240
content_type: project
flavours:
- python
pre: '<b> EASY: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/data-visualisation
  soft:
  - projects/data-science-specific/data-wrangling
ready: true
story_points: 8
submission_type: repo
tags:
- plotly
title: Plotly Dashboard Assignment
---

## Tutorials

- [Create a Plotly Dashboard in under 10 minutes](https://moderndata.plot.ly/create-a-plotly-dashboards-in-under-10-minutes/) (Easy)
- [Create a dashboard with Pusher and Flask](https://pusher.com/tutorials/live-dashboard-python) (Advanced)

## Assignment

In the Mobile Money Data Visualisation Assignment, you created graphs to display the relationship between the type of financial services accessed (non-mobile, mobile, both), how frequently these services were accessed, and socio-demographic information about the users (gender, land ownership type of income, and so forth). Create a Plotly dashboard of the 3-5 most informative graphs from this assignment.

Your dashboard should be both visually appealing and informative.

## Instructions for reviewer

1. The candidates repository must have a data folder as well as a source folder.
2. The data which will be used to create the plots and graphs has to be in the data folder.
3. The source code, that is, any .py or .ipynb files should be in the source folder.
4. There has to be a requirements.txt file which has been setup correctly.
5. In the source folder there should be at most two files, one that candidates usually call 'app.py' and another which
   candidates usually call 'processing.py'.
6. The graphs which will be presented on the dashboard should not be imported as saved images from the Financial services
   in Tanzania project, the graphs should be created in the 'processing.py' file.  Therefore, any data cleanup and changes
   to the data is to be done in the 'processing.py' file.
7. No less than three and no more than five graphs are to be displayed in a neat and orderly fassion on the dashboard.
8. The dashboard should have a large enough heading with an appropriate title.
9. There should be a small introduction below the heading to explain what the dashboard is about.
10. Any explanations regarding a graph should not be done in paragraph form but rather pointed out on the graph with a
   suitable annotation and perhaps a small piece of text.  The idea behind any visualizations is that it should be
   so well done that it becomes self explanatory.
11. Graphs must have suitable axes lables, things such as 'Count' is not descriptive at all.  If big data is being
   represented the candidate should consider adding a multiplier to the label, for instance,
   'Number of people [X10^5]'.  A candidate can also consider representing the log transform of the data if the data 
   represented is very large.
12. If the candidate selected to present a graph where age against mobile money is used, the candidate should ensure
    that the ages are grouped into age groups, for instance, 1-20, 21-40, 41-60, 61-80, 81-100.
13. All graphs should have legends which are descriptive.  The headings of the legends as well as any other headings
    must be in bold.  Legends should be placed at an appropriate spot so that they do not overlay the graph.
14. Graphs should be evenly spaced and their sizes should be in proportion to the overall page size and layout.
15. The layout of the '.app' file should be neat and tidy, emphasis should be placed on indentation.  HTML tags which
    belong to the same relevant code should be underneath one another.  Code should be indented such that it reads like
    a book.
