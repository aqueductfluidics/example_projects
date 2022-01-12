from typing import Union

import devices.base.obj
from devices.aqueduct.mfpp.constants import *


def instantiate_device(d_device, setup):
    return MFPP(**d_device)


class MFPP(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    CONTINUOUS = MODE_CONTINUOUS
    FINITE = MODE_FINITE

    FORWARD = DIRECTION_FORWARD
    REVERSE = DIRECTION_REVERSE

    ML_MIN = "ml_min"

    ML = "ml"

    def start(self,
              mode: Union[str, int] = "continuous",
              direction: Union[str, int] = "forward",
              rate_value: float = 10,
              rate_units: str = "ml_min",
              finite_value: Union[float, int, None] = None,
              finite_units: Union[str, None] = None,
              record: bool = False,
              wait_for_complete: bool = True
    ) -> dict:
        """Start the pump. The pump can be run indefinitely in `continuous` mode or for a finite
        number of mL's, seconds, or minutes.

        :Example: start the :class:`MFPP` named `MFPPSIM` in the forward direction at 10 ml/min continuously:

        .. code-block:: python

            MFPPSIM.start(mode="c", direction="forward", rate_value=10., rate_units="ml_min")

        :Example: start the :class:`MFPP` named `MFPPSIM` in the reverse direction at 1 ml_min for 2 mL:

        .. code-block:: python

            MFPPSIM.start(mode="f", direction="r", rate_value=1., rate_units="ml_min", finite_value=2., finite_units="ml")

        :param mode: 
            | set the operating mode
            | `"continuous"` or `"c"` for continuous operation,
            | `"finite"` or `"f"` for finite operation,
            | defaults to `"continuous"`
        :type mode: 
            | str
            | {`"continuous"`, `"c"`, `"finite"`, `"f"`}
        :param direction: 
            | set the operating direction
            | `"forward"`, `"f"`, `"0"`, or `0` to run in the forward direction,
            | `"reverse"`, `"r"`, `"1"`, or `1` to run in the reverse direction,
            | defaults to `"forward"`
        :type direction: 
            | str, int
            | {`"forward"`, `"f"`, `"0"`, `0`, `"reverse"`, `"r"`, `"1"`, `1`}
        :param rate_value: 
            | number-like value to set the pump's rate, units are determined by the `rate_units` parameter.
            | Defaults to `10`
        :type rate_value: 
            | float, int
        :param rate_units: 
            | `str` to set the rate_units, should be `"ml_min"`.
            | Defaults to `"ml_min"`
        :type rate_units: 
            | str
            | {`"ml_min"`}
        :param finite_value: 
            | number-like value to set the pump's operation duration in finite-mode 
            | should be number-like
        :type finite_value: 
            | int, float
        :param finite_units: 
            | `str` to set the *finite_units* in finite-mode operation
            | should be `"ml"`
        :type finite_units: 
            | {`"ml"`}
        :param record: record volume displaced (mL done), rate (mL/min), and direction (cw/ccw)
        :type record: bool
        :param wait_for_complete: 
            | flag to control whether a recipe waits for the pump to complete, a finite-mode operation
            | before continuing to the next step.
            Defaults to `True`
        :type wait_for_complete: 
            | bool

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
        return {}

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

    def change_speed(self, rate_value: float = 10, rate_units: str = "ml_min") -> dict:
        """Change the speed of a pump running in continuous- or finite- mode.

        :param rate_value:
            | number-like value to set the pump's rate, units are determined by the `rate_units` parameter.
            | Defaults to `10`
        :type rate_value: 
            | float, int
        :param rate_units:
            | `str` to set the rate_units,
            | should be `"ml_min"`
            | defaults to `"ml_min"`
        :type rate_units: 
            | str

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the MFPP device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          ml_done
          ml_min
        ====================

        :Example: clear the recorded data for the MFPP device names MFPPSIM:

        .. code-block:: python

            MFPPSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def ml_pumped(self) -> float:
        """Get the volume of fluid displaced by the pump since it was started. The volume resets
        to `0` when a `start` command is issued but not when a `resume` command is issued.

        :Example:

        .. code-block:: python

            MFPPSIM.start()
            time.sleep(1)
            MFPPSIM.ml_pumped() # returns 0.232
            time.sleep(1)
            MFPPSIM.ml_pumped() # returns 0.681
            PPSIM.stop() (not reset)
            MFPPSIM.ml_pumped() # returns 0.745
            MFPPSIM.start() (reset)
            time.sleep(1)
            MFPPSIM.ml_pumped() # returns 0.232

        :return: ml of fluid displaced by the pump, always positive
        :rtype: float
        """
        return float(10)

    def get_flow_rate(self, units: str = "ml_min") -> float:
        """Get the current flow rate of the pump in the specified units.

        :Example:

        .. code-block:: python

            f = MFPPSIM.get_flow_rate()
            print(f) # prints 10.232

        :return: current rate of the pump, always positive
        :rtype: float
        """
        return float(10)

    def internal_volume_ml(self) -> float:
        """Get the internal volume in mL of the pump. Useful when planning prime and
        dose steps.

        :Example:

        .. code-block:: python

            f = MFPPSIM.internal_volume_ml()
            print(f) # prints 0.2312

        :return: internal volume in mL of the pump
        :rtype: float
        """
        return float(3)

