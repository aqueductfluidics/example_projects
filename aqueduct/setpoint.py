import datetime
import io
import time
import threading
from types import ModuleType
from typing import Union, Callable


ALLOWED_DTYPES = [
    int.__name__, 
    float.__name__, 
    bool.__name__, 
    list.__name__, 
    datetime.__name__, 
    str.__name__
]


class Setpoint(object):
    """
    A class to provide simple interaction with Recipe values that
    appear as User Params on the Aqueduct Recipe Builder UI.

    :param name: name of the Setpoint, will be displayed on the UI, should be unique
    :type name: str, required
    :param value: value to be assigned to the Setpoint on creating
    :type value: float, int, bool, str, datetime.datetime, list, required
    :param dtype: specify the type of value, used to ensure that Users cannot
        enter an invalid value
    :type dtype: {'int', 'float', 'bool', 'list', 'datetime', 'str'}, optional
    """

    name: str = None
    value: Union[float, int, bool, str, datetime.datetime, list] = None
    dtype: str = None
    timestamp = None
    on_change: Callable = None
    args: list = []
    kwargs: dict = {}

    __user_id__: str = None
    __aqueduct__: "Aqueduct" = None

    def __init__(self, name: str, value: Union[float, int, bool, str, datetime.datetime, list], dtype: str = None):
        """
        Constructor method.
        """

        if dtype is None:
            try:
                dtype = type(value).__name__
                if dtype not in ALLOWED_DTYPES:
                    raise ValueError("Object of type {} is not allowed as a Setpoint".format({dtype}))
            except Exception:
                raise ValueError("Invalid Aqueduct Setpoint")

        self.name = name
        self.value = value
        self.dtype = dtype

    def __del__(self):
        """
        Destructor method.
        """
        if self.__aqueduct__ is not None:
            try:
                self.__aqueduct__.__setpoints__.pop(self.name)
            except KeyError:
                pass

    def __update__(self) -> None:
        """
        Private method to update the setpoint. Not for API use.

        :return:
        """
        return

    def get(self):

        return self.value

    def update(self, value):

        self.value = value
        self.__update__()