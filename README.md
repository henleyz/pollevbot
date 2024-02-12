# Pollevbot

Pollevbot is a simple bot designed to automatically respond to PollEv questions in a class.

## Usage

1. **Install selenium:**

    ```bash
    pip install selenium
    ```

2. **Install the Chrome driver:**
   - Download the Chrome driver from [here](https://sites.google.com/chromium.org/driver/).
   - Set the path of the Chrome driver in the `chrome_driver_path` variable in `config.json`.

3. **Get the user data path so that you stay logged in to PollEv:**
   - In Google Chrome, open a new tab and type `chrome://version`.
   - Copy the profile path and set it in the `user_data_path` variable in `config.json`.

4. **Set the presenter code in `config.json` or pass it as an argument to the main function.**

5. **Run the bot:**

    ```bash
    python main.py [optional presenter code]
    ```