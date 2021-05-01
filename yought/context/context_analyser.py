#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Context Analyser

Created on Tue Nov 24 18:40:39 2020

@author: JonNixonCodes
"""
# %% Import libraries
import spacy
from spacy.matcher import Matcher
from textblob import TextBlob

# %% Analyser definition    
class ContextAnalyser():
    """Analyse context of text"""
    
    SUBJ_PATTERN = [{"DEP":"poss","OP":"?"},{"POS":"ADJ","OP":"?"},{"DEP":"nsubj"}]
    VB_PATTERN = [{"DEP":{"NOT_IN":["nsubj"]},"OP":"*"},{"POS":"VERB"}]
    OBJ_PATTERN = [{"DEP":"det","OP":"?"},{"POS":"ADJ","OP":"?"},{"DEP":"dobj"}]
    SVO_PATTERN = SUBJ_PATTERN + VB_PATTERN + OBJ_PATTERN
    
    def __init__(self):
        """Initialise Analyser"""
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = Matcher(self.nlp.vocab)
        self.matcher.add("subj_phrase", None, self.SUBJ_PATTERN)
        self.matcher.add("svo_phrase", None, self.SVO_PATTERN)
        return
    
    def extract_entities(self, text):
        """Extract entities from text"""
        doc = self.nlp(text)
        matches = self.matcher(doc)
        entities_l = []
        for match_id, start, end in matches:
            if self.nlp.vocab.strings[match_id] == "subj_phrase":
                span = doc[start:end]
                entities_l.append(span)
        return entities_l
    
    def extract_themes(self, text):
        """Extract themes from text"""
        doc = self.nlp(text)
        matches = self.matcher(doc)
        themes_l = []
        for match_id, start, end in matches:
            if self.nlp.vocab.strings[match_id] == "svo_phrase":
                blob = TextBlob(doc[start:end].text)
                theme = {'text':blob.raw,
                         'polarity':blob.sentiment.polarity,
                         'subjectivity':blob.sentiment.subjectivity}
                themes_l.append(theme)
        return themes_l        
    
    def extract_sentiment(self, text):
        """Extract sentiment from text"""
        blob = TextBlob(text)
        sentiment = {'text':text,
                     'polarity':blob.sentiment.polarity,
                     'subjectivity':blob.sentiment.subjectivity}
        return sentiment
        