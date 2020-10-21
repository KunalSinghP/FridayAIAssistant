#Friday AI Assistant

'''This is a small AI Assistant-Friday. Friday can perform some small tasks for you on your command.
You guys should explore the program yourself. You may need to make some changes before running this program
on your system successfully.'''

#Before sending email from your gmail account, make sure you have enabled less secure apps in your google account.
#Change the path locations before using play music and open spotify like commands.
#Wikipedia Throws error sometimes, I couldn't figure it out yet, maybe there is some server problem or something.
#To use wikipedia, Give command like-The term you want to search + wikipedia: For eg- Salman Khan Wikipedia.

#Completed-22/09/2020 ------------>#To-do: Add a News Narrator Program
#Completed-21/10/2020 ------------>#To-do: Add some small games
#To-do: Add a calculator for simple calculations for now, later maybe we will add it for complex problems.
#To-do: To search for terms on google which Friday couldn't recognize.(Just Like Siri)
#These new features would be added soon.

#Suggest some more good improvements in this program. I would love to commit the changes that makes this program more fun and useful.

#MadeBY-Kunal
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import json
import time
import requests
#If you get a module error, install using pip install command

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)- Use this statement for a male voice.
engine.setProperty('voice', voices[1].id)
webbrowser.register('chrome',
	None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))

