from tkinter import *

from PIL import Image,ImageTk

import pyttsx3

import datetime

import speech_recognition as sr

import wikipedia

import webbrowser

import os

import random

import smtplib

from PIL import Image



#TO SET VOICE FOR ASSISTANT

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#START OF GUI

window = Tk()


global var
global var1


var = StringVar()
var1 = StringVar()


#STARTING OF SPEAK() FUNCTION


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#END OF SPEAK() FUNCTION


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id', 'password') # email id - use any email id whose security/privacy is off
    server.sendmail('email id', to, content)
    server.close()


#STARTING OF WISHME() FUNCTION


def wishme():

    hour = int(datetime.datetime.now().hour)
    dt=datetime.date.today()

    if hour >= 0 and hour <= 12:


        var.set(f"Good Morning Vijit..! Today is {dt}") #Name - your Name
        window.update()
        speak(f"Good Morning Vijit..! Today is {dt}")


    elif hour >= 12 and hour <= 18:


        var.set(f"Good Afternoon Vijit..! Today is {dt}")
        window.update()
        speak(f"Good Afternoon Vijit..! Today is {dt}")


    else:
        var.set(f"Good Evening Vijit..! Today is {dt}")
        window.update()
        speak(f"Good Evening Vijit..! Today is {dt}")


    var.set("STARTING LYDIA...")
    window.update()
    speak("Hey Vijit I am Lydia , I am your partner today , Please tell me how may I help u")


#END OF WISHME() FUNCTION


#STARTING OF TAKECOMMAND() FUNCTION


def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:

        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 0.9
        r.energy_threshold = 400
        audio = r.listen(source)

    try:

        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        return "None"

    var1.set(query)
    window.update()
    return query


#END OF TAKECOMMAND() FUNCTION


#STARTING OF PLAY() FUNCTION

def play():

    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()

    while True:

        btn1.configure(bg = 'orange')
        query = takeCommand().lower()

        if 'exit' in query:                                             #TO EXIT THE ASSISTANT

            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()

            speak("Closing myself vijit, Please remeber me again! Have a good day")
            var.set("Closing Lydia...")
            window.update()

            var1.set("User Said:")
            window.update()

            var.set("Welcome")
            window.update()
            break


#FOR OPENING WEB BROWSER PREOGRAMS


        elif 'wikipedia' in query:                                      #FOR WIKIEPEDIA

            if 'open wikipedia' in query:                               #FOR SEARCHING WIKIPEDIA ON INTERNET

                webbrowser.open('wikipedia.com')

            else:

                try:

                    speak("searching wikipedia")                        #FOR SEARCHING WIKIPEDIA FROM ASSISTANT
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    var1.set("User Said:")
                    window.update()
                    speak("According to wikipedia")
                    var1.set("User Said:")
                    window.update()
                    var.set(results)
                    window.update()
                    speak(results)

                except Exception as e:

                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')



        elif 'open youtube' in query:                                   #FOR YOUTUBE

            var1.set("User Said:")
            window.update()
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("www.youtube.com")



        elif 'open google' in query:                                    #FOR GOOGLE

            var1.set("User Said:")
            window.update()
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("www.google.com")



        elif 'open gmail' in query:                                     #FOR GMAIl

            var1.set("User Said:")
            window.update()
            var.set("opening gmail")
            window.update()
            speak("opening gmail")
            webbrowser.open('www.gmail.com')



        elif 'whatsapp' in query:                                       #FOR WHATASPP(WEB)

            var1.set("User Said:")
            window.update()
            var.set("opening whatsapp")
            window.update()
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")



        elif 'send email' in query:                                     #SENDING EMAIL

            speak("opening gmail to send email")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")


