import speech_recognition as sr
import pyttsx3
import datetime
import random as r
def random():
    ran = r.randrange(0,4)
    print(ran)
    return ran
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print('listeing....')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            query = r.recognize_google(audio)
            print('ok done')
        except:
            print('error')
            return('ok')
        return (query)
ran = random()
aboutme = ['Your are Muhhammad Taaseen Ansari.' ,'A smart and funny personality',' you born in 3rd february,1998 ','you created me ...' ]
wishme = ['Assaalaamu-alaykum','good morning sir','hello sir','Priya at your service,sir']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)
time = datetime.date.today()
engine.say(wishme[ran])
engine.say(f'today is {time}')
engine.say("")
engine.say("what can i do for you,sir")
engine.runAndWait()

txt = ''
while True:
    query = takeCommand().lower()
    print(query)
    if ('priya' in query and 'about' in query and 'yourself' in query) or ('priya' in query and 'apne' in query and 'bare'in query and 'batao' in query):
        engine.say('I m Priya , I m a vertual voice assistance of Mr. Taaseen. I born in twenty forth june,twenty twenty . My version is 0 point 1')
        engine.runAndWait()
    #elif('priya' in query and (('about' in query or 'bare'in query) and ('myself' in query or 'mere' in query)) or ('main' in query and 'kaun'in query and 'hun' in query)):
        #for i in range(0,len(aboutme)):
            #engine.say(aboutme[i])
            #engine.runAndWait()
    elif('priya' in query and ('my' in query or 'mera' in query) and ('date of birth' in query or 'birthday' in query)):
        engine.say(aboutme[2])
        engine.runAndWait()
    elif('priya' in query and 'love you' in query):
        engine.say('I love you to sir,you are the most charming person i ever meet')
        engine.runAndWait()
    elif ('priya' in query and('kaun' in query or 'who' in query or 'about' in query or 'bare' in query)):
        if ('faizan' in query):
            engine.say('Samroz faizan is friend of Mr. Taaseen ansari, every one called him chaamo')
            engine.runAndWait()
        if ('sabhi' in query):
            engine.say('shabby ahmad is friend of Mr. Taaseen ansari, every one called him chhedi')
            engine.runAndWait()
        if ('moin' in query):
            engine.say('Moin akhtar is the father  of Mr. Taaseen ansari')
            engine.runAndWait()
        if ('sabina' in query):
            engine.say('sabiha parween is the mother of Mr. Taaseen ansari')
            engine.runAndWait()
        if ('myself' in query or 'taseen' in query or 'main' in query or 'mere' in query):
            for i in range(0, len(aboutme)):
                engine.say(aboutme[i])
                engine.runAndWait()
        if ('liza' in query or 'lisa' in query):
            engine.say('leeza rehan is the sister of mr. taaseen ansari,She is very cute girl')
            engine.runAndWait()
    elif('priya' in query and ('stop' in query or 'bus karo'in query)):
        break
engine.say("thank you sir, have a good day ")
engine.runAndWait()




