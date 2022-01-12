import datetime
import time
from typing import Union


class Prompt(object):
    """
    A class to provide simple creation of User Prompts.

    :param message: string to flash in the Message
    :type message: str, required
    :param timeout_s: the length of time in seconds before the Recipe
        resumes execution if the Input has not been executed, set to None
        or leave blank to disable a time-out, should be number-like
    :type timeout_s: float, int, str, None, optional
    """
    message = None
    timeout_s = None
    start_time = None
    __user_id__ = None

    __DELAY_S = 0.5

    def __init__(self, message: str, timeout_s: Union[int, str]):
        """
        Constructor method.
        """
        self.start_time = datetime.datetime.now()
        self.message = message
        self.timeout_s = timeout_s

    def __bool__(self):
        """
        Override the built-in truth value testing.

        A prompt will return `True` when a truthiness
        test is performed until it has been dismissed by a
        User.

        :return: None
        """
        # add a small time delay to avoid continually hitting memory
        time.sleep(self.__DELAY_S)
        return False