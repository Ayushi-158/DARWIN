import wolframalpha
import pyttsx3
import speech_recognition

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def WolfRamAlpha(query):
    apikey="8PJEX4-QT7EA3PYRG"

    requester=wolframalpha.Client(apikey)
    requested=requester.query(query)

    try:
        answer=next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term=str(query)
    Term=Term.replace("darwin","")
    Term=Term.replace("multiply","*")
    Term = Term.replace("add", "+")
    Term = Term.replace("subtract", "-")
    Term = Term.replace("divide", "/")

    Final=str(Term)
    try:
        result=WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)
    except:
        speak("The value is not answerable")