# Translator-inator V0.1.2
# Created by Cybork
from googletrans import Translator
import random
import time
from prompter import yesno
from googletrans import LANGUAGES
translator = Translator()
languageList = list(LANGUAGES)
startingLanguage = ''
translateAmount = 0
stringToTranslate = ''
backToEnglish =''
translatedString=''
translatoredString = ''


# gathers user translation amount input and
# ensures translation times don't exceed setpoint (currently 50)
def takeInput():
    global translatorTimes
    translatorTimes = int(input('How many times would you like to translate this text? '))
    # print(translatorTimes)
    if translatorTimes > 51:
        print('Error! Must not exceed 50 translations to appease our Google overlords')
        takeInput()
# takes user input on text to be translated and scrambled
def takeString():
    global stringToTranslate
    stringToTranslate =input('What would you like to translate? ')
    detectStartLanguage()
    # print(stringToTranslate)

def detectStartLanguage():
    global startingLanguage
    startingLanguage = translator.detect(stringToTranslate).lang



# Chooses a language at random, ensures it's not being translated back to english prematurely
# and returns the langauge str back to letChaosReign function
def languageChooser():
    global languageChosen
    languageChosen = (random.choice(languageList))
    if languageChosen == 'en':
        languageChooser()
    else:
        # print(languageChosen)
        return languageChosen


# where the magic happens, the real star of the show. Translates input text repeatedly until set amount is reached.
# This funciton also contains error handeling in the event the API blocks the requests, and an exit handeling function. 
def letChaosReign():
    global stringToTranslate
    # print(translatorTimes)
    i=0
    print('Running translator-inator. Press ctrl+C to cancel. Except you Perry the Platapus, Do not pressy any keys')
    while i < translatorTimes:
        try:
            languageChooser()
            translatedString = translator.translate(stringToTranslate, dest=languageChosen)
            stringToTranslate = translatedString.text
            print(".  ", end="", flush=True)
            time.sleep(.5)
            # print(languageChosen)
            # print(translatedString.text)
            # print(i)
            i += 1
        except KeyboardInterrupt:
            print("Program interrupted by user. Thank you for using Translator-inator")
            exit()
        except:
            exit('Google is angry at us for calling them too many times. Try again later')
        
    else:    
        print('success!')
        time.sleep(2)
        backToStart()


# This function translate the very scrambled text back to english and serves it to the user
def backToStart():
    print('Translating back to original language')
    time.sleep(1)
    for x in range(6):
      print(".  ", end="", flush=True)
      time.sleep(1)
    print('')
    translatoredString = translator.translate(stringToTranslate, dest=startingLanguage)
    print('Results: ')
    print(translatoredString.text)


# Terms and conditions basically
def welcomeToMyJungle():
    print('Welcome! Thank you for using my Translator-Inator! Patent pending!')
    time.sleep(3)
    print('Please be aware this program techncially abuses an API by submitting neumerous calls in a matter of moments')
    time.sleep(3)
    print('This may anger the powers that be, so use at your own risk')
    time.sleep(3)
    
    consent = yesno('Do you wish to continue and accept responsibility for your actions here today (press ENTER after selection)')
    if consent == True:
        makeItGo()
    else:
        exit('Thank you for flying with DoofAir')


# this function makes it all go and controls the order
def makeItGo():
        takeString()
        takeInput()
        letChaosReign()
   
# calling the funciton that makes it all go.
welcomeToMyJungle()