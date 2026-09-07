import os, json
from gen_parts.gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def fix_recipes():
    # Hammers
    for metal, data in MATERIALS.items():
        ingot_item = f"{MOD_ID}:{metal}_ingot" if "ingot" in data["forms"] else f"minecraft:{metal}_ingot"
        if "hammer" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_hammer.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["III", "III", " S "],
                "key": {"I": {"item": ingot_item}, "S": {"item": "minecraft:stick"}},
                "result": {"id": f"{MOD_ID}:{metal}_hammer"}
            })

    # Gears
    for metal, data in MATERIALS.items():
        ingot_item = f"{MOD_ID}:{metal}_ingot" if "ingot" in data["forms"] else f"minecraft:{metal}_ingot"
        if "gear" in data["forms"] and "rod" in data["forms"] and "plate" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_gear.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": [" R ", "RPR", " R "],
                "key": {"R": {"item": f"{MOD_ID}:{metal}_rod"}, "P": {"item": f"{MOD_ID}:{metal}_plate"}},
                "result": {"id": f"{MOD_ID}:{metal}_gear"}
            })
            
    # Rings
    for metal, data in MATERIALS.items():
        ingot_item = f"{MOD_ID}:{metal}_ingot" if "ingot" in data["forms"] else f"minecraft:{metal}_ingot"
        if "ring" in data["forms"] and "rod" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_ring.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": [" R ", "R R", " R "],
                "key": {"R": {"item": f"{MOD_ID}:{metal}_rod"}},
                "result": {"id": f"{MOD_ID}:{metal}_ring"}
            })
            
    # Plates
    for metal, data in MATERIALS.items():
        ingot_item = f"{MOD_ID}:{metal}_ingot" if "ingot" in data["forms"] else f"minecraft:{metal}_ingot"
        if "plate" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_plate.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": ingot_item}, {"item": f"{MOD_ID}:iron_hammer"}],
                "result": {"id": f"{MOD_ID}:{metal}_plate"}
            })
            
    # Wrench
    write_json(f"{DATA_DIR}/recipes/engineering_wrench.json", {
        "type": "minecraft:crafting_shaped",
        "pattern": ["I I", " G ", " I "],
        "key": {"I": {"item": "minecraft:iron_ingot"}, "G": {"item": f"{MOD_ID}:iron_gear"}},
        "result": {"id": f"{MOD_ID}:engineering_wrench"}
    })
    
fix_recipes()
