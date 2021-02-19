
import speech_recognition as sr
import os

def audiotext(name):
    filename = 'static/'+name
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        message = r.recognize_google(audio_data)
    os.remove(filename)
    return message
