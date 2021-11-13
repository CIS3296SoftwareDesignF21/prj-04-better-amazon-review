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


stop_words = set(stopwords.words("english"))
lem = WordNetLemmatizer()
stem = PorterStemmer()

# Sentence Tokenization
text = """Great book so far, what can I say? It's a touchstone of science fiction. Ordered the first three books
 separately (because it was actually slightly cheaper to do that than get the box set) and kind of surprised the first
  book is larger in width and height than the other two. It's not a big deal I guess but kind of defeats the purpose of
   getting three books from a series that match each other. I just thought this was odd enough to mention in a review.

UPDATE: Figured it out, the first book is actually in Trade Paperback format; the other two are the NEW Mass Market
 Paperbacks. Unfortunately on Amazon, the latter is being sold without delineation as the "Paperback" option, often
  with the "Mass Market" option seeming to be OLDER editions of the MMP size. This is also true for the 6 book (unboxed)
   set that I later purchased twice, trying to get the rest of the books in the bigger size.

Note: I prefer the bigger size because it stays open when laid on a flat surface or in your lap. That sold it for me.
 On top of that, the font looks better somehow, and the narrow size just looked and felt kind of weird because the font
  size was the same but the pages are so narrow (I had an older edition of the first book that was MMP size but smaller
   font so it didn't look and read weird).

In all my frustrated searches on Amazon, it seemed really unusually difficult to find the rest of the books in the
 larger Trade Paperback size, so for your sake, here's what I figured out after way too much time: A) The official
  BOXED set is the Trade Paperback size of the first book. B) Or, if you are like me and only wanted to get the first
   few books in Trade Paperback size, go to the Penguin Random House website, find the individual Dune books, select
    "Paperback", and click on their Amazon link to buy it here
     (they also link to other major book dealers, if you prefer). I managed to find books two, three, and four this
      way., which were the only ones I really wanted anyway.

Note that as of writing this, the second and third books in Trade Paperback size on Amazon are both $9.99 each
 (same price as the NEW MMP books) but God Emperor is almost full price at $16.99 for some reason."""
tokenized_text = sent_tokenize(text)
print(tokenized_text)

# Word Tokenization
tokenized_word = word_tokenize(text)
print(tokenized_word)

# Stopwords
print(stop_words)
filtered_sent = []
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:", tokenized_text)
print("Filtered Words", filtered_sent)

# Lexicon Normalization (Stemming) - reduces words to their root word, or chops off the derivational affixes.
ps = PorterStemmer()
stemmed_words = []
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))
print("Filtered Words:", filtered_sent)
print("Stemmed Sentence:", stemmed_words)

# Lexicon Normalization (Lemmatization) - reduces words to their base word, which is linguistically correct lemmas.
lemma_words = []
for w in filtered_sent:
    lemma_words.append(lem.lemmatize(w, "v"))
print("Lemmatized Words:", lemma_words)

# PoS Tag
tagged_data = nltk.pos_tag(tokenized_word)
print(tagged_data)
# get adjectives
adjectives = []
for index, tuple in enumerate(tagged_data):
    element_one = tuple[0]
    element_two = tuple[1]
    if element_two == "JJ":
        adjectives.append(element_one)
adjectives_non_numerical = list(filter(('first').__ne__, adjectives))
print(adjectives_non_numerical)

# Frequency Distribution
fdist = FreqDist(adjectives_non_numerical)
print(fdist)
print(fdist.most_common(10))

fdist.plot(30, cumulative=False)
plt.show()
