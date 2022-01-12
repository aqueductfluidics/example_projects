from enum import Enum

import devices.base.constants


class Status(Enum):
    INACTIVE = 0
    ACTIVE = 1


NUMBER_INPUTS: int = 1
NODE_PREFIX = "probe_"

STATUS_KEY = devices.base.constants.DEVICE_GLOBAL_PARAM_PREFIX + 'status'
PERIOD_MS_KEY = "period_ms"
PH_VALUE_SUFFIX = "_value"

BASE = dict(
    type="PH",
    number_icons=1,
)

BASE_DTYPES = dict(
)

BASE.update({
    STATUS_KEY: Status.INACTIVE.value,
    PERIOD_MS_KEY: 0,
})

BASE_DTYPES.update({
    STATUS_KEY: int.__name__,
    PERIOD_MS_KEY: int.__name__,
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

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "pH Probe (" + DEVICE_TYPE + ")"

CATEGORY = "pH Probes"
