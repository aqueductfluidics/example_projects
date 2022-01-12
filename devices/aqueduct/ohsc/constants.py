import devices.base.constants

NUMBER_INPUTS: int = 4
BALANCE_PREFIX = 'balance_'

BASE = dict(
    type="OHSC",
    number_icons=4,
    period_ms=None,
    _number_balance_inputs=NUMBER_INPUTS,
)

BASE_DTYPES = dict(
    period_ms=int.__name__,
    _number_balance_inputs=int.__name__,
)

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + BALANCE_PREFIX + str(i) + '_value': 0,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + BALANCE_PREFIX + str(i) + '_units': "g",
    })
    BASE_DTYPES.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + BALANCE_PREFIX + str(i) + '_value': str.__name__,
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + BALANCE_PREFIX + str(i) + '_units': str.__name__,
    })

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Ohaus Scout Balance (" + DEVICE_TYPE + ")"

CATEGORY = "Balances"

# value returned by the OHSC device
# when one of the inputs is absent
NO_INPUT_VALUE = "X"

