import datetime
import pyttsx3
from playsound import playsound
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2])
engine.setProperty('voice', voices[1].id)


def speak(audio):
    print("Ivan: ", audio)

def speakP(audio):
    print("Ivan: ", audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
        playsound("C:\\Users\\Dhairya\\Desktop\\coding projects\\AI\\Ivan-main\\Jarvis Startup.mp3")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
        playsound("C:\\Users\\Dhairya\\Desktop\\coding projects\\AI\\Ivan-main\\Jarvis Startup.mp3")

    else:
        speak("Good Evening sir!")
        playsound("C:\\Users\\Dhairya\\Desktop\\coding projects\\AI\\Ivan-main\\Jarvis Startup.mp3")
  
    strdate = datetime.datetime.now().strftime("%D")
    # print(strdate)

    # Wishes of the festivals and birthdays
    if(strdate == "05/15/21"):
        speak("And please say Happy Birthday to your brother Shaurya")

    elif(strdate == "12/28/21"):
        speak("Happy Birthday Sir. Wish you many happy returns of the day!")

    elif(strdate == "12/25/21"):
        speak("Merry Christmas. Ho ho ho")

    elif(strdate == "05/14/21"):
        speak("Happy Akshay Tritya sir")


    speakP("Please tell me how may I help you")