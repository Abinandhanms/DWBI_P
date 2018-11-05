import re
from Writecsv import AppDetails as A
from bs4 import BeautifulSoup as soup

def Details(Title,page_soup):

    Details = {}
    #print(D)

    CategoryD = page_soup.findAll('span', {'class': 'T32cc UAO9ie'})
    # print(CategoryD)
    Pattern = ('itemprop=\"genre\">(.*?)<\/a><\/span>')
    l = re.compile(Pattern)
    caterogy = l.findall(str(CategoryD))

    for c in caterogy:
        #print("Catogery:" + c)
        #Details.append(c)
        Details['Category']=c
        #print(Details)

    ContainersR = page_soup.findAll('div', {'class': 'BHMmbe'})
    # print(Containers)
    Pattern = ('class=\"BHMmbe\">(.*?)<\/div>\]+')
    l = re.compile(Pattern)
    Rating = l.findall(str(ContainersR))

    for r in Rating:
        #print("Rating:" + r)
        #Details.append(r)
        Details['Rating'] =r

    CategoryS = page_soup.findAll('div', {'class': 'hAyfc'})
    # print(CategoryD)
    Pattern = ('Size<\/div><span class=\"htlgb\"><div><span class=\"htlgb\">(.*?)<\/span>')
    l = re.compile(Pattern)
    size = l.findall(str(CategoryS))

    for s in size:
        #print("Size:" + s)
        #Details.append(s)
        Details['Size'] = s

    CategoryI = page_soup.findAll('div', {'class': 'hAyfc'})
    # print(CategoryD)
    Pattern = ('Installs<\/div><span class=\"htlgb\"><div><span class=\"htlgb\">(.*?)<\/span>')
    l = re.compile(Pattern)
    installs = l.findall(str(CategoryI))


    for i in installs:
        #print("Size:" + i)
        #Details.append(i)
        Details['Installs'] = i

    A(Title,Details['Category'],Details['Rating'],Details['Size'],Details['Installs'])


