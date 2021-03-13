#import os
#import time
#import playsound
#import random
#from gtts import gTTS
#import PyAudio
import speech_recognition as sr
import subprocess
import pyttsx3
import webbrowser
import pygame,sys
import Mirascreen
import threading
#**********************************************************************************************************************

#commit
class myFred(threading.Thread):
    def __init__(self, iD):
        threading.Thread.__init__(self)
        self.iD = iD
    def run(self):
        if self.iD == 1:
        # *****************************************Anzeige**************************************************************
            x = 1960
            y = 1080
            pygame.init()                                  # startet das spiel
            fenster = pygame.display.set_mode((x, y))      # erstellt das fenster
            # fenster.fill((210, 121, 166))
            pygame.display.update()
            sprites = pygame.sprite.Group()                # erstellt die gruppe sprites
            sprites.add(Mirascreen.Mira(x, y))             #|fügt die sprites zur gruppe hinzu
            sprites.add(Mirascreen.Diamond(x, y))          #|
            sprites.add(Mirascreen.Frame(x, y))            #|
            ###sprites.draw(fenster)                       #zeichnet die sprites auf das Fenster
            pygame.display.update()
            # **********************************************************************************************************
            display_surface = pygame.display.set_mode((x, y))

            pygame.display.set_caption('Show Text')        #erstellt den Pygame Fernsternamen

            font = pygame.font.Font('freesansbold.ttf', 32)#erstellt ein font Objekt (font file, size of text)

            text = font.render('Ich bin Mira!', True,      #erstellt ein surface Objekt auf das der Text gezeichnet wird
                               (255, 255, 255),            #textfarbe
                               (210, 121, 166))            #hintergrundfarbe
            textRect = text.get_rect()                     #erstellt ein rechteckiges Objekt für das surface Objekt

            textRect.center = (x // 2, (y // 2) - 200)     #setzt die Mitte des rechteckigen objekts
            while True:
                fenster.fill((210, 121, 166))
                sprites.draw(fenster)
                # display_surface.fill((255,255,255))
                display_surface.blit(text, textRect)       #kopiert den Text auf die Mitte des surface Objekts

                for event in pygame.event.get():           #iteriert über die events in pygame
                    if event.type == pygame.QUIT:
                        pygame.quit()                      #deaktiviert pygame
                        quit()                             #beendet das programm
                    pygame.display.update()                #zeichnet das surface Objekt auf den Bildschirm
                # ******************************************************************************************************
        if self.iD == 2:
            zahl = 1

            def speak(text):
                converter = pyttsx3.init()                  #initialisiert den converter
                voices = converter.getProperty('voices')
                converter.setProperty('voice', voices[0].id)#setzt die stimme
                converter.setProperty('rate', 170)          #setzt die Sprechgeschwindigkeit, kann mehr als 100 sein
                converter.setProperty('volume', 0.7)        #setzt das vollumen (zwischen 0 und 1)

                while converter.say(text):
                    Mirascreen.miratalk()                   #führt miratalk aus solange gesprochen wird

                converter.runAndWait()                      #lehrt die say() schlange, das programm bleibt stehen bis fertig gesprochen

            def get_audio():
                r = sr.Recognizer()

                with sr.Microphone() as source:
                    print("listening...")
                    audio = r.listen(source)
                    said = ""
                    try:
                        said = r.recognize_google(audio, language="de")
                        print(said)
                    except Exception as e:
                        speak(" Ich habe dich nicht verstanden")
                        print(e)
                return said.lower()

            def note(text, zahl):
                punctuation = {"punkt": ".", "enter": "\n", "komma": ","}
                # for phrase in punctuation:
                # if phrase in text and phrase=="now point":
                # text.replace(phrase,punctuation.get(phrase))
                text.replace("punkt", ".")
                filename = str(zahl) + "-note.txt"
                with open(filename, "wb"):
                    subprocess.Popen(["notepad.exe", filename])

            # **********************************************************************************************************

            text = get_audio()

            GREETINGS = ["hallo", "guten morgen", "morgen", "hi", "hey"]
            if "mira" in text:
                if "sag hallo zu " in text:
                    w = text.index("u") + 1
                    z = len(text)
                    speak("hallo" + text[w:z] + ". wie geht es dir?")
                else:
                    for phrase in GREETINGS:
                        if phrase in text:
                            speak(phrase + ",wie geht es dir?")
                            break

                NOTES = ["schreib was auf", "mach notizen", "schreib etwas auf"]
                for phrase in NOTES:
                    if phrase in text:
                        speak("was soll ich für dich aufschreiben?")
                        note(get_audio(), zahl)

                if "chrome" in text:
                    webbrowser.open('http://google.co.kr', new=2)
                    speak("was soll ich eingeben?")
                    text = get_audio()
                    """with open("chrome.exe") as k:
                         f.write(str(text))
                     #    subprocess.Popen(["chrome.exe", filename])
                         zahl += 1"""
#*************************************************************************************************************************
t1 = myFred(1)#erstellt den ersten Thread
t2 = myFred(2)#erstellt den zweiten Thread
t1.start()#startet den ersten Thread
t2.start()#startet den zweiten Thread

"""TO DO:
    -kommentieren(!)
    -code aufräumen
    -persönliche begrüßung+
    -dinge in browerfenster schreiben
    """



