from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as ttx
import sys
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import numpy
import subprocess
import webbrowser
import winapps
from googlesearch import search

recognizer = speech_recognition.Recognizer()

speaker = ttx.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)
speaker.setProperty('rate',180)

todo_list=[]

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=0.5)
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            return "None"
        return statement
    
def create_note():
    global recognizer
    speaker.say("What do you want to add to your note")
    speaker.runAndWait()

    done=False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("choose a file name!")
                speaker.runAndWait()
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio,language='en-in')
                filename = filename.lower()
            with open(f"{filename}.txt",'a') as f:
                f.write(note)
                speaker.say("Do you want to add to do list to this note")
                speaker.runAndWait()
                statement = takeCommand().lower()
                if statement=="yes":
                    if len(todo_list)==0:
                        speaker.say("The list is empty please add something")
                        add_todo()
                        speaker.runAndWait()
                        f.write(todo_list)
                    else:                    
                        f.write(todo_list)
                
                done =True
                speaker.say("Successfully created a note.")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry, Please say again")
def birthday():
    speaker.say("Wish You a Happy Birthday")
    webbrowser.open_new("https://youtu.be/qb056tIqpX4")
    speaker.runAndWait()

def google():
    global recognizer
    webbrowser.open_new_tab("https://www.google.com")
    speaker.say("Google chrome is open now")
    speaker.runAndWait()

def gmail():
    global recognizer
    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    speaker.say("Google Mail open now")
    speaker.runAndWait()

def youtube():
    global recognizer
    webbrowser.open_new_tab("https://www.youtube.com/")
    speaker.say("youtube open now")
    speaker.runAndWait()

def time():
    global recognizer
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speaker.say(f"the time is {strTime}")
    speaker.runAndWait()

def wiki():
    global recognizer
    speaker.say("What to search in wikipedia")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                search = recognizer.recognize_google(audio,language='en-in')
                search = search.lower()
                speaker.say("Searching wikipedia..")
                results = wikipedia.summary(search, sentences=5)
                print(results)
                speaker.say(results)
                speaker.runAndWait()
        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry say again")
            speaker.runAndWait()           
                
def add_todo():
    global recognizer

    speaker.say("What do you want to add sir?")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio,language='en-in')
                item = item.lower()

                todo_list.append(item)
                done =True

                speaker.say("Added to To do List")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry say again")
            speaker.runAndWait()

def browse():
    global recognizer
    speaker.say("What can I search for you?")
    speaker.runAndWait()
    done =False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                searchdata = recognizer.recognize_google(audio,language='en-in')
                searchdata = searchdata.lower()
                j = search(searchdata, tld="co.in", num=10, stop=10, pause=2)
                j = list(j)
                for i in j:
                    print(i)
                # path = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
                # webbrowser.register('mozilla', None,webbrowser.BackgroundBrowser(path))
                # webbrowser.get('mozilla').open_new_tab(j[0])
                # webbrowser.open_new_tab(searchdata)

                done = True
                speaker.say("Opened succesfully")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("Sorry say again")
            speaker.runAndWait()

def show_todo():
    global recognizer
    speaker.say("The items on the to do list are following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def search_app():
    global recognizer
    speaker.say("Tell the name of the app you want to search")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                appname = recognizer.recognize_google(audio,language='en-in')
                appname = appname.lower()
                os.system(appname)
                done = True
        except speech_recognition.UnknownValueError:
            recognizer=speech_recognition.Recognizer()
            speaker.say("Sorry say again")
            speaker.runAndWait()

                

def hello():
    global recognizer
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speaker.say("Hello sir,Good Morning, How can I help you?")
        speaker.runAndWait()
        print("Hello sir,Good Morning, How can I help you?")
    elif hour>=12 and hour<18:
        speaker.say("Hello sir,Good Afternoon, How can I help you?")
        speaker.runAndWait()
        print("Hello sir,Good Afternoon, How can I help you?")
    else:
        speaker.say("Hello sir,Good Evening, How can I help you?")
        speaker.runAndWait()
        print("Hello sir,Good Evening, How can I help you?")

def note():
    global recognizer
    speaker.say("What to take note ")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio,language='en-in')
                text = text.lower()
                done =True

                speaker.say("Added to To do note")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Sorry say again")
            speaker.runAndWait()

    speaker.say("What shall i keep as file name?")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio= recognizer.listen(mic)
                data = recognizer.recognize_google(audio,language='en-in')
                data = data.lower()
                print(data)
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()

    file_name = str(data)+"-note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name])

def quitt():
    global recognizer
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)

def teams():
    os.system("C:\\Users\\Srisurya\\Downloads\\Teams_windows_x64.exe")
    speaker.say("Succesfully opened teams")
    speaker.runAndWait()

def whatsapp():
    os.system("C:\\Users\\Srisurya\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    speaker.say("Succesfully opened Whats app")
    speaker.runAndWait()


mappings = {
    'greetings':hello,
    'create':create_note,
    'add':add_todo,
    'show':show_todo,
    'google':google,
    'gmail':gmail,
    'youtube':youtube,
    'time':time,
    'note':note,
    'search':browse,
    'teams':teams,
    'search_app':search_app,
    'whatsapp':whatsapp,
    'wiki':wiki,
    'birthday':birthday,
    'exit':quitt,
}
assistant = GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()

speaker.say("Hello master, I am phoenix version 1.0, ready to serve you")
while True:
    statement = takeCommand().lower()
    # print(statement)

    if statement==0:
        continue
    else:
        assistant.request(statement)