import speech_recognition as sr
import pyttsx3
name = "agente"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            recognizer = listener.recognize_google(pc)
            recognizer = recognizer.lower()
            if name in recognizer: 
                recognizer = recognizer.replace(name, '')
    except:
        pass
    return recognizer

def run_agente():
    recognizer = listen()
    if 'reproduce' in recognizer:
        music = recognizer.replace('reproduce', '')
        print ("Reproduciendo " + music)
        talk("Reproduciendo " + music)

if __name__ == '_main_':
    run_agente()
