import datetime
import time
from enum import Enum
from typing import Union


class UserInputTypes(Enum):
    DROPDOWN = 'dropdown'
    TEXT_INPUT = 'text_input'
    BUTTONS = 'buttons'
    TABLE = 'table'
    CSV_UPLOAD = 'csv'


class Input(object):
    """
    A class to provide simple User Input interaction
    during a Recipe.

    :param message: string to flash in the Input
    :type message: str, required
    :param timeout_s: the length of time in seconds before the Recipe
        resumes execution if the Input has not been executed, set to None
        or leave blank to disable a time-out, should be number-like
    :type timeout_s: float, int, str, None, optional
    :param input_type: specify the type of Input pop-up to display
    :type input_type: {'text_input', 'dropdown', 'buttons'}, defaults to 'text_input'
    :param options: list of allowable options for dropdown menu, only used for input_type 'dropdown'
    :type options: {'list'}
    :param rows: list of row input fields, only used for input_type 'table'
    :type rows: {'list'}
    :param dtype: specify the type of value, used to ensure that Users cannot
        enter an invalid value
    :type dtype: {'int', 'float', 'bool', 'list', 'datetime', 'str'}, optional
    """

    message = None
    timeout_s = None
    start_time = None
    input_type = None
    options = []
    rows = []
    dtype = None
    __user_id__ = None

    __DELAY_S = 0.5

    def __init__(
        self, 
        message: str, 
        timeout_s: Union[int, str],
        input_type: str = UserInputTypes.TEXT_INPUT.value,
        options: list = None, 
        rows: list = None, 
        dtype: str = None
    ):
        """
        Constructor method.
        """
        if options is None:
            options = []

        if rows is None:
            rows = []

        self.start_time = datetime.datetime.now()
        self.message = message
        self.timeout_s = timeout_s
        self.input_type = input_type
        self.options = options
        self.rows = rows
        self.dtype = dtype

    def __bool__(self):
        """
        Override the built-in truth value testing.

        A prompt will return `True` when a truthiness
        test is performed until it has been dismissed by a
        User.

        :return: None
        """
        time.sleep(self.__DELAY_S)        
        return False

    def is_set(self) -> bool:
        """
        Check's to see whether the input value has been entered.

        Returns `True` if the value has been set and `False`
        if the value has not been set.

        :return: truthiness for whether the Input has been set or not
        :rtype: bool
        """
        return False

    def get_value(self, delete_if_set: bool = True):
        """
        Read the value from the user input.

        If `delete_if_set` is set to `True`, will delete the input upon readout
        if the Input has been executed.

        :param delete_if_set:
        :type delete_if_set: bool, defaults to True
        :return: Input's value
        :rtype: {'int', 'float', 'bool', 'list', 'datetime', 'str'}
        """
        return None