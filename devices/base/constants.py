from enum import Enum, unique

DEVICE_GLOBAL_PARAM_PREFIX = 'D_'


@unique
class DeviceBase(Enum):
    device_key = "device_key"
    id = "id"
    sn = "sn"
    name = "name"
    type = "type"
    link = "link"
    firmware_version = "firmware_version"
    verbose = "verbose"
    number_ports = "number_ports"
    number_decks = "number_deck"
    number_icons = "number_icons"


RS485_LINK = 0
ESB_LINK = 1

BASE = {
    DeviceBase.device_key.value: None,
    DeviceBase.id.value: None,
    DeviceBase.sn.value: None,
    DeviceBase.name.value: None,
    DeviceBase.type.value: None,
    DeviceBase.link.value: None,
    DeviceBase.firmware_version.value: None,
    DeviceBase.verbose.value: True,
    DeviceBase.number_ports.value: None,
    DeviceBase.number_decks.value: 0,
    DeviceBase.number_icons.value: 1,
}

BASE_DTYPES = {
    DeviceBase.device_key.value: str.__name__,
    DeviceBase.id.value: int.__name__,
    DeviceBase.sn.value: str.__name__,
    DeviceBase.name.value: str.__name__,
    DeviceBase.type.value: str.__name__,
    DeviceBase.link.value: int.__name__,
    DeviceBase.firmware_version.value: str.__name__,
    DeviceBase.verbose.value: bool.__name__,
    DeviceBase.number_ports.value: int.__name__,
    DeviceBase.number_decks.value: int.__name__,
    DeviceBase.number_icons.value: int.__name__,
}
