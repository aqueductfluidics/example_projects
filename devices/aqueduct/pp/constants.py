import devices.base.constants

BASE = dict(
    type="PP",
    number_ports=2,
    number_icons=1,
    D_steps_done=None,
    D_rpm=None,
    D_is_running=None,
    D_direction=None,
    acceleration=None,
    _mode=None,
    _steps_per_rev=200,
    _rev_per_ml=24,
    _motor_driver=None,
    _tubing_length_mm=None,
    _tubing_id_mm=None,
    _tubing_material=None,
    _max_rpm=500,
    _max_usteps=4294967295,
    _max_accel=50000,
)

BASE_DTYPES = dict(
    D_steps_done=int.__name__,
    D_rpm=float.__name__,
    D_is_running=int.__name__,
    D_direction=int.__name__,
    acceleration=int.__name__,
    _mode=int.__name__,
    _steps_per_rev=int.__name__,
    _rev_per_ml=float.__name__,
    _motor_driver=str.__name__,
    _tubing_length_mm=float.__name__,
    _tubing_id_mm=float.__name__,
    _tubing_material=str.__name__,
    _max_rpm=int.__name__,
    _max_usteps=int.__name__,
    _max_accel=int.__name__,
)

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Peristaltic Pump (" + DEVICE_TYPE + ")"

CATEGORY = "Pumps"

MODE_NOT_SET = -1
MODE_CONTINUOUS = 0
MODE_FINITE = 1

DIRECTION_FORWARD = 0
DIRECTION_REVERSE = 1

IS_RUNNING = 1
NOT_RUNNING = 0

VALID_FINITE_UNITS = ('steps', 's', 'min', 'degrees', 'ml')
VALID_RATE_UNITS = ('rpm', 'ml_min')

STEPS_PER_REV = 200
MAX_MICROSTEPS = 2147483648
MICROSTEPS_PER_STEP = 256
