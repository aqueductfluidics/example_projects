import datetime
from typing import Union

import devices.base.obj
from devices.aqueduct.pp.constants import *


def instantiate_device(d_device, setup):
    return PP(**d_device)


class PP(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    CONTINUOUS = MODE_CONTINUOUS
    FINITE = MODE_FINITE

    FORWARD = DIRECTION_FORWARD
    REVERSE = DIRECTION_REVERSE

    UL_MIN = "ul_min"
    ML_MIN = "ml_min"
    RPM = "rpm"

    ML = "ml"
    UL = "ul"
    STEPS = "steps"
    SECONDS = "seconds"

    def start(
            self,
            mode: str = "continuous",
            direction: str = "forward",
            rate_value: float = 100,
            rate_units: str = "rpm",
            finite_value: float = None,
            finite_units: str = None,
            record: bool = False,
            wait_for_complete: bool = True
    ) -> dict:
        """Start the pump. The pump can be run indefinitely in `continuous` mode or for a finite
        number of mL's, seconds, minutes, motor steps, or motor degrees.

        :Example: start the :class:`PP` named `PPSIM` in the forward direction at 100 rpm continuously:

        .. code-block:: python

            PPSIM.start(mode="c", direction="forward", rate_value=100., rate_units="rpm")

        :Example: start the :class:`PP` named `PPSIM` in the reverse direction at 1 ml_min for 2 mL:

        .. code-block:: python

            PPSIM.start(mode="f", direction="r", rate_value=1., rate_units="ml_min", finite_value=2., finite_units="ml")

        :param mode: `"continuous"` or `"c"` for continuous operation,
            `"finite"` or `"f"` for finite operation,
            defaults to `"continuous"`
        :type mode: {`"continuous"`, `"c"`, `"finite"`, `"f"`}
        :param direction: `"forward"`, `"f"`, `"0"`, or `0` to run in the forward direction,
            `"reverse"`, `"r"`, `"1"`, or `1` to run in the reverse direction,
            defaults to `"forward"`
        :type direction: {`"forward"`, `"f"`, `"0"`, `0`, `"reverse"`, `"r"`, `"1"`, `1`}
        :param rate_value: number-like value to set the pump's rate, units are determined by the `rate_units` parameter.
            Defaults to `100`
        :type rate_value: float, int, required
        :param rate_units: `str` to set the rate_units, should be one of `"rpm"` or `"ml_min"`.
            Defaults to `"rpm"`
        :type rate_units: {`"rpm"`, `"ml_min"`}}
        :param finite_value: number-like value to set the pump's operation
            duration in finite-mode, should be one number-like
        :type finite_value: int, float
        :param finite_units: `str` to set the *finite_units* in finite-mode operation, should be one of `"steps"` ,
            `"s"` , `"min"` , `"degrees"` , `"ml"`
        :type finite_units: {`"steps"` , `"s"` , `"min"` , `"degrees"` , `"ml"`}
        :param record: record the data from the pump
        :type record: bool
        :param wait_for_complete: flag to control whether a recipe waits for the pump to complete,
            a finite-mode operation before continuing to the next step.
            Defaults to `True`
        :type wait_for_complete: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def stop(self) -> dict:
        """Stop the pump.

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def pause(self) -> dict:
        """Pause the pump. If the pump was performing a finite-duration operation, the
        operation can be resumed using the `resume` command.

        :return: command dictionary
        :rtype: dict
        """
        content = devices.base.obj.add_object_info_to_content(vars(self), locals(), 'pause')
        devices.base.obj.enqueue_and_pause(vars(self), content)
        return content

    def resume(self, wait_for_complete: bool = True) -> dict:
        """Resume a finite-duration operation. Has no effect if the pump was paused or stopped
        after a continuous-duration operation.

        :param wait_for_complete:
            | flag to control whether a recipe waits for the pump to complete
            | a finite-mode operation before continuing to the next step
            | defaults to `True`
        :type wait_for_complete: bool

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def cancel(self) -> dict:
        """Cancel a finite-duration operation. The `resume` operation will have not be available
        after a `cancel` command is issued.

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def change_speed(self, rate_value: float = 100, rate_units: str = "rpm") -> dict:
        """Change the speed of a pump running in continuous- or finite- mode.

        :param rate_value:
            | number-like value to set the pump's rate, units are determined by the `rate_units` parameter.
            | Defaults to `100`
        :type rate_value: float, int, required
        :param rate_units:
            | `str` to set the rate_units,
            | should be one of `"rpm"` or `"ml_min"`
            | defaults to `"rpm"`
        :type rate_units: str

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the PP device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          steps_done
          rpm
        ====================

        for each input.

        :Example: clear the recorded data for the PP device names PPSIM:

        .. code-block:: python

            PPSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def ml_pumped(self, timestamp: bool = False) -> Union[float, tuple]:
        """Get the volume of fluid displaced by the pump since it was started. The volume resets
        to `0` when a `start` command is issued but not when a `resume` command is issued.

        :Example:

        .. code-block:: python

            PPSIM.start()
            time.sleep(1)
            PPSIM.ml_pumped() → 0.232
            time.sleep(1)
            PPSIM.ml_pumped() → 0.681
            PPSIM.stop() # not reset
            PPSIM.ml_pumped() → 0.745
            PPSIM.start() # reset
            time.sleep(1)
            PPSIM.ml_pumped() → 0.232
            time.sleep(1)
            PPSIM.ml_pumped(timestamp=True) → (0.232, Datetime object)

        :param timestamp:
            | boolean, if set to `True` will return the timestamp of the last updated ml_pumped value.
            | Defaults to `False`
        :type timestamp: bool, optional
        :return: ml of fluid displaced by the pump, always positive
        :rtype: float, tuple
        """
        if timestamp:
            return float(1), datetime.datetime.utcnow()
        return float(1)

    def rpm(self) -> float:
        """Get the current rate of the pump in rpm.

        :Example:

        .. code-block:: python

            rate = PPSIM.rpm()
            print("Current rate is: {} rpm".format(rate))

        :return: current rpm of the pump, always positive
        :rtype: float
        """
        return float(100)

    def internal_volume_ml(self) -> float:
        """Get the internal volume in mL of the pump. Useful when planning prime and
        dose steps.

        :Example:

        .. code-block:: python

            f = PPSIM.internal_volume_ml()
            print(f) → 0.2312

        :return: internal volume in mL of the pump
        :rtype: float
        """
        return float(1)

    def max_rate_ml_min(self) -> float:
        """Get the maximum rate in units of ml/min that the pump can operate
        based on the calibration value. The pump is limited to 500 rpm.

        :Example:

        .. code-block:: python

            f = PPSIM.max_rate_ml_min()
            print(f) → 14.23

        :return: maximum operating rate in units of ml/min, always positive
        :rtype: float
        """
        return float(20)


