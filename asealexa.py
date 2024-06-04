import speech_recognition as sr
import pyttsx3
#import sounddevice as sd
import pyaudio
import wikipedia
import pywhatkit
import datetime

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[18].id)
engine.say('I am your Asealexa')
engine.say('How can I help you?')
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def run_alexa():
    command = take_command()
    print(command)

    if "play" in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M:%S %p')
        print(time)
        speak('Current time is ' + time)

    elif "who is" in command or "what is" in command or "how is" in command or "what does" in command or "how many":
        person = command.replace('who is', '').replace('what is', '').replace('how is', '').replace('what does', '').replace('how many', '')
        info = wikipedia.summary(person, )
        print(info)
        speak(info)

    else:

        speak('Please say the command again')

run_alexa()
