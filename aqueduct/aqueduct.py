import datetime
import io
import time
import threading
from types import ModuleType
from typing import Union

from .recordable import Recordable
from .setpoint import Setpoint, ALLOWED_DTYPES
from .user_prompt import Prompt
from .user_input import Input, UserInputTypes


def private() -> None:
    return


class Aqueduct(object):
    """
    A class to help with Recipe execution and monitoring and User Interface input/outputs.

    When a Recipe is run using the Aqueduct Compile method from the Recipe Builder
    page, an :class:`Aqueduct` instance is created by default and the appropriate
    `user_id`, `pid`, `out`, and `err` parameters are provided.

    By default, the instance is named `aqueduct` and is added to the Globals
    dictionary that your code inherits. This means that you can use any
    instance methods for the :class:`Aqueduct` object in your code using...

    .. code-block:: python

            # this is done by default for any Recipes executed through
            # the Aqueduct Compile and Run methods
            aqueduct = Aqueduct(...)

            # so you can do this...
            aqueduct.prompt(...)
            aqueduct.input(...)
            aqueduct.setpoint(...)


    :param user_id: user_id
    :type user_id: str, required
    :param pid: process ID number for the Python interpreter that's executing the Recipe
    :type pid: int, required
    :param out: pointer to an IO stream to direct stdout stream
    :type out: io.TextIOWrapper, required
    :param err: pointer to an IO stream to direct stderr stream
    :type err: io.TextIOWrapper, required
    """

    def __init__(self, user_id: str, pid: int, out: io.TextIOWrapper, err: io.TextIOWrapper):
        """
        Constructor method.
        """
        self.__user_id__: str = user_id
        self.__pid__: int = pid
        self.__line_offset__: int = 0
        self.__values_to_save__: list = []
        self.__out__: io.TextIOWrapper = out
        self.__err__: io.TextIOWrapper = err
        self.__config__: ModuleType = None
        self.__update_interval_s__: int = 1.
        self.__helper__ = None
        self.__print__ = None
        self.__recordables__: dict = dict()
        self.__setpoints__: dict = dict()

    def __is_lab_mode__(self) -> bool:
        if self.__user_id__ == getattr(self.__config__, 'LAB_MODE_USER_ID', None):
            return True
        else:
            return False

    def __start__(self, g: dict) -> None:
        """
        Method run just prior to execution of the Recipe code.

        Redefines builtin method `print` method based on the configuration to the direct the
        output to a text file or memory.

        When run locally on a Hub, directs the output to the Aqueduct log file for a user
        located at ~/aqueduct_app/temp/__recipe__.XXX.log where XXX is the user_id.
        XXX = 'L' for lab mode.

        :param g: globals dictionary passed from script run prior to main code
            execution that contains keys for Devices, Containers, and Connections
        :type g: dict
        :return: None
        """

        def print(*s):
            __builtins__.get('print')(*s, end='')

        self.__print__ = print

        g['print'] = print

        t = threading.Thread(target=self.__helper__.run, daemon=True)
        t.start()

    def __finish__(self) -> None:
        """
        Method run after Recipe code execution.

        Marks the User's Recipe as complete in memory.

        :return: None
        """
        private()

    def __set_line_offset__(self, offset: int) -> None:
        """
        Helper method to set the number of line offsets to include for
        User recipe error reporting.

        :param offset: number of offset lines
        :type offset: int
        :return: None
        """
        private()

    @property
    def hub_sn(self) -> Union[int, str, None]:
        if isinstance(self.__config__, ModuleType):
            return self.__config__.SERIAL_NUMBER
        else:
            return None

    def is_lab_mode(self) -> bool:
        """
        Helper method to check whether the Recipe is being run in Lab Mode or Sim Mode.

        :return: is lab mode ?
        :rtype: bool
        """
        return self.__is_lab_mode__()

    def prompt(self, message: str = None, timeout_s: Union[int, float] = None, pause_recipe: bool = True) -> Prompt:
        """
        Create a user prompt.

        If `pause_recipe` is set to True, the recipe will be paused immediately and remain
        paused until the prompt is executed. For example, the following block of code will
        flash a User prompt and immediately pause the recipe -- this will prevent any
        other code from executing.

        .. code-block:: python

            # use the instantiated Aqueduct object to make a prompt
            aqueduct = Aqueduct(...)
            aqueduct.prompt(message="Stop!", pause_recipe=True)
            # recipe now paused here


        If `pause_recipe` is set to False, the recipe will continue to run. This is useful for
        continuing to monitor and log data until the prompt has been dismissed.

        .. code-block:: python

            # use the instantiated Aqueduct object to make a prompt
            aqueduct = Aqueduct(...)
            p = aqueduct.prompt(message="Stop! (but I'll keep working...)", pause_recipe=False)

            # the prompt will return True for a truthiness test
            # until it's been executed
            while p:
                # do some work
                monitor()
            # will get here when prompt dismissed

        If the `timeout_s` value is set to a non-None value, the Prompt will only block
        for the set period of time (in seconds), at which point the Prompt will expire.

        Param `timeout_s` defaults to None, which never times-out.

        .. code-block:: python

            # use the instantiated Aqueduct object to make a prompt
            aqueduct = Aqueduct(...)
            p = aqueduct.prompt(message="Stop! (but I'll keep working...)", timeout_s=10)

            # this code will execute when the prompt has been executed or after 10 seconds



        :param message: string to flash in the Prompt
        :type message: str
        :param timeout_s: number-like value for a timeout value in seconds
        :type timeout_s: int, float, defaults to None
        :param pause_recipe: bool, set to True to stop recipe execution until the Prompt is dismissed
        :type pause_recipe: bool
        :return: Prompt
        :rtype: Prompt
        """
        p = Prompt(message, timeout_s)
        p.__user_id__ = self.__user_id__
        private()
        return p

    def input(
        self,
        message: str = None, 
        timeout_s: Union[int, float] = None, 
        pause_recipe: bool = True,
        input_type: str = UserInputTypes.TEXT_INPUT.value,
        options: list = None, 
        rows: list = None, 
        dtype: str = None
    ) -> Input:
        """
        Create a user input.

        If `pause_recipe` is set to True, the recipe will be paused immediately until the
        input is entered. For example, the following block of code will flash a User input
        and immediately pause the recipe -- this will prevent any other code from executing.

        .. code-block:: python

            aqueduct = Aqueduct(...) # create the Aqueduct instance
            aqueduct.input(message="Enter your name!", pause_recipe=True, input_type="text_input", dtype="str")


        If `pause_recipe` is set to False, the recipe will continue to run. This is useful for
        continuing to monitor and log data until the input has been entered.

        .. code-block:: python

            aqueduct = Aqueduct(...) # create the Aqueduct instance
            input = aqueduct.input(message="Enter your name!", pause_recipe=False, input_type="text_input", dtype="str")
            while input:
                # do some work
                monitor()
            # will get here when input is entered

        If the `timeout_s` value is set, the Input will only block for the set period of time.
        Defaults to None, which never times-out.


        :param message: string to flash in the Input
        :param timeout_s: number-like value for a timeout value in seconds
        :param pause_recipe: bool, set to True to stop recipe execution until the Input is executed
        :param input_type:
        :param options:
        :param rows:
        :param dtype:
        :return: Input
        """
        if options is None:
            options = []

        if rows is None:
            rows = []

        i = Input(
            message=message,
            timeout_s=timeout_s,
            input_type=input_type,
            options=options,
            rows=rows,
            dtype=dtype
        )

        i.__user_id__ = self.__user_id__

        private()
        return i

    def log(self, data: str) -> None:
        """
        Record data to the Aqueduct log file.

        Prepends a timestamp with the ISO format 'YYYY-MM-DD HH:MM:SS.mmmmmm'.

        Only functions for a Hub installation deployment.

        :param data: string to be saved as a line in the log file
        :type data: str
        :return: None
        """
        string = datetime.datetime.now().isoformat() + ': ' + str(data)
        private()


    def setpoint(
        self, 
        name: str, 
        value: Union[float, int, bool, str, datetime.datetime, list],
        dtype: str = None
    ) -> Setpoint:
        """
        Create a Setpoint.

        Setpoints are values that can be edited from the Recipe Builder page and then used internally in
        Recipe Logic.

        .. code-block:: python

            aqueduct = Aqueduct(...) # create the Aqueduct instance
            sp = aqueduct.setpoint(name="counter", value=0, dtype="int")

            print(sp.get())
            # prints 0

        :param value: value to assign to the setpoint
        :param name: name to assign to the setpoint
        :param dtype: type of value
        :type dtype: {"float", "int", "bool", "str", "datetime.datetime", "list"}
        :return: Setpoint
        """
        s = Setpoint(name, value, dtype)
        s.__user_id__ = self.__user_id__
        s.__aqueduct__ = self
        self.__setpoints__.update({name: s})
        s.__update__()
        return s

    def recordable(
        self, 
        name: str, 
        value: Union[float, int, bool, str, datetime.datetime, list],
        dtype: str = None
    ) -> Recordable:
        """
        Create a Recordable.

        Recordables are can be used to associate data with a timestamp. Active `Recordables`
        are visible in the user interface in chart and tabular format.

        .. code-block:: python

            aqueduct = Aqueduct(...) # create the Aqueduct instance
            my_recordable = aqueduct.recordable(name="counter", value=0, dtype="int")

            time.sleep(1)

            my_recordable.update(5)
            # records the value 5

        :param value: value to assign to the setpoint
        :param name: name to assign to the setpoint
        :param dtype: type of value
        :type dtype: {"float", "int", "bool", "str", "datetime.datetime", "list"}
        :return: Setpoint
        """
        r = Recordable(name, value, dtype)
        r.__user_id__ = self.__user_id__
        r.__aqueduct__ = self
        self.__recordables__.update({name: r})
        r.__update__()
        return r

    def save_log_file(self, filename: str, timestamp: bool = False, overwrite: bool = False) -> None:
        """
        Save the recipe log file permanently.

        :param filename: assign a filename to the log file
        :param timestamp: if set to True, append a timestamp to the filename
        :param overwrite: if set to True, will overwrite an existing filename with the same filename, otherwise
            will append an incrementing number to make the filename unique
        :return: None
        """
        private()
