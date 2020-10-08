#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quora Web Scraper

Created on Wed Oct  7 19:02:18 2020

@author: JonNixonCodes
"""
# %% Import libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# %% Define constants
QUORA_URL = "https://www.quora.com"
SCROLL_PAUSE_TIME = 0.5

# %% Define Scraper
class Scraper:
    
    def __init__(self, url=QUORA_URL):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        input("\tWaiting for user login...\n\tEnter to continue\n")
    
    def goto_topic(self, topic):
        url = QUORA_URL + "/topic/" + topic
        self.driver.get(url)
    
    def scroll_to_bottom(self, timeout=SCROLL_PAUSE_TIME):
        # Get scroll height
        start_height = self.driver.execute_script("return document.body.scrollHeight")
        # Execute scroll
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    
        # Wait to load page
        time.sleep(timeout)
        # Get new scroll height
        end_height = self.driver.execute_script("return document.body.scrollHeight")
        if start_height == end_height:
            print("Bottom of webpage reached")
            return False
        return True
        
    def scrape_questions(self):
        elems_l = \
            self.driver.find_elements_by_class_name("puppeteer_test_question_title")
        questions_l = [item.text for item in elems_l if "?" in item.text]
        return questions_l
    
    def close(self):
        self.driver.close()

# %% Example script
# scraper = quora_scraper()
# scraper.goto_topic("Computer-Science")
# for i in range(100):
#     while scraper.scroll_to_bottom(random.randrange(1,5)) == True:
#         if i%10==0:
#             questions_l = scraper.scrape_questions()
#         questions_l = scraper.scrape_questions()