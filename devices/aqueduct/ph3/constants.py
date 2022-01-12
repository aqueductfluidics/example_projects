import devices.base.constants
from devices.aqueduct.ph.constants import *

NUMBER_INPUTS: int = 3

BASE = dict(
    type="PH3",
    number_icons=3,
    period_ms=None,
)

BASE_DTYPES = dict(
    period_ms=int.__name__,
)

BASE.update({
    STATUS_KEY: Status.INACTIVE.value,
})

BASE_DTYPES.update({
    STATUS_KEY: int.__name__,
})

for i in range(0, NUMBER_INPUTS):
    BASE.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + PH_VALUE_SUFFIX: 0,
    })
    BASE_DTYPES.update({
        devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + NODE_PREFIX + str(i) + PH_VALUE_SUFFIX: str.__name__,
    })

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get("type", "")

DISPLAY_NAME = "3 x pH Probe (" + DEVICE_TYPE + ")"

CATEGORY = "pH Probes"

# value returned by the PH3 device
# when one of the inputs is absent
NO_INPUT_VALUE = "X"
