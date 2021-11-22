from selectorlib import Extractor
import requests
from pprint import pprint
import sys
import json
from time import sleep
import csv
from dateutil import parser as dateparser


class Book:
    def __init__(self, title, productPage, reviewPage, isbn, reviewLinks):
        self.title = title
        self.productPage = productPage
        self.reviewPage = reviewPage
        self.isbn = isbn
        self.reviewLinks = reviewLinks

    def toString(self):
        if(self.title is not None):
            print("Title: " + self.title)
        else:
            print("Title: None")
        if(self.productPage is not None):
            print("ProductPage: " + self.productPage)
        else:
            print("ProductPage: None")
        if(self.reviewPage is not None):
            print("ReviewPage: " + self.reviewPage)
        else:
            print("ReviewPage: None\n")
        if (self.isbn is not None):
            print("ISBN: " + self.isbn +'\n')
        else:
            print("ISBN: None\n")


def scrape(url, configFile):
    e = Extractor.from_yaml_file(configFile)
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    r = requests.get(url, headers=headers)

    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, r.status_code))
        return None
    # Pass the HTML of the page and create

    return e.extract(r.text)


def getPermaLink(url):
    data = scrape(url, "permaLink.yml")
    return data['permaLink']


def cleanPermaLink(url):
    link = url.split('/')
    return link[4]


def reviewLinks(url):
    links = []
    i = 0
    if(url is None):
        return links
    else:
        for i in range(9):
            if (i == 0):
                try:
                    data = scrape(url, 'nextPage.yml')
                    if (data['nextPage'] is not None):
                        nextPage = "https://www.amazon.com" + data['nextPage']
                    else:
                        return links
                except AttributeError or TypeError:
                    return links
            else:
                try:
                    data = scrape(links[i - 1], 'nextPage.yml')
                    if (data['nextPage'] is not None):
                        nextPage = "https://www.amazon.com" + data['nextPage']
                    else:
                        return links
                except AttributeError or TypeError:
                    return links
            links.append(nextPage)

    return links


def scrapeReviews(outFile, bookList):
    # bookList used to be dictionary field urlDict
    csvFile = open(outFile, 'w')
    writer = csv.DictWriter(csvFile,
                            fieldnames=["title", "content", "date", "variant", "images", "verified", "author", "rating",
                                        "product", "url"], quoting=csv.QUOTE_ALL)
    writer.writeheader()
    # for key in urlDict:
    for book in bookList:
        reviePageLinks = bookList[book].reviewLinks()
        for link in reviewPageLinks:
            # url = urlDict[key]
            url = bookList[book].reviewPage()
            data = scrape(url, 'selectors.yml')
            pprint(data)
            if data:
                try:
                    for r in data['reviews']:
                        r["product"] = data["product_title"]
                        r['url'] = url
                        r['verified'] = 'Yes'
                        try:
                            r['rating'] = r['rating'].split(' out of')[0]
                        except AttributeError or TypeError:
                            r['rating'] = 'NA'
                        try:
                            date_posted = r['date'].split('on ')[-1]
                        except AttributeError or TypeError:
                            date_posted = 'NA'
                        if r['images']:
                            r['images'] = "\n".join(r['images'])
                        r['date'] = dateparser.parse(date_posted).strftime('%d %b %Y')
                        writer.writerow(r)
                except TypeError or AttributeError:
                    print('error:  ' + url)


def main():
    url = "https://www.amazon.com/gp/new-releases/books/1/ref=s9_acsd_onr_hd_bw_b1_clnk/ref=s9_acsd_onr_hd_bw_b1_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-11&pf_rd_r=3GDZW2R1F73HA683JN2S&pf_rd_t=101&pf_rd_p=4ffa09bb-694b-53c6-8154-5083807b8fdf&pf_rd_i=1"
    # url = str(sys.argv[1])
    data = scrape(url, 'bookURL.yml')
    bookList = []
    if data:
        i = 0
        for books in data['books']:
            '''
            if i == 2:
                for i in range(len(bookList)):
                    bookList[i].toString()
                break
            '''
            title = books['title']
            url = "https://www.amazon.com" + books['url']
            reviewData = scrape(str(url), 'reviewURLS.yml')
            if reviewData:
                try:
                    reviewURL = "https://www.amazon.com" + reviewData['productPages']['url']
                except TypeError:
                    reviewURL = None
                try:
                    isbn = reviewData['isbn']
                    isbn = reviewData['isbn2']
                except TypeError:
                    isbn = None

            book = Book(title, url, reviewURL, isbn, reviewLinks(reviewURL))
            if(reviewURL is not None and isbn is not None):
                book.toString()
                bookList.append(book)


            #i = i + 1
def runScrape(url):
    outfile = 'bookData.csv'
    scrapeReviews(outfile, urlDict)

runScrape()


#main()


