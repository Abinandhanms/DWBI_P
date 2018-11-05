from selenium import webdriver
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uRep
from Details import Details as D
from Writecsv import WriteHeaderD as W



df=pd.read_csv("D:\\MS\\DWBI\\Project\\Dataset2\\inp.csv")
URL="https://play.google.com/store/apps?hl=en"

#print(df['App'])
W()

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


    #Reqest module starts here
    uClient = uRep(str(AppUrl))
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    #print(page_soup)

    ######################Rating#############################
    D(STitle,page_soup)
    driver.close()
    #print("Details of "+STitle)


 except Exception:
  print("No such Apps in the name "+STitle +" in Play Store")
  driver.close()
