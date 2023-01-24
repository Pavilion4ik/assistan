import os
from commands.list import (
    open_google,
    open_youtube,
    news,
    open_pycharm,
    open_wikipedia,
    open_stackoverflow,
    tell_joke,
    tell_time,
    how_are_you,
    who_made_you,
    shutdown_system,
    dont_listen,
    camera,
    restart,
    sleep,
    log_out,
    write_a_note,
    show_note,
    weather,
    alarm_clock,
)
from voice.speaking import speak, greeting, username, command

commands = {"hello": greeting, "youtube": open_youtube, "google": open_google,
            "wikipedia": open_wikipedia, "news": news, "pycharm": open_pycharm,
            "stackoverflow": open_stackoverflow, "joke": tell_joke,
            "time": tell_time, "how are you": how_are_you, "who made you": who_made_you,
            "shutdown system": shutdown_system, "stop listen": dont_listen, "camera": camera,
            "restart": restart, "sleep mode": sleep, "log out": log_out, "note": write_a_note,
            "show note": show_note, "weather": weather, "alarm clock": alarm_clock}


def clear():
    return os.system("cls")


if __name__ == "__main__":
    clear()
    greeting()
    username()

    while True:
        query = command().lower()
        try:
            if commands[query]:
                commands[query]()
        except KeyError:
            while False:
                commands[query]()
        if query == "exit":
            speak("Goodbye")
            exit()
