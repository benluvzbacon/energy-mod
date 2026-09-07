import os, json
from gen_parts.gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_hardware_recipes():
    for metal, data in MATERIALS.items():
        if "bolt" in data["forms"] and "rod" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_bolt.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": f"{MOD_ID}:{metal}_rod"}],
                "result": {"id": f"{MOD_ID}:{metal}_bolt", "count": 2}
            })
        if "screw" in data["forms"]:
            bolt_item = f"{MOD_ID}:{metal}_bolt" if "bolt" in data["forms"] else f"{MOD_ID}:{metal}_rod"
            write_json(f"{DATA_DIR}/recipes/{metal}_screw.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": bolt_item}],
                "result": {"id": f"{MOD_ID}:{metal}_screw", "count": 2}
            })

gen_hardware_recipes()
