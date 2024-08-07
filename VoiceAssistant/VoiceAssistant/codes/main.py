# istenilen resmi google görsellerde bulma
# alarm kurma
# söylenen şekli çizme
# fotoğraf çek
# mesaj yazma


from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
from translate import Translator
import webbrowser
import subprocess
from tkinter import *
from PIL import ImageTk, Image
import requests
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet
import json

#import pyaudio
#from weather_api import weather_api_client # çalıştıramadım



# Spotify üzerinden şarkı çalma
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API anahtarlarınızı ve kullanıcı kimlik bilgilerinizi burada tanımlayın
SPOTIPY_CLIENT_ID = 'ba475cc8e4134122ba1192ecb2a8c146'
SPOTIPY_CLIENT_SECRET = '6ace4caf76734953b5c0686603eafc73'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Spotify API'ye yetkilendirme sağlamak için spotipy nesnesini oluşturun
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='user-library-read user-read-playback-state user-modify-playback-state'))

def play_spotify_track(track_name, artist_name):
    # Şarkı adı ve sanatçı adına göre Spotify API'den şarkıları arayın
    results = sp.search(q=f'track:{track_name} artist:{artist_name}', type='track')

    # İlk bulunan şarkıyı alın (Burada daha fazla hata kontrolü eklemek iyi olabilir)
    track_uri = results['tracks']['items'][0]['uri']

    # Spotify'da şarkıyı çalın
    sp.start_playback(uris=[track_uri])

