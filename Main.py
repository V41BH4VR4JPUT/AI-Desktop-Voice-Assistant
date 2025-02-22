import pyttsx3 # type: ignore
import datetime
import speech_recognition as sr # type: ignore
import pyaudio # type: ignore
import wikipedia # type: ignore
import webbrowser
import os
import smtplib


"""
To find the index of the microphone
"""
# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(f"Device {i}: {info['name']}")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Toto, How can I help you?")

def takeCommand():
    """
    It takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Analyzing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    """
    Note: You need to enable less secure apps in your google account to send email
    Then you need to enter your email and password in the below line
    """
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    Greetings()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            """
            Note: You need to change the directory of the music folder
            """
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "E:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(query)
        
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Vaibhavyouremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
        
        elif 'stop' in query:
            print("Thank you for using me!\nHave a nice day!")
            speak("Thank you for using me!")
            break