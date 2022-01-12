import config
import devices.base.obj
from devices.aqueduct.eust.constants import *

from typing import Union, Tuple


def instantiate_device(d_device, setup):
    return EUST(**d_device)


class MixerCommand(object):
    direction: Union[int, str]
    rpm: Union[float, int]

    def __init__(self, **kwargs):
        self.direction = Status.STATUS_CLOCKWISE.value
        self.rpm = 0.

        for k, v in kwargs.items():
            if k in self.__dict__.keys():
                if v is not None:
                    setattr(self, k, v)

    def _to_command(self):
        return self.direction, self.rpm


class EUST(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    CLOCKWISE: int = Status.STATUS_CLOCKWISE.value
    COUNTERCLOCKWISE: int = Status.STATUS_COUNTERCLOCKWISE.value

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the EUST device at the specified ``interval_s`` in seconds.

        The EUST device must be started to begin continuously updating readings from any attached
        mixers. This method should be called in a Recipe prior to using the :py:func:`temperature`, etc.
        methods to read out data.

        This method has no effect if the EUST device has already been started 
        and the py:func:`start` method is called again.

        :Example: start the :class:`EUST` named `EUSTSIM` with an update interval of 1 second:

        .. code-block:: python

            EUSTSIM.start()

        To record data, set the ``record`` argument to ``True``. This will make the temperature
        history available for plotting in the user interface.

        :Example: start the :class:`EUST` named `EUSTSIM` with an update interval of 1 second
        and record the data:

        .. code-block:: python

            EUSTSIM.start(record=True)

        :param interval_s: number-like value to specify the update interval in seconds
            between the Hub and the EUST Device Node
        :type interval_s: float, int, defaults to 1.
        :param record: set to ``True`` to record data
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the EUST device.

        After stopping the EUST device, data will no longer be accessible 
        through the :py:func:`temperature` method .

        This method has no effect if the EUST device has already been stopped 
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`EUST` named `EUSTSIM`:

        .. code-block:: python

            EUSTSIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the EUST device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          rpm
          torque
          temperature
        ====================

        :Example: clear the recorded data for the EUST device names EUSTSIM:

        .. code-block:: python

            EUSTSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def start_mixers(
            self,
            mixer0: Union[MixerCommand, None] = None,
            mixer1: Union[MixerCommand, None] = None,
            mixer2: Union[MixerCommand, None] = None,
            mixer3: Union[MixerCommand, None] = None,
    ):
        """Command to start the mixing motor on one or more mixers in either
        the clockwise or counterclockwise direction at a specified rpm.

        For each of the 4 pump inputs, pass a :class:`MixerCommand` or None.

        If a :class:`MixerCommand` is passed, the command must have valid `direction`
        and `rpm` members.

        :Example: start the mixing motor for input 0 on the :class:`EUST` named `EUSTSIM` in the clockwise direction at
        400 rpm:

        .. code-block:: python

            command = EUSTSIM.make_command(direction = EUSTSIM.CLOCKWISE, rpm=400)

            EUSTSTIM.start_mixers(mixer0=command, pump2=command)

        :param mixer0:
            | MixerCommand, None
            | Defaults to None
        :type mixer0: MixerCommand, None, required
        :param mixer1:
            | MixerCommand, None
            | Defaults to None
        :type mixer1: MixerCommand, None, required
        :param mixer2:
            | MixerCommand, None
            | Defaults to None
        :type mixer2: MixerCommand, None, required
        :param mixer3:
            | MixerCommand, None
            | Defaults to None
        :type mixer3: MixerCommand, None, required

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop_mixers(
                self,
                mixer0: Union[int, str, bool, None] = None,
                mixer1: Union[int, str, bool, None] = None,
                mixer2: Union[int, str, bool, None] = None,
                mixer3: Union[int, str, bool, None] = None,
        ):
        """Command to stop one or more mixers.

        For each of the 4 mixer inputs, pass an :class:`int`, :class:`str`, :class:`bool` or None.

        =================   ==========
              param           action
        =================   ==========
                1              stop
               "1"             stop
              True             stop
           all others          none
        =================   ==========

        :Example:

        .. code-block:: python

            # stop inputs 0 and 2

            EUSTSIM.stop_mixers(mixer0=True, mixer2=1)

        :param mixer0:
            | int, str, bool, None
            | Defaults to None
        :type mixer0: int, str, bool, None, not required
        :param mixer1:
            | int, str, bool, None
            | Defaults to None
        :type mixer1: int, str, bool, None, not required
        :param mixer2:
            | int, str, bool, None
            | Defaults to None
        :type mixer2: int, str, bool, None, not required
        :param mixer3:
            | int, str, bool, None
            | Defaults to None
        :type mixer3: int, str, bool, None, not required
        :return: tx_params
        :rtype: dict
        """

        return {}

    def temperature(self, index: int = 0) -> Union[float, None]:
        """
        Get a temperature reading from one of the 4 possible IKA Eurostar mixer inputs. The *index* argument
        selects the input channel (one of the 4 possible positions for an attached IKA Eurostar mixer) to retrieve.

        If no valid input is present or the temperature reading is invalid, returns `None`.

        =====  =================
        Index    Input Location
        =====  =================
          0      bottom left
          1      bottom right
          2      top right
          3      top left
        =====  =================

        :Example: read temperature from input 0:

        .. code-block:: python

            EUSTSIM.temperature(0)

        :Example: read temperature from input 3:

        .. code-block:: python

            EUSTSIM.temperature(3)

        :param index: input to read from, `0` is first input
        :type index: int, {0:3}
        :return: temperature
        :rtype: float, None
        """
        return 100

    def get_temperature(self, index: int = 0) -> Union[float, None]:
        """
        Alias for the py:func:`temperature` method.

        :Example: read temperature from input 3:

        .. code-block:: python

            EUSTSIM.get_temperature(3)

        :param index: input to read from, `0` is first input
        :type index: int, {0:3}
        :return: temperature
        :rtype: float, None
        """
        return self.temperature(index)

    def get_all_temperatures(self) -> Tuple[Union[float, None]]:
        """
        Get all of the temperature readings from an EUST Device Node.

        The method will always return a tuple of length 4. Inputs with valid temperature
        readings will return a `float` value. Inputs without valid readings
        will return `None`.

        =====  ==========  =================
        Index  Input Num     Input Location
        =====  ==========  =================
          0        0          bottom left
          1        1          bottom right
          2        2           top right
          3        3           top left
        =====  ==========  =================

        :Example: read all temperatures:

        .. code-block:: python

            temperatures = EUSTSIM.get_all_temperatures()
            len(temperatures) # 4

        :return: temperature values
        :rtype: list
        """
        return tuple(100, 100, 100, 100)

    def set_sim_temperature(self, value: float, index: int = 0):
        """
        In `Sim` mode, sets the simulated temperature reading for a given mixer input.

        Useful for checking logic based on feedback from a mixer.

        :Example: set the simulated temperature value of input 2 to 110 C:

        .. code-block:: python

            EUSTSIM.set_sim_temperature(110, index=2)

        :param value: simulated value to assign
        :type value: float
        :param index: input to assign the value to, `0` is first input
        :type index: int, {0:3}
        :return: None
        """
        return

    def set_sim_temperatures(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated temperatures of multiple inputs.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            EUSTSIM.set_sim_temperatures((45, , 23, ))

        would set input 0 to 45 C and input 2 to 23 C. Inputs 1 and 3 are not affected.

        If a dict is passed, the format should be:

        .. code-block:: python

            EUSTSIM.set_sim_temperatures({
                '0': 45,
                 1: 23,
            })

        where each key is a str or int for an input number and the value of the key is the desired sim temperature value.

        :param values: simulated values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    def set_sim_rates_of_change(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated rate-of-change, in C/s, for the temperature values.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            EUSTSIM.set_sim_rates_of_change((0.05, , -0.13, ))

        would input 0's rate of change to 0.05 C/s and input 2's rate of change
        to -0.13 C/s. Inputs 1 and 3 are not affected.

        If a dict is passed, the format should be:

        .. code-block:: python

            EUSTSIM.set_sim_rates_of_change({
                '0': 0.05,
                 1: -0.13.
            })

        where each key is a str or int for an input number and the value of the key is the desired input's
        temperature rate of change in C/s.

        :param values: simulated rate-of-change values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    def set_sim_noise(self, active: int = 1, values: Union[dict, tuple, list] = ()) -> None:
        """
        In `Sim` mode, simulated noise is added to the mixers' temperature readings by default.

        Turn off the simulated noise by passing ``active = 0``

        Turn on the simulated noise by passing ``active = 1``

        Affects all inputs.

        :Example: turn off the simulated noise of the :class:`EUST` device named `EUSTSIM`:

        .. code-block:: python

            EUSTSIM.set_sim_noise(active=0)

        Alternatively, adjust the simulated noise for individual inputs by passing
        a dict, tuple, or list as the `values` argument.

        If a list or tuple is passed, each element should be a value to set the corresponding input's noise to, eg.

        .. code-block:: python

            EUSTSIM.set_sim_noise((0.05, , 0.18, ))

        would set input 0's simulated noise to 0.05 C and input 2's simulated noise
        to 0.18 C. Inputs 1 and 3 would are not affected.

        The noise added to the reading during each simulated measurement acquisition 
        is selected randomly from a uniform distribution in the range [-v, +v] where v is the noise value assigned.

        If a `dict` is passed, the format should be:

        .. code-block:: python

            EUSTSIM.set_sim_noise({
                '0': 0.05,
                 2: .18.
            })

        where each key is a str or int for an input number and the value of the key is the desired input's
        simulated noise.

        :param active: noise control toggle
        :type active: int, {0,1}
        :param values: simulated values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    @staticmethod
    def make_command(direction: Union[int, str] = None, rpm: Union[float, int] = None, **kwargs) -> MixerCommand:
        """Helper method to create an instance of a :class:`MixerCommand`.

        A :class:`MixerCommand` is an object with the required fields to set the operation
        parameters for a mixer input.

        :return: mixer_command
        :rtype: MixerCommand
        """

        return MixerCommand(**{**kwargs, **locals()})










