import re
from Writecsv import AppDetails as A
from bs4 import BeautifulSoup as soup

def ContentR(page_html):
    CategoryD = page_html
    print(CategoryD)
    Pattern = ('<meta itemprop=\"contentRating\" content=\"(.*?)\"\/>')
    l = re.compile(Pattern)
    Details = l.findall(str(CategoryD))

    for C in Details:
       print("Content Rating:"+C)
       A(C)