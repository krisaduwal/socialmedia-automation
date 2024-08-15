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

option = webdriver.ChromeOptions()
# option.add_argument("start-maximized")
# option.add_argument("diasable-infobars")

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")

driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")
driver.maximize_window()
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

    # time.sleep(2)

    driver.implicitly_wait(30)
    notNow = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    notNow.click()
    print("clicked")
    #
    # text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[1]/div[2]/div/div[3]/div/span/span/text()").text
    # assert "INSTAGRAM" in text
    # print("login test passed")
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

# def follow():
    # time.sleep(2)
    # driver.switch_to.window(driver.current_window_handle)
    # driver.implicitly_wait(30)
    # print("ready to follow")
    # followElement = driver.find_element(By.XPATH, "")
    # print("follow button liyo")
    # followElement.click()
    # driver.implicitly_wait(30)

def message():
    time.sleep(2)
    msgElement = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[2]")
    msgElement.click()

    driver.switch_to.window(driver.current_window_handle)
    driver.implicitly_wait(30)

    msgtoSend = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div")
    msgtoSend.click()
    inputText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/p")
    inputText.send_keys("hi princess")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]").click()
    print("message sent")

    # time.sleep(10)

def profileVisit():
    time.sleep(3)
    visit = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/a/div/div/span/span")
    visit.click()
def findPost():
    time.sleep(2)
    post = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div/div[1]/div[1]/a/div[1]")
    post.click()
    # time.sleep(1)
    # time.sleep(1)
    # driver.implicitly_wait(30)
    print("waiting")


def likePost():
    # time.sleep(2)
    # like = driver.find_element(By.CLASS_NAME,'fr66n')
    # soup = bs(like.get_attribute('innerHTML'),'html.parser')
    #   if(soup.find('svg')['aria-label'] == 'Like'):
    #     like.click()
    # time.sleep(2)

    time.sleep(2)
    print("almost liking")
    driver.switch_to.window(driver.current_window_handle)

    postTolike = driver.find_element(By.CSS_SELECTOR,"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x78zum5.x1q0g3np.xwib8y2.x1yrsyyn.x1xp8e9x.x13fuv20.x178xt8z.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xo1ph6p.x1pi30zi.x1swvt13 > span.x1rg5ohu.xp7jhwk")
    print("found")
    postTolike.click()

    print("liked")
    driver.switch_to.window(driver.current_window_handle)


def comment():
    time.sleep(2)
    print("about to comment")
    driver.find_element(By.XPATH, "/html/body/div[9]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/div").click()
    time.sleep(1)
    # driver.find_element(By.XPATH, "/html/body/div[9]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea").click()
    toComment = driver.find_element(By.XPATH, "/html/body/div[9]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea")
    toComment.send_keys("pretty lady")
    print("comment liyo")
    time.sleep(10)

logIn()
print("search function call")
search()

print("search function call bhayoo")
# follow()
message()
print("message")
profileVisit()
findPost()
likePost()
comment()

driver.close()
