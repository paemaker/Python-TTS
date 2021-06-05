# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:45:31 2020

@author: THIS PC
"""

import pyttsx3
engine = pyttsx3.init();

TH_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI";

text = input('Enter your sentence : ');
engine.setProperty('rate', 100);
# Heenging.setProperty('voice', TH_voice);
engine.say(text);

engine.runAndWait();