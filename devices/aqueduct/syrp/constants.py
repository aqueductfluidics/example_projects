import devices.base.constants

NUMBER_INPUTS: int = 4
NODE_PREFIX: str = 'pump_'
STATUS_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + 'status'
MODE_SUFFIX = '_mode'
RATE_VALUE_SUFFIX = '_rate_value'
RATE_UNITS_SUFFIX = '_rate_units'
FINITE_VALUE_SUFFIX = '_finite_value'
FINITE_UNITS_SUFFIX = '_finite_units'
VOLUME_INFUSED_SUFFIX = '_infused'
VOLUME_WITHDRAWN_SUFFIX = '_withdrawn'
VOLUME_DISPLACED_UNITS_SUFFIX = '_vol_units'
COMMAND_PROTOCOL_SUFFIX = '_cmd_proto'
SYRINGE_LENGTH_SUFFIX = '_syringe_length_mm'
SYRINGE_DIAM_SUFFIX = '_syringe_diam_mm'
SYRINGE_MATERIAL_SUFFIX = '_syringe_material'
BLOCKING_SUFFIX = '_blocking'
BLOCKING_INTERVAL_KEY = 'blocking_interval_s'

ALL_STOPPED = 0x00
ALL_PAUSED = 0xFF

BASE = dict(
    type="SYRP",
    number_ports=2*NUMBER_INPUTS,
    number_icons=NUMBER_INPUTS,
    _number_pump_inputs=NUMBER_INPUTS,
)

BASE_DTYPES = dict(
    _status=int.__name__,
    _number_pump_inputs=int.__name__,
)

BASE.update({
    STATUS_KEY: ALL_STOPPED,
    BLOCKING_INTERVAL_KEY: 0,
})

BASE_DTYPES.update({
    STATUS_KEY: int.__name__,
    BLOCKING_INTERVAL_KEY: float.__name__
})

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + MODE_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RATE_VALUE_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RATE_UNITS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + FINITE_VALUE_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + FINITE_UNITS_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + VOLUME_INFUSED_SUFFIX: str(0),
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + VOLUME_WITHDRAWN_SUFFIX: str(0),
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + VOLUME_DISPLACED_UNITS_SUFFIX: 0,
        NODE_PREFIX + str(i) + SYRINGE_LENGTH_SUFFIX: 75,
        NODE_PREFIX + str(i) + SYRINGE_DIAM_SUFFIX: 25,
        NODE_PREFIX + str(i) + SYRINGE_MATERIAL_SUFFIX: "glass",
        NODE_PREFIX + str(i) + BLOCKING_SUFFIX: 0,
    })
    BASE_DTYPES.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + MODE_SUFFIX: int.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RATE_VALUE_SUFFIX: float.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RATE_UNITS_SUFFIX: int.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + FINITE_VALUE_SUFFIX: float.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + FINITE_UNITS_SUFFIX: int.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + VOLUME_INFUSED_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + VOLUME_WITHDRAWN_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + VOLUME_DISPLACED_UNITS_SUFFIX: int.__name__,
        NODE_PREFIX + str(i) + SYRINGE_LENGTH_SUFFIX: float.__name__,
        NODE_PREFIX + str(i) + SYRINGE_DIAM_SUFFIX: float.__name__,
        NODE_PREFIX + str(i) + SYRINGE_MATERIAL_SUFFIX: str.__name__,
        NODE_PREFIX + str(i) + BLOCKING_SUFFIX: int.__name__,
    })


BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Syringe Pump" + " (" + DEVICE_TYPE + ")"

CATEGORY = "Pumps"

ICON_XML_PATH = "static/images/devices/{0}/{1}.xml".format(DEVICE_TYPE.lower(), DEVICE_TYPE.upper())

STATUS_STOPPED = 0
STATUS_INFUSING = 1
STATUS_WITHDRAWING = 2
STATUS_PAUSED = 3

DIRECTION_MAPPING = dict(
    infuse=STATUS_INFUSING,
    inf=STATUS_INFUSING,
    i=STATUS_INFUSING,
    withdraw=STATUS_WITHDRAWING,
    wdw=STATUS_WITHDRAWING,
    w=STATUS_WITHDRAWING,
)

DIRECTION_MAPPING.update({
    str(STATUS_INFUSING): STATUS_INFUSING,
    str(STATUS_WITHDRAWING): STATUS_WITHDRAWING,
    STATUS_INFUSING: STATUS_INFUSING,
    STATUS_WITHDRAWING: STATUS_WITHDRAWING,
})

UL_MIN = 0
UL_HR = 1
ML_MIN = 2
ML_HR = 3

RATE_UNIT_MAPPING = dict(
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
    str(UL_MIN): UL_MIN,
    str(UL_HR): UL_HR,
    str(ML_MIN): ML_MIN,
    str(ML_HR): ML_HR,
    UL_MIN: 0,
    UL_HR: 1,
    ML_MIN: 2,
    ML_HR: 3,
})

VALID_RATE_UNITS = set(RATE_UNIT_MAPPING.keys())

UL = 0
ML = 1

VOL_UNIT_MAPPING = dict(
    ul=UL,
    ml=ML,
)

VOL_UNIT_MAPPING.update({
    str(UL): UL,
    str(ML): ML,
    UL: UL,
    ML: ML,
})

VALID_VOLUME_UNITS = set(VOL_UNIT_MAPPING.keys())

MODE_CONTINUOUS: int = 0
MODE_FINITE: int = 1

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

AUTO_STOP_EXPR_STR = ""
for i in range(0, NUMBER_INPUTS):
    prepend = "" if i == 0 else " and "
    AUTO_STOP_EXPR_STR += "{}((int(S)>>(2*{}))&3) in ({},{})".format(prepend, i, STATUS_STOPPED, STATUS_PAUSED)

AUTO_STOP_EXPR_CONSTANT = "S"

del i


