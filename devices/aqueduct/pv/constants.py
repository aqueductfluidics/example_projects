import devices.base.constants

BASE = dict(
    type="PV",
    number_ports=2,
    number_icons=1,
    D_pct_open=0,
    _connection_0_length_mm=1,
    _connection_0_id_mm=6,
    _connection_0_material='silicone',
)

BASE_DTYPES = dict(
    D_position_pct=float.__name__,
    _connection_0_length_mm=float.__name__,
    _connection_0_id_mm=float.__name__,
    _connection_0_material=str.__name__,
)

BASE = {**devices.base.constants.BASE, **BASE}
BASE_DTYPES = {**devices.base.constants.BASE_DTYPES, **BASE_DTYPES}

DEVICE_TYPE = BASE.get('type')

DISPLAY_NAME = "Pinch Valve" + " (" + DEVICE_TYPE + ")"

CATEGORY = "Valves"

ICON_XML_PATH = "static/images/devices/{0}/{1}.xml".format(DEVICE_TYPE.lower(), DEVICE_TYPE.upper())
