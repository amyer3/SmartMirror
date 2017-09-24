from threading import Thread
import speech_recognition as sr
import Voice_Actions as actions


r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
    try:
        rec = r.recognize_sphinx(audio)
        print(rec)
        if rec == "jasper":
            actions.master()
        else:
            listen()
    except sr.UnknownValueError:
        print("unknown value error")
    except sr.RequestError:
        print("request error")

listen()
