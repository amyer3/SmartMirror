from threading import Thread
import speech_recognition as sr


r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
    try:
        rec = r.recognize_sphinx(audio)
        print(rec)
        if rec == "jasper":
            JasperInit()
        else:
            listen()
    except sr.UnknownValueError:
        print("unknown value error")
    except sr.RequestError:
        print("request error")


def JasperInit():
    with sr.Microphone() as source:
        #setBGN()
        print("Jasper is listening")
        audio = sr.Recognizer().listen(source)
        string = sr.Recognizer().recognize_sphinx(audio)
        print(string)
        if "list" in string:
            addList(string)
        if "do math" in string:
            mathTest()
        if "reset" in string:
            setBGN()


def mathTest():
    print("2 + 2 = 4")
    listen()


def addList(string):
    words = string.split(" ")
    command = string.replace("list", "rep")
    print(command)
    print(finder(words))
    listen()


def finder(arr):
    r = arr.index("to")
    return r


def setBGN():
    with sr.Microphone() as source:
        sr.Recognizer().adjust_for_ambient_noise(source)
    print("completed")

    # TODO make jasper init with a 1s pause to adjust for ambient noise?

listen()
