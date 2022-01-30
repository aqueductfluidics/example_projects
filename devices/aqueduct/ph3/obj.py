from typing import List, Union

import devices.base.obj
from devices.aqueduct.ph3.constants import *


def instantiate_device(d_device, setup):
    return PH3(**d_device)


class PH3(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the PH3 device at the specified ``interval_s`` in seconds.

        The PH3 device must be started to begin continuously updating readings from any attached
        pH probes. This method should be called in a Recipe prior to using the :py:func:`get_value` 
        or :py:func:`get_all_values` methods to read out data.

        This method has no effect if the PH3 device has already been started 
        and the py:func:`start` method is called again.

        :Example: start the :class:`PH3` named `PH3SIM` with an update interval of 1 second:

        .. code-block:: python

            PH3SIM.start()

        :param interval_s: number-like value to specify the update interval in seconds
            between the Hub and the PH3 Device Node
        :type interval_s: float, int, defaults to 1.
        :param record: record the data from each pH electrode
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the PH3 device.

        After stopping the PH3 device, data will no longer be accessible 
        through the ::py:func:`get_value` or :py:func:`get_all_values` methods.

        This method has no effect if the PH3 device has already been stopped 
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`PH3` named `PH3SIM`:

        .. code-block:: python

            PH3SIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the PH3 device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          pH
        ====================

        for each input.

        :Example: clear the recorded data for the PH3 device names PH3SIM:

        .. code-block:: python

            PH3SIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def value(self, index: int = 0):
        """
        Get a pH value reading from one of the 3 possible pH probe inputs. The *input_num* argument
        selects the input channel (one of the 3 possible positions for an attached pH probes) to read.

        If no valid input is present or the pH reading is invalid, returns `None`.

        =====  =================
        Index    Input Location
        =====  =================
          0      top
          1      middle
          2      bottom
        =====  =================

        :Example: read pH from input 0:

        .. code-block:: python

            PH3.value(0)

        :Example: read pH from input 3:

        .. code-block:: python

            PH3.value(3)

        :param index: input to read from, `0` is first input
        :type index: int, {0:2}
        :return: value, in pH
        :rtype: float, None
        """
        return float(7)


    def get_value(self, index: int = 0):
        """
        Alias for the py:func:`value` method.

        :Example: read pH from input 3:

        .. code-block:: python

            PH3.get_value(3)

        :param index: input to read from, `0` is first input
        :type index: int, {0:2}
        :return: value, in pH
        :rtype: float, None
        """
        return self.value(index)

    def get_all_values(self) -> List[float]:
        """
        Get all of the pH readings from a PH3 Device Node.

        The method will always return a list of length 3. Inputs with valid pH
        readings will return a `float` value. Inputs without valid readings
        will return `None`.

        =====  =================
        Index    Input Location
        =====  =================
          0      top
          1      middle
          2      bottom
        =====  =================

        :Example: read all transducers:

        .. code-block:: python

            pH_values = PH3.get_all_values()
            len(weights) # 3

        :return: pH values
        :rtype: list
        """
        return (7.0, 7.0, 7.0)

    def set_sim_value(self, value: float, index: int = 0):
        """
        In `Sim` mode, sets the simulated pH reading for a given electrode input.

        Useful for checking logic based on feedback from a pH probe.

        :Example: set the simulated pH value of input 2 to 6.85:

        .. code-block:: python

            PH3SIM.set_sim_value(6.85, index=2)

        :param value: simulated value to assign
        :type value: float
        :param index: input to assign the value to, `0` is first input
        :type index: int, {0:2}
        :return: None
        """
        return

    def set_sim_values(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated pH readings of multiple inputs.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            PH3SIM.set_sim_values((4.5, , 7.3, ))

        would set input 0 to 4.5 pH and input 2 to 7.3 pH. Inputs 1 and 3 would are not affected.

        If a dict is pass, the format should be:

        .. code-block:: python

            PH3SIM.set_sim_values({
                '0': 4.5,
                 1: 7.
            })

        where each key is a str or int for an input number and the value of the key is the desired pH reading.

        :param values: simulated values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    def set_sim_rates_of_change(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated rate-of-change, in grams/s, for the weight readings.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            PH3SIM.set_sim_rates_of_change((0.05, , -0.13, ))

        would input 0's rate of change to 0.05 g/s and input 2's rate of change
        to -0.13 g/s. Inputs 1 and 3 would are not affected.

        If a dict is pass, the format should be:

        .. code-block:: python

            PH3SIM.set_sim_rates_of_change({
                '0': 0.05,
                 1: -0.13.
            })

        where each key is a str or int for an input number and the value of the key is the desired input's pH
        rate of change.

        :param values: simulated rate-of-change values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    def set_sim_noise(self, active: int = 1, values: Union[dict, tuple, list] = ()) -> None:
        """
        In `Sim` mode, simulated noise is added to the pH readings by default.

        Turn off the simulated noise by passing ``active = 0``

        Turn on the simulated noise by passing ``active = 1``

        Affects all inputs.

        :Example: turn off the simulated noise of the :class:`PH3` device named `PH3SIM`:

        .. code-block:: python

            PH3SIM.set_sim_noise(active=0)

        Alternatively, adjust the simulated noise for individual inputs by passing
        a dict, tuple, or list to set the `values` argument.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            PH3SIM.set_sim_noise((0.05, , 0.13, ))

        would set input 0's simulated noise to 0.05 g and input 2's simulated noise
        to 0.13 pH. Inputs 1 and 3 would are not affected.

        If a `dict` is passed, the format should be:

        .. code-block:: python

            PH3SIM.set_sim_noise({
                '0': 4.5,
                 1: 25.
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

