"""
Name: setpoint_with_callback.py

Description:

This demo illustrates creating a `Setpoint` named
`counter` that increments itself forever in an 
infinite while loop. 

The counter value can be modified from the Aqueduct
user interface.

This is a simple example, but it illustrates the general
process of creating an externally modifiable value 
that can be used in your Recipe logic while still being
available externally.
"""

import time
import aqueduct.aqueduct

# a guard to make sure we have an Aqueduct instance "aqueduct" in scope
aqueduct: aqueduct.aqueduct.Aqueduct
if not globals().get("aqueduct"):
    aqueduct = aqueduct.aqueduct.Aqueduct("G", None, None, None)
else:
    aqueduct = globals().get("aqueduct")


my_counter = aqueduct.setpoint(
    name="my_counter",
    value=0,
    dtype=int.__name__,
)

print_on_demand = aqueduct.setpoint(
    name="print_me",
    value="",
    dtype=str.__name__,
)

def print_the_counter(sp):
    print(f"Hey, {sp.value}, the current counter value is {my_counter.value}...")

print_on_demand.on_change = print_the_counter
print_on_demand.kwargs = dict(sp=print_on_demand)

while True:
    v = my_counter.get()
    print(f"Setpoint value: {v}")
    my_counter.update(v+1)
    time.sleep(1)