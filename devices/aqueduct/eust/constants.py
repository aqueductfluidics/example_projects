import devices.base.constants
from enum import Enum


class Status(Enum):
    STATUS_STOPPED = 0
    STATUS_CLOCKWISE = 1
    STATUS_COUNTERCLOCKWISE = 2


class MixerSeries(Enum):
    _60 = 0


class TemperatureUnits(Enum):
    CELCIUS = 0
    FARENHEIT = 1
    KELVIN = 2


NUMBER_INPUTS: int = 4
NODE_PREFIX = 'mixer_'
SERIES_SUFFIX = '_series'
RPM_SUFFIX = '_rpm'
DIRECTION_SUFFIX = '_dir'
TORQUE_SUFFIX = '_tq'
TEMP_VALUE_SUFFIX = '_temp_val'
TEMP_UNITS_SUFFIX = '_temp_uni'

BASE = dict(
    type="EUST",
    number_icons=4,
    period_ms=None,
    _number_mixer_inputs=NUMBER_INPUTS,
)

BASE_DTYPES = dict(
    period_ms=int.__name__,
    _number_mixer_inputs=int.__name__,
)

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        NODE_PREFIX + str(i) + SERIES_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RPM_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + DIRECTION_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + TORQUE_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + TEMP_VALUE_SUFFIX: 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + TEMP_UNITS_SUFFIX: "C",
    })
    BASE_DTYPES.update({
        NODE_PREFIX + str(i) + SERIES_SUFFIX: MixerSeries._60.value,  # noqa
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + RPM_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + DIRECTION_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + TORQUE_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + TEMP_VALUE_SUFFIX: str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + TEMP_UNITS_SUFFIX: str.__name__,
    })

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "IKA Eurostar 60 (" + DEVICE_TYPE + ")"

CATEGORY = "Mixers"

# value returned by the EUST device
# when one of the inputs is absent
NO_INPUT_FLOAT_VALUE = "---.--"
NO_INPUT_INT_VALUE = "---"

