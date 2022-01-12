import devices.base.constants

from enum import Enum

NUMBER_PUMPS: int = 12
NODE_PREFIX: str = 'pump_'
STATUS_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + 'status'
MODE_SUFFIX = '_mode'
STEPS_DONE_SUFFIX = '_steps_done'
RPM_SUFFIX = '_rpm'
REV_PER_ML_SUFFIX = '_rev_per_ml'
TUBING_LENGTH_MM_SUFFIX = '_tubing_length_mm'
TUBING_ID_MM_SUFFIX = '_tubing_id_mm'
TUBING_MATERIAL_SUFFIX = '_tubing_material'
BLOCKING_SUFFIX = '_blocking'
BLOCKING_INTERVAL_KEY = 'blocking_interval_s'

ALL_STOPPED = 0x00
ALL_PAUSED = 0xFF

BASE = dict(
    type="PP12",
    number_ports=2*NUMBER_PUMPS,
    number_icons=NUMBER_PUMPS,
    _number_pump_inputs=NUMBER_PUMPS,
)

BASE_DTYPES = dict(
    _status=int.__name__,
    _number_pump_inputs=int.__name__,
)


def update_base_common(base: dict, base_dtypes: dict):
    base.update({
        STATUS_KEY: ALL_STOPPED,
        BLOCKING_INTERVAL_KEY: 0,
    })

    base_dtypes.update({
        STATUS_KEY: int.__name__,
        BLOCKING_INTERVAL_KEY: float.__name__
    })


def update_base(base: dict, base_dtypes: dict, number_pumps: int) -> None:

    for i in range(0, number_pumps):
        base.update({
            devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + MODE_SUFFIX: 0,
            devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + STEPS_DONE_SUFFIX: 0,
            devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RPM_SUFFIX: 0,
            NODE_PREFIX + str(i) + REV_PER_ML_SUFFIX: 24,
            NODE_PREFIX + str(i) + TUBING_LENGTH_MM_SUFFIX: 121.5,
            NODE_PREFIX + str(i) + TUBING_ID_MM_SUFFIX: 1.,
            NODE_PREFIX + str(i) + TUBING_MATERIAL_SUFFIX: "pharmaline",
            NODE_PREFIX + str(i) + BLOCKING_SUFFIX: 0,
        })
        base_dtypes.update({
            devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + MODE_SUFFIX: int.__name__,
            devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + STEPS_DONE_SUFFIX: int.__name__,
            devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RPM_SUFFIX: float.__name__,
            NODE_PREFIX + str(i) + REV_PER_ML_SUFFIX: float.__name__,
            NODE_PREFIX + str(i) + TUBING_LENGTH_MM_SUFFIX: float.__name__,
            NODE_PREFIX + str(i) + TUBING_ID_MM_SUFFIX: float.__name__,
            NODE_PREFIX + str(i) + TUBING_MATERIAL_SUFFIX: str.__name__,
            NODE_PREFIX + str(i) + BLOCKING_SUFFIX: int.__name__,
        })


update_base_common(BASE, BASE_DTYPES)
update_base(BASE, BASE_DTYPES, NUMBER_PUMPS)

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DeviceBase = Enum('DeviceBase', {k: k for k in BASE.keys()})

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "12 x Peristaltic Pump (" + DEVICE_TYPE + ")"

CATEGORY = "Pumps"

STATUS_STOPPED = 0
STATUS_CLOCKWISE = 1
STATUS_COUNTERCLOCKWISE = 2
STATUS_PAUSED = 3

DIRECTION_MAPPING = dict(
    forward=STATUS_CLOCKWISE,
    f=STATUS_CLOCKWISE,
    cw=STATUS_CLOCKWISE,
    reverse=STATUS_COUNTERCLOCKWISE,
    r=STATUS_COUNTERCLOCKWISE,
    ccw=STATUS_COUNTERCLOCKWISE,
)

DIRECTION_MAPPING.update({
    str(STATUS_CLOCKWISE): STATUS_CLOCKWISE,
    str(STATUS_COUNTERCLOCKWISE): STATUS_COUNTERCLOCKWISE,
    STATUS_CLOCKWISE: STATUS_CLOCKWISE,
    STATUS_COUNTERCLOCKWISE: STATUS_COUNTERCLOCKWISE,
})

RPM = 0
UL_MIN = 1
UL_HR = 2
ML_MIN = 3
ML_HR = 4

RATE_UNIT_MAPPING = dict(
    rpm=RPM,
    ul_min=UL_MIN,
    ul_hr=UL_HR,
    ml_min=ML_MIN,
    ml_hr=ML_HR,
)

RATE_UNIT_MAPPING.update({
    "ul/min": UL_MIN,
    "ul/hr": UL_HR,
    "ml/min": ML_MIN,
    "ml/hr": ML_HR,
    str(RPM): RPM,
    str(UL_MIN): UL_MIN,
    str(UL_HR): UL_HR,
    str(ML_MIN): ML_MIN,
    str(ML_HR): ML_HR,
    RPM: RPM,
    UL_MIN: UL_MIN,
    UL_HR: UL_HR,
    ML_MIN: ML_MIN,
    ML_HR: ML_HR,
})

VALID_RATE_UNITS = set(RATE_UNIT_MAPPING.keys())

MODE_NOT_SET = -1
MODE_CONTINUOUS = 0
MODE_FINITE = 1

MODE_MAPPING = dict(
    continuous=MODE_CONTINUOUS,
    c=MODE_CONTINUOUS,
    finite=MODE_FINITE,
    f=MODE_FINITE,
)

MODE_MAPPING.update({
    str(MODE_CONTINUOUS): MODE_CONTINUOUS,
    str(MODE_FINITE): MODE_FINITE,
    MODE_FINITE: MODE_FINITE,
    MODE_CONTINUOUS: MODE_CONTINUOUS,
})

STEPS_PER_REV = 200
MAX_MICROSTEPS = 2147483648
MICROSTEPS_PER_STEP = 256


STEPS = 0
SECONDS = 1
MINUTES = 2
DEGREES = 3
ML = 4
UL = 5
REVOLUTIONS = 6

FINITE_UNIT_MAPPING = dict(
    steps=STEPS,
    seconds=SECONDS,
    minutes=MINUTES,
    degrees=DEGREES,
    ml=ML,
    ul=UL,
    s=SECONDS,
)

FINITE_UNIT_MAPPING.update({
    str(STEPS): STEPS,
    str(SECONDS): SECONDS,
    str(MINUTES): MINUTES,
    str(DEGREES): DEGREES,
    str(UL): UL,
    str(ML): ML,
    str(REVOLUTIONS): REVOLUTIONS,
    STEPS: STEPS,
    SECONDS: SECONDS,
    MINUTES: MINUTES,
    DEGREES: DEGREES,
    UL: UL,
    ML: ML,
    REVOLUTIONS: REVOLUTIONS,
})

VALID_FINITE_UNITS = set(FINITE_UNIT_MAPPING.keys())

AUTO_STOP_EXPR_STR = ""
for i in range(0, NUMBER_PUMPS):
    prepend = "" if i == 0 else " and "
    AUTO_STOP_EXPR_STR += "{}((int(S)>>(2*{}))&3) == {}".format(prepend, i, STATUS_STOPPED)

AUTO_STOP_EXPR_CONSTANT = "S"

del i