from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import smtplib,dns
from dns import resolver
import re,random
import socket


weight = 0
def emailVerifier(email_address):
    #step 1
    addressToVerify = email_address
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    if match == None:
        print('Bad Syntax in ' + addressToVerify)
        raise ValueError('Bad Syntax')
    else:
        weight = random.uniform(20.0,30.0)


    #step 2 get the mx record(available record name)
    domain_name = email_address.split('@')[1]
    try:
        records = resolver.query(domain_name, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        host = socket.gethostname()
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mxRecord)
        server.helo(host)
        server.mail('me@domain.com')
        code, message = server.rcpt(str(addressToVerify))
        server.quit()
        if code == 250:
            weight = checkUsername(addressToVerify)
            if weight >= 85:
               return [{'status':"verified"},{'confidence':weight}]
            else:
                return [{'status':"not verified"},{'confidence':weight}]
        else:
            weight = random.uniform(55.0,65.0)
            return [{'status':"not verified"},{'confidence':weight}]
    except resolver.NXDOMAIN:
       weight =  random.uniform(40.0,50.0)
       return [{'status':"not verified"},{'confidence':weight}]


def checkUsername(addressToVerify):
    driver = webdriver.PhantomJS(executable_path = '/Users/standarduser/Documents/pratha/phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.get('https://mail.google.com/mail/u/0/#inbox')
    #WebDriverWait(driver,500).until(EC.presence_of_element_located((By.CLASS_NAME,'aXBtI Wic03c')))
    driver.find_element_by_id('identifierId').send_keys(addressToVerify)
    driver.find_element_by_id('identifierNext').click()
    driver.implicitly_wait(1)
    try:
        text = "try again with that email"
        k = driver.find_element_by_xpath('//div[contains(text(), "' + text + '")]')
        return random.uniform(65.0,75.0)
    except NoSuchElementException:
        driver.quit()
        return random.uniform(85.0,99.0)
    driver.quit()
