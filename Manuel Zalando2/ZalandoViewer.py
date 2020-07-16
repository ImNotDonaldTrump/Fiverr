#import section

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import sys

#begin variables

url = input("[+] URL : ")
driver = webdriver.Chrome()
openUA = open("User_Agent", "r")
usrAgt = openUA.read()

#defining User agent, product, etc
headers = {"User-Agent" : usrAgt}
page = requests.get(url, headers=headers)
driver.get(url)
notAvailable = ""
notAvailableC = False

#starting
print("")
print("[+] Seite geöffnet") #site opened
print("[+] Bitte Größe auswählen")
ready = input("[+] Programmm starten ? y/n :") #Start the prgram ? y/n
rd = "n"

if ready == "y":
    rd = "y"
else:
    sys.exit()

#loop for checking if product is available

while rd == "y":
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        notAvailable = driver.find_element_by_xpath('//*[@id="z-pdp-topSection"]/button/span[1]')


    except Exception:
        print(notAvailable)
        time.sleep(5)
        print("[+] Produkt verfügbar -> gehe zum Kauf")


    if notAvailable != "":
        notAvailableBool = True
        #print(notAvailable)
    else:
        notAvailableBool = False
        print(notAvailable)

    if notAvailableBool == False:
        addToBag = driver.find_element_by_xpath('//*[@id="z-pdp-topSection"]/div[1]/div/div[2]')
        addToBag.click()
        goToBag = driver.find_element_by_xpath(
            '//*[@id="z-navicat-header-root"]/header/div[2]/div/div/div/div/z-grid/z-grid-item/div/div[1]/div[3]/div/div[4]/a')
        goToBag.click()
        time.sleep(1)
        goToCheckOut = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/button/div')
        goToCheckOut.click()
        goToBuy = driver.find_element_by_id('payz-selection-bottom-submit')
        goToBuy.click()
        print("[+] Produkt gekauft")

    else:
        print("[+] Produkt nicht verfügbar !")
        time.sleep(3)