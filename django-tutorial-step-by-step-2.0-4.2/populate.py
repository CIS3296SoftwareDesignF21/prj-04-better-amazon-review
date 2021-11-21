import pandas as pd
import sqlite3

conn = sqlite3.connect('book_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE reviews (title text, content text, date text, variant text, images text, verified text, author text, rating int, product text, url text, ISBN text, reviewID text)''')
reviews = pd.read_csv('bookData4.csv')
reviews.to_sql('reviews', conn, if_exists='append', index=False)
