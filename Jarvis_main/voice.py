import speech_recognition as sr
import pyttsx3
import json

def read_config():
    with open('config.json') as file:
        return json.load(file)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening:")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        command = ''

        try:
            print("Recognizing")
            command = r.recognize_google(audio, language='en-in')

            print(f"You said: {command}\n")

        except Exception as e:
            print("Exception: " + str(e))

        return command


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)

if __name__ == "__main__":
    #start()
    while True:
        command = get_audio().lower()
        intent = ''
        
        
            

        # intent = ''
        # for key in config:
        #     utterances = 
        if 