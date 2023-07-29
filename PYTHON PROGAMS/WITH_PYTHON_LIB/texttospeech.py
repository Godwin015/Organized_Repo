import pyttsx3
pyobj=pyttsx3.init()
location = input("what do you want me to pronounce for you?\n")
pyobj.say(location)
pyobj.runAndWait()