import requests
import json
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict={"bussiness":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3cd43e5c40f34cbcb8d5c651d24b5d90",
             "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3cd43e5c40f34cbcb8d5c651d24b5d90",
             "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3cd43e5c40f34cbcb8d5c651d24b5d90",
             "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3cd43e5c40f34cbcb8d5c651d24b5d90",
             "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3cd43e5c40f34cbcb8d5c651d24b5d90",
             "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3cd43e5c40f34cbcb8d5c651d24b5d90"}

    content=None
    url=None
    speak("Which field news do you want , sir, [bussiness] [health] [technology] [entertainent] [science] [sports]?")
    field=input("Type news that you want:")
    for key ,value in apidict.items():
        if key.lower() in field.lower():
            url=value
            print(url)
            print("url was found")
            break
        else:
            url=True
    if url is True:
        print("url not found")

    news=requests.get(url).text
    news=json.loads(news)
    speak("Here is the first news.")
    arts=news["articles"]
    for articles in arts:
        article=articles["title"]
        print(article)
        speak(article)
        news_url=articles["url"]
        print(f"For more info visit:{news_url}")

        a=input("[press 1 to continue] and [press 2 to stop]")
        if str(a)=="1":
            pass
        elif str(a)=="2":
            break
    speak("Thats all")
