---
_db_id: 240
content_type: project
flavours:
- python
pre: '<b> EASY: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/data-visualisation/mobile-money-viz
  soft:
  - projects/data-science-specific/data-wrangling
ready: true
story_points: 8
submission_type: repo
tags:
- plotly
- dashboard
- data-visualisation
title: Plotly Dashboard Assignment
---

## Tutorials

- [Create a basic Plotly Dashboard](https://pythoninoffice.com/python-dash-web-app-tutorial/) (Simple)
- [Create a Plotly Dashboard in under 10 minutes](https://realpython.com/python-dash/) (Easy)
- [Create a dashboard with Pusher and Flask](https://pusher.com/tutorials/live-dashboard-python) (Advanced)

## Here’s the scenario
Imagine you are working for a telcom provider or bank that wants to go into the mobile money market. Are you familiar with mobile money? Go poke around on Mtn and MoMo payment if you haven’t. It will give you a bit more context.

Your stakeholders are interested in understanding the relationship between mobile services usage, geographic factors and demographic factors, such as age, gender, marital status, land ownership, and type of income.

Your visualization needs to capture the stakeholders' attention and convey the key findings in a clear and concise manner. By doing so, you will be able to provide valuable insights to the stakeholders that they can use to make informed decisions about their business strategies.

## Why data visualization matters
In the real world as a data professional, Most of your visualizations will have to live outside of your notebook where your stakeholders/users will be able to interact with them. Therefore, it is important to create visualizations that are clear, concise, and easy to understand, even for non-technical stakeholders. 

This means that you will need to carefully consider your audience, and tailor your visualizations to their needs and level of expertise. You will also need to choose the right visualization tools and techniques to effectively communicate information visually, your findings and insights to your stakeholders. 

Ultimately, the goal of creating visualizations as a data professional is to help stakeholders make informed decisions based on data and to drive positive outcomes for the business or organization.

Visualization is an art, your dashboard is your canvas and you are the artist.

## Assignment

In the Mobile Money Data Visualisation Assignment, you created graphs to display the relationship between the type of financial services accessed (non-mobile, mobile, both) and socio-demographic information about the users (gender, land ownership, type of income, and so forth). Create a Plotly dashboard of the following graphs:

1. Create appropriate graphs to visually represent the relationship between how often mobile services are used and age, gender, marital status, land ownership and type of income.

2. Create maps to visually explore geographic distribution of mobile services coverage with respect to type of income. You can choose to create one map and use dropdowns/checkbox to filter type of income.

Your dashboard should be both visually appealing and informative.

## Instructions for reviewer

1. The candidates' repository must have a data folder as well as a source folder.
2. The data which will be used to create the plots and graphs has to be in the data folder.
3. The source code, that is, any .py or .ipynb files should be in the source folder.
4. There has to be a requirements.txt file which has been set up correctly.
5. In the source folder there should be at most two files, one that candidates usually call 'app.py' and another which
   candidates usually call 'processing.py'.
6. The graphs which will be presented on the dashboard should not be imported as saved images from the Financial Services
   in Tanzania project, the graphs should be created in the 'processing.py' file.  Therefore, any data cleanup and changes
   to the data is to be done in the 'processing.py' file.
7. Graphs are to be displayed neat and orderly on the dashboard.
8. The dashboard should have a large enough heading with an appropriate title.
9. There should be a small introduction below the heading to explain what the dashboard is about and you think about use of financial services in Tanzania. Which demographic and geographic factors do you think are associated with mobile money use.
10. Any explanations regarding a graph should not be done in paragraph form but rather pointed out on the graph with a
   suitable annotation and perhaps a small piece of text.  The idea behind any visualisations is that it should be
   so well done and clear that it becomes self-explanatory. 
11. Graphs must have suitable axes labels, things such as 'Count' is not descriptive at all.  If big data is being
   represented the candidate should consider adding a multiplier to the label, for instance,
   'Number of people [X10^5]'.  A candidate can also consider representing the log transform of the data if the data 
   represented is very large.
12. If the candidate selected to present a graph where age against mobile money is used, the candidate should ensure
    that the ages are grouped into age groups, for instance, 1-20, 21-40, 41-60, 61-80, 81-100.
13. All graphs should have legends which are descriptive.  The headings of the legends as well as any other headings
    must be in bold.  Legends should be placed at an appropriate spot so that they do not overlay the graph.
14. Graphs should be evenly spaced, and their sizes should be in proportion to the overall page size and layout.
15. The layout of the '.app' file should be neat and tidy, emphasis should be placed on indentation.  HTML tags which
    belong to the same relevant code should be underneath one another.  Code should be indented such that it reads like
    a book.

## Variables

The table below gives the variable names in the mobile money data file, with a description of the questions and a key to the answer values.

| Variable ID       | Question             | Values           |
| :---------------: | :------------------- | :--------------- |
| ID        | Unique respondent ID | String
| Q1        | Age                  | Number   
| Q2        | Gender               | 1 Male   
|           |                      | 2 Female
| Q3        | Marital status       | 1 Married
|           |                      | 2 Divorced
|           |                      | 3 Widowed
|           |                      | 4 Single/never married
| Q4        | Highest level of education completed? | 1 No formal education
|           |               | 2 Some primary
|           |               | 3 Primary completed
|           |               | 4 Post primary technical training
|           |               | 5 Some secondary
|           |               | 6 University or other higher education
|           |               | 7 Don’t know
| Q5        | Which of the following applies to you? Read out; Single response | 1 You personally own the land/plot where you live
|           |               | 2 You own the land/plot together with someone else
|           |               | 3 A household member owns the land/plot
|           |               | 4 The land/plot is rented
|           |               | 5 You don’t own or rent the land
|           |               | 6 Don’t know
| Q6        | Do you personally own land (other than the land you live on) that you have land certificates of ownership for? | 1 Yes
|       |               | 2 No
| Q7    | Do you personally own a mobile phone? | 1 Yes
|       |               | 2 No
| Q8_1 through Q8_11 | Different people have different ways of getting money, please tell me how you get the money you spend? |      | Multiple mention possible
Q8_1    | Salaries/wages | 1 Yes
|       |               | 0 No
Q8_2    | Money from trading/selling Anything you produce/grow/raise/make/collect with the intention of selling | 1 Yes
|       |               | 0 No
Q8_3    | Money from providing a service – i.e. such as transport, hairdressing, processing, hospitality services (food & accommodation) | 1 Yes
|       |               | 0 No
Q8_4    | Piece work/Casual labor/Occasional jobs | 1 Yes
|       |               | 0 No
Q8_5    | Rental income | 1 Yes
|       |               | 0 No
Q8_6    | Interest from savings, investments, stocks, unit trusts etc. | 1 Yes
|       |               | 0 No
Q8_7    | Pension | 1 Yes
|       |               | 0 No
Q8_8    | Social welfare money/grant from Government | 1 Yes
|       |               | 0 No
Q8_9    | Rely on someone else/others to give/send me money | 1 Yes
|       |               | 0 No
Q8_10   | Don’t get money – someone else pays my expenses | 1 Yes
|       |               | 0 No
Q8_11   | Other | 1 Yes
|       |               | 0 No
Q9      | Only for those who said they get a salary/wages. Who do you work for? | -1 not applicable
|       |               | 1 Government
|       |               | 2 Private company/business
|       |               | 3 Individual who owns his own business
|       |               | 4 Small scale farmer
|       |               | 5 Commercial farmer
|       |               | 6 Work for individual/household e.g. security guard, maid etc.
|       |               | 7 Other
Q10     | Only for those who said they get money from selling things – what kind of things do you MAINLY sell (get most money from)? | -1 not applicable
|       |               | 1 Crops/produce I grow
|       |               | 2 Products I get from livestock
|       |               | 3 Livestock
|       |               | 4 Fish you catch yourself/aquaculture
|       |               | 5 Things you buy from others – agricultural products
|       |               | 6 Things you buy from others – non-agricultural products
|       |               | 7 Things you make (clothes, art, crafts)
|       |               | 8 Things you collect from nature (stones, sand, thatch, herbs)
|       |               | 9 Things you process (honey, dairy products, flour)
|       |               | 10 Other
Q11     | Only for those who said they get money from providing a service – what kind of services do you MAINLY provide (get most money from)? | -1 not applicable
|       |               | 1 Personal services (hairdressers, massage, etc.)
|       |               | 2 Telecommunications/IT
|       |               | 3 Financial services
|       |               | 4 Transport
|       |               | 5 Hospitality – Accommodation, restaurants, etc.
|       |               | 6 Information/research
|       |               | 7 Technical – mechanic, etc.
|       |               | 8 Educational/child care
|       |               | 9 Health services – traditional healer etc.
|       |               | 10 Legal services
|       |               | 11 Security
|       |               | 12 Other, specify
Q12     | In the past 12 months, have you sent money to someone in a different place within the country or outside of Tanzania? | 1 Yes
|       |               | 2 No
Q13     | When did you last send money? | -1 not applicable
|       |               | 1 Yesterday/today
|       |               | 2 In the past 7 days
|       |               | 3 In the past 30 days
|       |               | 4 In the past 90 days
|       |               | 5 More than 90 days ago but less than 6 months ago  
|       |               | 6 6 months or longer ago
Q14 | In the past 12 months, have you received money from someone in a different place within the country or from outside the country? | 1 Yes
|       |               | 2 No
Q15     | When did you last receive money? | -1 not applicable
|       |               | 1 Yesterday/today
|       |               | 2 In the past 7 days
|       |               | 3 In the past 30 days
|       |               | 4 In the past 90 days
|       |               | 5 More than 90 days ago but less than 6 months ago  
|       |               | 6  6 months or longer ago
Q16     | In the past 12 months, how often did you use mobile money for purchases of goods and/or services? | -1 not applicable
|       |               | 1 Never
|       |               | 2 Daily
|       |               | 3 Weekly
|       |               | 4 Monthly
|       |               | 5 Less often than monthly
Q17     | In the past 12 months, how often did you use mobile money for paying your bills? | -1 not applicable
|       |               | 1 Never
|       |               | 2 Daily
|       |               | 3 Weekly
|       |               | 4 Monthly
|       |               | 5 Less often than monthly
Q18     | Literacy in Kiswhahili | 1 Can read and write  
|       |               | 2 Can read only  
|       |               | 3 Can write only  
|       |               | 4 Can neither read nor write  
|       |               | 5 Refused to read
Q19     | Literacy in English | 1 Can read and write  
|       |               | 2 Can read only  
|       |               | 3 Can write only  
|       |               | 4 Can neither read nor write  
|       |               | 5 Refused to read
Latitude  | Approximate latitude | Number
Longitude | Approximate longitude | Number
Mobile_money | Do you use mobile money? | 1 Yes
|       |               | 0 No
Savings | Do you save? | 1 Yes
|       |               | 0 No
Borrowing | Do you borrow? | 1 Yes
|       |               | 0 No
Insurance | Do you have insurance? | 1 Yes
|       |               | 0 No
Mobile_money_classification |   | 0 no mobile money and no other financial service (saving, borrowing, insurance)
|       |               | 1 no mobile money, but at least one other financial service
|       |               | 2 mobile money only
|       |               | 3 mobile money and at least one other financial service