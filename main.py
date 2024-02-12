
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import json
import sys




PRESENTER_CODE = "aried"
CHROME_DRIVER_PATH = "C:\\Users\\henle\\Desktop\\chromedriver.exe"
CHROME_PROFILE_PATH = "C:\\Users\\henle\\AppData\\Local\\Google\\Chrome\\User Data"

#get vars from config.json
with open('config.json') as f:
    data = json.load(f)
    PRESENTER_CODE = data['presenter_code']
    CHROME_DRIVER_PATH = data['chrome_driver_path']
    CHROME_PROFILE_PATH = data['chrome_profile_path']


if len(sys.argv) > 1:
    PRESENTER_CODE = sys.argv[1]

def main():
        #TODO change where your chrome webdriver is
        service = Service(CHROME_DRIVER_PATH)

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        #TODO Replace "henle" with your user folder name
        options.add_argument("user-data-dir=" + CHROME_PROFILE_PATH)

        options.add_argument('--profile-directory=Default')


        driver = webdriver.Chrome(service=service, options=options)
        url = 'https://pollev.com/' + PRESENTER_CODE
        driver.get(url)


        # wait for the page to load
        time.sleep(2)

        while True:
            try:
                #check for ranking mode 
                number_of_buttons_to_select = 1
                poll_header = driver.find_element(By.XPATH, '//div[@class="component-response-header__status"]')
                header_text = poll_header.text

                # check if poll is locked
                is_locked = "locked" in header_text
                if is_locked:
                    print("Poll is locked, waiting for next poll")
                    time.sleep(1)
                    continue
                
                # check if poll is a select all that apply poll, and select a random number of buttons
                match = re.search(r'\d+', header_text)
                if match:
                    print("Responding to select all that apply poll with " + match.group() + " options")
                    number_of_buttons_to_select = int(match.group())
                    print(number_of_buttons_to_select)
                else:
                        print("Responding to normal MC poll")
                buttons = driver.find_elements(By.XPATH, '//button[@class="component-response-multiple-choice__option__vote"]')
                #get random button
                selected_buttons = random.sample(buttons, number_of_buttons_to_select)
                for button in selected_buttons:
                    button.click()
                    time.sleep(0.5)
                time.sleep(30)
            except:
                #if poll is not found, wait for 1 second and check again
                time.sleep(1)
                print("Checking for polls")

main()


