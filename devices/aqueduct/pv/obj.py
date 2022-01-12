import devices.base.obj
from devices.aqueduct.pv.constants import *


def instantiate_device(d_device, setup):
    return PV(**d_device)


class PV(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_config(self) -> None:
        """Get the configuration settings of the PV device from firmware.

        :Example:

        .. code-block:: python

            PVSIM.get_config()

        :return: None
        :rtype: None
        """
        return None

    def set_config(self, name: str = None) -> None:
        """Set the configuration settings of the PV device on firmware.

        :param name:
            | A string-like value to be assigned as the device's name.
            | No spaces allowed.
        :type name: str

        :Example:

        .. code-block:: python

            PVSIM.set_config(name="MYPV")

        :return: None
        :rtype: None
        """
        return None

    def set_position(self, pct_open: float = 1., record: bool = False):
        """Set the position of the pinch valve.

        :Example:

        .. code-block:: python

            PVSIM.set_position(0.70)

        :param pct_open:
            | A float-like value.
            | Range must be between 0. and 1.
            | `pct_open` = 1. sets the valve fully open,
            | `pct_open` = 0. sets the valve fully closed.
        :type pct_open: float,  [0., 1.]
        :param record:
            | record the operational data of the pump
            | Defaults to False
        :type record: bool
        :return: None
        :rtype: None
        """
        return {}

    def clear_recorded(self):
        """Clear the recorded data for the PV device. The recordable data includes:

        ====================
          Recordable Data
        ====================
          pct_open
        ====================

        for each input.

        :Example: clear the recorded data for the PV device names PVSIM:

        .. code-block:: python

            PVSIM.clear_recorded()

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def position(self) -> float:
        """Get the position of the pinch valve.

        :Example:

        .. code-block:: python

            pos = PVSIM.position()
            print(pos) # 0.70

        :return: position of the pinch valve
        :rtype:
            | A float-like value.
            | Range between 0. and 1.
        """
        return 1.









