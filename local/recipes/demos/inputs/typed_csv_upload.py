"""
Name: typed_csv_upload.py

Description:

This demo illustrates creating a CSV `Input`. The CSV file
contain 3 columns: a Name Column, a Type Column, and a Value Column.

Example CSV data:

Name,Type,Value
Input0,"int",10
Input1,"int",3
Input2,"float",1
Input3,"int",40
Input4,"str","a string"
Input5,"float",34.011
Input6,"int",100

For use with demo CSV 'ExampleUploadTyped.csv'

After uploading the CSV, we'll create a `Tabular Input` with the values
from the CSV asking the user to confirm. Adjustments to the parameters
may be made at this point.

After submitting the Tabular Input, we'll typecast the values for use in
Recipe logic.
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


def start_csv_upload():
    # prompt the user to upload a CSV with the correct formatting
    # Row 0 is the header row with data labels. Within a row the data (columns) are separated by commas.
    return aqueduct.input(
        message="Upload a CSV file.<br>"
                "Each row should contain a key, data type, and value.<br>"
                "For use with demo CSV 'ExampleUploadTyped.csv'<br>"
                "<br>",
        input_type="csv",
        dtype="str"
    )


valid_csv = False
as_list = []

while not valid_csv:
    try:
        csv_ipt = start_csv_upload()
        table_data = csv_ipt.get_value()
        as_list = json.loads(table_data)
        valid_csv = True
    except BaseException as e: # noqa
        print("[ERROR]: Invalid CSV upload.")


# `as_list` is a list of lists with each entry of format [Name, Type, Value]
# [['Name', 'Type', 'Value'], ['Input0', 'int', '10'], ['Input1', 'int', '3'], ...]
print(as_list)

new_list = []
row_contents = []
confirmed_data_d: dict = {}

# get the data starting at row index 1 (0 is a header). Store the values in new_list
# update the confirmed_data_d dict in each loop so we know what param names we're looking for
for i, r in enumerate(as_list[1::]):
    row_contents.append(dict(
        name=f"{r[0]}", value=r[1]))

    new_list.append(dict(
        hint=f"{r[0]}",
        value=r[2],
        dtype=r[1],
        name=f"{r[0]}"
    ))

    confirmed_data_d.update({
        f"{r[0]}": dict(
            dtype=r[1],
            value=r[2],
        )
    })

# prompt the user to confirm the uploaded csv data looks correct
tabular_ipt = aqueduct.input(
    message="Confirm the uploaded data.",
    input_type="table",
    dtype="str",
    rows=new_list,
)

# format the confirmed data (str) into a list and return the list new_rates.
confirmed_values = json.loads(tabular_ipt.get_value())

# [{'value': '10', 'name': 'Input0'}, {'value': '3', 'name': 'Input1'}, {'value': '1', 'name': 'Input2'}, ...]
print(confirmed_values)

new_params = []

for cv in confirmed_values:
    name = cv.get('name')
    if name in confirmed_data_d:
        if confirmed_data_d[name]['dtype'] == float.__name__:
            confirmed_data_d[name]['value'] = float(cv.get('value'))
        elif confirmed_data_d[name]['dtype'] == int.__name__:
            confirmed_data_d[name]['value'] = int(cv.get('value'))
        elif confirmed_data_d[name]['dtype'] == str.__name__:
            confirmed_data_d[name]['value'] = str(cv.get('value'))
        else:
            confirmed_data_d[name]['value'] = cv.get('value')

print(confirmed_data_d)
# {'Input0': {'dtype': 'int', 'value': 100}, 'Input1': {'dtype': 'int', 'value': 3}, ...}

print("Recipe complete...")

