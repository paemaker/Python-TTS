# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:50:06 2020

@author: THIS PC
"""

import pyttsx3

engine = pyttsx3.init();
#engine.save_to_file('Hello World' , 'test.mp3');
engine.save_to_file('Chan rak khun mark mark', 'test.mp3');
engine.runAndWait();