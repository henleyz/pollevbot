# Pollevbot

Pollevbot is a simple bot designed to automatically respond to PollEv questions in a class.

## Usage

1. **Install selenium and web driver manager:**

    ```bash
    pip install selenium
    ```

    ```bash
    pip install webdriver_manager
    ```

3. **Get the user data path so that you stay logged in to PollEv:**
   - In Google Chrome, open a new tab and type `chrome://version`.
   - Copy the profile path and set it in the `user_data_path` variable in `config.json`.

4. **Set the presenter code in `config.json` or pass it as an argument to the main function.**

5. **Run the bot:**

    ```bash
    python main.py [optional presenter code]
    ```

    Press q to quit.

Note: I don't condone the use of this bot for any abuse or academic dishonesty. It was only created so I don't miss polls when I randomly zone out in class.