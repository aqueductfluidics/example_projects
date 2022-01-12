import devices.base.constants

BASE = dict(
    type="SV",
    number_ports=9,
    number_icons=1,
    D_current_angle=None,
    firmware_verbose=None,
    _min_angle_deg=0.0,
    _max_angle_deg=359.99,
    _connection_material='PTFE',
    _connection_length_mm=10.,
    _connection_id_mm=0.5,
)

BASE_DTYPES = dict(
    D_current_angle=float.__name__,
    firmware_verbose=bool.__name__,
    _min_angle_deg=float.__name__,
    _max_angle_deg=float.__name__,
    _connection_material=str.__name__,
    _connection_length_mm=float.__name__,
    _connection_id_mm=float.__name__,
)

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Rotary Selector Valve (" + DEVICE_TYPE + ")"

CATEGORY = "Valves"

