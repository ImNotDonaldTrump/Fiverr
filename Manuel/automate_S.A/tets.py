from pynput.mouse import Button, Controller
import time
import keyboard
import copy
import pyperclip
mouse = Controller()
ae = 0
inp1 = False

print("-------------------------------------------------")
print("Bitte Loggen sie sich in OutLook ein")
print("Bitte gehen sie zu den Einstellungen in Outlook. ")
print("Bitte gehen sie zu E-Mail und dann zu Junk-E-Mail")
print("Gehen sie mit dem Cursor zu 'Sichere Absender und Domänen' .")
print("Das Programm übernimmt nun")
print("-------------------------------------------------")

inp = input("Sind sie bereit ? (y/n) : ")
if inp == "y":
    inp1 = True

else:
    print("Bitte Loggen sie sich ein.")

time.sleep(2)
print("Programm startet in 5 Sekunden")
time.sleep(1)
print("Programm startet in 4 Sekunden")
time.sleep(1)
print("Programm startet in 3 Sekunden")
time.sleep(1)
print("Programm startet in 2 Sekunden")
time.sleep(1)
print("Programm startet in 1 Sekunden")
time.sleep(1)



import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)



while inp1 == True:
    with open("E-mails", "r") as eo:


        for line in eo:
            line = line
            cp = copy.copy(line)
            ae = ae + 1
            print(ae)
            print(cp)
            mouse.click(Button.left, 1)
            addToClipBoard(line)
            keyboard.press("strg")
            keyboard.press("v")
            time.sleep(0.25)
            keyboard.press("enter")
        inp1 = False
print("")
print("Alle Emails hinzugefügt.")







