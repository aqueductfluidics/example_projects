from typing import Union
from devices.aqueduct.pp12.constants import NUMBER_PUMPS

import devices.base.obj
from devices.aqueduct.syrp.constants import *


def instantiate_device(d_device, setup):
    return SYRP(**d_device)


class PumpCommand(object):
    mode: Union[int, str]
    direction: Union[int, str]
    rate_value: Union[float, int]
    rate_units: Union[int, str]
    finite_value: Union[float, int, None] = None
    finite_units: Union[int, str, None] = None
    wait_for_complete: Union[bool, None] = None

    def __init__(self, **kwargs):
        self.mode = MODE_CONTINUOUS
        self.direction = STATUS_INFUSING
        self.rate_value = 0.
        self.rate_units = ML_MIN
        self.finite_value = None
        self.finite_units = None

        for k, v in kwargs.items():
            if k in self.__dict__.keys():
                if v is not None:
                    setattr(self, k, v)

    def _to_command(self):
        mode = MODE_MAPPING.get(self.mode)
        direction = DIRECTION_MAPPING.get(self.direction)
        rate_units = RATE_UNIT_MAPPING.get(self.rate_units)
        finite_units = VOL_UNIT_MAPPING.get(self.finite_units)

        return mode, direction, self.rate_value, rate_units, self.finite_value, finite_units

    def _to_wait_for_complete(self):
        if self.wait_for_complete is True and MODE_MAPPING.get(self.mode) == MODE_FINITE:
            return True
        return False


