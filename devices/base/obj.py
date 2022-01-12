class Device(object):
    """
    Devices are instantiated in Recipes and contain the attributes necessary
    to control execution between the device worker and the main recipe thread.
    """
    def __init__(self, **kwargs):
        self.__device_key__ = kwargs.get('device_key')
        self.__type__ = kwargs.get('type')
        self.__enqueue__ = kwargs.get('enqueue')
        self.__recipe_pid__ = kwargs.get('pid')


def initialize_object(obj: object, **kwargs):
    return


def add_object_info_to_content(inst: dict, locs: dict, action_name: str):
    content = {k: v for k, v in locs.items() if k != 'self'}
    return content


def enqueue_and_pause(inst: dict, content: dict) -> None:
    return

