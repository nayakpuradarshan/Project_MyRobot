import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """This function will speak based on the entered voice"""
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """
    This function is going to check the timezone and based on that wish morning retine,
    also it is going to introduce him self.
    """
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("good Eveing!")

    speak("I am Jarvish , Please tell me how may i help you!")


def takecommand():
    """"it takes microphones input from the user and returns the string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='english')
        print(f"User said {query}\n")

    except Exception as e:
        # print(e)      # This will give exception error so that added in comment
        print("say that again please...")
        return "none"  # This is none string

    return query


"""
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)    # with smtp you can send email 
    server.ehlo()
    server.starttls()
    server.login('darshannayakpura@gmail.com', 'your-password')     # mention your password only it's important
    server.sendmail('darshannayakpura@gmail.com', to, content)
    server.close()
"""

if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand().lower()
        # Logic for excuting task based on query
        if wikipedia in query:
            speak("seariching wikipedia...")
            query = query.replace("wikiedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accouring to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open python' in query:
            webbrowser.open("python.org")

        elif 'open selenium' in query:
            webbrowser.open("selenium.dev")

        elif 'open pytest' in query:
            webbrowser.open("pytest.org")

        elif 'open Selenium with Python' in query:
            webbrowser.open("selenium-python.readthedocs.io")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open Amazon' in query:
            webbrowser.open("amazon.in")

        elif 'open Flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open code' in query:
            codePath = "C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)

# This feature is under worknig
"""
        elif 'email to Darshan' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "darshannayakpura@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent to darshan!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 
"""