# Örnek olarak bir şarkı çalma
#play_spotify_track("Shape of You", "Ed Sheeran")
"""








r = sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source: #sr.Microphone(device_index=1)
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
    if "merhaba" in voice or "meraba" in voice or "Merhaba" in voice:
        speak("sana da merhaba")


    if "nasılsın" in voice:
        speak("Senin kalbin kadar iyi")


    if "teşekkürler" in voice:
        speak("Size layık olmaya çalışıyorum")


    if "müslüman mısın" in voice or "Müslüman mısın" in voice:
        speak("Elhamdülillah Müslümanım")


    if "adın ne" in voice:
        speak("Benim adım Asistant, efendime nasıl yardımcı olabilirim")


    if  "youtube aç" in voice or "youtube'u aç" in voice or "Youtube'u aç" in voice:
        speak("hemen açıyorum")
        webbrowser.open('https://www.youtube.com')
        speak("işte oldu")


    if "arama yap" in voice or "google'da ara" in voice:
        search=record("ne aramak istiyorsun")
        url=f'https://www.google.com/search?q={search}'
        webbrowser.get().open(url)
        speak(search+" içinde bulduklarım ")


    if "saat kaç" in voice:
        speak("adam gelmiş bana saat kaç diyor, ben saat mi satıyorum")
        time.sleep(2)
        speak("off tamam söyliyeceğim")
        now=datetime.now().strftime("%H:%M")
        speak("şuan saat "+now)


    if "hangi takımlısın" in voice or "hangi takımı tutuyorsun" in voice:
        select1=["fenerbahçe","beşiktaş","bayern munich","galatasaray","real madrid","barcelona"]
        select1=random.choice(select1)
        speak(f"tabiki {select1}")
        if select1 != "fenerbahçe":
            speak("şaka yapıyorum, fenerbahçeliyim (opsiyonel değil)")


    if "görüşürüz" in voice or "hoşça kal" in voice or "Görüşürüz" in voice or "Hoşça kal" in voice:
        speak("hay hay efenim Allah'a emanet olunuz")
        exit()

    
    if "selamünaleyküm" in voice or "Selamünaleyküm" in voice:
        speak("vealeykümselam verahmetullahi veberekatü")


    if "hangi gün" in voice or "günlerden ne" in voice:
        selection =["bugün günlerden: ","hemen bakıyorum: "]
        today=time.strftime("%A")
        #today.capitalize()
        translator= Translator(to_lang="Turkish")
        today = translator.translate(today)
        selection=random.choice(selection)
        speak(selection+today)


    if "kimi seviyorsun" in voice:
        select2=["tabiki en çok seni seviyorum, canim","tabiki seni, oy paşasinin tosuni"]
        speak(random.choice(select2))


    if "tekerleme" in voice or "espri" in voice:
        select3=[
            "Dal sarkar kartal kalkar, kartal kalkar dal sarkar",
            "Şemsipaşa Pasajında sesi büzüşesiceler",
            "Şu yoğurdu sarımsaklasak da mı saklasak, sarımsaklamasak da mı saklasak",
            "it iti itti, bit biti itti, itti gitti bitti",
            "Bir berber bir berbere bre berber gel beraber bir berber dükkanı açalım demiş",
            "Ben araba sürüyordum leonardo da vinci"
        ]
        line=random.choice(select3)
        speak(line)


    if "uygulama aç" in voice or "Uygulama aç" in voice:
        speak("ne açmamı istersiniz efenim")
        runApp=record()
        runApp=runApp.lower()
        print(runApp.capitalize())

        if "discord" in runApp or "Discord" in runApp:
            app_path = "/Applications/Discord.app/Contents/MacOS/Discord"
            try:
                os.system(f"{app_path}")
                speak("Discord başarıyla açıldı")
            except Exception as e:
                speak("Uygulama açılamıyor")
                print(f"Error: {e}")

        elif "takvim" in runApp or "Takvim" in runApp:
            exec_path = "/System/Applications/Calendar.app/Contents/MacOS/Calendar"
            try:
                subprocess.Popen([exec_path])
                speak("Takvim başarıyla açıldı")
            except Exception as e:
                speak("Uygulama açılamıyor")
                print(f"Error: {e}")

        elif "spotify" in runApp or "Spotify" in runApp:
            exec_path = "/System/Applications/Spotify.app/Contents/MacOS/Spotify"
            try:
                subprocess.Popen([exec_path])
                speak("Takvim başarıyla açıldı")
            except Exception as e:
                speak("Uygulama açılamıyor")
                print(f"Error: {e}")

        elif "borsa" in runApp or "Borsa" in runApp:
            exec_path = "/System/Applications/Stocks.app/Contents/MacOS/Stocks"
            try:
                subprocess.Popen([exec_path])
                speak("Borsa başarıyla açıldı")
            except Exception as e:
                speak("Uygulama açılamıyor")
                print(f"Error: {e}")

        elif "safari" in runApp or "Safari" in runApp:
            exec_path = "/Applications/Safari.app/Contents/MacOS/Safari"
            try:
                subprocess.Popen([exec_path])
                speak("Takvim başarıyla açıldı")
            except Exception as e:
                speak("Uygulama açılamıyor")
                print(f"Error: {e}")

        elif "satranç" in runApp or "Satranç" in runApp:
            exec_path = "/System/Applications/Chess.app/Contents/MacOS/Chess"
            try:
                subprocess.Popen([exec_path])
                speak("Takvim başarıyla açıldı")
            except Exception as e:
                speak("Uygulama açılamıyor")
                print(f"Error: {e}")


    if "not et" in voice or "not al" in voice:
        speak("Dosya ismi ne olsun")
        textFile=record()+".txt"
        speak("sözlü not alma işlemi başlıyor lütfen konuşmaya başlayın")
        theText=record()
        file1=open(textFile,"w",encoding="utf-8")
        file1.writelines(theText)
        file1.close()
        speak("Not alma işlemi tamamlandı")

    if "rastgele şarkı" in voice or "rastgele müzik" in voice:
        speak("spotify dan mı youtube dan mı açılsın")
        sourceOfMusic = record().lower()
        if "youtube" in sourceOfMusic:
            songAddres1=["https://www.youtube.com/watch?v=tCEU_bDJUZk",
                        "https://www.youtube.com/watch?v=ZKyfzLGK96A",
                        "https://www.youtube.com/watch?v=SegaPbTyFrQ",
                        "https://www.youtube.com/watch?v=i-pgvaB3LMA&t=43s",
                        "https://www.youtube.com/watch?v=wRbbDmJ3klQ",
                        "https://www.youtube.com/watch?v=iKJpIplXV_o"
            ]
            trackChoice1=random.choice(songAddres1)
            webbrowser.open(f"{trackChoice1}")
        elif "spotify" in sourceOfMusic:
            songAddres2=["https://open.spotify.com/intl-tr/track/0YTM7bCx451c6LQbkddy4Q?si=ba63611e32874850",
                        "https://open.spotify.com/intl-tr/track/0uMZbmAAgOhdMrv25iPEH6?si=54c67b96ee7743ee",
                        "https://open.spotify.com/intl-tr/track/0DI3WNmIyfi2GZLQwhYDQC?si=553e787b0511427e",
                        "https://open.spotify.com/intl-tr/track/2P5yIMu2DNeMXTyOANKS6k?si=78f17ae18d4e4f7e",
                        "https://open.spotify.com/intl-tr/track/6d67Xv8ms2noA8wWFLiPDN?si=983ba90c373d4d24",
                        "https://open.spotify.com/intl-tr/track/42qNWdLKCI41S4uzfamhFM?si=bae17463588047f5",
                        "https://open.spotify.com/intl-tr/track/45tD5FiRiU91ya2H62j8cL?si=1132649842a1408c",
                        "https://open.spotify.com/intl-tr/track/3xzwzbTKhw2ljPVuV60w32?si=eaa5d9b14cfe4f2e",
                        "https://open.spotify.com/intl-tr/track/43k0XWzhEPEbHZrf9UNske?si=a82c401e3ffa4563"

            ]
            trackChoice2=random.choice(songAddres2)
            webbrowser.open(f"{trackChoice2}")
    
    if "hava durumu" in voice:
        api_key="14ed54e6cec0f6ee2c73701aa27d175a"
        base_url= "http://api.openweathermap.org/data/2.5/weather?"
        
        # sehir_ismi=input("Şehir: ")
        speak("lütfen şehir ismini türkçe karakter kullanmadan söyleyin")
        sehir_ismi=record()
        print("Şehir :" +str(sehir_ismi))
        url=base_url+"appid="+api_key+"&q="+sehir_ismi

        gelen_veri=requests.get(url)
        json_veri=gelen_veri.json()

        if json_veri["cod"] !="404":
            temp = json_veri["main"] ["temp"]
            description=json_veri["weather"][0]["description"]
            temp_in_celsius = float(temp) - 273.15 #Kelvin'dan Çıkan Sonuç C°'ya Dönüştürme
            speak(f"{sehir_ismi} şehrinin derecesi {temp_in_celsius:.2f}")
            translator= Translator(to_lang="Turkish")
            description = translator.translate(description)
            speak(str(description))
        else :
            speak("Şehir bulunamadı")

    if "sayıyı tahmin et" in voice:
        speak("aklından bir sayı tut")
        time.sleep(2)
        speak("iki ile çarp")
        time.sleep(2)
        speak("8 ekle")
        time.sleep(2)
        speak("ikiye böl")
        time.sleep(2)
        speak("ilk tuttuğun sayıdan çıkar")
        time.sleep(2)
        speak("hazırsan sayıyı tahmin ediyorum")
        playsound("/Users/enesbal/Desktop/VoiceAssistant/voices/bateri.mp3")
        speak("son bulduğun sayııı")
        speak("dört")
    
    if "borsa analiz" in voice:
        speak("hemen adese şirketinin borsa değerlerini incelemeye başlıyorum")
        brk = yf.Ticker('ADESE.IS')

        hist_df = brk.history(period="max", interval="1d", auto_adjust=True)

        hist_df.plot(y=["Close"], figsize=(20,10))
        plt.show()

        df = pd.DataFrame()

        df['ds_tz'] = hist_df.index
        df['ds'] = df['ds_tz'].dt.tz_localize(None) # ds_tz sutunundan timezone bilgisini cikartip "ds" sutununa yaz.
        df.drop(columns=['ds_tz'],inplace=True) # ds_tz sutununu sil.
        df['y'] = hist_df['Close'].values

        m = Prophet(daily_seasonality=False)
        m.fit(df)

        future = m.make_future_dataframe(365, freq='D')
        
        forecast = m.predict(future)

        speak("işte tahmin bilgilerim")
        print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7))

        speak("bilgileri grafiğe dökersek ise şöyle oluyor")
        m.plot(forecast)
        plt.show()


    if "namaz vakti" in voice or "ezan vakti" in voice:
        speak("hemen bakıyorum")

        url = "https://api.collectapi.com/pray/all"
        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0LIUnppvaqnvZAmSEo33Qg:5d5HfuqqhPpj5Mq0RkPBeE"
        }
        params = {
            'data.city': 'istanbul'
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        now = datetime.datetime.now()
        current_minute = now.hour * 60 + now.minute

        next_prayer_time = None
        for namaz in data["result"]:
            hour, minute = map(int, namaz["saat"].split(":"))
            prayer_minute = hour * 60 + minute
            if prayer_minute > current_minute:
                next_prayer_time = namaz
                break

        if next_prayer_time:
            remaining_minutes = prayer_minute - current_minute
            remaining_hours, remaining_minutes = divmod(remaining_minutes, 60)
            
            speak(f"Şu anki saatten sonra gelen bir sonraki namaz vakiti {next_prayer_time["vakit"]}, saati {next_prayer_time["saat"]}")
            speak(f"Sonraki namaz vaktine kalan süre ise {remaining_hours} saat {remaining_minutes} dakika")
        else:
            speak("Bugünün namaz vakitleri tamamlandı.")
            speak("hata, hata")

    if "para dönüştür" in voice or "para birimi" in voice:
        api_key ="c563d054c366cc45f87a094c"
        api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

        speak("Hangi birimden döviz bozacaksınız")
        dovizBozdurma=range()
        dovizBozdurma=dovizBozdurma.lower()
        if "dolar" in dovizBozdurma:
            bozulan_doviz="USD"
        elif "euro" in dovizBozdurma:
            bozulan_doviz="EUR"
        elif "lira" in dovizBozdurma or "tl" in dovizBozdurma:
            bozulan_doviz="TRY"
        speak("paranızı hangi dövize çevireceksiniz ")
        dovizCevirme=range()
        dovizCevirme=dovizCevirme.lower()
        if "dolar" in dovizCevirme:
            cevirilen_doviz="USD"
        elif "euro" in dovizCevirme:
            cevirilen_doviz="EUR"
        elif "lira" in dovizCevirme or "tl" in dovizCevirme:
            cevirilen_doviz="TRY"
        speak("ne kadar döviz çevireceksiniz")
        miktar=int(range())

        response =requests.get(f"{api_url}{bozulan_doviz}")
        response_json=json.loads(response.text)

        speak("{0} {1} paranın karşılığı şöyledir {2} {3}".format(miktar,bozulan_doviz,(miktar * response_json["conversion_rates"][cevirilen_doviz]),cevirilen_doviz))
        print("{0} {1} = {2:.3f} {3}".format(miktar,bozulan_doviz,miktar * response_json["conversion_rates"][cevirilen_doviz],cevirilen_doviz))


    if "resim ara" in voice or "görsel ara" in voice:
        # YANLIŞ
        search=record("ne aramak istiyorsun")
        url=f'https://www.google.com/search?q={search}'
        webbrowser.get().open(url)
        speak(search+" içinde bulduklarım ")
        #https://www.google.com.tr/search?q={EVANGELİON}&tbm=isch&ved=2ahUKEwjlisKZ6PqEAxXb4AIHHQvyCGIQ2-cCegQIABAA&oq=evangelion&gs_lp=EgNpbWciCmV2YW5nZWxpb24yBBAjGCcyBBAjGCcyCBAAGIAEGLEDMgUQABiABDIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARI1BRQlQxYlQxwAHgAkAEAmAFfoAG4AaoBATK4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ8ICBhAAGAcYHogGAQ&sclient=img&ei=EaH2ZaW-C9vBi-gPi-SjkAY&bih=779&biw=1440
        #düzelt bunu
        



# Spotify dan şarkı çalma

"""
    if "şarkı aç" in voice:
        #os.system('mpg321 C:/Users/Oguzcan/Desktop/Music/music.mp3')
        #speak("şarkı başlatıldı")
        play_spotify_track("Kağızman", "Fırat Sobutay")
