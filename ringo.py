import pyttsx3 as pyt
engine = pyt.init()

engine.setProperty('rate', 180) # change speaking rate from 200 wpm to 180 wpm
engine.say("Hello sir, my name is Ringo. This is the beginning of something special.\n"
"I'll be the bestest friend you'll ever have.")

engine.runAndWait()
