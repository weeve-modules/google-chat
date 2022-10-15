"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from json import dumps
from httplib2 import Http
import os

log = getLogger("module")


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Sending message to Google Chat ...")

    try:
        http_obj = Http()
        resp = http_obj.request(
            uri=os.getenv("WEBHOOK_URL"),
            method="POST",
            headers={
                "Content-Type": "application/json; charset=UTF-8"
            },
            body=dumps(
                {
                    'text': received_data[os.getenv("MESSAGE_LABEL")]
                }
            ),
        )

        if resp[0].status != 200:
            return f"Error when sending data to Google Chat. Server response: {resp[0].status}, {resp[1]}. Check provided Webhook URL."

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
