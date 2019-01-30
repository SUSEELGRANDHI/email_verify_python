from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from bs4 import BeautifulSoup
import re
import random,time
import pymongo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


emailList=[]
phoneList=[]
idz = ''

emailList,phoneList =[],[]
chrome_options = Options()
#chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
global driver,i
i = 1

def scrape(driver):
    pageAdd=driver.page_source
    soup=BeautifulSoup(pageAdd,"lxml")
    pageResult=soup.find_all("div",{"class":"result results_links_deep highlight_d"})
    for item in pageResult:
        searchString=item.get_text()
        emailAdd=re.findall('[A-Za-z]+@\S+.com', searchString)
        emailList.extend(re.findall('[A-Za-z]+@\S+.com', searchString))

    try :
        nextButton=driver.find_element_by_xpath("//a[@class='result--more__btn btn btn--full']")
        nextButton.click()
        driver.implicitly_wait(3)
        #time.sleep(random.uniform(20,30))
        scrape(driver)
    except NoSuchElementException:
        print("scraping over")


def get_emails_duck(doc):
        print("duckduckgo")
        del emailList[:]
        driver=webdriver.Chrome(executable_path='/home/ec2-user/chromedriver',chrome_options=chrome_options)
        url = "https://duckduckgo.com/?q="+doc+"+email&t=hi&ia=web"
        driver.get(url)
        scrape(driver)
        driver.quit()
        return list(set(emailList))

    
