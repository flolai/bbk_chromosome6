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
    driver.get("http://www.google.com")
    search_form = driver.find_element(By.TAG_NAME, "form")
    search_box = search_form.find_element(By.NAME, "q")
    search_box.send_keys("webdriver")
  
    for e in search_form:
        print (e.text)