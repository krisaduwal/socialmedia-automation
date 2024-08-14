import time
import os
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

dotenv_path = Path('.venv/.env')
load_dotenv(dotenv_path=dotenv_path)

driver = webdriver.ChromeOptions()
driver.add_argument("start-maximized")
driver.add_argument("diasable-infobars")

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")

driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")
time.sleep(3)

def logIn():
    userElement = driver.find_element(By.XPATH, "//input[@class = '_aa4b _add6 _ac4d _ap35']")
    userElement.send_keys(os.getenv("MYNAME"))
    time.sleep(1)

    passElement = driver.find_element(By.XPATH, "//input[@type = 'password']")
    passElement.send_keys(os.getenv("MYPASS"))
    time.sleep(2)

    buttonElement = driver.find_element(By.XPATH, "//button[@class = ' _acan _acap _acas _aj1- _ap30']")
    buttonElement.click()
    print("login successful!")
    # time.sleep(2)

    driver.implicitly_wait(30)
    notNow = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    notNow.click()
    print("clicked")
    # time.sleep(2)

def search():
    # time.sleep(2)
    # print("error here")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div").click()
    # searchElement.click()
    print("search button clicked")
    time.sleep(1)
    nameSearch = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
    nameSearch.send_keys("bebe_manika")
    profileElement = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div")
    profileElement.click()
    # time.sleep(2)

    # time.sleep(5)

def follow():
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button").click()

def message():
    time.sleep(2)
    msgElement = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[2]")
    msgElement.click()

    driver.switch_to.window(driver.current_window_handle)
    driver.implicitly_wait(30)

    msgtoSend = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div")
    msgtoSend.click()
    inputText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/p")
    inputText.send_keys("hi mini")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]").click()
    print("message sent")


    time.sleep(10)


logIn()
print("search function call")
search()
print("search function call bhayoo")
message()
print("message")

driver.close()