#-------------------------------------------------------------------------------



      #OPENING PROGRAMS/FILES IN COMPUTER



        elif 'open zoom' in query:                                      #OPENING ZOOM

           var1.set("User Said:")
           window.update()
           var.set("opening zoom")
           speak("opening zoom")
           os.startfile("C:\\Users\\vijit\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")



        elif 'open atom' in query:                                      #OPENING ATOM IDE

            var1.set("User Said:")
            window.update()
            var.set("opening atom")
            window.update()
            speak("opening atom")
            os.startfile("C:\\Users\\vijit\\AppData\\Local\\atom\\atom.exe")



        elif 'current time' in query:                                   #CURRENT TIME

            strTime=datetime.datetime.now().strftime("%H:%M:%S")

            var1.set("User Said:")
            window.update()
            var.set(f"The time is {strTime}")
            speak(f"The time is {strTime}")

            window.update()



        elif 'open sublime text' in query:                              #OPENING SUBLIME TEXT

            var1.set("User Said:")
            window.update()
            var.set("opening text")
            window.update()
            speak("opening sublime text")
            sub="C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(sub)



        elif 'open cmd'in query:                                        #OPENING COMMAND PROMPT

            var1.set("user said")
            window.update()
            var.set("opening cmd")
            window.update()
            speak("opening command prompt")
            os.startfile("cmd.exe")



        elif 'open git bash' in query:                                  #OPENING GIT BASH

            var1.set("User Said:")
            window.update()
            var.set("opening git bash")
            window.update()
            speak("opening git bash")
            bash="C:\Program Files\Git\git-bash.exe"
            os.startfile(bash)






        elif 'open notepad' in query:                                   #OPENING NOTEPAD

            var1.set("User Said:")
            window.update()
            var.set("opening notepad")
            window.update()
            speak("opening notepad")
            os.startfile("C:\\WINDOWS\\system32\\notepad.exe")



        elif 'open python' in query:                                    #OPENING PYTHON

            var1.set("User Said:")
            window.update()
            var.set("opening python")
            window.update()
            speak("opening python")
            os.startfile("C:\\Users\\vijit\\anaconda3\\python.exe")



        elif 'recorder' in query:                                       #NW

            var1.set("User Said:")
            window.update()
            var.set("opening obs recorder")
            window.update()
            speak("opening obs recorder")
            os.startfile("C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe")



        elif 'attendance' in query:                                     #ATTENDANCE

            var1.set("User Said:")
            window.update()
            var.set("opening semester 5 attendance")
            window.update()
            speak("opening semester 5 attendance")
            os.startfile("C://Users//vijit//Desktop//ATTENDANCE 5 SEM.txt")



        elif 'alexa' in query:                                          #

            var1.set("User Said:")
            window.update()
            var.set("opening Video")
            window.update()
            speak("opening video")
            os.startfile("C:\\Users\\vijit\\Videos\\2020-08-19 23-41-51.mkv")



        elif 'semester 5'in query:                                      #SEMESTER 5 (VIDEOS)

            var1.set("User Said:")
            window.update()
            var.set("opening semester 5 study")
            window.update()
            speak("opening semester 5 study")
            os.startfile("C:\\Users\\vijit\\Videos\\SEMESTER 5")



        elif 'movies' in query:                                         #OPENING LIST OF MOVIES

            var1.set("User Said:")
            window.update()
            var.set("opening list of movies")
            window.update()
            speak("opening list of movies")
            os.startfile("C:\\Users\\Nikita\\Desktop\\MINE\\movies.txt")



        elif 'dates' in query:                                         #OPENING LIST OF MOVIES

            var1.set("User Said:")
            window.update()
            var.set("opening dates")
            window.update()
            speak("opening dates")
            os.startfile("C:\\Users\\Nikita\\Desktop\\MINE\\DATES.txt")



        elif 'example' in query:

            ved_dir="C:\\VIJIT RAWAL\\VEDIOS"
            songs=os.listdir(ved_dir)
            var.set(songs)
            window.update()
            from random import randint
            r=randint(0,4)
            print("\n")
            print(r)
            print("\n")

            os.startfile(os.path.join(ved_dir,songs[r]))



        elif 'pc'in query:

            speak("opening wps")
            os.startfile("This PC")



#-------------------------------------------------------------------------------


         #CLOSING ALL APPLICATION





        elif 'shutdown' in query:                    #SHUTTING DOWN THE COMPUTER


            speak("shutting down ur computer")
            speak("closing all applications")


            os.system("taskkill/im atom.exe")
            os.system("taskkill/im notepad.exe")
            os.system("taskkill/im git-bash.exe")
            os.system("shutdown /s")





        elif 'close notepad' in query:               #CLOSING NOTEPAD

            var1.set("User Said:")
            window.update()
            var.set("closing notepad")
            window.update()
            speak("closing notepad")
            os.system("taskkill/im notepad.exe")






        elif 'close cmd' in query:                #CLOSING COMMAND PROMPT

            var1.set("User Said:")
            window.update()
            var.set("closing command prompt")
            window.update()
            speak("closing command prompt")
            os.system("taskkill/im cmd.exe")






        elif 'close atom' in query:               #CLOSING ATOM IDE

            var1.set("User Said:")
            window.update()
            var.set("closing atom")
            window.update()
            speak("closing atom")
            os.system("taskkill/im atom.exe")



#--------------------------------------------------------------------------------


#LOGIC OF TKINTER

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
window.update()
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()


photo=Image.open("four.jpg")
frames= [ImageTk.PhotoImage(photo)]



window.title('LYDIA...')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
