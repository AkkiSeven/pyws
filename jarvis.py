import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if voice.languages[0] == u'en_US':
        engine.setProperty('voice', voice.id)
        break
engine.say('Hi!!! I am Jarvis.')
time.sleep(1)
engine.say('Please wait...')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            engine.say('What can I do for you?')
            engine.runAndWait()
            print(
                '''
  Hi, I am

  Ｊ．Ａ．Ｒ．Ｖ．Ｉ．Ｓ
  A.I

  I am listening...
          '''
            )
            voice = listener.listen(source)
            # command = listener.recognize_google(voice)
            command = "jarvis shutdown"
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Please wait for about 5 seconds.')
        time.sleep(0.2)
        talk(f'playing {song} on YouTube.com')
        pywhatkit.playonyt(song)
    elif 'shutdown' or 'shut down' in command:
        talk("Shutting down, goodbye!!!")
        os.system("shutdown /s")
    else:
        talk('Sorry, I don\'t understand. ')


run_jarvis()
