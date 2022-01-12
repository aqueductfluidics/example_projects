import devices.base.constants
from devices.aqueduct.pp12.constants import *

NUMBER_PUMPS: int = 6

BASE = dict(
    type="PP6",
    number_ports=2*NUMBER_PUMPS,
    number_icons=NUMBER_PUMPS,
    _number_pump_inputs=NUMBER_PUMPS,
)

BASE_DTYPES = dict(
    _number_pump_inputs=int.__name__,
)

update_base_common(BASE, BASE_DTYPES)
update_base(BASE, BASE_DTYPES, NUMBER_PUMPS)

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')
DISPLAY_NAME = "6 x Peristaltic Pump (" + DEVICE_TYPE + ")"

AUTO_STOP_EXPR_STR = ""
for i in range(0, NUMBER_PUMPS):
    prepend = "" if i == 0 else " and "
    AUTO_STOP_EXPR_STR += "{}((int(S)>>(2*{}))&3) == {}".format(prepend, i, STATUS_STOPPED)

AUTO_STOP_EXPR_CONSTANT = "S"

del i