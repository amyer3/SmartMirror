import speech_recognition as sr
import evernote as en



def master(string):
    if "list" in string:
        addList(string)
    if "do math" in string:
        mathTest(string)

def mathTest(string):
    print("2 + 2 = 4")


def addList(string):
    words = string.split(" ")
    command = string.replace("list", "rep")
    print(command)
    print(finder(words))

def finder(arr):
    r = arr.index("to")
    return r

def setBGN(string):

