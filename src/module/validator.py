"""
Validates whether the incoming data has an acceptable type and structure.

Edit this file to verify data expected by you module.
"""

from logging import getLogger
import os

log = getLogger("validator")


def data_validation(data: any) -> str:
    """
    Validate incoming data i.e. by checking if it is of type dict or list.
    Function description should not be modified.

    Args:
        data (any): Data to validate.

    Returns:
        str: Error message if error is encountered. Otherwise returns None.

    """

    log.debug("Validating ...")

    try:
        # YOUR CODE HERE

        allowed_data_types = [dict]

        if not type(data) in allowed_data_types:
            return f"Detected type: {type(data)} | Supported types: {allowed_data_types} | invalid!"

        if not os.getenv("MESSAGE_LABEL") in data.keys():
            return f"Provided message label ({os.getenv('MESSAGE_LABEL')}) is not in the received data. Received labels: {list(data.keys())}"

        return None

    except Exception as e:
        return f"Exception when validating module input data: {e}"
