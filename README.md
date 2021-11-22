# Abstract

Both avid and amateur readers, whom utilize Amazon's bountiful list of purchaseable books, find that they may spend more time than that which is affordable when they peruse seemingly endless book categories and offerings; a numerical scale (star rating system) is often the only way to discern a collective synthesis without having to sift through reviews to discover the average sentiment or salient qualities of a particular book offering. Thus, we propose a utilization of the Python-supported NLTK (Natural Language Toolkit) toward effectively decreasing the amount of time required to acknowledge the most prominent aspects of a book offering. Using NLTK in sequence with a web scraper, we are able to perform a number of methods of text analysis such as stemming, lemmatisation, and part-of-speech tagging. Eventually, after creating a list of commonly reoccuring adjectives, which are non-descriptive, we are able to then compare this list against our extracted adjectives to enable a final filtering. Therefore, we have successfully extracted the most salient features of each book offering according to the cumulative opinion of the Amazon reader community, and constructed a mechanism for a succinct determination of interest alignment for all readers looking to make their next purchase.

# Project Description - Useful Definitions & Links

#### Natural Language Toolkit
> The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language. https://www.nltk.org/

#### Stemming
> In linguistic morphology and information retrieval, stemming is the process of reducing inflected words to their word stem, base or root form—generally a written word form (e.g., 'change', 'changing', and 'changes' are reduced to 'chang').

#### Lemmatisation
> In linguistics, lemmatisation is the process of grouping together the inflected forms of a word so they can be analysed as a single item, identified by the word's lemma, or dictionary form (e.g., 'change', 'changing', and 'changes' are reduced to 'change').

#### Part-Of-Speech
> In traditional grammar, a part of speech or part-of-speech is a category of words that have similar grammatical properties.

# Build Instructions

#### Creation of virtual environment (to be conducted prior to pulling repository)

- mkdir myproject
- cd myproject
- py -3 -m venv venv
- venv\Scripts\activate
- cd venv

#### Installation of dependencies

- pip install flask
- pip install nltk
- pip install matplotlib

> Note: Pull the repo such that the files and folders shown in it are existing within venv. You may need to delete all of the current files and folders in venv prior to pulling the repo. 

## Running the project (through Windows command-line)

- set FLASK_APP=nlp
- flask run

> Note: You will need to open your browser and enter the address displayed in the command-line.



##### README.md Log

###### Week 1 - README.md

https://github.com/CIS3296SoftwareDesignF21/prj-04-better-amazon-review/blob/b27cb107336dafd3bb011018c8cc75028460aa4a/README.md

##### Week 2 - README.md

https://github.com/CIS3296SoftwareDesignF21/prj-04-better-amazon-review/blob/e28d9a4c69769796b8cea3b55ba1f2c529563be5/Week2.md

##### Week 3 - README.md

https://github.com/CIS3296SoftwareDesignF21/prj-04-better-amazon-review/blob/main/Week3.md
