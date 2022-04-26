import speech_recognition as sr
import time

r = sr.Recognizer()
INITIAL = "hey tv"
TV_ON = "turn on"
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    in1 = r.listen_in_background(source)
    c1 = r.recognize_google(in1,language = "en-GB")
    if INITIAL in c1.lower():
        print("detected")
    else:
        continue