---
_db_id: 244
available_flavours:
- python
content_type: project
pre: '<b>MEDIUM: </b>'
prerequisites:
  hard:
  - projects/data-science-specific/data-visualisation/linux-evolution
  - topics/jupyter-notebooks-best-practices
  - topics/python-self-learning
  soft:
  - projects/tdd/simple-calculator-part1
ready: true
story_points: 8
submission_type: repo
tags:
- data-visualisation-mobile-money
title: Financial Services Use in Tanzania
---

## Background

The [training](training.csv) dataset contains demographic information and what financial services are used by approximately 10,000 individuals across Tanzania. This data was extracted from the FSDT Finscope 2017 survey and prepared specifically for this challenge.

Each individual is classified into four mutually exclusive categories:

- No_financial_services: Individuals who do not use mobile money, do not save, do not have credit, and do not have insurance
- Other_only: Individuals who do not use mobile money, but do use at least one of the other financial services (savings, credit, insurance)
- Mm_only: Individuals who use mobile money only
- Mm_plus: Individuals who use mobile money and also use at least one of the other financial services (savings, credit, insurance)

This dataset is the geospatial mapping of all cash outlets in Tanzania in 2012. Cash outlets in this case included commercial banks, community banks, ATMs, microfinance institutions, mobile money agents, bus stations and post offices. This data was collected by FSDT.

## Instructions:

1. Examine the dataset. Are there any missing observations or columns where the data do not seem valid?

2. Get basic descriptive statistics for the dataset.

3. Create appropriate graphs to visually represent the relationship between financial services accessed (non-mobile, mobile, both) and age, gender, marital status, land ownership and type of income.

4. Create appropriate graphs to visually represent the relationship between how often mobile services are used and age, gender, marital status, land ownership and type of income.

5. Create a map to visually explore geographic distribution of mobile services coverage with respect to type of income.

6. What can you conclude about use of financial services in Tanzania? Which demographic and geographic factors are associated with mobile money use?

## Variables

The table below gives the variable names in the mobile money data file, with a description of the questions and a key to the answer values.

|    Variable ID     | Question                                                                                                       | Values                                            |
| :----------------: | :------------------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
|         ID         | Unique respondent ID                                                                                           | String                                            |
|         Q1         | Age                                                                                                            | Number                                            |
|         Q2         | Gender                                                                                                         | 1 Male                                            |
|                    | 2 Female                                                                                                       |
|         Q3         | Marital status                                                                                                 | 1 Married                                         |
|                    | 2 Divorced                                                                                                     |
|                    | 3 Widowed                                                                                                      |
|                    | 4 Single/never married                                                                                         |
|         Q4         | Highest level of education completed?                                                                          | 1 No formal education                             |
|                    | 2 Some primary                                                                                                 |
|                    | 3 Primary completed                                                                                            |
|                    | 4 Post primary technical training                                                                              |
|                    | 5 Some secondary                                                                                               |
|                    | 6 University or other higher education                                                                         |
|                    | 7 Don’t know                                                                                                   |
|         Q5         | Which of the following applies to you? Read out; Single response                                               | 1 You personally own the land/plot where you live |
|                    | 2 You own the land/plot together with someone else                                                             |
|                    | 3 A household member owns the land/plot                                                                        |
|                    | 4 The land/plot is rented                                                                                      |
|                    | 5 You don’t own or rent the land                                                                               |
|                    | 6 Don’t know                                                                                                   |
|         Q6         | Do you personally own land (other than the land you live on) that you have land certificates of ownership for? | 1 Yes                                             |
|                    | 2 No                                                                                                           |
|         Q7         | Do you personally own a mobile phone?                                                                          | 1 Yes                                             |
|                    | 2 No                                                                                                           |
| Q8_1 through Q8_11 | Different people have different ways of getting money, please tell me how you get the money you spend?         |

