from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AccountVerify:

    def __init__(self,address):
        self.address = address
        self.url = "/Users/macbook/Desktop/email_verify_python/phantomjs-2.1.1-macosx/bin/phantomjs"
        self.driver = webdriver.PhantomJS(executable_path = self.url)
        self.yahoolink = "https://login.yahoo.com/config/login_verify2?MsgId=8934_0_1252_1721_9103_0_67_428&.src=ym&.intl=us"
        self.outlook = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1540886182&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3da9e68d0f-e99e-2082-2698-11c4e8bf0cba&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"

    def yahoo_verification(self):
        print("yahoo")
        self.driver.get(self.yahoolink)
        self.driver.find_element_by_id("login-username").send_keys(self.address)
        self.driver.find_element_by_id("login-signin").click()
        try:
            WebDriverWait(self.driver,8).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-passwd']")))
            self.driver.find_element_by_xpath("//input[@id='login-passwd']")
            self.driver.quit()
            return True
        except TimeoutException:
            self.driver.quit()
            return False

    def outlook_verification(self):
         self.driver.get(self.outlook)
         self.driver.find_element_by_id("i0116").send_keys(self.address)
         self.driver.find_element_by_id("idSIButton9").click()
         try:
             WebDriverWait(self.driver,8).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='displayName']")))
             self.driver.find_element_by_xpath("//div[@id='displayName']")
             self.driver.quit()
             return True
         except TimeoutException:
             self.driver.quit()
             return False

    def gmail_verification(self):
         self.driver.get('https://mail.google.com/mail/u/0/#inbox')
         self.driver.find_element_by_id('identifierId').send_keys(self.address)
         self.driver.find_element_by_id('identifierNext').click()
         self.driver.implicitly_wait(1)
         try:
             WebDriverWait(self.driver,8).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='passwordNext']")))
             self.driver.find_element_by_xpath("//div[@id='passwordNext']")
             self.driver.quit()
             return True
         except TimeoutException:
             self.driver.quit()
             return False



    def check_through_all(self):
        response = self.gmail_verification()
        if response == False:
            self.driver = webdriver.PhantomJS(executable_path = self.url)
            response = self.outlook_verification()
            if response == False:
                 self.driver = webdriver.PhantomJS(executable_path = self.url)
                 response = self.yahoo_verification()
        return response
