from threading import Thread
import speech_recognition as sr
import Voice_Actions as res


r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)

try:
    print(r.recognize_sphinx(audio))
    res.master(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("ukve")
except sr.RequestError:
    print("ReqE")

