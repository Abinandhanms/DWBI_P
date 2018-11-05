from selenium import webdriver
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uRep
import re
from Writecsv import WriteCsv as w
from Writecsv import WriteHeader as h

df = pd.read_csv('D:\\MS\\DWBI\\Project\\Dataset2\\inp.csv')
URL = 'https://play.google.com/store/apps?hl=en'
h('Application Name','Reviews','URL')
#print(df['App'])

for index,row in df.iterrows():
 #print(row['App'])
 #getting application name
 STitle=(row['App'])

#chrome driver path
 Chromedriver='C:\\Users\\Abinandhan\\PycharmProjects\\DWBI\\chromedriver.exe'

#creating instances of Chrome
 driver=webdriver.Chrome(Chromedriver)

#Main Url
 driver.get(URL)

#searching the application using names
 elem = driver.find_element_by_css_selector('#gbqfq')
 elem.send_keys(str(STitle))
 sleep(1)
 elem.submit()

#Searching Url
 curl=driver.current_url
 driver.get(curl)
 #print("Search URL:"+curl)


 #Navigating to Correct Application
 try:
    driver.find_element_by_link_text(str(STitle)).click()
    AppUrl=driver.current_url

    #printing Application Details
    #print("Application Name:"+ STitle)
    #print("Application URL:" + AppUrl)

    try:
           driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/div[2]')

           #Reqest module starts here
           uClient = uRep(str(AppUrl))
           page_html = uClient.read()
           uClient.close()

           #BS4
           page_soup = soup(page_html, "html.parser")
           #print(page_soup.prettify())

           # Regex
           Pattern = ('5,null,\"(.*?)\",\[+')
           l = re.compile(Pattern)
           Details = l.findall(str(page_soup))
           driver.close()

           for Review in Details:
                #print("------------------------------------------")
                #print("AppName:" + STitle)
                #print("Details:" + Review)
                #print("------------------------------------------")
                w(STitle,Review,AppUrl)


    except Exception:
            print("No Reviews for this App")
            w(STitle,'N/A',AppUrl)
            driver.close()

 except Exception:
            print("No such Apps in the name "+STitle +" in Play Store")
            w(STitle)
            driver.close()
