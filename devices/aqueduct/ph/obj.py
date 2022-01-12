from typing import Union

import devices.base.obj
from devices.aqueduct.ph.constants import *


def instantiate_device(d_device, setup):
    return PH(**d_device)


class PH(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_config(self):
        return {}

    def set_config(self, name: str = None):
        return {}

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the PH device at the specified ``interval_s`` in seconds.

        The PH device must be started to begin continuously updating readings from the probe.
        This method should be called in a Recipe prior to using the :py:func:`get_ph` method to read out data.

        This method has no effect if the PH device has already been started
        and the py:func:`start` method is called again.

        :Example: start the :class:`PH` named `PHSIM` with an update interval of 1 second:

        .. code-block:: python

            PH.start()

        :param interval_s: number-like value to specify the update interval in seconds
            between the Hub and the OHSA Device Node
        :type interval_s: float, int, defaults to 1.
        :param record: record the data from each balance
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the PH device.

        After stopping the PH device, data will no longer be accessible
        through the :py:func:`get_ph` method .

        This method has no effect if the PH device has already been stopped
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`PH` named `PHSIM`:

        .. code-block:: python

            PHSIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        content = devices.base.obj.add_object_info_to_content(vars(self), locals(), 'stop')
        devices.base.obj.enqueue_and_pause(vars(self), content)
        return content

    def clear_recorded(self):
        """Clear the recorded data for the PH device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          pH
        ====================

        for each input.

        :Example: clear the recorded data for the PH device names PHSIM:

        .. code-block:: python

            PHSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def get_ph(self):
        """
        Get a pH reading from the pH probe.

        If no valid input is present or the pH reading is invalid, returns `None`.

        :Example: read pH:

        .. code-block:: python

            current_val = PHSIM.get_ph()
            print(current_val) # prints 4.53

        :return: pH value
        :rtype: float, None
        """
        return float(7)

    def set_sim_ph_value(self, ph: Union[int, float]):
        """
        In `Sim` mode, sets the simulated pH value of the probe.

        Pass a float or int to set the value.

        .. code-block:: python

            PHSIM.set_sim_ph_value(7.0)

        :param ph: simulated value to assign
        :type ph: int, float
        :return: None
        """
        return

    def set_sim_rate_of_change(self, rate_of_change: Union[int, float]):
        """
        In `Sim` mode, sets the simulated rate-of-change, in pH/s, for the pH value.

        Pass a float or in to set the value.

        .. code-block:: python

            PHSIM.set_sim_rate_of_change(0.01)

        will set the pH value's rate of change to 0.01 pH/s.

        :param rate_of_change: simulated rate-of-change values to assign
        :type rate_of_change: int, float
        :return: None
        """
        return

    def set_sim_noise(self, value: Union[int, float]) -> None:
        """
        In `Sim` mode, simulated noise is added to the balance weight readings by default.

        Turn off the simulated noise by passing ``value = 0``

        Turn on the simulated noise by passing ``value = XX``

        :Example: turn off the simulated noise of the :class:`PH` device named `PHSIM`:

        .. code-block:: python

            PHSIM.set_sim_noise(value=0)

        :param value: noise magnitude
        :type value: int, float
        :return: None
        """
        return








