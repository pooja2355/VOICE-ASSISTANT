import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
from News import *
import randfacts
from weather import *
import datetime

init = p.init()
engine = init
rate=engine.getProperty('rate')
engine.setProperty('rate',170)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date=datetime.datetime.now()

r = sr.Recognizer()

speak("hello maam i'm your voice assistant. How are you? ")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("iam also having a good day maam")
speak("what can i do for you?")

flag = False

while True:
    if flag == True:
        speak("what else can i do for you?")
    flag = True

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)

    if "information" in text2:
        speak("you need information related to which topic?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
        speak("searching {} in wikipedia".format(infor))
        assist = infow()
        assist.get_info(infor)
    elif ("date" or "time") in text2:
        speak("sure maam, Today is"+ today_date.strftime("%d") + today_date.strftime("%B") + ", And its currently" + today_date.strftime("%I") + today_date.strftime("%M") + today_date.strftime("%p"))

    elif "play" and  "video" in text2:
        speak("you want me to play which video??")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listening")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
        print("playing {} on youtube".format(vid))
        speak("playing {} on youtube".format(vid))

        assist = music()
        assist.play(vid)

    elif "news" in text2:
        print("sure maam, now i will read news for you.")
        speak("sure maam , now i will read news for you.")
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif ("fact" or "facts") in text2:
        speak("sure maam,")
        x = randfacts.getFact()
        print(x)
        speak("Did you know that ," + x)
    elif "weather" in text2:
        speak(" Sure Mam. Today's Temperature in Punjab is" + str(temp()) + "degree celcius " + "and with" + str(des()))

    elif "nothing" and "thank you" in text2:
        print("YOUR WELCOME maam, Have a good day")
        speak("YOUR WELCOME maam, Have a good day")

        break


    else:
        speak("I did not get you. Can you please repeat?")
        flag = False


