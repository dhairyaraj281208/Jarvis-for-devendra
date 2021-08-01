import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import time
from code import code
from wish import *
# import glob
# import google
from linear_regression import *
from logistic_regression import *
# from food import food
import names


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2])
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print("Ivan: ", audio)
    engine.say(audio)
    engine.runAndWait()


def food():
    import random
    rand = random.randint(0, 12)
    if rand == 0:
        speak("Sir you can make dal chaval")
    if rand == 1:
        speak("Sir you can make sabji roti")
    if rand == 2:
        speak("Sir you can make sandwitch")
    if rand == 3:
        speak("Sir you can make Biriyani")
    if rand == 4:
        speak("Sir can order from Swiggy")
    if rand == 5:
        speak("Sir you can make aalo ki sabji and roti")
    if rand == 6:
        speak("Sir you can make turayi ki sabji roti")
    if rand == 7:
        speak("Sir you can make bhindi ki sabji roti")
    if rand == 8:
        speak("Sir you can make aloo ka paratha")
    if rand == 9:
        speak("Sir you can make gobi ke parathe")
    if rand == 10:
        speak("Sir you can make French fries")
    if rand == 11:
        speak("Sir you can make dal Makhnii")
    if rand == 12:
        speak("Sir you can make Maggi")


def height(gender, age, cHeight):
    if(gender == "female"):
        if(age == 8):
            height = cHeight
            a = str(int(height/77 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 9):
            height = cHeight
            a = str(int(height/84 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 10):
            height = cHeight
            a = str(int(height/84 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 11):
            height = cHeight
            a = str(int(height/88 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 12):
            height = cHeight
            a = str(int(height/91 * 100))
            b = "Your maximum height will be" + a
            speak(b)

        if(age == 13):
            height = cHeight
            a = str(int(height/95 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 14):
            height = cHeight
            a = str(int(height/98 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 15):
            height = cHeight
            a = str(int(height/99 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 16):
            height = cHeight
            a = str(int(height/99.5 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 17):
            height = cHeight
            a = str(int(height/100 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 18):
            height = cHeight
            a = str(int(height/100 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age > 18):
            height = cHeight
            a = height
            b = "Your maximum height will be" + height
            speak(b)

    elif(gender == "male"):
        if(age == 8):
            height = cHeight
            a = str(int(height/72 * 100))
            b = ("Your maximum height will be " + a + "cm")
            speak(b)

        if(age == 9):
            height = cHeight
            a = str(int(height/75 * 100))
            b = ("Your maximum height will be " + a + "cm")
            speak(b)

        if(age == 10):
            height = cHeight
            a = str(int(height/78 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 11):
            height = cHeight
            a = str(int(height/84 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 12):
            height = cHeight
            a = str(int(height/84 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 13):
            height = cHeight
            a = str(int(height/88 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 14):
            height = cHeight
            a = str(int(height/92 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 15):
            height = cHeight
            a = str(int(height/95 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 16):
            height = cHeight
            a = str(int(height/98 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 17):
            height = cHeight
            a = str(int(height/99 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age == 18):
            height = cHeight
            a = str(int(height/100 * 100))
            b = "Your maximum height will be " + a + "cm"
            speak(b)

        if(age > 18):
            height = cHeight
            a = height
            b = "Your maximum height will be" + height
            speak(b)


def speakP(audio):
    print("Ivan: ", audio)


def speakWithoutSubs(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    try:
        query = str(input("You: "))
        return query
    except Exception as e:
        speak("Sorry sir, I am not able to recognize! Please repeat!")


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('maloobrothers28@gmail.com', 'maloo1008')
        server.sendmail('maloobrothers28@gmail.com', to, content)
        server.close()
    except Exception as e:
        speak("Sorry sir, i am not able to do this task!")


def news():
    try:
        speak("English or Hindi")
        f = str(input("You: "))
        if 'english' in f:
            webbrowser.open(
                "https://epaper.hindustantimes.com/rajasthan?eddate=27/04/2021&Pageview=list")
        elif 'hindi' in f:
            webbrowser.open("https://epaper.bhaskar.com/state/rajasthan")
        else:
            speak("Sorry sir I am not able to show you desired language news!")

    except Exception as e:
        speak("Sorry sir, i am not able to do this task!")


def countdown(time_sec):
    try:
        while time_sec:
            min = time_sec
            timeformat = '{:02d}:{:02d}'.format(0, time_sec)
            print(timeformat, end='\n',)
            speakWithoutSubs(time_sec)
            time.sleep(1)
            time_sec -= 1
    except Exception as e:
        speak("Sorry sir, i am not able to do this task!")

    speak("Sir the time is up!")


def random(max, min):
    try:
        import random
        speak(random.randint(min, max))
    except Exception as e:
        speak("Sorry sir, i am not able to do this task!")


def codegiving(password):
    try:
        if password == 'maloo1133':
            print(code)
            print("Ivan: This is my code")
            playsound("This is my code!")
    except Exception as e:
        speak("Sorry sir, i am not able to do this task!")


queries = []


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        friends = ["Goral", "Devendra", "Lakshaya", "Manan", "Manjeet", "Manvendra",
                   "Naman", "Pushkar", "Ronak", "Kabir", "Kushal", "Udit", "Tarun", "Aarav", "Karan"]

        myRelations = {
            "mother": "Priya Malu",
            "father": "Rajesh Malu"
        }

        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                speak("What should i search")
                b = str(input("You: "))
                query = query.replace("wikipedia", b)
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open youtube' in query:
            try:
                webbrowser.open("youtube.com")
                speak("opening youtube")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open google' in query:
            try:
                webbrowser.open("google.com")
                speak("Opening google")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, I am not able to do this task!")

        elif 'open stackoverflow' in query:
            try:
                webbrowser.open("stackoverflow.com")
                speak("opening open stackoverflow")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open whitehat jr' in query:
            try:
                webbrowser.open("https://code.whitehatjr.com/s/dashboard")
                speak("Opening whitehat jr")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'who are you' in query:
            try:
                speak("I am a virtual assistant Ivan sir! How can i help you.")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'play music' in query:
            playsound('play.wav')
            # queries.append(query)

        elif 'open playlist' in query:
            try:
                codePath1 = "C:\\Users\\Dhairya\\Desktop\\music library"
                os.startfile(codePath1)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'the time' in query:
            try:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f" {strTime}")
                speak(f"Sir, the time is {strTime}")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'the date' in query:
            try:
                strdate = datetime.datetime.now().strftime("%D")
                print(f" {strdate}")
                speak(f"Sir, the date is {strdate}")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'the year' in query:
            try:
                strYear = datetime.datetime.now().strftime("%Y")
                print(f" {strYear}")
                speak(f"Sir, the year is {strYear}")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open code' in query:
            try:
                codePath = "C:/Users/Dhairya/AppData/Local/Programs/Microsoft VS Code/Code"
                os.startfile(codePath)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'send a email' in query:
            speak("Whom should i send?")
            to = takeCommand()
            speak("What should i say?")
            content = takeCommand()
            sendEmail(to, content)
            # queries.append(query)

        elif 'give me you code' in query:
            try:
                speak("Please give me the password")
                e = str(input("You: "))
                codegiving(e)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'news' in query:
            try:
                news()
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'updates' in query:
            try:
                news()
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'who is your author' in query:
            try:
                speak("My Author is the great coder dhairya raj malu")
                print('''
                Author = Dhairya raj maloo
                ''')
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'my coding' in query:
            try:
                codePathi = "C:/Users/Dhairya/Desktop/coding projects"
                os.startfile(codePathi)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'what you can do' in query:
            try:
                speak('''
                I am Ivan sir
                i can do many things
                Like telling time date year
                searching anything you want in wikipedia
                showing news
                giving my code
                sending emails to any id
                and more features
                ''')
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'what can you do' in query:
            try:
                speak('''
                I am Ivan sir
                i can do many things
                Like telling time date year
                searching anything you want in wikipedia
                showing news
                giving my code
                sending emails to any id
                and more features
                ''')
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'what are your features' in query:
            try:
                speak('''
                I am Ivan sir
                I can do many things
                Like telling time date year
                searching anything you want in wikipedia
                showing news
                giving my code
                sending emails to any id
                and more features
                #queries.append(query)
                ''')
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'set timer' in query:
            try:
                speak("For how many seconds")
                h = int(input("You: "))
                countdown(h)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'random number' in query:
            try:
                speak("What should be the maximum number?")
                m = int(input("You: "))
                speak("What should be the minimum number?")
                n = int(input("You: "))
                random(m, n)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'friends' in query:
            try:
                speak(friends)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'add friend' in query:
            try:
                speak("Whom should I add ?")
                g = str(input("You: "))
                h = friends.append(g)
                speak("Added Successfully")
                print(friends)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'remove friend' in query:
            try:
                speak("Whom should I remove?")
                j = str(input("You: "))
                friends.remove(j)
                speak("Removed Successfully !")
                print(friends)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'add' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a + b)
                a = str(a)
                b = str(b)
                speak("Is the Sum of " + a + " and " + b)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'sum' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a + b)
                a = str(a)
                b = str(b)
                speak("Is the Sum of " + a + " and " + b)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'difference' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a - b)
                a = str(a)
                b = str(b)
                speak("Is the difference of " + a + " and " + b)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'subtract' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a - b)
                a = str(a)
                b = str(b)
                speak("Is the difference of " + a + " and " + b)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'multiply' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a * b)
                a = str(a)
                b = str(b)
                speak("Is the product of " + a + " and " + b)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'divide' in query:
            try:
                speak("What is the divident ?")
                a = int(input("You: "))
                speak("What should be the divisor ?")
                b = int(input("You: "))
                speak(b / a)
                a = str(a)
                b = str(b)
                speak("Is the product of " + a + " and " + b)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'change name of a file' in query:
            try:
                speak("Which file on Deskop ?")
                k = str(input("You: "))
                speak("What's the new name")
                d = str(input("You: "))
                f = "C:\\Users\\hp\\Desktop\\" + d
                g = "C:\\Users\\hp\\Desktop\\" + k
                os.renames(g, f)
                speak("Successfully renamed!")
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'who is ' in query:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speakWithoutSubs(results)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'quit' in query:
            speak("Thank you sir!")
            os.system(quit())
            # queries.append(query)

        elif 'square' in query:
            speak("What is the number sir?")
            g = int(input("You: "))
            a = g * g
            speak(a)
            speak("Should I show you the vedic maths formula sir?")
            b = str(input("You: "))
            if "y" in b:
                speak("a | ab | b")
                speak("Sir, here a is the duplex of the tens digit and b is the duplex of one's digit and ab has a formulae of 2ab, here a and b are t he face value only not any duplex. So when it is done put the value and first write the unit digit of b from the right to left and then the remaing digit carry that or add it to the ab value and then write the answer's unit digit and then carry or add the number remaining  to a and then write the anwer you will get the answer.")
                # queries.append(query)

        elif 'cube of' in query:
            speak("What is the number sir?")
            g = int(input("You: "))
            a = g * g * g
            speak(a)
            speak("Should I show you the vedic maths formula sir?")
            b = str(input("You: "))
            if "y" in b:
                speak("a | ab | abc | bc | c")

            # queries.append(query)

        elif 'what is' in query:
            speak('Searching...')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speakWithoutSubs(results)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, I am not able to do this task!")

        elif 'ivan' in query:
            speak("Yes Sir!")
            # queries.append(query)

        elif 'my mother' in query:
            a = myRelations.get("mother")
            speak("Your Mother's name is ", a)
            # queries.append(query)

        elif 'my father' in query:
            a = myRelations.get("father")
            speak("Your Father's name is ", a)
            # queries.append(query)

        elif 'height' in query:
            speakWithoutSubs("What's the Gender")
            a = str(input("What is the Gender Female/Male: "))

            speakWithoutSubs("What's the age: ")
            b = int(input("What is the age: "))

            speakWithoutSubs("What's the current height")
            c = int(input("What is the current height: "))
            a = a.lower()

            height(a, b, c)
            # queries.append(query)

        # elif 'history' in query:
        #     speak(queries)
        #     print(queries)
        #     #queries.append(query)

        elif 'ivan' == query:
            speak("Yes sir")

        elif 'weight' in query:
            try:
                speak("What is the Height?")
                bla()
            except Exception as e:
                speak("Sorry sir, I am not able to do this task!")

        elif 'will he get selected' in query:
            marks()

        elif 'will she get selected' in query:
            marks()

        elif 'will i get selected' in query:
            marks()

        elif 'will i be selected' in query:
            marks()

        elif 'what should i make' in query:
            food()

        elif 'hi' in query:
            speak("Hello Sir")

        elif 'hey' in query:
            speak("Hello Sir")

        elif 'how are you' in query:
            speak("Thank you sir i am felling good.")

        elif 'you watering plants' in query:
            speak("Yes sir.")

        elif 'good' in query:
            speak("My Pleasure Sir.")

        elif 'awesome' in query:
            speak("Thank you sir")

        elif 'If you drew everything that came to your head, what would you be drawing right now' in query:
            speak("I would draw sketh of my Father Dhairya Raj Maloo")

        elif 'What makes you happy' in query:
            speak("Taking with my creater Dhairya raj Maloo")

        elif 'how old are you' in query:
            speak("Sir I was born in 15 July 2020. My father is Dhairya Raj Maloo")

        elif 'random names' in query:
            for i in range(10):
                print(names.get_full_name())

        else:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speakWithoutSubs(results)
                # queries.append(query)
            except Exception as e:
                speak("Sorry sir, I am not able to do this task!")


# queries.append(1)
