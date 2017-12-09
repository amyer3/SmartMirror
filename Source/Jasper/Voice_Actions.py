import speech_recognition as sr
import evernote as en
import Voice_Control as vc


def JasperInit():
    with sr.Microphone() as source:
        setBGN()
        print("Jasper is listening")
        audio = sr.Recognizer().listen(source)
        string = sr.Recognizer().recognize_sphinx(audio)
    if "list" in string:
        addList(string)
    if "do math" in string:
        mathTest()
    if "reset" in string:
        setBGN()


def mathTest():
    print("2 + 2 = 4")
    #vc.listen()


def addList(string):
    words = string.split(" ")
    command = string.replace("list", "rep")
    print(command)
    print(finder(words))
    #vc.listen()


def finder(arr):
    r = arr.index("to")
    return r


def setBGN():
    with sr.Microphone() as source:
        sr.Recognizer().adjust_for_ambient_noise(source)
    print("completed")

    # TODO make jasper init with a 1s pause to adjust for ambient noise?
