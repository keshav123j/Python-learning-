# its about using an external module to do anything so here it speaks whatever we write 
import pyttsx3
a = input("Enter :")
engine = pyttsx3.init()
engine.say(a)
engine.runAndWait()