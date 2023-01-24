import datetime
import json
import os
import subprocess
import time
import webbrowser
from urllib.request import urlopen
from dotenv import load_dotenv
from voice.speaking import speak, command
import pyjokes
from ecapture import ecapture as ec
import requests
import winsound

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
WEATHER_KEY = os.getenv("WEATHER_KEY")


def open_youtube():
    speak("Here you go to YouTube")
    webbrowser.open("youtube.com")


def open_google():
    speak("Opening Google")
    webbrowser.open("google.com")


def open_wikipedia():
    speak("Opening wikipedia")
    webbrowser.open("wikipedia.com")


def open_stackoverflow():
    speak("Here you go to Stackoverflow. Happy coding!")
    webbrowser.open("stackoverflow.com")


def tell_joke():
    speak(pyjokes.get_joke())


def tell_time():
    time_str = datetime.datetime.now()
    speak(time_str)


def how_are_you():
    speak("I am fine, thank you")
    speak("How are you?")
    answer = command()
    if "fine" in answer or "good" in answer:
        speak("It's good to know, that you are fine")
    elif "bad" in answer:
        speak("Do you want me to tell you a joke??")
        answer_1 = command()
        if "yes" in answer_1:
            tell_joke()
        else:
            speak("What can i do for you?")


def who_made_you():
    speak("I have been created by Pavilion4ik")
    print("https://github.com/Pavilion4ik")


def open_pycharm():
    appli = r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.3\bin\pycharm64.exe"
    speak("Opening pycharm. Have a nice coding!")
    os.startfile(appli)


def news():
    i = 1
    try:
        json_obj = urlopen(
            f"https://newsapi.org/v2/everything?q=Ukraine&sortBy=popularity&apiKey={API_KEY}"
        )
        data = json.load(json_obj)

        speak("Here are some top news about Ukraine")
        for item in data["articles"]:
            print(f"{i}. {item['title']}\n")
            print(f"{item['description']}\n")
            print(item["url"] + "\n")
            speak(f"{i}. {item['title']}\n")
            i += 1
            if i >= 6:
                break
    except Exception as e:
        print(str(e))


def shutdown_system():
    speak("Hold on a sec, your system is on its way to shut down.")
    subprocess.call("shutdown / p /f")


def dont_listen():
    speak("For how much time you want me to stop listening commands?")
    x_time = int(command())
    time.sleep(x_time)
    print(x_time)


def camera():
    ec.capture(0, "assistant camera", "img.jpg")


def restart():
    subprocess.call(["shutdown", "/r"])


def sleep():
    speak("Sleeping")
    subprocess.call("shutdown / h")


def log_out():
    speak("Make sure all the application are closed before log-out")
    time.sleep(7)
    subprocess.call("shutdown / h")


def write_a_note():
    speak("What should i write?")
    note = command()
    with open("notes.txt", "a") as file_out:
        file_out.write(f"{note}\n")
    speak("Note successfully added")


def show_note():
    speak("Showing notes")
    with open("notes.txt", "r") as file:
        print(file.read())
        speak(file.read(7))


def weather():
    speak("In which city do you want to know weather?")
    city = command()
    response = requests.get(URL, params={"key": WEATHER_KEY,
                                         "q": city}).json()
    location = response["location"]
    current = response["current"]

    speak(f"Country: {location['country']}")
    speak(f"City: {location['name']}")
    print(f"City: {location['name']}")
    speak(f"Date: {location['localtime']}")
    speak(f"Temperature: {current['temp_c']}")
    print(f"Temperature: {current['temp_c']}")
    speak(f"Feel Like: {current['feelslike_c']}")
    print(f"Feel Like: {current['feelslike_c']}")
    speak(f"Humidity: {current['humidity']}")
    speak(f"Wind Speed: {current['wind_mph']}")


def alarm_clock():
    speak("In what time?")
    hour = command()
    speak("Minute?")
    minute = command()
    set_alarm = f"0{hour}:{minute}"
    speak(set_alarm)
    print(set_alarm)

    current_time = datetime.datetime.now().strftime("%H:%M")

    if current_time == set_alarm:
        speak("Time to Wake up")
        # Playing sound
        winsound.PlaySound("test.wav", 0)
