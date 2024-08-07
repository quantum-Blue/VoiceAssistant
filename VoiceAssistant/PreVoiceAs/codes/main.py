from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import random
import os

#import pyaudio


r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
        return voice

def speak(string):
    tts=gTTS(text=string,lang="tr",slow=False)
    rand=random.randint(1,10000)
    file="audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def response(voice):
    if "hey namık" in voice:
        speak("Sizi dinliyorum")
        if "merhaba" in voice or "Merhaba" in voice:
            speak("sana da merhaba")


playsound("/Users/enesbal/Desktop/ProtoA/voices/naber.mp3")
while True:
    voice=record()
    if voice != "":
        voice.lower()
        print(voice.capitalize())
        response(voice)
