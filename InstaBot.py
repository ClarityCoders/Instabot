from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(browser):
    browser.get("https://www.instagram.com/?hl=en")
    time.sleep(5)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")

    #YOUR USERNAME GOES HERE
    username.send_keys("my_username")
    #YOUR Password GOES HERE
    password.send_keys("mypass291")
    login.click()



    time.sleep(5)


def Vist_Tag(browser, url):
    sleepy_time = 5
    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    image_count = 0

    for picture in pictures:
        if image_count >= 3:
            break

        picture.click()
        time.sleep(sleepy_time)

        heart = browser.find_element_by_css_selector("[aria-label='Like']")
        heart.click()

        close = browser.find_element_by_css_selector("[aria-label='Close']")
        close.click()

        image_count += 1
        time.sleep(sleepy_time)

def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = [ 
        "programming",
        "softwaredeveloper",
        "programminglife",
        "programmerslife",
        "programmerlife",
        "developerlife",
        "programmers",
    ]

    while True:
        for tag in tags:
            Vist_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(3600)

main()
