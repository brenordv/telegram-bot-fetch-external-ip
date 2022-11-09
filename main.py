# -*- coding: utf-8 -*-
import logging
import time

from bot_helper import start_bot

wait_in_seconds_between_retries = 30
try_count = 0


def main(token: str, chat_id: int):
    global try_count
    logging.basicConfig(level=logging.INFO)
    try:

        start_bot(token=token, chat_id=chat_id)

    except Exception:
        logging.exception(f"Bot failed for some reason. Waiting {wait_in_seconds_between_retries} to try again.")
        time.sleep(wait_in_seconds_between_retries)

        try_count += 1
        logging.info(f"Starting retry #{try_count}")

        main(token=token, chat_id=chat_id)


if __name__ == '__main__':
    main(
        token="your bot token here",
        chat_id=00000000  # < your chat_id there
    )
