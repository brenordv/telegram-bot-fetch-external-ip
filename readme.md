# Telegram bot: External IP fetcher

_Quick-N-Dirty edition_

This is a simple Telegram bot that will fetch the external IP whenever it receives the `/ip` command.

It was designed to be resilient and keep going even when any errors happen. Is this a good thing? For this use case, yes. (but not always...) 


# How to use
## 1: Create a Bot
Follow this tutorial to create a Bot and get the token: https://core.telegram.org/bots/tutorial#obtain-your-bot-token

## 2: Get your chat_id
Since the bot will only answer to one person, you must find out your user_id (aka: chat_id)

To do that, follow this tutorial: https://www.alphr.com/find-chat-id-telegram/

## 3: Add token + chat_id to main.py
Open file `main.py` and add your data there.
> Attention: Careful not to add your secrets to a public repository. Don't do that, please!

Let's say your token is `1a2b3c-4d-5e-6f-7g` and your chat_id is `42`.
In your `main.py` file, the call to main method should be something like this:
```python
    main(
        token="1a2b3c-4d-5e-6f-7g",
        chat_id=42
    )
```

## 4: Install Python requirements.
This bot requires Python 3.9+ to work and relies on two packages:
1. requests
2. python-telegram-bot

To install all dependencies, while in root folder of the project, run the command:
```shell
pip install -r requirements.txt
```

## 5: Run the bot!
To start the bot, run the command:
```shell
python main.py
```
