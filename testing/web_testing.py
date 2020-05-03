#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:22:18 2020

@author: florence
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    first_result = driver.get("http://student.cryst.bbk.ac.uk/~az001/search.html")
    #driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    #first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
    print(first_result.get_attribute("textContent"))
  