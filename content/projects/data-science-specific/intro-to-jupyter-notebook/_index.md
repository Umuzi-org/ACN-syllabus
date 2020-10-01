---
_db_id: 249
available_flavours:
- python
content_type: project
ready: true
submission_type: repo
title: Introduction to Jupyter Notebooks
---

## Setting Up Your Environment

Download and install miniconda on your machine. This will install python
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
- scikit-learn

You can install packages by typing `conda install name-of-package`, e.g.
`conda install numpy`.

To launch a new jupyter instance (kernel), open up a new terminal, navigate to the directory in which you want to be
and type `jupyter notebook`(and press enter). A new jupyter kernel will open in your browser. You can now open an existing
notebook (`*.ipynb`) or create a new notebook.

When you are done, click 'Close and Halt Kernel' or press `Ctrl+C` twice to shut down the kernel from the terminal.

## Assignment

Complete the (Nobel Prize Winner assignment)[http://somewhere.nice] and upload it to Github. You will need to create a Github account if you do not already have one.

You may want to go through DataCamp's [Python Programming](https://www.datacamp.com/tracks/python-programming) track to get the
basic skills you will need to complete the assignment.

## Supporting Material

- [Python For Data Science Cheat Sheets](http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf)
- [Jupyter Notebook Keyboard Shortcuts](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw/)
- [Basic Python 3 Programming for Scientists](http://www.sixthresearcher.com/didactic-materials/)
- {{% contentlink path="topics/jupyter-notebooks-best-practices" %}}