# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:30:54 2020

@author: THIS PC
"""

from gtts import gTTS
import playsound
import os
    
while 1:
    text = input("Input Text:")
    tts = gTTS(text=text,lang='th')
    tts.save('freak.mp3')
    playsound.playsound('freak.mp3', True)
    os.system('freak.mp3')