| Multiple mention possible
Q8_1 | Salaries/wages | 1 Yes
| | 0 No
Q8_2 | Money from trading/selling Anything you produce/grow/raise/make/collect with the intention of selling | 1 Yes
| | 0 No
Q8_3 | Money from providing a service – i.e. such as transport, hairdressing, processing, hospitality services (food & accommodation) | 1 Yes
| | 0 No
Q8_4 | Piece work/Casual labor/Occasional jobs | 1 Yes
| | 0 No
Q8_5 | Rental income | 1 Yes
| | 0 No
Q8_6 | Interest from savings, investments, stocks, unit trusts etc. | 1 Yes
| | 0 No
Q8_7 | Pension | 1 Yes
| | 0 No
Q8_8 | Social welfare money/grant from Government | 1 Yes
| | 0 No
Q8_9 | Rely on someone else/others to give/send me money | 1 Yes
| | 0 No
Q8_10 | Don’t get money – someone else pays my expenses | 1 Yes
| | 0 No
Q8_11 | Other | 1 Yes
| | 0 No
Q9| Only for those who said they get a salary/wages. Who do you work for? | -1 not applicable
| | 1 Government
| | 2 Private company/business
| | 3 Individual who owns his own business
| | 4 Small scale farmer
| | 5 Commercial farmer
| | 6 Work for individual/household e.g. security guard, maid etc.
| | 7 Other
Q10 | Only for those who said they get money from selling things – what kind of things do you MAINLY sell (get most money from)? | -1 not applicable
| | 1 Crops/produce I grow
| | 2 Products I get from livestock
| | 3 Livestock
| | 4 Fish you catch yourself/aquaculture
| | 5 Things you buy from others – agricultural products
| | 6 Things you buy from others – non-agricultural products
| | 7 Things you make (clothes, art, crafts)
| | 8 Things you collect from nature (stones, sand, thatch, herbs)
| | 9 Things you process (honey, dairy products, flour)
| | 10 Other
Q11 | Only for those who said they get money from providing a service – what kind of services do you MAINLY provide (get most money from)? | -1 not applicable
| | 1 Personal services (hairdressers, massage, etc.)
| | 2 Telecommunications/IT
| | 3 Financial services
| | 4 Transport
| | 5 Hospitality – Accommodation, restaurants, etc.
| | 6 Information/research
| | 7 Technical – mechanic, etc.
| | 8 Educational/child care
| | 9 Health services – traditional healer etc.
| | 10 Legal services
| | 11 Security
| | 12 Other, specify
Q12 | In the past 12 months, have you sent money to someone in a different place within the country or outside of Tanzania? | 1 Yes
| | 2 No
Q13 | When did you last send money? | -1 not applicable
| | 1 Yesterday/today
| | 2 In the past 7 days
| | 3 In the past 30 days
| | 4 In the past 90 days
| | 5 More than 90 days ago but less than 6 months ago  
 | | 6 6 months or longer ago
Q14 | In the past 12 months, have you received money from someone in a different place within the country or from outside the country? | 1 Yes
| | 2 No
Q15 | When did you last receive money? | -1 not applicable
| | 1 Yesterday/today
| | 2 In the past 7 days
| | 3 In the past 30 days
| | 4 In the past 90 days
| | 5 More than 90 days ago but less than 6 months ago  
 | | 6 6 months or longer ago
Q16 | In the past 12 months, how often did you use mobile money for purchases of goods and/or services? | -1 not applicable
| | 1 Never
| | 2 Daily
| | 3 Weekly
| | 4 Monthly
| | 5 Less often than monthly
Q17 | In the past 12 months, how often did you use mobile money for paying your bills? | -1 not applicable
| | 1 Never
| | 2 Daily
| | 3 Weekly
| | 4 Monthly
| | 5 Less often than monthly
Q18 | Literacy in Kiswhahili | 1 Can read and write  
 | | 2 Can read only  
 | | 3 Can write only  
 | | 4 Can neither read nor write  
 | | 5 Refused to read
Q19 | Literacy in English | 1 Can read and write  
 | | 2 Can read only  
 | | 3 Can write only  
 | | 4 Can neither read nor write  
 | | 5 Refused to read
Latitude | Approximate latitude | Number
Longitude | Approximate longitude | Number
Mobile_money | Do you use mobile money? | 1 Yes
| | 0 No
Savings | Do you save? | 1 Yes
| | 0 No
Borrowing | Do you borrow? | 1 Yes
| | 0 No
Insurance | Do you have insurance? | 1 Yes
| | 0 No
Mobile_money_classification | | 0 no mobile money and no other financial service (saving, borrowing, insurance)
| | 1 no mobile money, but at least one other financial service
| | 2 mobile money only
| | 3 mobile money and at least one other financial service