from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(browser):
    browser.get("https://www.instagram.com/?hl=en")
    time.sleep(5)

    username_element = browser.find_elements_by_css_selector( "[aria-label='Phone number, username, or email']" ) 
    password_element = browser.find_elements_by_css_selector( "[aria-label='Password']" )
    login_button = browser.find_elements_by_css_selector("button")
    # "button[class='sqdOP  L3NKy   y3zKF     ']"

    input_username = username_element[0]
    input_password = password_element[0]
    input_login = login_button[0]

    input_username.send_keys("j_low_17")
    input_password.send_keys("test17!91")
    input_login.click()
    time.sleep(5)

def Visit_Tag(browser, url):
    sleepy_time = 4
    image_count = 0
    try:
        browser.get(url)
        time.sleep(sleepy_time)
        
        input1_elem = browser.find_elements_by_css_selector("div[class='_9AhH0']")
        for image in input1_elem:
            if image_count > 3:
                break
            image.click()
            time.sleep(sleepy_time)
            no_results = browser.find_elements_by_css_selector("[aria-label='Unlike']")
            image_count += 1
            if len(no_results) == 0:
                heart_locator = "button[class='wpO6b ']"
                heart_elm = browser.find_elements_by_css_selector(heart_locator)
                heart_button = heart_elm[0]
                heart_button.click()
                time.sleep(sleepy_time)
            close = browser.find_elements_by_css_selector("[aria-label='Close']")
            print(close[0])
            close[0].click()
        

    except Exception as e:
        print("error in process_jobs")
        print("\n")
        print(str(e) + "\n")


def main():
    tags = [ 
            "programming",
            "softwaredeveloper",
            "programminglife",
            "programmerslife",
            "programmerlife",
            "developerlife",
            "programmers",
        ]
    browser = webdriver.Chrome()
    login(browser)

    for tag in tags:
        Visit_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}/")

    


main()