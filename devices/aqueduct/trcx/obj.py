import devices.base.obj
from devices.aqueduct.trcx.constants import *

from typing import List, Tuple, Union


def instantiate_device(d_device, setup):
    return TRCX(**d_device)


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


class SetValveCommand(object):
    position: Union[int, str]
    direction: Union[int, str] = None

    def __init__(self, position, direction: int = None, **kwargs):
        self.position = position
        self.direction = direction

    def _to_command(self):
        return self.position, self.direction


class PumpConfig(object):
    """Class containing the configuration values for each pump input.

    Each configuration contains three attributes:
        config: int, the configuration of the syringe pump input
            NO_PUMP = 0
            NO_VALVE = 1
            THREE_PORT_DISTRIBUTION = 2
            SIX_PORT_DISTRIBUTION = 3
        series: int, the series of the syringe pump input
            CX6000 = 0
            CX48000 = 1
            C3000 = 2
            C24000 = 3
        syringe_vol_ul: float, the volume of the syringe in uL
        plgr_mode: int, the plunger resolution of the pump input
            0 = N0
            1 = N1
            2 = N2

    Attributes:
        config (int)
        series (int)
        syringe_vol_ul (float)
        plgr_mode (int)
    """

    def __init__(self, **kwargs):

        self._config: int = None
        self._series: int = None
        self._syringe_vol_ul: float = None
        self._plgr_mode: int = None

        for k, v in kwargs.items():
            if k == PUMP_CONFIG_SUFFIX.strip("_"):
                self._config: int = int(v)
            elif k == PUMP_SERIES_SUFFIX.strip("_"):
                self._series: int = int(v)
            elif k == SYRINGE_VOLUME_UL_SUFFIX.strip("_"):
                self._syringe_vol_ul: float = float(v)
            elif k == PLUNGER_MODE_SUFFIX.strip("_"):
                self._plgr_mode: int = int(v)

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        try:
            self._config = int(value)
        except ValueError as e:
            pass

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, value):
        try:
            self._series = int(value)
        except ValueError as e:
            pass

    @property
    def syringe_vol_ul(self):
        return self._syringe_vol_ul

    @syringe_vol_ul.setter
    def syringe_vol_ul(self, value):
        try:
            self._syringe_vol_ul = float(value)
        except ValueError as e:
            pass

    @property
    def plgr_mode(self):
        return self._plgr_mode

    @plgr_mode.setter
    def plgr_mode(self, value):
        try:
            self._plgr_mode = int(value)
        except ValueError as e:
            pass


