from selenium import webdriver
import time
from pynput.mouse import Button, Controller

import selenium
driver = webdriver.Chrome()
driver.get("https://outlook.live.com")
mouse = Controller()


print("-------------------------------------------------")
print("Bitte Loggen sie sich ein")
print("Bitte gehen sie zu den Einsteelungen in outlook. ")
print("Bitte gehen sie zu E-Mail und dann zu Junk-E-Mail")
print("Das programm übernimmt danach.")
print("-------------------------------------------------")

conti  = input("Eingeloggt ? (y/n) : ")



if conti == "y":
    with open("E-mails", "r") as eo:
        print("")
        ae = 0
        for line in eo:
            print(line, end='')
            ae = ae + 1
            print(ae)
            time.sleep(0.25)
            mouse.click(Button.left, 1)
            time.sleep(111)

else:
    print("Loggen sie sich bitte ein")













