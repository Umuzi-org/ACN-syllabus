---
_db_id: 499
content_type: project
flavours:
- python
prerequisites:
  hard:
  - topics/data-science-specific/datacamp/intro-to-python
  soft:
  - topics/data-science-specific/intro-to-google-colab
submission_type: repo
title: Bootcamp Exploratory Data Analysis
---

You will need to download and add all the relevant files from [here](https://drive.google.com/drive/folders/1scmLfz6SswLqKoj1S6s3VytezCR7m_dJ?usp=sharing) and add them to the repo supplied.

Your repo should contain everything needed to replicate your work:
- data
- notebook
- `requirements.txt`

## Instructions

Your task is to use the given data to answer the questions found in `questions.md`. Any other additional analysis you think will help your submission is cool with us but NO external data may be used.

We will not only be assessing your code but also how you structure and present your analysis.

## Setting Up Your Environment

If you are going through bootcamp on your mobile device or using public resources please check out [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb), this [article](https://towardsdatascience.com/intro-to-google-colab-for-data-analytics-da5e3a37af8a) can also help you get started.
This is cloud based computing environment so your work will be saved and you can access it on any machine.

### Working locally on your machine

Download and install [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your machine. This will install python
and the conda package manager for python. NB Make sure that you set the
python path! Setting the path will allow you to simply type `python`
into the terminal to open python.

You also want to install the following packages:  
- jupyter-notebook
- numpy
- pandas
- matplotlib
- seaborn
- scipy

You can install packages by typing `conda install name-of-package`, e.g.
`conda install numpy`.

To launch a new jupyter instance (kernel), open up a new terminal, navigate to the directory in which you want to be
and type `jupyter notebook`(and press enter). A new jupyter kernel will open in your browser. You can now open an existing
notebook (`*.ipynb`) or create a new notebook.

When you are done, click 'Close and Halt Kernel' or press `Ctrl+C` twice to shut down the kernel from the terminal.
