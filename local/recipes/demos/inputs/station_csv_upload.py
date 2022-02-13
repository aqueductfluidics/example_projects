"""
Name: station_csv_upload.py

Description:

This demo illustrates creating a CSV `Input`. The CSV file
is structured for applications where a Recipe is controlling multiple
stations that require independent input parameters.

Example CSV data:

Station,Param1,Param2,Param3,Param4
0,454,222,"test",232
1,120,232,"test1",232
2,234,221,"test2",232
3,123,262,"test3",232

For use with demo CSV 'StationUpload.csv'

After uploading the CSV, we'll create a `Tabular Input` with the values
from the CSV asking the user to confirm. Adjustments to the parameters
may be made at this point.
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
        message="Upload a CSV file. Within a row use commas to separate column entries from left to right. <br>"
                "Each new line will be a new row.  <br>"
                "Ensure row 0 is a header row (labels).  <br>",
        input_type="csv",
        dtype="str"
    )


valid_csv = False
as_list = []
labels = []

while not valid_csv:
    try:
        csv_ipt = start_csv_upload()
        table_data = csv_ipt.get_value()
        as_list = json.loads(table_data)
        valid_csv = True
    except BaseException as e: # noqa
        print("[ERROR]: Invalid CSV upload.")


# `as_list` is a list of lists with each entry of format [Name, Type, Value]
# [['Station', 'Param1', 'Param2', 'Param3', 'Param4'], ['0', '454', '222', 'test', '232'], ...]
print(as_list)

# get the data labels and store in a list
for column in as_list[0]:
    labels.append(column)

new_list = []
row_contents = []

# get the data starting at row index 1 (0 is a header). Store the values in new_list
# update the confirmed_data_d dict in each loop so we know what param names we're looking for
# get the data starting at row index 1 (not row to omit the header row). Store the values in new_list.
for i, r in enumerate(as_list[1::]):
    row_index = i
    row_contents = []
    for j, column in enumerate(r):
        row_contents.append(dict(
            name=f"{labels[j]}", value=column))

    new_list.append(dict(
        hint=f"csv row: {row_index}",
        value=row_contents,
        dtype="list",
        name=f"data{i}"
    ))

# prompt the user to confirm the uploaded csv data looks correct
tabular_ipt = aqueduct.input(
    message="Confirm the uploaded data.",
    input_type="table",
    dtype="str",
    rows=new_list,
)

# format the confirmed data (str) into a list and return the list new_rates.
confirmed_values = json.loads(tabular_ipt.get_value())
new_params = []

# [{'value': '10', 'name': 'Input0'}, {'value': '3', 'name': 'Input1'}, {'value': '1', 'name': 'Input2'}, ...]
print(confirmed_values)

for cv in confirmed_values:
    row = {}
    for value in cv:
        try:
            row.update({
                value.get('name'): float(value.get('value'))
            })
        except ValueError:
            row.update({
                value.get('name'): value.get('value')
            })
    new_params.append(row)

print(new_params)
# [{'Station': 0.0, 'Param1': 454.0, 'Param2': 222.0, 'Param3': 'test', 'Param4': 232.0}, ...]

print("Recipe complete...")

