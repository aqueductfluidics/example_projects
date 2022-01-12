import devices.base.obj
from devices.aqueduct.sv.constants import *


def instantiate_device(d_device, setup):
    return SV(**d_device)


class SV(devices.base.obj.Device):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_config(self):
        return {}

    def set_config(self, name: str = None, _connection_id_mm: float = None,
                   _connection_length_mm: float = None, _connection_material: str = None):
        return {}

    def set_angle(self, angle: float):
        """Set the rotor angle in the Selector Valve in units of `degrees` from 0 to 359.9.

        Example: set the angle of SVSIM's rotor to 180 deg:

        .. code-block:: python

            SVSIM.set_angle(180)

        :param angle:
            | units of `degrees` from 0 to 359.9
        :type angle: int, float, required

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def set_port(self, port_index: int):
        """Set the rotor in a Selector Valve to a port by index.

        =====  =====
        Angle   Port
        =====  =====
           0     1
          45     2
          90     3
         135     4
         180     5
         225     6
         270     7
         315     8
        =====  =====

        Example: set the port of SVSIM to 5:

        .. code-block:: python

            SVSIM.set_port(5)

        :param port_index:
            | from 1 to 8
        :type port_index: int, required

        :return: command dictionary
        :rtype: dict
        """
        return {}

    def get_port(self) -> int:
        """Get the current port index of a Selector Valve.

        Example:

        .. code-block:: python

            SVSIM.set_port(5)
            SVSIM.get_port() → 5

        :return: port index
        :rtype: int
        """
        return 0

    def internal_volume_ml(self) -> float:
        """Get the internal volume in mL of the valve. Useful when planning prime and
        dose steps.

        :Example:

        .. code-block:: python

            f = SVSIM.internal_volume_ml()
            print(f) → 0.021

        :return: internal volume in mL of the pump
        :rtype: float
        """
        return 1.0





