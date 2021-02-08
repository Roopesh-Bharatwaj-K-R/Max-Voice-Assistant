# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:19:05 2020

@author: user
"""

# -- coding: utf-8 --
"""
Created on Sat Dec 26 20:14:35 2020

@author: Yukki
"""

import speech_recognition as sr
import pyttsx3 # pip install pyttsx3
import pyaudio #conda install PyAudio
import pywhatkit # for online search/play
import datetime
#from temperature import temp
import wikipedia # pip install wikipedia
#import pyjokes # pip install pyjokes 

listener = sr.Recognizer() # for sr

engine =pyttsx3.init()# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:19:05 2020

@author: user
"""

# -- coding: utf-8 --
"""
Created on Sat Dec 26 20:14:35 2020

@author: Yukki
"""

import speech_recognition as sr
import pyttsx3 # pip install pyttsx3
import pyaudio #conda install PyAudio
import pywhatkit # for online search/play
import datetime
#from temperature import temp
import wikipedia # pip install wikipedia
#import pyjokes # pip install pyjokes 

listener = sr.Recognizer() # for sr

engine =pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
 
    #engine.say("Sure, I will help you with that !!!")
    engine.say(text)
    engine.runAndWait()
def to_speak():
    try:
        with sr.Microphone() as source:
            print('listening.....!')
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            # for specific command with starting 'max'
            command = command.lower()
            if 'max' in command:
                command = command.replace("max","")
               # engine.say
                print(command)
    except:
        print("pass")
    return command
def run_max():
    command = to_speak()
    print(command)
    if "play" in command:#
        song= command.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I : %M  %p')
        talk('The current time is'+time)
        print(time)
    
        # WIKIPEDIA
    elif "wikipedia" in command or "what is" or "tell about" or"how is" or "who is" in command:
        wiki= command.replace("wikipedia","")
        wiki =command.replace("what is", "")
        wiki =command.replace("tell about","")
        wiki =command.replace("how is", "")
        wiki=command.replace("who is","")
        info =wikipedia.summary(wiki, 3)
        talk(info)
        print(info)
        # GENERAL ENQUIRY
    elif "how are you " or "Hi Max, How are you " or"Hey Max, How are you" or  "How are you doing" in command:
        person=  ("Hi, I'm Good, How are you doing ")
        talk(person)
        print(person)
        if "im very fine" or "im very good" or "i'm great" in command:
            person1= ("Thats nice to know about you and you are welcome")
            talk(person1)
            print(person1)
    if "what is Max" or "who is Max  " in command:
        answer = ("My name is Max")
        talk(answer)
        print(answer)
    elif "Shall we go for date" or "can i date you" in command : 
        talk("Sorry about that ")   
    elif "Are you married" or "are you single" in command:
        talk("Sorry i can not answer this but i have relationship with the internet ")
    if "who created you" or "where were you born" or "who Made you" or "who are you" in command:
        answer1 =(" I was created at the Favour Labarotory on 26th December, 2020. at Athlone, Ireland,  My current Version is : 1.  On Trial Basis of Advanced  Speech Recognition  of MAX - Developed by the DeepNet Corporation.  ")
        talk (answer1)
        print(answer1)
   #elif"Tell me a joke" in command:
        #talk(pyjokes.get_joke(language= 'en', category ='neutral'))
while True:
   run_max()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
 
    #engine.say("Sure, I will help you with that !!!")
    engine.say(text)
    engine.runAndWait()
def to_speak():
    try:
        with sr.Microphone() as source:
            print('listening.....!')
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            # for specific command with starting 'max'
            command = command.lower()
            if 'max' in command:
                command = command.replace("max","")
               # engine.say
                print(command)
    except:
        print("pass")
    return command
def run_max():
    command = to_speak()
    print(command)
    if "play" in command:#
        song= command.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I : %M  %p')
        talk('The current time is'+time)
        print(time)
    
        # WIKIPEDIA
    elif "wikipedia" in command or "what is" or "tell about" or"how is" or "who is" in command:
        wiki= command.replace("wikipedia","")
        wiki =command.replace("what is", "")
        wiki =command.replace("tell about","")
        wiki =command.replace("how is", "")
        wiki=command.replace("who is","")
        info =wikipedia.summary(wiki, 3)
        talk(info)
        print(info)
        # GENERAL ENQUIRY
    elif "how are you " or "Hi Max, How are you " or"Hey Max, How are you" or  "How are you doing" in command:
        person=  ("Hi, I'm Good, How are you doing ")
        talk(person)
        print(person)
        if "im very fine" or "im very good" or "i'm great" in command:
            person1= ("Thats nice to know about you and you are welcome")
            talk(person1)
            print(person1)
    if "what is Max" or "who is Max  " in command:
        answer = ("My name is Max")
        talk(answer)
        print(answer)
    elif "Shall we go for date" or "can i date you" in command : 
        talk("Sorry about that ")   
    elif "Are you married" or "are you single" in command:
        talk("Sorry i can not answer this but i have relationship with the internet ")
    if "who created you" or "where were you born" or "who Made you" or "who are you" in command:
        answer1 =(" I was created at the Favour Labarotory on 26th December, 2020. at Athlone, Ireland,  My current Version is : 1.  On Trial Basis of Advanced  Speech Recognition  of MAX - Developed by the DeepNet Corporation.  ")
        talk (answer1)
        print(answer1)
   #elif"Tell me a joke" in command:
        #talk(pyjokes.get_joke(language= 'en', category ='neutral'))
while True:
   run_max()