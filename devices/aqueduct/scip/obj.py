from typing import List, Tuple, Union

import devices.base.obj
from devices.aqueduct.scip.constants import *


def instantiate_device(d_device, setup):
    return SCIP(**d_device)


class SCIP(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start(self, interval_s: float = 1., record: bool = False):
        """Start receiving data from the SCIP device at the specified ``interval_s`` in seconds.

        The SCIP device must be started to begin continuously updating readings from any attached
        SciLog modules. This method should be called in a Recipe prior to using the :py:func:`get_pressure` 
        method to read out data.

        This method has no effect if the SCIP device has already been started 
        and the py:func:`start` method is called again.

        :Example: start the :class:`SCIP` named `SCIPSIM` with an update interval of 1 second:

        .. code-block:: python

            SCIPSIM.start()

        :param interval_s:
            | number-like value to specify the update interval in seconds between the Hub and the SCIP Device Node
            | numbers less than `1` will be set to 1
        :type interval_s: float, int, defaults to 1.
        :param record: record the data from each transducer
        :type record: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self):
        """Stop receiving data from the SCIP device.

        After stopping the SCIP device, data will no longer be accessible 
        through the :py:func:`get_pressure` method .

        This method has no effect if the OHSA device has already been stopped 
        and the py:func:`stop` method is called again.

        :Example: stop the :class:`SCIP` named `SCIPSIM`:

        .. code-block:: python

            SCIPSIM.stop()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the SCIP device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          pressure
        ====================

        for each input.

        :Example: clear the recorded data for the SCIP device names SCIPSIM:

        .. code-block:: python

            SCIPSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def get_pressure(self, input_num: int = 0, txdcr_num: int = 0, units: str = "psi") -> Union[float, None]:
        """
        Get a pressure reading from one of the SciLog Device Node's 12 possible transducer inputs.
        The *input_num* argument selects the input channel (one of the 4 possible positions for
        an attached SciLog device) and the *txdcr_num* argument selects which of the
        3 possible transducers per input to read.

        If no valid pressure input or transducer is present, returns `None`.

        :Example: read transducer 1 from input 0:

        .. code-block:: python

            SCIPSIM.get_pressure(0,1)

        :Example: read transducer 0 from input 3:

        .. code-block:: python

            SCIPSIM.get_pressure(3,0)

        :param input_num: input to read from, `0` is first input
        :type input_num: 
            | An integer value
            | Value must be between 0 and 3
            | input_num 0: bottom left DB-9 connector on Device Node
            | input_num 1: bottom right DB-9 connector on Device Node
            | input_num 2: top right DB-9 connector on Device Node
            | input_num 3: top left DB-9 connector on Device Node
        :param txdcr_num: the transducer number to read
        :type txdcr_num: 
            | An integer value
            | Value must be between 0 and 2
            | txdcr_num 0: Transducer 1 on the SciLog
            | txdcr_num 1: Transducer 2 on the SciLog
            | txdcr_num 2: Transducer 3 on the SciLog
        :param units: pressure units to convert the return value to 
            | not yet implemented
        :type units: {'‘psi’, ‘bar’, ‘Pa’,'}

        :return: pressure value
        :rtype: float, None
        """
        if input_num >= NUMBER_INPUTS:
            raise ValueError("Invalid Pressure Reading input index: {}".format(input_num))
        if txdcr_num >= NUMBER_TRANSDUCERS_PER_INPUT:
            raise ValueError("Invalid Pressure Reading transducer index: {}".format(txdcr_num))
        return float(5)

    def get_all_pressures(self, units: str = "psi") -> List[float]:
        """
        Get all of the pressure readings a SciLog Device Node.

        The method will always return a list of length 12. Inputs with valid pressure
        readings will return a `float` value. Inputs without valid readings
        will return `None`.

        =====  ==========  =================  ==============
        Index  Input Num     Input Location    Txdcr Number
        =====  ==========  =================  ==============
          0        0          bottom left           1
          1        0          bottom left           2
          2        0          bottom left           3
          3        1          bottom right          1
          4        1          bottom right          2
          5        1          bottom right          3
          6        2           top right            1
          7        2           top right            2
          8        2           top right            3
          9        3           top left             1
          10       3           top left             2
          11       3           top left             3
        =====  ==========  =================  ==============

        :Example: read all transducers:

        .. code-block:: python

            pressures = SCIPSIM.get_all_pressures(0,1)
            len(pressures) # 12

        :param units: pressure units to convert the return value to
        :type units: {'‘psi’, ‘bar’, ‘Pa’,'}

        :return: pressure values
        :rtype: list
        """
        return (NUMBER_TRANSDUCERS * (float(5),))

    def set_sim_pressure(self, value: float = 0., input_num: int = 0, txdcr_num: int = 0) -> None:
        """
        Set the simulated pressure reading for one of the SciLog's 12 possible transducer inputs.

        Only functions in Sim Mode.

        The *input_num* argument selects the input channel (one of the 4 possible positions for
        an attached SciLog device) and the *txdcr_num* argument selects which of the 3 possible
        transducers per input to read.

        :Example: set transducer 1 from input 0 to 25 psi:

        .. code-block:: python

            SCIPSIM.set_sim_pressure(25,0,1)

        :param value: pressure value
        :type value: float, int
        :param input_num: input to read from, `0` is first input
        :type input_num: int, {0:3}
        :param txdcr_num: transducer to read, `0` is first transducer
        :type txdcr_num: int, {0:3}
        :return: pressure value
        :rtype: float, None
        """
        return

    def set_sim_pressures(self, values: Union[dict, tuple, list]):
        """
        In `Sim` mode, sets the simulated pressure readings of multiple inputs.

        Pass a dict, tuple, or list to set the values.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            OHSCSIM.set_sim_pressures((4.5, , 0.3, ))

        would set input 0 to 4.5 psi and input 2 to 0.3 psi. Inputs 1 and 3-11 are not affected.

        If a dict is pass, the format should be:

        .. code-block:: python

            OHSCSIM.set_sim_pressures({
                '0': 4.5,
                 1: 0.3.
            })

        where each key is a str or int for an input number and the value of the key is the desired pressure reading.

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

            SCIPSIM.set_sim_rates_of_change((0.05, , -0.13, ))

        would input 0's rate of change to 0.05 g/s and input 2's rate of change
        to -0.13 g/s. Inputs 1 and 3 would are not affected.

        If a dict is pass, the format should be:

        .. code-block:: python

            SCIPSIM.set_sim_weights({
                '0': 4.5,
                 1: 25.
            })

        where each key is a str or int for an input number and the value of the key is the desired weight reading's
        rate of change.

        :param values: simulated rate-of-change values to assign
        :type values: dict, tuple, list
        :return: None
        """
        return

    def set_sim_noise(self, active: int = 1, values: Union[dict, tuple, list] = ()) -> None:
        """
        In `Sim` mode, simulated noise is added to the pressure readings by default.

        Turn off the simulated noise by passing ``active = 0``

        Turn on the simulated noise by passing ``active = 1``

        Affects all inputs.

        :Example: turn off the simulated noise of the :class:`SCIP` device named `SCIPSIM`:

        .. code-block:: python

            SCIPSIM.set_sim_noise(active=0)

        Alternatively, adjust the simulated noise for individual inputs by passing
        a dict, tuple, or list to set the `values` argument.

        If a list or tuple is passed, each element should be a value to set the corresponding input to, eg.

        .. code-block:: python

            SCIPSIM.set_sim_noise((0.05, , -0.13, ))

        would set input 0's simulated noise to 0.05 g and input 2's simulated noise
        to -0.13 g. Inputs 1 and 3 would are not affected.

        If a `dict` is passed, the format should be:

        .. code-block:: python

            SCIPSIM.set_sim_noise({
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
