"""
Name: user_prompt_no_pause.py

Description:

This demo illustrates creating a `Prompt` named `prompt`.

In this demo, we won't pause the recipe while waiting for 
the Prompt to be acknowledged - we'll just print out the number
of times we've waited...
"""
import time
import aqueduct.aqueduct as aq_module

# a guard to make sure we have an Aqueduct instance "aqueduct" in scope
aqueduct: aq_module.Aqueduct
if not globals().get("aqueduct"):
    aqueduct = aq_module.Aqueduct("G", None, None, None)
else:
    aqueduct = globals().get("aqueduct")


print("Prompt not yet created...")

# create the input
prompt = aqueduct.prompt(
    message="Press me to continue!",
    pause_recipe=False,
)

i = 0

while prompt:
    print(f"Waiting on the prompt for the {i}th time...")
    time.sleep(1)
    i += 1

print(f"Prompt complete!")

