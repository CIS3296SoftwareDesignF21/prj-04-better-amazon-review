from selectorlib import Extractor
import requests
from pprint import pprint
import sys
import json
from time import sleep
import csv
from dateutil import parser as dateparser

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
    #print("Downloading %s" % url)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n" % url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d" % (url, r.status_code))
        return None
    # Pass the HTML of the page and create

    return e.extract(r.text)

def removeInvalidEntries(dict):
    for key, value in list(dict.items()):
        if (value == 'NA'):
            del dict[key]

def scrapeReviews(outFile,urlDict):
        csvFile = open(outFile, 'w')
        writer = csv.DictWriter(csvFile, fieldnames=["title","content","date","variant","images","verified","author","rating","product","url"],quoting=csv.QUOTE_ALL)
        writer.writeheader()
        x = 0
        for key in urlDict:
            url = urlDict[key]
            data = scrape(url,'selectors.yml')
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


#url = "https://www.amazon.com/gp/new-releases/books/1/ref=s9_acsd_onr_hd_bw_b1_clnk/ref=s9_acsd_onr_hd_bw_b1_c2_x_c2cl?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-11&pf_rd_r=3GDZW2R1F73HA683JN2S&pf_rd_t=101&pf_rd_p=4ffa09bb-694b-53c6-8154-5083807b8fdf&pf_rd_i=1"


url = str(sys.argv[1])
data = scrape(url, 'bookURL.yml')
urlDict = {}


if data:
    i = 0
    for books in data['books']:
        '''
        if i == 4:
            pprint(urlDict)
            break
        '''
        bookTitle = books['title']
        urlDict[bookTitle] = "https://www.amazon.com" + books['url']
        reviewURL = urlDict.get(bookTitle)
        reviewData = scrape(str(reviewURL),'reviewURLS.yml')
        #pprint(reviewURL)
        if reviewData:
            try:
                urlDict[bookTitle] = "https://www.amazon.com" + reviewData['productPages']['url']
            except TypeError:
                urlDict[bookTitle] = 'NA'
                

        i = i + 1
outfile = 'bookData.csv'
removeInvalidEntries(urlDict)
pprint(urlDict)
scrapeReviews(outfile,urlDict)


