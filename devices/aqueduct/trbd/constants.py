import devices.base.constants
from enum import Enum


class SensorConfiguration(Enum):
    NO_SENSOR = 0
    SENSOR = 1


class SensorStatus(Enum):
    INACTIVE = 0
    ACTIVE = 1


NUMBER_INPUTS: int = 3
NODE_PREFIX: str = 'sensor_'
STATUS_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + 'status'
TRANSMITTED_INTENSITY_VALUE_SUFFIX = "_trnsmt_value"
NINETY_DEGREE_INTENSITY_VALUE_SUFFIX = "_90deg_value"
SENSOR_CONFIG_SUFFIX = '_config'
LED_CURRENT_SUFFIX = '_led_current'
PULSE_NUMBER_TRNSMT_SUFFIX = '_trnsmt_pulse_n'
PULSE_NUMBER_NINETY_DEGREE_SUFFIX = '_90deg_pulse_n'
INTERNAL_AVERAGE_TRNSMT_SUFFIX = '_trnsmt_int_avg'
INTERNAL_AVERAGE_NINETY_DEGREE_SUFFIX = '_90deg_int_avg'
TIA_GAIN_TRNSMT_SUFFIX = '_trnsmt_tia_gain'
TIA_GAIN_NINETY_DEGREE_SUFFIX = '_90deg_tia_gain'

BASE = dict(
    type="TRBD",
    number_icons=NUMBER_INPUTS,
)

BASE_DTYPES = dict(
)

BASE.update({
    STATUS_KEY: SensorStatus.INACTIVE.value,
})

BASE_DTYPES.update({
    STATUS_KEY: int.__name__,
})

for __i in range(0, NUMBER_INPUTS):
    BASE.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(__i) + TRANSMITTED_INTENSITY_VALUE_SUFFIX: 0.,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(__i) + NINETY_DEGREE_INTENSITY_VALUE_SUFFIX: 0.,
        NODE_PREFIX + str(__i) + SENSOR_CONFIG_SUFFIX: SensorConfiguration.SENSOR.value,
        NODE_PREFIX + str(__i) + LED_CURRENT_SUFFIX: 0,
        NODE_PREFIX + str(__i) + PULSE_NUMBER_TRNSMT_SUFFIX: 0,
        NODE_PREFIX + str(__i) + PULSE_NUMBER_NINETY_DEGREE_SUFFIX: 0,
        NODE_PREFIX + str(__i) + INTERNAL_AVERAGE_TRNSMT_SUFFIX: 0,
        NODE_PREFIX + str(__i) + INTERNAL_AVERAGE_NINETY_DEGREE_SUFFIX: 0,
        NODE_PREFIX + str(__i) + TIA_GAIN_TRNSMT_SUFFIX: 0,
        NODE_PREFIX + str(__i) + TIA_GAIN_NINETY_DEGREE_SUFFIX: 0,
    })
    BASE_DTYPES.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(__i)
        + TRANSMITTED_INTENSITY_VALUE_SUFFIX: int.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(__i)
        + NINETY_DEGREE_INTENSITY_VALUE_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + SENSOR_CONFIG_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + LED_CURRENT_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + PULSE_NUMBER_TRNSMT_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + PULSE_NUMBER_NINETY_DEGREE_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + INTERNAL_AVERAGE_TRNSMT_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + INTERNAL_AVERAGE_NINETY_DEGREE_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + TIA_GAIN_TRNSMT_SUFFIX: int.__name__,
        NODE_PREFIX + str(__i) + TIA_GAIN_NINETY_DEGREE_SUFFIX: int.__name__,
    })

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

NO_INPUT_VALUE = "X"

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Turbidity Sensor (" + DEVICE_TYPE + ")"

CATEGORY = "Optical Sensors"

ICON_XML_PATH = "static/images/devices/{0}/{1}.xml".format(DEVICE_TYPE.lower(), DEVICE_TYPE.upper())

ICON_XML_TEMPLATE_PATH = "devices/{0}/{1}.xml".format(DEVICE_TYPE.lower(), DEVICE_TYPE.upper())

del __i

