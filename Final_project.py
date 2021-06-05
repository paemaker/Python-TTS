# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:56:04 2020

@author: THIS PC
"""

import os
import tkinter as tk
from langdetect import detect
from tkinter import filedialog 
from gtts import gTTS

# New window and assign to new variable
app = tk.Tk();

# Window title
app.title('Text To Speech by CS-VIP');
app.resizable(width = False, height = False);

# Label at the top of window
header = tk.Label(text = 'Text To Speech using Python', fg = '#373a40', bg = '#eeeeee', width = '30', font = (50));
header.pack();

# Label for input
label_input = tk.Label(text = 'Input word(s) or sentence(s)');
label_input.pack();

# Text box
text_box = tk.Text(bd = 5, width = 50, height = 10);
text_box.pack();

# Frame
frame_btn = tk.Frame();
frame_btn.pack(ipadx = 10, ipady = 10);

# Text To Speech using text from input
def tts_text():
    try:
        
        # Read text from input and set to UPPERCASE
        language = detect(text_box.get(1.0, tk.END));
        language = language.upper();
        print(language);
        print(text_box.get(1.0, tk.END));
        
        # -1c is to delete 1  character before end
        tts_text = gTTS(text = text_box.get(1.0, tk.END + "-1c"), lang = language);
        tts_text.save('tts_text_' + language + '.mp3');
        os.system('tts_text_' + language + '.mp3');
        
        # Save text from input as a file
        save_file = open('tts_text_' + language + '.txt', 'w');
        save_file.write(text_box.get(1.0, tk.END));
        save_file.close();
        
        done_btn = tk.Button(text = 'TTS text is done!\n This language is "' + language + '"', fg = 'green', command = lambda: done_btn.pack_forget());
        done_btn.pack(pady = 10);
        
    except:
        error_btn = tk.Button(text = 'Can\'t detect what language it is \n Click to close', fg = 'red', command = lambda: error_btn.pack_forget());
        error_btn.pack(pady = 10);
    
# Text To Speech using text from uploading file
def tts_file():  
    try:
        
        # Get path of the file
        path = filedialog.askopenfilename(initialdir = "/", 
        title = 'Select a File', filetypes = (('Text files', '*.txt*'), ('all files', '*.*'))); 
        
        # Read path
        file = open(path, 'r', encoding = 'utf-8', errors = 'ignore').read().replace('\n', ' ');
        language = detect(file);
        language = language.upper();
        print(language);
        print(file);
        
        # Insert text from a file to display in input
        text_box.insert('1.0', file);
        
        tts_file = gTTS(text = str(file), lang = language);
        tts_file.save('tts_file_' + language + '.mp3');
        os.system('tts_file_' + language + '.mp3');
        
        done_btn = tk.Button(text = 'TTS file is done!\n This language is "' + language + '"', fg = 'green', command = lambda: done_btn.pack_forget());
        done_btn.pack(pady = 10);
        
    except:
        error_btn = tk.Button(text = 'Can\'t detect what language it is \n Click to close', fg = 'red', command = lambda: error_btn.pack_forget());
        error_btn.pack(pady = 10);
    
# Speaking button
spekaing_btn = tk.Button(master = frame_btn, text = 'Make some noise!', width = 20, command = tts_text);
spekaing_btn.pack(side = tk.LEFT, padx = 10);

# Browsing button
browsing_btn = tk.Button(master = frame_btn, text = 'Browse Files', width = 20, command = tts_file);
browsing_btn.pack(side = tk.RIGHT, padx = 10);

# Run Tkinter and listen to event
app.mainloop();

def liber():
    try: 
        ?
    except: 
        unacceptable