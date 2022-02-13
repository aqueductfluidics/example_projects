"""
Name: tabular_input.py

Description:

This demo illustrates creating a Tabular `Input`.
"""
import json

import aqueduct.aqueduct as aq_module

# a guard to make sure we have an Aqueduct instance "aqueduct" in scope
aqueduct: aq_module.Aqueduct
if not globals().get("aqueduct"):
    aqueduct = aq_module.Aqueduct("G", None, None, None)
else:
    aqueduct = globals().get("aqueduct")


print("Input not yet created...")

rows = [
    dict(
        hint=f"Enter an integer value for Param1",
        value=10,
        dtype=int.__name__,
        name=f"Param1"
    ),
    dict(
        hint=f"Enter a float for Param2",
        value=24.1,
        dtype=float.__name__,
        name=f"Param2"
    ),
    dict(
        hint=f"Enter a string for Param3",
        value="a string value",
        dtype=str.__name__,
        name=f"Param3"
    ),
]

# prompt the user to confirm the uploaded csv data looks correct
tabular_ipt = aqueduct.input(
    message="Confirm the uploaded data.",
    input_type="table",
    dtype="str",
    rows=rows,
)

# format the confirmed data (str) into a list and return the list new_rates.
values = json.loads(tabular_ipt.get_value())

# [{'value': 10, 'name': 'Param1'}, {'value': 24.1, 'name': 'Param2'}, {'value': 'a string value', 'name': 'Param3'}]
print(values)

print("Recipe complete...")

