import config
import devices.base.constants

NUMBER_INPUTS: int = 4
NUMBER_TRANSDUCERS_PER_INPUT: int = 3
NUMBER_TRANSDUCERS: int = NUMBER_INPUTS * NUMBER_TRANSDUCERS_PER_INPUT

BASE = dict(
    type="SCIP",
    number_icons=NUMBER_TRANSDUCERS,
    number_ports=NUMBER_TRANSDUCERS * 2,
)

BASE_DTYPES = dict(

)

for i in range(0, NUMBER_TRANSDUCERS):
    BASE.update({
        config.DEVICE_GLOBAL_PARAM_PREFIX + 'txdcr_' + str(i) + '_pressure_value': 0,
        config.DEVICE_GLOBAL_PARAM_PREFIX + 'txdcr_' + str(i) + '_pressure_units': "psi",
        '_connection_' + str(i) + '_length_mm': 30,
        '_connection_' + str(i) + '_id_mm': 6,
        '_connection_' + str(i) + '_material': 'polysulfone',
    })
    BASE_DTYPES.update({
        config.DEVICE_GLOBAL_PARAM_PREFIX + 'txdcr_' + str(i) + '_pressure_value': float.__name__,
        config.DEVICE_GLOBAL_PARAM_PREFIX + 'txdcr_' + str(i) + '_pressure_units': str.__name__,
        '_connection_' + str(i) + '_length_mm': float.__name__,
        '_connection_' + str(i) + '_id_mm': float.__name__,
        '_connection_' + str(i) + '_material': str.__name__,
    })

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        '_input_' + str(i) + '_active': 0,
    })
    BASE_DTYPES.update({
        '_input_' + str(i) + '_active': int.__name__,
    })

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Parker SciPres (" + DEVICE_TYPE + ")"

CATEGORY = "Pressure Transducers"

ICON_XML_PATH = "static/images/devices/{0}/{1}.xml".format(DEVICE_TYPE.lower(), DEVICE_TYPE.upper())

# value returned by the SCIP device
# when one of the transducers is absent
NO_TRANSDUCER_VALUE = "-"

# value returned by the SCIP device
# when one of the inputs is absent
NO_INPUT_VALUE = '?'
