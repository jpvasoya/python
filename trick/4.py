import pyttsx3
friend=pyttsx3.init()
speach=input("say something:")
friend.say(speach)
friend.runAndWait()