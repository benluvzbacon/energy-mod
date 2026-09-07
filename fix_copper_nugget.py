import os, json
from gen_parts.gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def fix_nuggets():
    for metal, data in MATERIALS.items():
        ingot_item = f"{MOD_ID}:{metal}_ingot" if "ingot" in data["forms"] else f"minecraft:{metal}_ingot"
        if "nugget" in data["forms"]:
            # If ingot is not in forms, we are using vanilla ingot
            write_json(f"{DATA_DIR}/recipes/{metal}_nugget.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": ingot_item}],
                "result": {"id": f"{MOD_ID}:{metal}_nugget", "count": 9}
            })
            write_json(f"{DATA_DIR}/recipes/{metal}_ingot_from_nuggets.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["NNN", "NNN", "NNN"],
                "key": {"N": {"item": f"{MOD_ID}:{metal}_nugget"}},
                "result": {"id": ingot_item, "count": 1}
            })

fix_nuggets()
