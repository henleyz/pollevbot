import time
import random
import re
import json
import sys
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Global variables
PRESENTER_CODE = "oski"
CHROME_DRIVER_PATH = "C:\\Users\\henle\\Desktop\\chromedriver.exe"
CHROME_PROFILE_PATH = "C:\\Users\\henle\\AppData\\Local\\Google\\Chrome\\User Data"
QUIT_FLAG = False

# Get variables from config.json
with open('config.json') as f:
    data = json.load(f)
    PRESENTER_CODE = data['presenter_code']
    CHROME_DRIVER_PATH = data['chrome_driver_path']
    CHROME_PROFILE_PATH = data['chrome_profile_path']

if len(sys.argv) > 1:
    PRESENTER_CODE = sys.argv[1]

def listen_for_quit():
    global QUIT_FLAG
    while True:
        user_input = input("")
        print("")
        if user_input.lower() == 'q':
            QUIT_FLAG = True
            break

def main():
    global QUIT_FLAG
    # Service setup
    service = Service(CHROME_DRIVER_PATH)

    # Chrome options setup
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("user-data-dir=" + CHROME_PROFILE_PATH)
    options.add_argument('--profile-directory=Default')

    # WebDriver setup
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://pollev.com/' + PRESENTER_CODE
    driver.get(url)

    # Wait for the page to load
    time.sleep(2)

    # Start a thread to listen for quit command
    quit_thread = Thread(target=listen_for_quit)
    quit_thread.start()

    spinny_char = '|'
    while True:
        if QUIT_FLAG:
            break
        spinny_char = next_spinny_char(spinny_char)
        try:
            # Check for ranking mode
            number_of_buttons_to_select = 1
            poll_header = driver.find_element(By.XPATH, '//div[@class="component-response-header__status"]')
            header_text = poll_header.text

            # Check if poll is locked
            is_locked = "locked" in header_text
            if is_locked:
                print(f"Poll is locked, waiting for next poll {spinny_char}", end='\r')
                time.sleep(1)
                continue

            # Check if poll is a select all that apply poll, and select a random number of buttons
            match = re.search(r'\d+', header_text)
            if match:
                print("Responding to select all that apply poll with " + match.group() + " options")
                number_of_buttons_to_select = int(match.group())
            else:
                print("Responding to a normal MC poll")
            
            buttons = driver.find_elements(By.XPATH, '//button[@class="component-response-multiple-choice__option__vote"]')
            # Get random button
            selected_buttons = random.sample(buttons, number_of_buttons_to_select)
            for button in selected_buttons:
                button.click()
                time.sleep(0.5)
            time.sleep(30)
        except:
            # If poll is not found, wait for 1 second and check again
            time.sleep(0.5)
            
            print(f"Checking for polls {spinny_char}", end='\r')

    # Close the WebDriver and join the quit thread
    driver.quit()
    quit_thread.join()


#utility functions
def next_spinny_char(current):
    characters = '|/-\\'
    if current in characters:
        index = characters.index(current)
        next_index = (index + 1) % len(characters)
        return characters[next_index]
    else:
        return characters[0]
    

if __name__ == "__main__":
    main()


