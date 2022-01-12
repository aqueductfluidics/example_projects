import config
import devices.base.obj
from devices.aqueduct.trbd.constants import *

from typing import Union


def instantiate_device(d_device, setup):
    return TRBD(**d_device)


class TRBD(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_config(self):
        return {}

    def set_config(self, name: str = None):
        return {}

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the TRBD device at the specified ``interval_s`` in seconds.

        The TRBD device must be started to begin continuously updating readings from any attached
        sensors. This method should be called in a Recipe prior to using the :py:func:`get_values` method
        to read out data.

        This method has no effect if the TRBD device has already been started
        and the py:func:`start` method is called again.

        :Example: start the :class:`TRBD` named `TRBDSIM` with an update interval of 1 second:

        .. code-block:: python

            TRBDSIM.start()

        :param interval_s: number-like value to specify the update interval in seconds
            between the Hub and the TRBD Device Node
        :type interval_s: float, int, defaults to 1.
        :param record: reserved and not yet implemented
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the TRBD device.

        After stopping the TRBD device, data will no longer be accessible
        through the :py:func:`get_values` method .

        This method has no effect if the TRBD device has already been stopped
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`TRBD` named `TRBDSIM`:

        .. code-block:: python

            TRBDSIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the TRBD device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          tx intensity
          90 deg intensity
        ====================

        for each input.

        :Example: clear the recorded data for the TRBD device names TRBDSIM:

        .. code-block:: python

            TRBDSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def get_values(self):
        """
        Get all of the turbidity (both transmitted and 90 degree scattered) readings from an TRBD Device Node.

        The method will always return a tuple of length 3 with each element a tuple of length 2.
        Inputs with valid turbidity readings will return an `int` value. Inputs without valid readings
        will return `None`.

        =====  ==========  =================
        Index  Input Num     Input Location
        =====  ==========  =================
          0        0          bottom left
          1        1          bottom right
          2        2           top right
          3        3           top left
        =====  ==========  =================

        :Example: read all transducers:

        .. code-block:: python

            values = TRBDSIM.get_values()
            len(values) # 3
            len(values[0]) # 2
            print(values) # ((1212,122),(124,1231),(None,None))

        :return: turbidity values
        :rtype: tuple[tuple[int]]
        """
        return NUMBER_INPUTS * ((100000, 100000),)

    def set_sim_turbidity_values(self, values: tuple) -> dict:
        """
        In `Sim` mode, sets the simulated turbidity reading for a given sensor input.

        Useful to checking logic based on feedback from a sensor.

        :Example: set the simulated turbidity values (transmitted, 90 deg) of input 0 to 1000 and 100, respectively:

        .. code-block:: python

            TRBDSIM.set_sim_turbidity_values((1000,100),(),())
            # also acceptable
            TRBDSIM.set_sim_turbidity_values((1000,100),)

        :param values: simulated values to assign
        :type values: tuple[tuple]
        :return: None
        """
        return None

    def set_sim_rates_of_change(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated rate-of-change (in a.u./second) for the turbidity readings.

        Pass a tuple to set the values.

        :Example: set the rates-of-change for the simulated turbidity values (transmitted, 90 deg)
            of input 0 to 5 a.u./second and -10 a.u./second, respectively:

        .. code-block:: python

            TRBDSIM.set_sim_rates_of_change((5, -10),(),())
            # also acceptable
            TRBDSIM.set_sim_rates_of_change((5, -10),)

        :param values: simulated rate-of-change values to assign
        :type values: tuple
        :return: None
        """
        return None

    def set_sim_noise(self, active: int = 1, values: Union[dict, tuple, list] = ()) -> None:
        """
        In `Sim` mode, simulated noise is added to the turbidity readings by default.

        Turn off the simulated noise by passing ``active = 0``

        Turn on the simulated noise by passing ``active = 1``

        Affects all inputs.

        :Example: turn off the simulated noise of the :class:`TRBD` device named `TRBDSIM`:

        .. code-block:: python

            TRBDSIM.set_sim_noise(active=0)

        Alternatively, adjust the simulated noise for individual inputs by passing
        a dict, tuple, or list to set the `values` argument.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            TRBDSIM.set_sim_noise((0.05, , -0.13, ))

        would set input 0's simulated noise to 0.05 g and input 2's simulated noise
        to -0.13 g. Inputs 1 and 3 would are not affected.

        If a `dict` is passed, the format should be:

        .. code-block:: python

            TRBDSIM.set_sim_noise({
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
        return None








