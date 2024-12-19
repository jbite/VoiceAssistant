import os
import time

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)

speak("hello tim")