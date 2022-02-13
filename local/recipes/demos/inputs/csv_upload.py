"""
Name: csv_upload.py

Description:

This demo illustrates creating a CSV `Input`. The CSV file
contain 2 columns: a Name Column and a Value Column.

Example CSV data:

Name,Value
Input0,10
Input1,3
Input2,1
Input3,40
Input4,"a string"
Input5,34.011
Input6,100

For use with demo CSV 'ExampleUpload.csv'
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
                "Each row should contain a key and value.<br>"
                "For use with demo CSV 'ExampleUpload.csv'<br>"
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


# `as_list` is a list of lists with each entry of format [Name, Value]
# [['Name', 'Value'], ['Input0', '10'], ['Input1', '3'], ['Input2', '1'], ['Input3', '40'], ...]
print(as_list)

new_list = []
row_contents = []
confirmed_data_d: dict = {}

# get the data starting at row index 1 (0 is a header). Store the values in new_list.
for i, r in enumerate(as_list[1::]):
    row_contents.append(dict(
        name=f"{r[0]}", value=r[1]))

    new_list.append(dict(
        hint=f"{r[0]}",
        value=r[1],
        dtype=str.__name__,
        name=f"{r[0]}"
    ))

    confirmed_data_d.update({
        f"{r[0]}": dict(
            dtype=str.__name__,
            value=r[1],
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
        confirmed_data_d[name]['value'] = cv.get('value')

print(confirmed_data_d)
# {'Input0': {'dtype': 'str', 'value': '10'}, 'Input1': {'dtype': 'str', 'value': '3'}, ...}

print("Recipe complete...")

