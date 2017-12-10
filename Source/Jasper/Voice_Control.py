from threading import Thread
import speech_recognition as sr


r = sr.Recognizer()
r.energy_threshold = 16000


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
    with sr.Microphone() as source2:
        #setBGN()
        print("Jasper is listening")
        audio2 = r.listen(source2)
        string = r.recognize_sphinx(audio2)
        print(string)
        if "list" in string:
            addList(string)
        if "do math" in string:
            mathTest()
        if "reset" in string:
            setBGN()
        else:
            listen()


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
    return arr.index("to")


def setBGN():
    with sr.Microphone() as source:
        sr.Recognizer().adjust_for_ambient_noise(source)
    print("completed")

    # TODO make jasper init with a 1s pause to adjust for ambient noise?

listen()
