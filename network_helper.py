# -*- coding: utf-8 -*-
import logging
from typing import Union
from requests import get


def get_external_ip() -> Union[str, None]:
    """
    This method tries to get the external IP using Ipify API.
    If it fails, will return None.
    :return: string containing the IP or None if something bad happens.
    """
    logging.info("Fetching external IP...")
    try:
        ip = get('https://api.ipify.org').content.decode('utf8')
        return ip
    except Exception:
        logging.exception("Failed to get external public IP.")

    return None
