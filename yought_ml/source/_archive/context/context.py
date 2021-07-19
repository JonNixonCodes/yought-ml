#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Context

Created on Tue Feb  2 01:08:45 2021

@author: JonNixonCodes
"""
# %% Import libraries
from .context_analyser import ContextAnalyser

# %% Context definition
class Context():
    """Object containing contextual analysis of text"""
    
    def __init__(self, text):
        self.text = text
        self.analyser = ContextAnalyser()
        self.entities = self.analyser.extract_entities(self.text)
        self.themes = self.analyser.extract_themes(self.text)
        self.sentiment = self.analyser.extract_sentiment(self.text)