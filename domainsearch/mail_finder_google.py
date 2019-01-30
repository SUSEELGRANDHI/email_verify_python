from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from bs4 import BeautifulSoup
import re
import random,time
import pymongo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options



idz = ''

emailList = []
chrome_options = Options()
#chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
global driver,i
i = 1

def scrape(driver): 
    pageAdd=driver.page_source
    soup=BeautifulSoup(pageAdd,"lxml")
    pageResult=soup.find("div",{"id":"rso"})
    searchResult=pageResult.findAll("div",{"class":"srg"})
    for item in searchResult:
        searchString=item.get_text()
        emailAdd=re.findall('[A-Za-z]+@\S+.com', searchString)
        emailList.extend(re.findall('[A-Za-z]+@\S+.com', searchString))
    try:
        nextButton=driver.find_element_by_id("pnnext")
        nextButton.click()
        driver.implicitly_wait(3)
        scrape(driver)
    except:
        print("Scrapping is complete Boss")
        print(emailList)


def get_emails_google(doc):
        print("google")
        del emailList[:]
        driver=webdriver.Chrome(executable_path='/home/ec2-user/chromedriver',chrome_options=chrome_options)
        driver.get("https://www.google.com/")
        searchBox=driver.find_element_by_name("q")
        searchBox.send_keys('"'+doc+'" email')
        searchBox.submit()
        scrape(driver)
        driver.quit()
        return list(set(emailList))


    
