import devices.base.constants


NUMBER_INPUTS: int = 4
DEVICE_TYPE = "DOBT"
STATUS_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + 'status'
SUCTION_STATUS_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + 'suction'
INPUT_PREFIX = "arm_"
X_AXIS_SUFFIX = '_x_mm'
Y_AXIS_SUFFIX = '_y_mm'
Z_AXIS_SUFFIX = '_z_mm'
EFFECTOR_ANGLE_SUFFIX = '_effec_ang_deg'
TARGET_AXIS_SUFFIX = '_target'
RAW_AXIS_SUFFIX = '_raw'
AXES = (X_AXIS_SUFFIX, Y_AXIS_SUFFIX, Z_AXIS_SUFFIX, EFFECTOR_ANGLE_SUFFIX)
THETA_SUFFIX = '_theta'
DELTA_X_SUFFIX = '_dx'
DELTA_Y_SUFFIX = '_dy'
Z_OFFSET_SUFFIX = '_dz'

MM_XY_MAX = 328
MM_XY_MIN = 111

MM_MAX_SQ = MM_XY_MAX ** 2
MM_MIN_SQ = MM_XY_MIN ** 2

ALL_IN_POSITION = 15
OUT_OF_POSITION = 0

ALL_SUCTION_OFF = 0

MINIMUM_VELOCITY = 100
MAXIMUM_VELOCITY = 1000

BASE = dict(
    type=DEVICE_TYPE,
    number_icons=4,
    number_decks=4,
    _number_robot_inputs=NUMBER_INPUTS,
)

BASE_DTYPES = dict(
    _number_robot_inputs=int.__name__,
)

BASE.update({
    STATUS_KEY: ALL_IN_POSITION,
    SUCTION_STATUS_KEY: ALL_SUCTION_OFF,
})

BASE_DTYPES.update({
    STATUS_KEY: int.__name__,
    SUCTION_STATUS_KEY: int.__name__,
})

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + X_AXIS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + Y_AXIS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + Z_AXIS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + EFFECTOR_ANGLE_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + X_AXIS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + Y_AXIS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + Z_AXIS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + EFFECTOR_ANGLE_SUFFIX: 0,
        INPUT_PREFIX + str(i) + RAW_AXIS_SUFFIX + X_AXIS_SUFFIX: 0,
        INPUT_PREFIX + str(i) + RAW_AXIS_SUFFIX + Y_AXIS_SUFFIX: 0,
        INPUT_PREFIX + str(i) + RAW_AXIS_SUFFIX + Z_AXIS_SUFFIX: 0,
        INPUT_PREFIX + str(i) + THETA_SUFFIX: 0,
        INPUT_PREFIX + str(i) + DELTA_X_SUFFIX: 0,
        INPUT_PREFIX + str(i) + DELTA_Y_SUFFIX: 0,
        INPUT_PREFIX + str(i) + DELTA_Y_SUFFIX: 0,
        INPUT_PREFIX + str(i) + Z_OFFSET_SUFFIX: 0,
    })
    BASE_DTYPES.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + X_AXIS_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + Y_AXIS_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + Z_AXIS_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + EFFECTOR_ANGLE_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + X_AXIS_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + Y_AXIS_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + Z_AXIS_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + INPUT_PREFIX + str(i) + TARGET_AXIS_SUFFIX + EFFECTOR_ANGLE_SUFFIX: str.__name__,
        INPUT_PREFIX + str(i) + RAW_AXIS_SUFFIX + X_AXIS_SUFFIX: str.__name__,
        INPUT_PREFIX + str(i) + RAW_AXIS_SUFFIX + Y_AXIS_SUFFIX: str.__name__,
        INPUT_PREFIX + str(i) + RAW_AXIS_SUFFIX + Z_AXIS_SUFFIX: str.__name__,
        INPUT_PREFIX + str(i) + THETA_SUFFIX: float.__name__,
        INPUT_PREFIX + str(i) + DELTA_X_SUFFIX: float.__name__,
        INPUT_PREFIX + str(i) + DELTA_Y_SUFFIX: float.__name__,
        INPUT_PREFIX + str(i) + Z_OFFSET_SUFFIX: float.__name__,
    })

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DISPLAY_NAME = "Dobot Arm (" + DEVICE_TYPE + ")"

CATEGORY = "Robots"

MOVE_JUMP_MODE = 0
MOVE_JOINT_MODE = 1
MOVE_LINEAR_MODE = 2

NUMBER_DECKS = 4

X_GRID_SIZE_MM = 35.
Y_GRID_SIZE_MM = 35.

# center of square
A1_X_MM = -280.0
A1_Y_MM = -152.5

# center of square
I14_X_MM = 0.
I14_Y_MM = 302.5

# center of square
Q2_X_MM = 280.
Q2_Y_MM = -117.5

DECK_GENERATOR = (
    ("A", (2, 9)),
    ("B", (1, 10)),
    ("C", (1, 11)),
    ("D", (2, 12)),
    ("E", (9, 13)),
    ("F", (10, 13)),
    ("G", (10, 14)),
    ("H", (10, 14)),
    ("I", (10, 14)),
    ("J", (10, 14)),
    ("K", (10, 14)),
    ("L", (10, 13)),
    ("M", (9, 13)),
    ("N", (2, 12)),
    ("O", (1, 11)),
    ("P", (1, 10)),
    ("Q", (2, 9)),
)


DEFAULT_THETA = 0
DEFAULT_DELTA_X = 0
DEFAULT_DELTA_Y = 0

del i
