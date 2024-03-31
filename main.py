import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import pywhatkit
import pyjokes
import requests
from bs4 import BeautifulSoup


for i in range(3):
    a=input("Enter the password to start DARWIN: ")
    pw_file=open("password.txt","r")
    pw=pw_file.read()
    pw_file.close()
    if(a==pw):
        print("Welcome sir, I am Darwin!")
        break
    elif(i==2 and pw!=a):
        exit()
    elif(a!=pw):
        print("Try again..")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am your virtual assistant DARWIN ,how can I help you?")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold=1
        print("Listening...")
        audio=r.listen(source)

    try:
        print("Recognizing..")
        a = r.recognize_google(audio,language='en-in')
        #speak(a)
        #return a
        print(f"You said:{a}\n")


    except Exception as e:
        #print(e)
        speak("Sorry an error occurred ,Say that again please!")
        return "None"
    return a


if __name__=="__main__":
    wishMe()
    while 1:
        query = takeCommand()
        if 'exit' in query.lower():
            speak("Logging off , Take care!!")
            exit()
        if "hello" in query.lower():
            speak("Hey sir how are you and how can I help u?")
        if "i a fine" in query.lower():
            speak("That's great sir..!")
        if "how are you" in query.lower():
            speak("I'm perfect sir, Thanks for asking!/")
        if "thank you" in query.lower():
            speak("Your Welcome Sir..")
        if "news" in query.lower():
            from newsRead import latestnews
            latestnews()
        if "calculate" in query.lower():
            from calculation import WolfRamAlpha
            from calculation import Calc
            query=query.replace("calculate","")
            query=query.replace("darwin","")
            Calc(query)
        sites=[["my instagram","https://www.instagram.com/_ayushi_nanda_/"],["leetcode","https://leetcode.com/problemset/"],["instagram","https://instagram.com"],["youtube","https://www.youtube.com"],["google","https://www.google.com"],["gfg","https://auth.geeksforgeeks.org/user/ayushinas2yo"],["Linkedin","https://www.linkedin.com/in/ayushi-nanda-b0333825b/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "time" in query.lower():
            hour=datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            sec = datetime.datetime.now().strftime("%S")
            speak(f"Sir the time is{hour} hours {min} minutes {sec}seconds ")

        elif "temperature" in query.lower():
            search="Temperature in Patna"
            url=f"https://www.google.com/search?q=+{search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div", class_ = "BNeawe").text
            speak(f"Current{search} is {temp}")


        elif 'wikipedia' in query.lower():
                speak("Searching ...")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia..")
                print(results)
                speak(results)
        apps = [["telegram", "C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"],["visual studio code","E:\\VS code\\Code.exe"],["chrome","C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"],["pycharm","C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.3.5\\bin\\pycharm64.exe"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                speak(f"Opening {app[0]} sir..")
                os.startfile(app[1])

        if 'play' in query.lower():
            song=query.replace('play',"")
            speak("Playing"+song)
            pywhatkit.playonyt(song)
        elif 'joke' in query.lower():
            speak("Searching one for you...")
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)







