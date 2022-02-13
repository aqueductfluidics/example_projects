"""
Name: button_input.py

Description:

This demo illustrates creating a button `Input` named
`button_input`.

We'll pause the Recipe while waiting for the Input to receive
data by setting `pause_recipe=True` when we create the input.
"""
import aqueduct.aqueduct as aq_module

# a guard to make sure we have an Aqueduct instance "aqueduct" in scope
aqueduct: aq_module.Aqueduct
if not globals().get("aqueduct"):
    aqueduct = aq_module.Aqueduct("G", None, None, None)
else:
    aqueduct = globals().get("aqueduct")

print("Input not yet created...")

options = [1, 2, 3, 4]

# create the input
button_input = aqueduct.input(
    message="Pick a number!",
    input_type=aq_module.UserInputTypes.BUTTONS.value,
    pause_recipe=True,
    options=options,
    dtype=int.__name__,
)

print(f"Input has received data: {button_input.get_value()}")
