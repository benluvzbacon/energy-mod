import os, json
from gen_parts.gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_misc_recipes():
    # Wires (Rod -> Wire)
    for metal, data in MATERIALS.items():
        if "wire" in data["forms"] and "rod" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_wire.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": f"{MOD_ID}:{metal}_rod"}, {"item": f"{MOD_ID}:iron_hammer"}],
                "result": {"id": f"{MOD_ID}:{metal}_wire"}
            })

    # Rubber pulp from slime
    write_json(f"{DATA_DIR}/recipes/raw_rubber_pulp.json", {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [{"item": "minecraft:slime_ball"}, {"item": "minecraft:stick"}],
        "result": {"id": f"{MOD_ID}:raw_rubber_pulp", "count": 2}
    })

gen_misc_recipes()
