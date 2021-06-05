# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:55:08 2020

@author: THIS PC
"""

import pyttsx3

def onWord(name, location, length):
   print('word', name, location, length);
   
   if location > 10:
      engine.stop();
      
engine = pyttsx3.init();
engine.connect('started-word', onWord);

engine.say('The quick brown fox jumped over the lazy dog.');
engine.runAndWait();

'''
# Chaning voices
engine = pyttsx3.init();
voices = engine.getProperty('voices');

for voice in voices:
   engine.setProperty('voice', voice.id);
   engine.say('The quick brown fox jumped over the lazy dog.');
engine.runAndWait();
'''
'''
# Chaning speech rate to faster or slower
engine = pyttsx3.init();
rate = engine.getProperty('rate');

engine.setProperty('rate', rate + 50);
engine.say('The quick brown fox jumped over the lazy dog.');
engine.runAndWait();
'''