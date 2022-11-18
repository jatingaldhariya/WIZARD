virsion = 1.1
from Brain.AiBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting Wizard.....")
from Body.Speak import Speak
import webbrowser

# from Features.WakeUp import WakeupDetected
print(">> Started Wizard!")

def MainExecution():

    Speak("Hello Sir")
    Speak("I'm Wizard,I'm Ready To Assist You Sir.")
    while True:

        Data = MicExecution()
        Data = str(Data)

        if (len(Data))<=3:
            pass

        elif 'who are you' in Data:
            Speak(f"I Am Wizard,Ai Based Persnoal Assistant Currently Running On Virsion {virsion} , I Am Devloped By Jatin Galdhariya")


        elif 'exit' in Data:
            Speak("Okay Sir,You Can Call Me Any Time")
            break

        elif 'youtube search' in Data:
            Data=Data.replace("wizard","")
            Data=Data.replace("youtube search for","")
            Data=Data.replace("youtube search","")
            # query=query.replace("","")
            Speak(f"Okay Sir, Searching In Youtube For {Data}...")
            web = 'https://www.youtube.com/results?search_query='+Data
            webbrowser.open(web)
            Speak("Done Sir")


        elif "what is" in Data or "where is" in Data or "question"in Data or "answer" in Data:
            Reply= QuestionsAnswer(Data)
            Speak(Reply)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

MainExecution()