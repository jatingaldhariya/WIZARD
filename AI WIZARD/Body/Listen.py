#file 1

import speech_recognition as sr #pip install SpeechRecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
import pyaudio 

#listen function

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en")

    except:
        return ""

    query = str(query).lower()
    return query


# print(Listen())

#translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You :{data}.")
    return data

#Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

