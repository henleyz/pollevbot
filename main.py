
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
PRESENTER_CODE = "henleyzhang720"

def main():
        #TODO change where your chrome webdriver is
        service = Service("C:\\Users\\henle\\Desktop\\chromedriver.exe")

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        #TODO Replace "henle" with your user folder name
        options.add_argument("user-data-dir=C:\\Users\\henle\\AppData\\Local\\Google\\Chrome\\User Data")

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
                time.sleep(60)
            except:
                time.sleep(1)
                print("Checking for polls")

main()


