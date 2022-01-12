import devices.base.constants

MODE_NOT_SET = -1
MODE_CONTINUOUS = 0
MODE_FINITE = 1

BASE = dict(
    type="MFPP",
    number_ports=2,
    number_icons=1,
    D_ml_done=None,
    D_ml_min=None,
    D_is_running=None,
    D_direction=None,
    acceleration=None,
    _mode=MODE_NOT_SET,
    _tubing_length_mm=None,
    _tubing_id_mm=None,
    _tubing_material=None,
    _max_ml_min=500,
    _masterflex_sn=None,
    _valid_finite_units=['ml'],
    _valid_rate_units=['ml_min'],
)

BASE_DTYPES = dict(
    D_ml_done=int.__name__,
    D_ml_min=float.__name__,
    D_is_running=int.__name__,
    D_direction=int.__name__,
    acceleration=int.__name__,
    _mode=int.__name__,
    _tubing_length_mm=float.__name__,
    _tubing_id_mm=float.__name__,
    _tubing_material=str.__name__,
    _max_ml_min=int.__name__,
    _masterflex_sn=str.__name__,
    _valid_finite_units=list.__name__,
    _valid_rate_units=list.__name__,
)

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "MasterFlex Pump (" + DEVICE_TYPE + ")"

CATEGORY = "Pumps"

DIRECTION_FORWARD = 0
DIRECTION_REVERSE = 1

IS_RUNNING = 1
NOT_RUNNING = 0
