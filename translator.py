from googletrans import Translator
import random
import time
from googletrans import LANGUAGES
translator = Translator()
languageChoice = list(LANGUAGES)
translateAmount = 0
stringToTranslate = ''
backToEnglish =''
translatedString=''
translatoredString = ''

def takeInput():
    global translatorTimes
    translatorTimes = int(input("how many times would you like to translate this text?"))+1
    # print(translatorTimes)
    if translatorTimes > 51:
        print('Error! Must not exceed 50 translations to appease our Google overlords')
        takeInput()

def takeString():
    global stringToTranslate
    stringToTranslate =input("What would you like to translate?")
    # print(stringToTranslate)

# print(languageChoice)
def languageChooser():
    global languageChosen
    languageChosen = (random.choice(languageChoice))
    # print(languageChosen)
    return languageChosen

def letChaosReign():
    global stringToTranslate
    # print(translatorTimes)
    i=0
    while i < translatorTimes:
        languageChooser()
        translatedString = translator.translate(stringToTranslate, dest=languageChosen)
        stringToTranslate = translatedString.text
        time.sleep(.5)
        print(languageChosen)
        print(translatedString.text)
        print(i)
        i += 1
    else:    
        backToEnglish()

def backToEnglish():
    translatoredString = translator.translate(stringToTranslate, dest='en')
    print(translatoredString.text)

     


def makeItGo():
    takeString()
    takeInput()
    letChaosReign()

makeItGo()