class TRCX(devices.base.obj.Device):
    """Class encapsulating the functionality of the TR(CX) Series Syringe Pumps.

    Attributes:
        configs (list[PumpConfig], len 12): PumpConfig instances for each pump input. These
            objects are generated at Recipe start, so any changes to the configuration once
            the Recipe has started will not be captured.

        infuse (int): Constant to specify the infuse direction.
        withdraw (int): Constant to specify the withdraw direction.

        finite (int): Constant to specify finite mode operation.
        continuous (int): Constant to specify continuous mode operation.

        ul_min (int): Constant to specify uL/min rate units.
        ul_hr (int): Constant to specify uL/hr rate units.
        ml_min (int): Constant to specify mL/min rate units.
        ml_hr (int): Constant to specify mL/hr rate units.

        ml (int): Constant to specify mL volume units.
        ul (int): Constant to specify uL volume units.

        clockwise (int): Constant to specify clockwise valve rotation.
        counterclockwise (int): Constant to specify counterclockwise valve rotation.

    """

    config: List[PumpConfig] = NUMBER_INPUTS * [None]

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

    clockwise: int = VALVE_ROTATION_CLOCKWISE
    counterclockwise: int = VALVE_ROTATION_COUNTERCLOCKWISE

    INFUSE: int = STATUS_INFUSING
    WITHDRAW: int = STATUS_WITHDRAWING

    FINITE: int = MODE_FINITE
    CONTINUOUS: int = MODE_CONTINUOUS

    UL_MIN: int = UL_MIN
    UL_HR: int = UL_HR
    ML_MIN: int = ML_MIN
    ML_HR: int = ML_HR

    ML: int = ML
    UL: int = UL

    CLOCKWISE: int = VALVE_ROTATION_CLOCKWISE
    COUNTERCLOCKWISE: int = VALVE_ROTATION_COUNTERCLOCKWISE

    def get_config(self):
        return {}

    def set_config(self, name: str = None):
        return {}

    def pump(
            self,
            pump0: Union[PumpCommand, dict, None] = None,
            pump1: Union[PumpCommand, dict, None] = None,
            pump2: Union[PumpCommand, dict, None] = None,
            pump3: Union[PumpCommand, dict, None] = None,
            pump4: Union[PumpCommand, dict, None] = None,
            pump5: Union[PumpCommand, dict, None] = None,
            pump6: Union[PumpCommand, dict, None] = None,
            pump7: Union[PumpCommand, dict, None] = None,
            pump8: Union[PumpCommand, dict, None] = None,
            pump9: Union[PumpCommand, dict, None] = None,
            pump10: Union[PumpCommand, dict, None] = None,
            pump11: Union[PumpCommand, dict, None] = None,
            wait_for_complete: bool = True,
            update_interval_s: int = 0.5,
            record: bool = True,
    ):
        """Command to start one or more pump inputs in either finite or continuous mode.

        For each of the 12 pump inputs, pass a :class:`PumpCommand`, a dictionary (specified keys below), or None.

        If a :class:`PumpCommand` is passed, the command must have valid `mode`, `direction`, `rate_value`,
        and `rate_units` members. If `mode` is set to `finite`, the command must have valid `finite_units` and
        `finite_value` members.

        Here's an example of starting pump inputs 0 and 2 in continuous
        infuse mode at a rate of 1 mL/min. Note the use of the :class:`TRCX` class constants
        for mode, direction, and rate_units. Since no parameters are passed to
        inputs 1 and 3-11, no action is taken for those pumps. Since the mode of operation
        for both input 0 and 2 is non-blocking, the Recipe will resume execution after
        confirmation of successful communication.

        :Example:

        .. code-block:: python

            command = TRCXSIM.make_command(mode = TRCXSIM.continuous, direction = TRCXSIM.infuse,
                                           rate_value = 1.0, rate_units = TRCXSIM.ml_min)

            TRCXSIM.pump(pump0=command, pump2=command)


        Here's another example of starting a single pump input, 1, in finite mode in the
        withdraw direction. Since the mode of operation here is `finite`, the Recipe
        will be blocked from continuing until the pump has withdrawn the assigned amount.
        To prevent blocking, set `wait_for_complete` to False.

        :Example:

        .. code-block:: python

            command = TRCXSIM.make_command(mode = TRCXSIM.finite, direction = TRCXSIM.withdraw,
                                           rate_value = 1.0, rate_units = TRCXSIM.ml_min,
                                           finite_value = 5.0, finite_units = TRCXSIM.ml)

            TRCXSIM.pump(pump1=command)

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
                'mode': TRCXSIM.finite,
                'direction': TRCXSIM.infuse,
                'rate_value': 3.5,
                'rate_units': TRCXSIM.ul_min
            }

            TRCXSIM.pump(pump1=dict_command)

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
        :param pump4:
            | PumpCommand, dict, or None to control actions for pump input 4
            | Defaults to None
        :type pump4: PumpCommand, dict, None, required
        :param pump5:
            | PumpCommand, dict, or None to control actions for pump input 5
            | Defaults to None
        :type pump5: PumpCommand, dict, None, required
        :param pump6:
            | PumpCommand, dict, or None to control actions for pump input 6
            | Defaults to None
        :type pump6: PumpCommand, dict, None, required
        :param pump7:
            | PumpCommand, dict, or None to control actions for pump input 7
            | Defaults to None
        :type pump7: PumpCommand, dict, None, required
        :param pump8:
            | PumpCommand, dict, or None to control actions for pump input 8
            | Defaults to None
        :type pump8: PumpCommand, dict, None, required
        :param pump9:
            | PumpCommand, dict, or None to control actions for pump input 9
            | Defaults to None
        :type pump9: PumpCommand, dict, None, required
        :param pump10:
            | PumpCommand, dict, or None to control actions for pump input 10
            | Defaults to None
        :type pump10: PumpCommand, dict, None, required
        :param pump11:
            | PumpCommand, dict, or None to control actions for pump input 11
            | Defaults to None
        :type pump11: PumpCommand, dict, None, required
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

    def stop(
            self,
            pump0: Union[int, str, bool, None] = None,
            pump1: Union[int, str, bool, None] = None,
            pump2: Union[int, str, bool, None] = None,
            pump3: Union[int, str, bool, None] = None,
            pump4: Union[int, str, bool, None] = None,
            pump5: Union[int, str, bool, None] = None,
            pump6: Union[int, str, bool, None] = None,
            pump7: Union[int, str, bool, None] = None,
            pump8: Union[int, str, bool, None] = None,
            pump9: Union[int, str, bool, None] = None,
            pump10: Union[int, str, bool, None] = None,
            pump11: Union[int, str, bool, None] = None
    ):
        """Command to stop one or more pumps.

        For each of the 12 pump inputs, pass an :class:`int`, :class:`str`, :class:`bool` or None.

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

            TRCXSIM.stop(pump0=True, pump2=1)

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
        :param pump4:
            | int, str, bool, None
            | Defaults to None
        :type pump4: int, str, bool, None, not required
        :param pump5:
            | int, str, bool, None
            | Defaults to None
        :type pump5: int, str, bool, None, not required
        :param pump6:
            | int, str, bool, None
            | Defaults to None
        :type pump6: int, str, bool, None, not required
        :param pump7:
            | int, str, bool, None
            | Defaults to None
        :type pump7: int, str, bool, None, not required
        :param pump8:
            | int, str, bool, None
            | Defaults to None
        :type pump8: int, str, bool, None, not required
        :param pump9:
            | int, str, bool, None
            | Defaults to None
        :type pump9: int, str, bool, None, not required
        :param pump10:
            | int, str, bool, None
            | Defaults to None
        :type pump10: int, str, bool, None, not required
        :param pump11:
            | int, str, bool, None
            | Defaults to None
        :type pump11: int, str, bool, None, not required
        :return: tx_params
        :rtype: dict
        """

        return {}

    def set_valves(
            self,
            pump0: Union[SetValveCommand, int, str, None] = None,
            pump1: Union[SetValveCommand, int, str, None] = None,
            pump2: Union[SetValveCommand, int, str, None] = None,
            pump3: Union[SetValveCommand, int, str, None] = None,
            pump4: Union[SetValveCommand, int, str, None] = None,
            pump5: Union[SetValveCommand, int, str, None] = None,
            pump6: Union[SetValveCommand, int, str, None] = None,
            pump7: Union[SetValveCommand, int, str, None] = None,
            pump8: Union[SetValveCommand, int, str, None] = None,
            pump9: Union[SetValveCommand, int, str, None] = None,
            pump10: Union[SetValveCommand, int, str, None] = None,
            pump11: Union[SetValveCommand, int, str, None] = None,
    ):
        """Command to set the valve position for one or more pump inputs.

        For each of the 12 pump inputs, pass a :class:`SetValveCommand`, a dictionary (specified keys below), or None.

        If a :class:`SetValveCommand` is passed, the command must have valid `position` and `direction` members.

        The `position` member sets the target port for the valve and the `direction` member sets the
        desired rotation direction during actuation.

        Here's an example of setting pump inputs 0 and 2 valves to port 2 in the clockwise direction.
        Since no parameters are passed to inputs 1 and 3-11, no action is taken for those pumps.

        :Example:

        .. code-block:: python

            command = TRCXSIM.make_valve_command(position = 2, direction = TRCXSIM.clockwise)

            TRCXSIM.set_valves(pump0=command, pump2=command)

        :param pump0:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump0: SetValveCommand, int, str, None, required
        :param pump1:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump1: SetValveCommand, int, str, None, required
        :param pump2:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump2: SetValveCommand, int, str, None, required
        :param pump3:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump3: SetValveCommand, int, str, None, required
        :param pump4:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump4: SetValveCommand, int, str, None, required
        :param pump5:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump5: SetValveCommand, int, str, None, required
        :param pump6:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump6: SetValveCommand, int, str, None, required
        :param pump7:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump7: SetValveCommand, int, str, None, required
        :param pump8:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump8: SetValveCommand, int, str, None, required
        :param pump9:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump9: SetValveCommand, int, str, None, required
        :param pump10:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump10: SetValveCommand, int, str, None, required
        :param pump11:
            | SetValveCommand, int, or str
            | Defaults to None
        :type pump11: SetValveCommand, int, str, None, required
        :return: tx_params
        :rtype: dict
        """

        return {}

    def set_plunger_resolution(
            self,
            pump0: Union[int, str, None] = None,
            pump1: Union[int, str, None] = None,
            pump2: Union[int, str, None] = None,
            pump3: Union[int, str, None] = None,
            pump4: Union[int, str, None] = None,
            pump5: Union[int, str, None] = None,
            pump6: Union[int, str, None] = None,
            pump7: Union[int, str, None] = None,
            pump8: Union[int, str, None] = None,
            pump9: Union[int, str, None] = None,
            pump10: Union[int, str, None] = None,
            pump11: Union[int, str, None] = None,
    ):
        """Command to set the plunger resolution (N0, N1, or N2) for one or more pump inputs.

        For each of the 12 pump inputs, pass an :class:`int` or :class:`str` in 0, 1, or 2 to set the resolution.

        Here's an example of setting the plunger resolution of pump inputs 0 and 2 to 2.

        :Example:

        .. code-block:: python

            TRCXSIM.set_plunger_resolution(pump0=2, pump2=2)

        :param pump0:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump0: int, str, None, required
        :param pump1:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump1: int, str, None, required
        :param pump2:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump2: int, str, None, required
        :param pump3:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump3: int, str, None, required
        :param pump4:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump4: int, str, None, required
        :param pump5:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump5: int, str, None, required
        :param pump6:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump6: int, str, None, required
        :param pump7:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump7: int, str, None, required
        :param pump8:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump8: int, str, None, required
        :param pump9:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump9: int, str, None, required
        :param pump10:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump10: int, str, None, required
        :param pump11:
            | int, or str
            | Defaults to None, must be in 0, 1, 2, "0", "1", "2"
        :type pump11: int, str, None, required
        :return: tx_params
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the TRCX device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          ul_min
          ul_infused
          ul_withdrawn
          plgr_position
        ====================

        for each input.

        :Example: clear the recorded data for the TRCX device names TRCXSIM:

        .. code-block:: python

            TRCXSIM.clear_recorded()

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

            vol_pumped = TRCXSIM.vol_pumped()
            # the volume infused by input 0
            print("Input 0 infused {} mL".format(vol_pumped[0][0]))
            # the volume withdrawn by input 2
            print("Input 2 withdrew {} mL".format(vol_pumped[2][1]))

        :return: vol_pumped
        :rtype: tuple(tuple(float, float))
        """
        return NUMBER_INPUTS * ((1.0, 1.0),)

    def is_active(
        self,
        pump0: Union[int, str, bool, None] = None,
        pump1: Union[int, str, bool, None] = None,
        pump2: Union[int, str, bool, None] = None,
        pump3: Union[int, str, bool, None] = None,
        pump4: Union[int, str, bool, None] = None,
        pump5: Union[int, str, bool, None] = None,
        pump6: Union[int, str, bool, None] = None,
        pump7: Union[int, str, bool, None] = None,
        pump8: Union[int, str, bool, None] = None,
        pump9: Union[int, str, bool, None] = None,
        pump10: Union[int, str, bool, None] = None,
        pump11: Union[int, str, bool, None] = None
    ) -> bool:
        """Check whether one or more pump inputs is active (plunger currently moving).

        This will return a boolean value of True if any of the requested inputs is active:

        :Example:

        .. code-block:: python
            # check whether pump0 OR pump2 is active
            is_active = TRCXSIM.is_active(pump0 = 1, pump2 = 1)

        :return: any of the targeted inputs is active
        :rtype: bool
        """

        return True

    def get_status(self) -> Tuple[bool]:
        """Get the status of each pump input. A pump is considered active in the plunger is moving.

        This will return a :class:`tuple` or boolean values:

        :Example:

        .. code-block:: python
            # check whether pump0 OR pump2 is active
            is_active = TRCXSIM.is_active(pump0 = 1, pump2 = 1)

        :return: any of the targeted inputs is active
        :rtype: bool
        """
        return NUMBER_INPUTS * (True,)

    def get_plunger_positions(self, include_status: bool, include_resolution: bool) -> Tuple[Tuple[int, any, any]]:
        """Get the plunger position of each pump input in steps.

        Optionally, choose to get the status and plunger resolution of each input.

        This will return a :class:`tuple` of integer values:

        :Example:

        .. code-block:: python
            # get the plunger position of pump 2 (index = 2)
            pump2_position = TRCXSIM.get_plunger_positions()[2]
            print(pump2_position)  # (32124, None, None) // None, None since

        .. code-block:: python
            # get the plunger position of pump 4 (index = 4) and get the status and resolution, too...
            pump4_position = TRCXSIM.get_plunger_positions(include_status=True, include_resolution=True)[4]
            print(pump4_position)  # (32124, 1, 2)  # Status == 1, plunger resolution == 2

            # STATUS_STOPPED = 0
            # STATUS_INFUSING = 1
            # STATUS_WITHDRAWING = 2

        :return: a tuple of all the pump inputs plunger positions
        :rtype: tuple
        """
        if include_status and include_resolution:            
            return NUMBER_INPUTS * ((1000, 1, 1),)
        elif include_status:
            return NUMBER_INPUTS * ((1000, 1, None),)
        elif include_resolution:
            return NUMBER_INPUTS * ((1000, None, 1),)
        else:
            return NUMBER_INPUTS * ((1000, None, None),)

    def calc_current_ul(self, index: int, plunger_position: int, plunger_resolution: int) -> Union[float, None]:
        """Get the volume, in microliters, available to infuse. This method can be useful
        as a counter to track volume infused or withdrawn.

        :Example:

        .. code-block:: python

            # the max flow rate in uL/min for pump index 3
            max_rate_ul_min = TRCXSIM.get_max_rate_ul_min(index=3)

        :param index:
            | int
            | Defaults to None
        :type index: the index to calculate the max rate for, from 0 to 11
        :param plunger_position:
            | int
            | Defaults to None
        :type plunger_resolution: the plunger resolution, (0, 1, 2)
        :param index:
            | int
            | Defaults to None
        :type index: the index to calculate the max rate for, from 0 to 11
        :return: syringe_vols
        :rtype: tuple(float)
        """
        return None

    def get_syringe_volumes_ul(self) -> tuple:
        """Get the volume of each of the syringes.

        This will return a :class:`tuple` of :class:`floats`s or class :class:`Nones`s:

        (5000, 12500, None, ...)

        for the 12 pump inputs.

        :Example:

        .. code-block:: python

            syringe_vols = TRCXSIM.get_syringe_volumes_ul()
            # the volume of the syringe in pump0
            print("Input 0 syringe volume: {} uL".format(syringe_vols[0]))

        :return: syringe_vols
        :rtype: tuple(float)
        """
        return NUMBER_INPUTS * (5000.,)

    def get_max_rate_ul_min(self, index: int = None) -> Union[float, None]:
        """Get the maximum plunger rate, in uL/min, based on the input's syringe volume,
        pump series, and plunger resolution.

        :Example:

        .. code-block:: python

            # the max flow rate in uL/min for pump index 3
            max_rate_ul_min = TRCXSIM.get_max_rate_ul_min(index=3)

        :param index:
            | int
            | Defaults to None
        :type index: the index to calculate the max rate for, from 0 to 11
        :return: syringe_vols
        :rtype: tuple(float)
        """
        if isinstance(index, int) and index in range(0, NUMBER_INPUTS):
            return 500.
        return None

    def get_min_rate_ul_min(self, index: int = None) -> Union[float, None]:
        """Get the minimum, non-zero plunger rate, in uL/min, based on the input's syringe volume,
        pump series, and plunger resolution.

        :Example:

        .. code-block:: python

            # the min flow rate in uL/min for pump index 7
            max_rate_ul_min = TRCXSIM.get_min_rate_ul_min(index=7)

        :param index:
            | int
            | Defaults to None
        :type index: the index to calculate the max rate for, from 0 to 11
        :return: syringe_vols
        :rtype: tuple(float)
        """
        if isinstance(index, int) and index in range(0, NUMBER_INPUTS):
            return 1.
        return None

    @staticmethod
    def calc_max_rate_ul_min(syringe_vol_ul: Union[float, int], series: int, mode: int) -> Union[float, None]:
        """
        Caclulate the maximum plunger rate, in uL/min, based on a syringe volume, in uL, a pump
        series, and a plunger resolution mode.

        series: int, the series of the syringe pump input
            CX6000 = 0
            CX48000 = 1
            C3000 = 2
            C24000 = 3

        syringe_vol_ul: float, the volume of the syringe in uL

        plgr_mode: int, the plunger resolution of the pump input
            0 = N0
            1 = N1
            2 = N2

        :Example:

        .. code-block:: python

            # the max flow rate in uL/min for pump index 3
            max_rate_ul_min = TRCXSIM.get_max_rate_ul_min(index=3)

        :param syringe_vol_ul:
        :param series: int, the series of the syringe pump input
            | CX6000 = 0
            | CX48000 = 1
            | C3000 = 2
            | C24000 = 3
        :type series: int
        :param mode:
        :return:
        """
        return 100

    def calc_min_rate_ul_min(self, index: int = None) -> Union[float, None]:
        """Get the minimum, non-zero plunger rate, in uL/min, based on the input's syringe volume,
        pump series, and plunger resolution.

        :Example:

        .. code-block:: python

            # the min flow rate in uL/min for pump index 7
            max_rate_ul_min = TRCXSIM.get_min_rate_ul_min(index=7)

        :param index:
            | int
            | Defaults to None
        :type index: the index to calculate the max rate for, from 0 to 11
        :return: syringe_vols
        :rtype: tuple(float)
        """
        return None

    @staticmethod
    def make_command(mode: Union[int, str] = None, direction: Union[int, str] = None, rate_value: Union[float, int] = None,
                     rate_units: Union[int, str] = None, finite_value: Union[float, int, None] = None,
                     finite_units: Union[int, str, None] = None, **kwargs) -> PumpCommand:
        """Helper method to create an instance of a :class:`PumpCommand`.

        A :class:`PumpCommand` is an object with the required fields to set the operation
        parameters for a pump input.

        :return: pump_command
        :rtype: PumpCommand
        """

        return PumpCommand(**{**kwargs, **locals()})

    @staticmethod
    def make_valve_command(position: Union[int, str] = None, direction: Union[int, str] = None, **kwargs) -> SetValveCommand:
        """Helper method to create an instance of a :class:`SetValveCommand`.

        A :class:`SetValveCommand` is an object with the required fields to set the operation
        parameters for a valve movement.

        :return: set_valve_command
        :rtype: SetValveCommand
        """

        return SetValveCommand(**{**kwargs, **locals()})
