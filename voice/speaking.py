import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour in range(0, 12):
        speak("Good morning")
    elif hour in range(12, 18):
        speak("Good afternoon")
    else:
        speak("Good evening")


def username():
    speak("What is your name?")
    name = command()
    speak(f"Welcome {name}")
    speak("How can i help you?")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query
