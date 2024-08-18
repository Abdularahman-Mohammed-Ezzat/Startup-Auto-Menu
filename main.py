import json
import subprocess
import os

# Configure The Category List
category_selected: str = "Improvement"
configurations: dict = json.load(open(r"menu_configurations.json", "r"))
catagories: dict = configurations['catagories']
catigories_names: tuple = tuple(catagories)

# Configure The SubList
sub_options: dict = catagories[category_selected]
status: dict = sub_options["Status"]
sublist: tuple = tuple(sub_options)[2:]
addons: str = sub_options["Addons"]
addons_names: tuple = tuple(sub_options["Addons"])
options_selected: tuple = []

for option in options_selected:
    if option in options_selected[:-1]:
        os.system(f"{sub_options[option]} &")
    else:
        os.system(f"{sub_options[option]}")