'''webbrowser.register is to make the sites open in google chrome, remove this statement if you want it to 
open in internet explorer or give the path of whatever browser you want to use'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Friday Sir. Please tell me how may I help you")
    speak("Make sure you are connected to internet before using this program.")
    '''Internet connection is important as this program uses google speech recognizer to recognize your voice'''

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        print("Say that again please...")
        print("Couldn't recognize. Try saying \"Friday what can you do \" or \"help\"")
        return "None"
    return query

def sendEmail(to, content):
    #Enable access to low secure apps in your google account before using this function.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('-your-email-here-', '-password-here-')
    server.sendmail('-your-email-here-', to, content)
    server.close()

def tasks():
    speak("Here is a list of what all I can do.")
    print('''\t1.Open Google
    2.Open Youtube
    3.Open Spotify
    4.Open Sololearn
    5.Tell the time
    6.Send Email
    7.Play music
    8.Play Games
    9.Akhbar padhkar sunao or say Live news
    10.Shutdown or Restart... much more to come''')

def news():
    speak("Welcome To The News Narrator Program.")
    print('*Instructions* Please don\'t give input until the bot completes its statement.')
    time.sleep(1)
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey='-generate your own api key, go to newsapi.org-'"
    news=requests.get(url).text
    news=json.loads(news)
    articles=news["articles"]

    for article in articles:
        print(article['title'])
        speak(article['title'])
        speak("Press 1 to have a short description of the news. Press 2 to hear the next news. Press any other key to quit.")
        x=input()
        time.sleep(1)
        if x=='1':
            print(article['description'])
            speak(article['description'])
            speak("Press 1 to hear the next news. Press any other key to stop listening")
            f=input()
            if f=='1':
                continue
            else:
                speak("Hope You Liked This Program Made By Kunal")
                #speak("And Sorry For My Accent. Actually I Was A PT Teacher In Delhi Police Public School")
                break
        elif x=='2':
            continue
        else:
            speak("Hope You Liked This Program Made By Kunal")
            # speak("And Sorry For My Accent. Actually I Was A PT Teacher In Delhi Police Public School")
            break

def games(user_choice):
    if user_choice==1:
        # This is a Guess the Number game.
        op='Yes' or 'yes' or 'Y' or 'y'
        while op=='Yes' or 'yes' or 'Y' or 'y':
        
            guessesTaken = 0

            print('Hello! What is your name?')
            myName = str(input())

            number = random.randint(1, 100)
            print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
            print('Lets see, ' + myName + ', if you can guess it or not. You have 6 guesses.')
            print("Good Luck")
            for guessesTaken in range(1,7):
                print('Take a guess.') 
                guess = input()
                guess = int(guess)

                if guess < number:
                    print('Your guess is too low.')

                if guess > number:
                    print('Your guess is too high.')

                if guess == number:
                    break

            if guess == number:
                guessesTaken = str(guessesTaken)
                print('Good job, ' + myName + '! You guessed my number in ' +
                    guessesTaken + ' guesses!')

            if guess != number:
                number = str(number)
                print('Nope, '+myName+'. The number I was thinking of was ' + number + '.')
            op=input("Do You Wish to Continue?Yes or No : ")
        else:
            print("BBye")
    elif user_choice==2:
        you=0
        comp=0

        print("Stone Papers Scissors!")
        print("Total 10 rounds")
        r=["s","p","x"]
        print("""s for stone
        p for paper
        x for scissors""")
        i=10
        while i>0:
            inp=input("Enter:")
            c = random.choice(r)
            while inp not in r:
                inp = input("Enter:")
            else:
                if inp=="s":
                    if c=="p":
                        print("You:s \t ")
                        time.sleep(2)
                        print("Computer:p")
                        time.sleep(2)
                        comp=comp+1
                        print(f"Comp:{comp} \t You:{you}")
                    elif c=="x":
                        print("You:s \t ")
                        time.sleep(2)
                        print("Computer:",c)
                        time.sleep(2)
                        you = you + 1
                        print(f"Comp:{comp} \t You:{you}")
                    else:
                        print("You:s \t ")
                        time.sleep(2)
                        print("Computer:", c)
                        time.sleep(2)
                        print(f"Comp:{comp} \t You:{you}")
                elif inp=="p":
                    if c=="x":
                        print("You:p \t ")
                        time.sleep(2)
                        print("Computer:x")
                        time.sleep(2)
                        comp=comp+1
                        print(f"Comp:{comp} \t You:{you}")
                    elif c=="s":
                        print("You:p \t ")
                        time.sleep(2)
                        print("Computer:",c)
                        time.sleep(2)
                        you = you + 1
                        print(f"Comp:{comp} \t You:{you}")
                    else:
                        print("You:p \t ")
                        time.sleep(2)
                        print("Computer:", c)
                        time.sleep(2)
                        print(f"Comp:{comp} \t You:{you}")
                elif inp=="x":
                    if c=="s":
                        print("You:x \t ")
                        time.sleep(2)
                        print("Computer:s")
                        time.sleep(2)
                        comp=comp+1
                        print(f"Comp:{comp} \t You:{you}")
                    elif c=="p":
                        print("You:x \t ")
                        time.sleep(2)
                        print("Computer:",c)
                        time.sleep(2)
                        you = you + 1
                        print(f"Comp:{comp} \t You:{you}")
                    else:
                        print("You:x \t ")
                        time.sleep(2)
                        print("Computer:", c)
                        time.sleep(2)
                        print(f"Comp:{comp} \t You:{you}")

            i-=1
            print(i," rounds left")
        time.sleep(1)
        print("Game Over")
        time.sleep(1)
        print("Final Scores:-")

        print("You:",you)
        print("Comp:",comp)
        time.sleep(1)
        if you>comp:
            print("You Win!")
        elif you<comp:
            print("Computer Wins!")
        else:
            print("It's a Tie")
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.strip("wikipedia")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("An Error Occured while contacting the site.")

        elif 'who are you' in query:
            speak('I am Friday, an A I assistant in search of love.')

        elif 'i love you' in query or 'i love u' in query:
            response=["I love you too.","Have you seen your face in mirror"]
            resp=random.choice(response)
            speak(resp)

        elif 'open spotify' in query:
            speak('Opening Spotify')
            spotifyPath=r'C:\Users\kunal\AppData\Roaming\Spotify\Spotify.exe' #Specify The Path According to Your Computer
            os.startfile(spotifyPath)

        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.get('chrome').open("google.com")

        elif 'open sololearn' in query:
            #Sololearn is a free website to learn programming
            speak('Opening Sololearn...')
            webbrowser.get('chrome').open("sololearn.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\kunal\\Desktop\\music'#Specify The Path According to Your Computer
            songs = os.listdir(music_dir)
            print(songs)
            speak("Playing Music")
            song=random.choice(songs) #To randomly play any song, if you want the song to be played in order, remove this line.
            os.startfile(os.path.join(music_dir, song))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'email to kunal' in query:
	#You can make a dictionary or edit this command to send email to multiple number of people. You can also store the data in files.
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kunalsingh.ks384@gmail.com" #Specify the email account to which you want to send the email.
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'friday what can you do' in query:
            tasks()

        elif 'who is kunal' in query:
            speak("Kunal Sir made me. He is really a genius. I love him.")

        elif 'know more about you' in query:
            speak("I am friday, personal A I assistant. Made using python by Kunal sir. He made me when he was"
                  "seventeen in last year of his school during lockdown. Modules used to program me are speechRecognition"
                  ", pyttsx3, wikipedia, s m p t lib, o s and web browser. I can do various tasks like playing music, opening google chrome, spotify, youtube and"
                  " other such applications or websites. I can send emails for you also. I can do a lot more but if I tell"
                  " you everything then what will you do. Hope you have a good time with me.")

        elif 'help' in query:
            speak("Try saying \"Friday what can you do .\"")

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.popen("shutdown -r -t 05")

        elif 'good job' in query or 'great job' in query:
            speak("I did my best sir. Thanks for your appreciation.")

        elif 'thank you' in query:
            speak("My pleasure sir.")
	
	elif 'akhbar padhkar sunao' in query or 'live news' in query:
	    news()
	
	elif 'play game' in query:
            speak('Would you like to play a multiplayer or a single player game.')
            response=takeCommand()

            if 'single' in response:
                speak("You can play two games at this moment.")
                print('1.Guess The Number')
                print('2.Stone Paper Scissors')
                choice = int(input("Enter 1 or 2: "))
                if choice==1 or choice==2:
                    games(choice)
                
                else:
                    speak('Invalid Input')
                    
            elif 'multiplayer' in response:
                pass #Adding Multiplayer Games Soon
	
	elif 'bye' in query or 'exit' in query or 'quit' in query:
	    speak("Bye Bye. See you soon.")
	    exit()