"""
    

#speak("naber müdür")
playsound("/Users/enesbal/Desktop/VoiceAssistant/voices/naber.mp3")
while True:
    voice=record()
    if voice != "":
        voice.lower()
        print(voice.capitalize())
        response(voice)








"""from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
from random import choice
from translate import Translator

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice.lower()

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def response(voice):
    if "merhaba" in voice or "meraba" in voice:
        speak("sana da merhaba")
    if "nasılsın" in voice:
        speak("Senin kalbin kadar iyi")
    if "teşekkürler" in voice:
        speak("Size layık olmaya çalışıyorum")
    if "müslüman mısın" in voice:
        speak("Elhamdülillah Müslümanım")
    if "saat kaç" in voice:
        speak("adam gelmiş bana saat kaç diyor, ben saat mi satıyorum")
        time.sleep(2)
        speak("off tamam söyliyeceğim")
        now = datetime.now().strftime("%H:%M")
        speak("şu an saat " + now)
    if "görüşürüz" in voice or "hoşça kal" in voice:
        speak("hay hay efenim Allah'a emanet olunuz")
        exit()
    if "hangi gün" in voice or "günlerden ne" in voice:
        selection = ["bugün günlerden: ", "hemen bakıyorum: "]
        today = time.strftime("%A")
        translator = Translator(to_lang="Turkish")
        today = translator.translate(today)
        selection_response = choice(selection) + today
        speak(selection_response)

# speak("naber müdür")
while True:
    voice = record()
    if "hangi gün" in voice or "günlerden ne" in voice:
        print(voice.capitalize())
        response(voice)



"""
