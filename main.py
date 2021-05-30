import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()
def take_command():

    try:
        with sr.Microphone() as source:


            print('listening..')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'sky' in command:
                command2=command.replace('sky','')

    except:
        pass
    return command2
def run_sky():
    command2=take_command()
    print(command2)

    if 'play' in command2:
        song=command2.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'what is your name' in command2:
        talk('my name is sky')
    elif 'time' in command2:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is'+ time)
        print(time)
    elif 'date' in command2:
        date=datetime.datetime.now().strftime('%d/%m/%y')
        print(date)
        talk('todays date is'+ date)
    elif 'joke' in command2:
        talk(pyjokes.get_joke())


    elif ' tell me about' or 'what is ' or 'who is' in command2:
        if( 'tell me about' in command2):
            person=command2.replace(' tell me about','')
            info =wikipedia.summary(person,2)
            print(info)
            talk(info)
        elif('what is' in command2):
            person=command2.replace('what is','')
            info =wikipedia.summary(person,2)
            print(info)
            talk(info)
        elif('who is' in command2):
            person=command2.replace('who is','')
            info =wikipedia.summary(person,2)
            print(info)
            talk(info)


while True:
    run_sky()













