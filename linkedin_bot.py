# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:40:10 2020

@author: Raja
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:29:41 2020

@author: Raja
"""
from selenium import webdriver #connect python with webbrowser-chrome
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
import time



def login():
 username = driver.find_element_by_id("username")
 username.send_keys("your_email")
 password = driver.find_element_by_id("password")
 password.send_keys("your_password")
 log_in=driver.find_element_by_xpath("//*[@type='submit']")
 log_in.click()
 print("successfully logged in")
 
def network():
 try:
   driver.find_element_by_id("mynetwork-tab-icon").click()

   time.sleep(3)
   
 except:
   print("[+] Some Error Occoured \n Directly opening networks tab")
   body = driver.find_element_by_tag_name("body")
   body.send_keys(Keys.CONTROL + "t")
   driver.get(nurl)
   
   time.sleep(2)

def connect():

 for i in range(0,5):
   time.sleep(4)  
   pag.click(760,600)
   time.sleep(2)
   driver.find_element_by_class_name("pv-s-profile-actions").click()
   time.sleep(2)
   pag.click(1090,400)
   
   #driver.find_element_by_class_name('mr1').click()
   #time.sleep(3)
   customMessage="Hello, I have found your area of interest and my area of interest same and it would be my pleasure connecting with u!"
   messageID=driver.find_element_by_id('custom-message')
   messageID.send_keys(customMessage)
   time.sleep(2) 
   driver.find_element_by_class_name('ml1').click()
   time.sleep(1)
   
   
   
   print("["+str(i)+"] Connection request sent ")
   pag.click(35,60)
 print("done")

url = "http://linkedin.com/login"
nurl = "http://linkedin.com/mynetwork/"
driver = webdriver.Chrome('C:\\Windows\\chromedriver.exe')
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get(url)
login()
network()
connect()
  
