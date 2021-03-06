"""
Usage - Copy this template when creating a new Recipe
protocol.

In DEV MODE, the template creates an
Aqueduct Object (with Prompt, Input, etc.. helpers),
Device Objects.

IN LAB MODE or SIM MODE (run through the Aqueduct Recipe
Runner), the Aqueduct and Device Objects are inherited
from the Python interpreters Globals() dict

The Data, Setpoints, Watchdog, and Process Objects are constructed
using the appropriate Aqueduct and Devices objects.
"""

import config
# local imports
import local.lib.ph_control.classes

if not config.LAB_MODE_ENABLED:

    from aqueduct.aqueduct import Aqueduct

    aqueduct = Aqueduct('G', None, None, None)

    # make the Devices object
    devices = local.lib.ph_control.classes.Devices.generate_dev_devices()

else:

    # pass the aqueduct object
    aqueduct = globals().get('aqueduct')

    # pass the globals dictionary, which will have the
    # objects for the Devices already instantiated
    devices = local.lib.ph_control.classes.Devices(**globals())

# make the Data object, pass the new devices object
# and the aqueduct object
data = local.lib.ph_control.classes.Data(devices, aqueduct)

# make the Process object
process = local.lib.ph_control.classes.ProcessHandler(
    devices_obj=devices,
    aqueduct=aqueduct,
    data=data,
)

"""
Add code here
"""
