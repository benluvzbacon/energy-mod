import os, json
from gen_parts.gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_machine_recipes():
    # Macerator recipes
    os.makedirs(f"{DATA_DIR}/recipes/macerating", exist_ok=True)
    for metal, data in MATERIALS.items():
        if "crushed" in data["forms"]:
            if "ore" in data["forms"]:
                write_json(f"{DATA_DIR}/recipes/macerating/{metal}_ore_to_crushed.json", {
                    "type": f"{MOD_ID}:macerating",
                    "ingredient": {"item": f"{MOD_ID}:{metal}_ore"},
                    "result": {"id": f"{MOD_ID}:{metal}_crushed", "count": 2}
                })
            else:
                vanilla_ore = f"minecraft:{metal}_ore" if metal in ["copper", "iron", "gold", "coal"] else None
                if vanilla_ore:
                    write_json(f"{DATA_DIR}/recipes/macerating/{metal}_ore_to_crushed.json", {
                        "type": f"{MOD_ID}:macerating",
                        "ingredient": {"item": vanilla_ore},
                        "result": {"id": f"{MOD_ID}:{metal}_crushed", "count": 2}
                    })
            if "ingot" in data["forms"]:
                write_json(f"{DATA_DIR}/recipes/macerating/{metal}_ingot_to_dust.json", {
                    "type": f"{MOD_ID}:macerating",
                    "ingredient": {"item": f"{MOD_ID}:{metal}_ingot"},
                    "result": {"id": f"{MOD_ID}:{metal}_dust", "count": 1}
                })
            else:
                vanilla_ingot = f"minecraft:{metal}_ingot" if metal in ["copper", "iron", "gold"] else None
                if vanilla_ingot:
                    write_json(f"{DATA_DIR}/recipes/macerating/{metal}_ingot_to_dust.json", {
                        "type": f"{MOD_ID}:macerating",
                        "ingredient": {"item": vanilla_ingot},
                        "result": {"id": f"{MOD_ID}:{metal}_dust", "count": 1}
                    })
            if "crushed" in data["forms"] and "dust" in data["forms"]:
                write_json(f"{DATA_DIR}/recipes/macerating/{metal}_crushed_to_dust.json", {
                    "type": f"{MOD_ID}:macerating",
                    "ingredient": {"item": f"{MOD_ID}:{metal}_crushed"},
                    "result": {"id": f"{MOD_ID}:{metal}_dust", "count": 1}
                })

    # Compressor recipes
    os.makedirs(f"{DATA_DIR}/recipes/compressing", exist_ok=True)
    for metal, data in MATERIALS.items():
        if "plate" in data["forms"]:
            if "ingot" in data["forms"]:
                write_json(f"{DATA_DIR}/recipes/compressing/{metal}_plate.json", {
                    "type": f"{MOD_ID}:compressing",
                    "ingredient": {"item": f"{MOD_ID}:{metal}_ingot"},
                    "result": {"id": f"{MOD_ID}:{metal}_plate", "count": 1}
                })
            else:
                vanilla_ingot = f"minecraft:{metal}_ingot" if metal in ["copper", "iron", "gold"] else None
                if vanilla_ingot:
                    write_json(f"{DATA_DIR}/recipes/compressing/{metal}_plate.json", {
                        "type": f"{MOD_ID}:compressing",
                        "ingredient": {"item": vanilla_ingot},
                        "result": {"id": f"{MOD_ID}:{metal}_plate", "count": 1}
                    })

gen_machine_recipes()
