import pyttsx3 as pyt
import speech_recognition as sr
import wikipedia
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime
from datetime import date 
import webbrowser
from bs4 import BeautifulSoup
import playsound

from time import sleep 
import os
import music

#from facerec import facerec as fr

# initializing txt -> speech
engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160) # change speaking rate from 200 wpm to 180 wpm

#browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Chrome(executable_path=r'C:/Users/chand/Downloads/chromedriver_win32/chromedriver.exe')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        print("Analyzing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Cannot understand input.")
        return "None"
    
    return query

today = date.today()
hour = datetime.datetime.now().time().strftime('%H')

spotObj = music.SpotMusic()
called = False
while True:
    query = takeCommand().lower()
    #faces = fr.faceRec()
    #print(faces)

    if ("ringo" in query or called):
        if called == False:
            called = True
        # check for commands
        if ("hey" in query or "hello" in query or "hi" in query or "wake up" in query):
                if (int(hour) > 20):
                    # almost midnight
                    speak(f"It is {str(int(hour) % 12)} PM sir..."
                    "Maybe you should go to bed soon.")
                elif (int(hour) < 4):
                    # midnight
                    speak(f"It is {str(int(hour))} AM, sir..."
                    "You need to rest.")
                else:
                    speak("Hello sir...")

        elif ("stop listening" in query):
            break

        elif ("my beat" in query or "my song" in query):
            speak("If you wish sir...")
            playsound.playsound(r'C:\Users\chand\voiceAssist\ringo\music\AC_DC - Back In Black (Official Video) (1).mp3')

        elif ("play" in query and "song" in query):
            speak("Ok, I hope you enjoy sir...")
            spotObj.play_randPlaylist()    

        elif ("play" in query):
            # just one song
            query = query.replace("ringo", "")
            query = query.replace("play", "")
            print(f"Song to play: {query}")
            spotObj.playSpecific(query)

        elif 'wikipedia' in query:
            speak('Alright, searching the internet...')
            query = query.replace("wikipedia", "")
            query = query.replace("ringo", "")
            try:
                results = wikipedia.summary(query, sentences = 3, auto_suggest=False)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            except Exception as e:
                print("Exception:", e)

        elif 'life' in query:
            results = wikipedia.summary('absurdism', sentences = 2)
            speak(results)
            playsound.playsound(r'C:\Users\chand\voiceAssist\ringo\sounds\Lex Fridman reads Charles Bukowski poem.mp3')