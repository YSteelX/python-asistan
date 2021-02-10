#YSteelX God
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

#Fonksiyon
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language = 'tr-TR')
        except sr.UnknownValueError:
            speak("Dediğin Şeyi Anlamadım")
        except sr.RequestError:
            speak("Sistem bozuk.Yapımcıma bildirin.")
        return voice

def response(voice):
    if 'ara' in voice:
        value = record('Aramak İstediğin Kelime Veya Cümle')
        url = 'https://www.google.com/search?q='+ str(value)
        speak("Tarayıcı Açılıyor...")
        webbrowser.get().open(url)
        speak(value+'İçin Sonuçlar')
    if 'Merhaba' in voice:
        speak("Merhaba.Sana Nasıl Yardımcı Olabilirim")
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'kapan' in voice:
        speak("Görüşürüz")
        exit()

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,1000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
