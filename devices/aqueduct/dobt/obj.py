from typing import List, Union

import devices.base.obj
from devices.aqueduct.dobt.constants import *


def instantiate_device(d_device, setup):
    return DOBT(setup, **d_device)


class MoveCommand(object):
    x: Union[int, float, None] = None
    y: Union[int, float, None] = None
    z: Union[float, float, None] = None
    z_threshold: Union[int, float, None] = None
    container: Union["classes.containers.Container", str, None] = None
    position: Union[str, None] = None
    position_offset_mm: Union[int, float, None] = None
    wait_for_complete: Union[bool, None] = None

    def __init__(self, *args, **kwargs):
        self.x = None
        self.y = None
        self.z = None
        self.z_threshold = None

        for v, k in zip(args, ('x', 'y', 'z', 'z_threshold')):
            setattr(self, k, v)

        for k, v in kwargs.items():
            if k in self.__dict__.keys():
                if v is not None:
                    setattr(self, k, v)

    def _to_command(self) -> tuple:

        return self.x, self.y, self.z, self.z_threshold

    def _to_multipoint_command(self) -> tuple:

        return self.x, self.y, self.z


class DOBT(devices.base.obj.Device):

    def __init__(self, setup, **kwargs):
        super().__init__(**kwargs)
        self.__decks__ = NUMBER_DECKS * [[]]


    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__decks__[item]

    def get_position(self, arm_index: int) -> tuple:
        """Command to get the position of a an arm.

        The position reading will be fresh, so this command can be used to get the latest
        arm position even after moving an arm manually.

        Returns a tuple of (x_mm, y_mm, z_mm, end_effector_angle).

        :param arm_index:
        :return: positions
        :rtype: tuple
        """ 

        return tuple(100, 100, 100, 5)

    def move(self, commands: List[tuple], wait_for_complete: bool = True, update_interval_s: float = 1.):

        return {}

    def move_xyz(
            self,
            arm0: Union[MoveCommand, None] = None,
            arm1: Union[MoveCommand, None] = None,
            arm2: Union[MoveCommand, None] = None,
            arm3: Union[MoveCommand, None] = None,
            commands: List[tuple] = None,
            wait_for_complete: bool = True,
            update_interval_s: float = 1.
    ):
        """Command to move one or more arms in x, y, and z.

        For each of the 4 arm inputs, pass a :class:`MoveCommand`, a dictionary (specified keys below), or None.

        If a :class:`MoveCommand` is passed, the command must have valid `x`, `y`, `z`,
        and `z_threshold` members.

        If only `x` and `y` are set (`z` and `z_threshold` not specified), the arm will move only
        in the xy plane and will not move vertically.

        If only `z` is set, the arm will move along the z axis only and will not move in the xy plane.

        If `x`, `y`, and `z` are set, the arm will move first in the xy plane to the target xy position and
        then move vertically to the target z position.

        If `x`, `y`, `z`, and `z_threshold` are set, the arm will move first in the z axis to ensure the arm
        is above the `z_threshold` height, then move in the xy plane to the target position, and
        then move vertically to the target z position.

        Here's an example of moving the arm 0 in the xy plane.

        :Example:

        .. code-block:: python

            command = DOBTSIM.make_command(x = 200, y = 0)

            DOBTSIM.move_xyz(arm0=command)

        Here's another example of moving arm 0 in x, y, and z while ensuring that the
        arm is above 20mm before moving in the xy plane.

        :Example:

        .. code-block:: python

            command = DOBTSIM.make_command(x = 270, y = -45, z = -20, z_threshold = 20)

            DOBTSIM.move_xyz(arm0=command)

        If a :class:`dict` is passed as a parameter for `armN`, the command must have at least:

        =================  ==========
              key           required
        =================  ==========
          'x'                 no
          'y'                 no
          'z'                 no
          't_threshold'       no
        =================  ==========

        :Example:

        .. code-block:: python

            dict_command = {
                'x': 200,
                'y': 200,
            }

            DOBTSIM.move_xyz(arm0=dict_command)

        :param arm0:
            | MoveCommand, dict, or None to control motion for arm input 0
            | Defaults to None
        :type arm0: MoveCommand, dict, None, required
        :param arm1:
            | MoveCommand, dict, or None to control motion for arm input 1
            | Defaults to None
        :type arm1: MoveCommand, dict, None, required
        :param arm2:
            | MoveCommand, dict, or None to control motion for arm input 2
            | Defaults to None
        :type arm2: MoveCommand, dict, None, required
        :param arm3:
            | MoveCommand, dict, or None to control motion for arm input 3
            | Defaults to None
        :type arm3: MoveCommand, dict, None, required
        :param commands:
            | tuple, list,
            | Defaults to None
        :type commands: tuple or tuples or lists, list or tuples or lists
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

        :return: tx_params
        :rtype: dict
        """
        return {}

    def multipoint_move(
            self,
            arm0: List[MoveCommand] = None,
            arm1: List[MoveCommand] = None,
            arm2: List[MoveCommand] = None,
            arm3: List[MoveCommand] = None,
            commands: List[List[tuple]] = None,
            velocity_commands: List[float] = None,
            wait_for_complete: bool = True,
            update_interval_s: float = 1.
        ):
        """Command to move one or more arm inputs to multiple defined x, y, and z points.

        For each of the 4 arm inputs, pass a list of :class:`MoveCommand`, a dictionary (specified keys below), or None.

        If a list of :class:`MoveCommand` is passed, the commands must have valid `x`, `y`, and `z` members.

        If only `x` and `y` are set (`z` not specified), the arm will move only in the xy-plane
        and will not move vertically.

        If only `z` is set, the arm will move only along the z axis and will not move in the xy-plane.

        If `x`, `y`, and `z` are set, the arm will first move in the xy-plane to the target position and
        then move vertically to the target z position.

        Additionally, a list of floats can be passed to the 'velocity_command' attribute in order to change the overall
        speed of each arm.

        Here's an example of moving the arm in the xy-plane to three discrete points.

        :Example:

        .. code-block:: python

            command = DOBTSIM.make_command(x = 200, y = 0)
            command1 = DOBTSIM.make_command(x = 200, y = 300)
            command2 = DOBTSIM.make_command(x = 0, y = 300)

            DOBTSIM.multipoint_move(arm0=[command, command1, command2], velocity_command=[500,0,0,0])

        If a :class:`dict` is passed as a parameter for `armN`, the command must have at least:

        =================  ==========
              key           required
        =================  ==========
          'x'                 no
          'y'                 no
          'z'                 no
        =================  ==========

        :Example:

        .. code-block:: python

            dict_command = {
                'x': 200,
                'y': 200,
            }
            dict_command1 = {
                'x': 200,
                'y': 0,
            }

            DOBTSIM.multipoint_move(arm0=[dict_command, dict_command1])

        :param arm0:
            | List of type MoveCommand or dict, or None to control motion for arm input 0
            | Defaults to None
        :type arm0: List of MoveCommands or dicts or None, required
        :param arm1:
            | List of type MoveCommand or dict, or None to control motion for arm input 1
            | Defaults to None
        :type arm1: List of MoveCommands or dicts or None, required
        :param arm2:
            | List of type MoveCommand or dict, or None to control motion for arm input 2
            | Defaults to None
        :type arm2: List of MoveCommands or dicts or None, required
        :param arm3:
            | List of type MoveCommand or dict, or None to control motion for arm input 3
            | Defaults to None
        :type arm3: List of MoveCommands or dicts or None, required
        :param commands:
            | list of list of tuple points (commands)
            | Defaults to None
        :type commands: list of list of tuples
        :param wait_for_complete:
            | Determines blocking behavior of command, if set to `True`, requires
            | any finite operations to complete before proceeding, if set to a tuple of
            | bools, requires only inputs flagged to complete
            | Defaults to True
        :type wait_for_complete: bool, tuple of tuples of bools
        :param update_interval_s:
            | interval to update, should be greater than 0.5
            | Defaults to 1
        :type update_interval_s: PumpCommand, dict, None, required
        :param velocity_commands:
            | combined velocity and acceleration of each arm for this command
        :type velocity_commands: list of floats

        :return: tx_params
        :rtype: dict
        """
        return {}

    def move_container(
            self,
            container: Union[str, "classes.containers.Container"],
            position: str = None,
            position_offset_mm: Union[int, float] = None,
            z: Union[int, float] = None,
            z_threshold: Union[int, float] = None,
            wait_for_complete: bool = True,
            update_interval_s: float = 1.
    ) -> dict:
        """
        Experimental.

        """

        return {}

    def suction(
            self,
            arm0: Union[int, bool, None] = None,
            arm1: Union[int, bool, None] = None,
            arm2: Union[int, bool, None] = None,
            arm3: Union[int, bool, None] = None
    ):
        """Command to turn the suction on or off for one or more arms.

        For each of the 4 arm inputs, pass an :class:`int`, :class:`str`, :class:`bool` or None.

        =================      ==========
              param               action
        =================      ==========
                1              suction on
               "1"             suction on
              True             suction on
                0              suction off
               "0"             suction off
              False            suction off
           all others          no action
        =================      ==========

        :Example:

        .. code-block:: python

            # turn vacuum on inputs 0 and 2 on

            DOBTSIM.suction(pump0=True, pump2=1)

        :Example:

        .. code-block:: python

            # turn vacuum on input 1 on and vacuum on input 3 off

            DOBTSIM.suction(pump1=True, pump3=False)

        :param arm0:
            | int, str, bool, None
            | Defaults to None
        :type arm0: int, str, bool, None, not required
        :param arm1:
            | int, str, bool, None
            | Defaults to None
        :type arm1: int, str, bool, None, not required
        :param arm2:
            | int, str, bool, None
            | Defaults to None
        :type arm2: int, str, bool, None, not required
        :param arm3:
            | int, str, bool, None
            | Defaults to None
        :type arm3: int, str, bool, None, not required

        :return: tx_params
        :rtype: dict
        """
        return {}

    @staticmethod
    def make_command(
            x: Union[int, float, str] = None,
            y: Union[int, float, str] = None,
            z: Union[int, float, str] = None,
            z_threshold: Union[int, float, str] = None, **kwargs
    ) -> MoveCommand:
        """Helper method to create an instance of a :class:`MoveCommand`.

        A :class:`MoveCommand` is an object with the required fields to set the motion
        parameters for an arm input.

        :return: move_command
        :rtype: MoveCommand
        """
        return MoveCommand(**{**kwargs, **locals()})
