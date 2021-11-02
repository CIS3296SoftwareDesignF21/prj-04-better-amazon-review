# Project Abstract
Often, I find myself more confused whether to a book is good or not from amazon after reading their reviews. Some reviews are full of hatred, making a mountain out of a molehill for a particular book due to distain for a single character, at the same time people share over the top praise for a mediocre book. My solution to this is to offer analysis of the top books on Amazon. Looking at the reviews can tell a lot about a book and offer lots of interesting statistics users can use to make a more informed decision. User will be able to look at data associated with...
- Average score compared to average length of review
- Average score compared to legitimacy of reviewer 
- Keywords and keyword combinations
- Score bell curve and standard deviation

![image](https://user-images.githubusercontent.com/89652481/139957337-9f3281c5-9382-4069-9dc4-d78ae9dc2d81.png)


# Educational Goals
The project is a very data heavy, and data driven project, data analysis is not worth anything if the data is not organized well and unreliable. Therefore, it will be incredibly important to plan our project according to UML as well as familiarize ourselves with databases and their traversal. Speed will be important we would not want out users waiting more than a few seconds for their results, so we must implement thoughtful program and algorithm design to optimize performance. As mentioned earlier this project is very open ended, so there will be plenty of room for on-the-fly coding in the form of adding additional analysis / features throughout the lifecycle of the project, as well as the potential for future updates with new features.

# Project 
Components: Django, Python, NLTK library (Python), Pandas library (Python), Amazon API.
Vision statement: The purpose of this software is to enhance user experience and data extraction as it pertains to Amazon's reviews and ratings - specifically, for trending books, which are the backbone of Amazon's identity and presence. We aim to incorporate sentiment and topic analysis mechanisms to effectively create a stronger filtering and weight-creation mechanism, such that users can have access to data that makes a slew of reviews more comprehensible. 

# How to Run (Django tutorial)

python manage.py runserver -> Runs local server.

python manage.py makemigrations -> Your models will be scanned and compared to the versions currently contained in your migration files, and then a new set of migrations will be written out.

python manage.py migrate -> Applies new migration files to database.


Additional commands can be found at https://docs.djangoproject.com/en/3.2/

# How to Install (Django tutorial)

Using a Windows command-line, enter the following sequence of commands (a supported version of Python must be installed):

python -m venv venv

cd venv

cd Scripts

activate

pip install Django

django-admin startproject mysite


Then, follow the provided tutorial -> https://docs.djangoproject.com/en/3.2/intro/tutorial01/

# Personas
Ben : Michael is an avid reader who finds immense joy in reading both historical biographies and science fiction novels. Michael doesn't have time to scour the internet or his local library for his newest book, and thus utilizes charts featuring popular novels to find his next purchase.

Max : Janet is a 43 year old school teacher who has decided to start reading more but does not know where to start. She has looked over Amazon's book section for a new book to read but is overwhelmed with the varying reviews on some of their top rated books. She is busy with her career and children so when she commits to reading a book she wants to make sure its worth her time. She does not want to get halfway through a book and realize she doesn't like it. Janet uses Better Amazon Book reviews to find what people really think about Amazon's top books, and makes an further informed choice as to what her next read will be.  
