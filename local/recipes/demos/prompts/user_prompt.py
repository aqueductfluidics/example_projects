"""
Name: user_prompt.py

Description:

This demo illustrates creating a `Prompt` named `prompt`.

We'll pause the Recipe while waiting for the Prompt to be
acknowledged by setting `pause_recipe=True` when we create the prompt.
"""
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
    pause_recipe=True,
)

print(f"Prompt complete!")


