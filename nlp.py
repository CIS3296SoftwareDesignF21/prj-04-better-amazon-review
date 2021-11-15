#!/usr/bin/env python3

from operator import itemgetter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import classify
from nltk import NaiveBayesClassifier
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import csv
import array as arr


class Library:
    books = []

    def get_books(self):
        return self.books

    def set_books(self, books):
        self.books = books

    def add_book(self, Book):
        self.books.append(Book)


class Book:
    reviews = []
    review_count = 0

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_reviews(self):
        return self.reviews

    def set_reviews(self, reviews):
        self.reviews = reviews

    def add_review(self, Review):
        self.reviews.append(Review)
        self.review_count += 1

    def remove_review(self, Review):
        self.reviews.remove(Review)

    def get_review_count(self):
        return self.review_count

    def set_review_count(self, review_count):
        self.review_count = review_count


class Review:

    def __init__(self, title, content, date, variant, images, verified, author, rating, product, url):
        self.title = title
        self.content = content
        self.date = date
        self.variant = variant
        self.images = images
        self.verified = verified
        self.author = author
        self.rating = rating
        self.product = product
        self.url = url

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_variant(self):
        return self.variant

    def set_variant(self, variant):
        self.variant = variant

    def get_images(self):
        return self.images

    def set_images(self, images):
        self.images = images

    def get_verified(self):
        return self.verified

    def set_verified(self, verified):
        self.verified = verified

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url


class StatTool:

    def read_csv(self):
        stop_words = set(stopwords.words("english"))
        lem = WordNetLemmatizer()
        stem = PorterStemmer()
        with open('bookData', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            titles = []
            reviews = []
            library = Library()
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    new_review = Review({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]},
                                        {row[8]}, {row[9]})
                    reviews.append(new_review)
                    if {row[8]} in titles:
                        continue
                    else:
                        book = Book({row[6]}, {row[8]})
                        titles.append({row[8]})
                        library.add_book(book)
            for entry in library.get_books():
                fd = FreqDist()
                for review in reviews:
                    if review.get_product() == entry.get_title():
                        entry.add_review(review)
                        #  print(entry.get_title(), review.get_product())
                        text = str(review.get_content()).lower()
                        tokenized_word = word_tokenize(text)
                        filtered_sent = []
                        for w in tokenized_word:
                            if w not in stop_words:
                                filtered_sent.append(w)
                        ps = PorterStemmer()
                        stemmed_words = []
                        for w in filtered_sent:
                            stemmed_words.append(ps.stem(w))
                        lemma_words = []
                        for w in filtered_sent:
                            lemma_words.append(lem.lemmatize(w, "v"))
                        for word in lemma_words:
                            word.replace("'", "")
                        tagged_data = nltk.pos_tag(lemma_words)
                        adjectives = []
                        for index, tuple in enumerate(tagged_data):
                            element_one = tuple[0]
                            element_two = tuple[1]
                            if element_two == 'JJ':
                                if str(element_one).endswith('ical') or str(element_one).endswith('ic') or \
                                        str(element_one).endswith('al') or str(element_one).endswith('ive') or \
                                        str(element_one).endswith('able') or str(element_one).endswith('ful') or \
                                        str(element_one).endswith('ous'):
                                    if not str(element_one).startswith("'") and element_one != 'total' and \
                                            element_one != 'pedestal' and element_one != 'receive' and \
                                            element_one != 'thankful' and element_one != 'moral' and \
                                            element_one != 'several' and element_one != 'able' and \
                                            element_one != 'dive' and element_one != 'lyric' and \
                                            element_one != 'give' and element_one != 'public' and \
                                            element_one != 'available' and element_one != 'arrive' and \
                                            element_one != 'deal' and element_one != 'previous' and \
                                            element_one != 'final' and element_one != 'table' and \
                                            element_one != 'conceive' and element_one != 'live' and \
                                            element_one != 'potential' and element_one != 'perspective' and \
                                            element_one != 'oral' and element_one != 'narrative' and \
                                            element_one != 'deceive' and element_one != 'loyal' and \
                                            element_one != 'positive' and element_one != 'additional' and \
                                            element_one != 'careful' and element_one != 'initial' and \
                                            element_one != 'pic' and element_one != 'individual' and \
                                            element_one != 'physical' and element_one != 'pacific' and \
                                            element_one != 'literal' and element_one != 'seal' and \
                                            element_one != 'capable' and element_one != 'actual' and \
                                            element_one != 'drive' and element_one != 'digital' and \
                                            element_one != 'various' and element_one != 'negative' and \
                                            element_one != 'usable' and element_one != 'survive' and \
                                            element_one != 'doable' and element_one != 'numerous' and \
                                            element_one != 'material' and element_one != 'alive' and \
                                            element_one != 'grateful':
                                        adjectives.append(element_one)
                            fd.update(adjectives)
                print(entry.get_title(), fd.most_common(10))
                fd.plot(10, cumulative=False, title=entry.get_title())
                plt.show()


stat_tool = StatTool()
stat_tool.read_csv()
