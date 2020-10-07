#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quora Web Scraper

Created on Wed Oct  7 19:02:18 2020

@author: JonNixonCodes
"""
# %% Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# %% Define constants
QUORA_URL = "https://www.quora.com"

# %% Define Scraper
class Scraper:
    
    def __init__(self, url=QUORA_URL):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        input("\tWaiting for user login...\n\tEnter to continue\n")
    
    def goto_topic(self, topic):
        url = QUORA_URL + "/topic/" + topic
        self.driver.get(url)
    
    def scrape_questions(self):
        elems_l = \
            self.driver.find_elements_by_class_name("puppeteer_test_question_title")
        questions_l = [item.text for item in elems_l if "?" in item.text]
        return questions_l
    
    def close(self):
        self.driver.close()