class SYRP(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    infuse: int = STATUS_INFUSING
    withdraw: int = STATUS_WITHDRAWING

    finite: int = MODE_FINITE
    continuous: int = MODE_CONTINUOUS

    ul_min: int = UL_MIN
    ul_hr: int = UL_HR
    ml_min: int = ML_MIN
    ml_hr: int = ML_HR

    ml: int = ML
    ul: int = UL

    def get_config(self):
        content = devices.base.obj.add_object_info_to_content(vars(self), locals(), 'get_config')
        devices.base.obj.enqueue_and_pause(vars(self), content)
        return content

    def set_config(self, name: str = None):
        content = devices.base.obj.add_object_info_to_content(vars(self), locals(), 'set_config')
        devices.base.obj.enqueue_and_pause(vars(self), content)
        return content

    def pump(self,
             pump0: Union[PumpCommand, None] = None,
             pump1: Union[PumpCommand, None] = None,
             pump2: Union[PumpCommand, None] = None,
             pump3: Union[PumpCommand, None] = None,
             wait_for_complete: bool = True,
             update_interval_s: int = 1,
             record: bool = True,
             ):
        """Command to start one or more pump inputs in either finite or continuous mode.

        For each of the 4 pump inputs, pass a :class:`PumpCommand`, a dictionary (specified keys below), or None.

        If a :class:`PumpCommand` is passed, the command must have valid `mode`, `direction`, `rate_value`,
        and `rate_units` members. If `mode` is set to `finite`, the command must have valid `finite_units` and
        `finite_value` members.

        Here's an example of starting pump inputs 0 and 2 in continuous
        infuse mode a rate of 1 mL/min. Note the use of the :class:`SYRP` class constants
        for mode, direction, and rate_units. Since no parameters are passed to
        inputs 1 and 3, no action is taken for those pumps. Since the mode of operation
        for both input 0 and 2 is non-blocking, the Recipe will resume execution after
        confirmation of successful communication.

        :Example:

        .. code-block:: python

            command = SYRPSIM.make_command(mode = SYRPSIM.continuous, direction = SYRPSIM.infuse,
                                           rate_value = 1.0, rate_units = SYRPSIM.ml_min)

            SYRPSIM.pump(pump0=command, pump2=command)


        Here's another example of starting a single pump input, 1, in finite mode in the
        withdraw direction. Since the mode of operation here is `finite`, the Recipe
        will be blocked from continuing until the pump has withdrawn the assigned amount.
        To prevent blocking, set `wait_for_complete` to False.

        :Example:

        .. code-block:: python

            command = SYRPSIM.make_command(mode = SYRPSIM.finite, direction = SYRPSIM.withdraw,
                                           rate_value = 1.0, rate_units = SYRPSIM.ml_min,
                                           finite_value = 5.0, finite_units = SYRPSIM.ml)

            SYRPSIM.pump(pump1=command)

        If a :class:`dict` is passed as a parameter for `pumpN`, the command must have at least:

        =================  ==========
              key           required
        =================  ==========
          'mode'              yes
          'direction'         yes
          'rate_value'        yes
          'rate_units'        yes
          'finite_value'      no
          'finite_units'      no
        =================  ==========

        :Example:

        .. code-block:: python

            dict_command = {
                'mode': SYRSIM.finite,
                'direction': SYRPSIM.infuse,
                'rate_value': 3.5,
                'rate_units': SYRPSIM.ul_min
            }

            SYRPSIM.pump(pump1=dict_command)

        :param pump0:
            | PumpCommand, dict, or None to control actions for pump input 0
            | Defaults to None
        :type pump0: PumpCommand, dict, None, required
        :param pump1:
            | PumpCommand, dict, or None to control actions for pump input 1
            | Defaults to None
        :type pump1: PumpCommand, dict, None, required
        :param pump2:
            | PumpCommand, dict, or None to control actions for pump input 2
            | Defaults to None
        :type pump2: PumpCommand, dict, None, required
        :param pump3:
            | PumpCommand, dict, or None to control actions for pump input 3
            | Defaults to None
        :type pump3: PumpCommand, dict, None, required
        :param wait_for_complete:
            | Determines blocking behavior of command, if set to `True`, requires
            | any finite operations to complete before proceeding, if set to a tuple of
            | bools, requires only inputs flagged to complete
            | Defaults to True
        :type wait_for_complete: bool, tuple of bools
        :param update_interval_s:
            | interval to update, should be greater than 0.5
            | Defaults to 1
        :type update_interval_s: PumpCommand, dict, None, required
        :param record:
            | record the operational data of the pump
            | Defaults to False
        :type record: bool

        :return: tx_params
        :rtype: dict
        """
        return {}

    def stop(self,
             pump0: Union[int, str, bool, None] = None,
             pump1: Union[int, str, bool, None] = None,
             pump2: Union[int, str, bool, None] = None,
             pump3: Union[int, str, bool, None] = None
             ):
        """Command to stop one or more pumps.

        For each of the 4 pump inputs, pass an :class:`int`, :class:`str`, :class:`bool` or None.

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

            SYRPSIM.stop(pump0=True, pump2=1)

        :param pump0:
            | int, str, bool, None
            | Defaults to None
        :type pump0: int, str, bool, None, not required
        :param pump1:
            | int, str, bool, None
            | Defaults to None
        :type pump1: int, str, bool, None, not required
        :param pump2:
            | int, str, bool, None
            | Defaults to None
        :type pump2: int, str, bool, None, not required
        :param pump3:
            | int, str, bool, None
            | Defaults to None
        :type pump3: int, str, bool, None, not required

        :return: tx_params
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the SYRP device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          pressure
        ====================

        for each input.

        :Example: clear the recorded data for the SYRP device names SYRPSIM:

        .. code-block:: python

            SYRPSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        {}

    def vol_pumped(self, units: Union[int, str] = ML) -> tuple:
        """Get the volume of fluid displaced by the all of the pump inputs.

        This will return a :class:`tuple` of :class:`tuple`s:

        ((vol_infused, vol_withdrawn), (vol_infused, vol_withdrawn), ...)

        for the four pump inputs.

        :Example:

        .. code-block:: python

            vol_pumped = SYRPSIM.vol_pumped()
            # the volume infused by input 0
            print("Input 0 infused {} mL".format(vol_pumped[0][0]))
            # the volume withdrawn by input 2
            print("Input 2 withdrew {} mL".format(vol_pumped[2][1]))

        :return: vol_pumped
        :rtype: tuple(tuple(float, float))
        """
        return (NUMBER_PUMPS * (float(1),))

    @staticmethod
    def make_command(
            mode: Union[int, str] = None,
            direction: Union[int, str] = None,
            rate_value: Union[float, int] = None,
            rate_units: Union[int, str] = None,
            finite_value: Union[float, int, None] = None,
            finite_units: Union[int, str, None] = None,
            **kwargs
    ) -> PumpCommand:
        """Helper method to create an instance of a :class:`PumpCommand`.

        A :class:`PumpCommand` is an object with the required fields to set the operation
        parameters for a pump input.

        :return: pump_command
        :rtype: PumpCommand
        """

        return PumpCommand(**{**kwargs, **locals()})
