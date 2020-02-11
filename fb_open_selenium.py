from selenium import webdriver
from collections import OrderedDict
import pandas as pd


browser= webdriver.Chrome("E:\Driver\chromedriver.exe")

browser.get("https://m.facebook.com/?_rdr")

fb_id=browser.find_element_by_name("email")
fb_id.send_keys("mohit121993@gmail.com")

fb_pass=browser.find_element_by_name("pass")
fb_pass.send_keys("xxyyzz")  #your password

login=browser.find_element_by_name("login")
login.click()

ok=browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[2]/form/div/button')
ok.click()

