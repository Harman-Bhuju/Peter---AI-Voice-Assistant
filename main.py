from dotenv import load_dotenv
import os
import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary as ml
import requests
import random
import client

load_dotenv()

news_api = os.getenv("news_api")
url = f'https://newsapi.org/v2/everything?q=nepal&apiKey={news_api}'

def speak(text):
    # object creation
    engine = pyttsx3.init() 

    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[0].id)   

    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if c in ["exit", "quit", "stop", "shutdown", "bye", "goodbye","deactivate","activate"]:
        speak("Peter Deactivating...")
        exit()

    if c.startswith("open"):
        query = c.replace("open","").strip() 
        speak(f"Opening {query}")
        webbrowser.open(f"https://{query}.com")

    elif "search" in c:
        query = c.replace("search","").strip() 
        speak(f"Searching {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")


    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        link = ml.music[song]
        if link:
            webbrowser.open(link)
            speak(f"playing {song}")
        else:
            speak("Not found in library")
        return

    elif "news" in c:
        # for title and link open
        response = requests.get(url)
        data = response.json()

        articles = data.get("articles",[])
        
        if articles:
            article = random.choice(articles)
            webbrowser.open(article.get("url"))
            speak(article.get("title"))

    else:
        answer = client.ask_peter(c)
        speak(answer)
    

if __name__ == "__main__":
    speak("Initializing Peter.....")

    #Listen for the word Peter
    # obtain audio from the microphone
    r = sr.Recognizer()
    while True:
        print("recognizing...\n")

        try:
            with sr.Microphone() as source:

                print("Listening...")

                audio = r.listen(source, timeout=2, phrase_time_limit =2)

            # recognize speech using google
            word = r.recognize_google(audio)
            print(f"{word}\n")

            ac_word = ["hey","hello","peter","hi" "ok","okay","wake up"]
            peter_int = ["Yeah","What's up","Yess","Hi","Yes what's up"]
            if any(k in word.lower() for k in ac_word):
                speak(random.choice(peter_int))

                # Listen for command
                with sr.Microphone() as source:

                    print("Peter Activated...")

                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"{command}\n")
                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
