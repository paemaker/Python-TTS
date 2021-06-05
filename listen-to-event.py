# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:53:01 2020

@author: THIS PC
"""

import pyttsx3

def onStart(name):
   print('starting', name);
   
def onWord(name, location, length):
   print('word', name, location, length);
   
def onEnd(name, completed):
   print('finishing', name, completed);
   
engine = pyttsx3.init();
engine.connect('started-utterance', onStart);
engine.connect('started-word', onWord);
engine.connect('finished-utterance', onEnd);
engine.say('The quick brown fox jumped over the lazy dog.');
engine.runAndWait();

