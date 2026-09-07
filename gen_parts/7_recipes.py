import os, json
from gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_recipes():
    os.makedirs(f"{DATA_DIR}/recipes", exist_ok=True)
    
    # Smelting Ores/Dusts to Ingots
    for metal, data in MATERIALS.items():
        if "ingot" in data["forms"]:
            # From raw/ore
            for src in ["raw", "ore", "dust", "crushed"]:
                if src in data["forms"]:
                    write_json(f"{DATA_DIR}/recipes/{metal}_{src}_smelting.json", {
                        "type": "minecraft:smelting",
                        "ingredient": {"item": f"{MOD_ID}:{metal}_{src}"},
                        "result": {"id": f"{MOD_ID}:{metal}_ingot"},
                        "experience": 0.7,
                        "cookingtime": 200
                    })
                    write_json(f"{DATA_DIR}/recipes/{metal}_{src}_blasting.json", {
                        "type": "minecraft:blasting",
                        "ingredient": {"item": f"{MOD_ID}:{metal}_{src}"},
                        "result": {"id": f"{MOD_ID}:{metal}_ingot"},
                        "experience": 0.7,
                        "cookingtime": 100
                    })
        elif metal == "copper" or metal == "iron" or metal == "gold":
            # For vanilla metals, smelt dusts/crushed to vanilla ingots
            vanilla_ingot = f"minecraft:{metal}_ingot"
            for src in ["raw", "ore", "dust", "crushed"]:
                if src in data["forms"]:
                    write_json(f"{DATA_DIR}/recipes/{metal}_{src}_smelting.json", {
                        "type": "minecraft:smelting",
                        "ingredient": {"item": f"{MOD_ID}:{metal}_{src}"},
                        "result": {"id": vanilla_ingot},
                        "experience": 0.7,
                        "cookingtime": 200
                    })
                    write_json(f"{DATA_DIR}/recipes/{metal}_{src}_blasting.json", {
                        "type": "minecraft:blasting",
                        "ingredient": {"item": f"{MOD_ID}:{metal}_{src}"},
                        "result": {"id": vanilla_ingot},
                        "experience": 0.7,
                        "cookingtime": 100
                    })
                    
    # Block <-> Ingot
    for metal, data in MATERIALS.items():
        if "block" in data["forms"] and "ingot" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_block.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["III", "III", "III"],
                "key": {"I": {"item": f"{MOD_ID}:{metal}_ingot"}},
                "result": {"id": f"{MOD_ID}:{metal}_block"}
            })
            write_json(f"{DATA_DIR}/recipes/{metal}_ingot_from_block.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": f"{MOD_ID}:{metal}_block"}],
                "result": {"id": f"{MOD_ID}:{metal}_ingot", "count": 9}
            })
            
    # Nugget <-> Ingot
    for metal, data in MATERIALS.items():
        if "nugget" in data["forms"] and "ingot" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_ingot_from_nuggets.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["NNN", "NNN", "NNN"],
                "key": {"N": {"item": f"{MOD_ID}:{metal}_nugget"}},
                "result": {"id": f"{MOD_ID}:{metal}_ingot"}
            })
            write_json(f"{DATA_DIR}/recipes/{metal}_nugget.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": f"{MOD_ID}:{metal}_ingot"}],
                "result": {"id": f"{MOD_ID}:{metal}_nugget", "count": 9}
            })
            
    # Rods
    for metal, data in MATERIALS.items():
        ingot_item = f"{MOD_ID}:{metal}_ingot" if "ingot" in data["forms"] else f"minecraft:{metal}_ingot"
        if "rod" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_rod.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["I", "I"],
                "key": {"I": {"item": ingot_item}},
                "result": {"id": f"{MOD_ID}:{metal}_rod", "count": 2}
            })

    # Gears
    for metal, data in MATERIALS.items():
        if "gear" in data["forms"] and "rod" in data["forms"] and "plate" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_gear.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": [" R ", "RPR", " R "],
                "key": {"R": {"item": f"{MOD_ID}:{metal}_rod"}, "P": {"item": f"{MOD_ID}:{metal}_plate"}},
                "result": {"id": f"{MOD_ID}:{metal}_gear"}
            })
            
    # Rings
    for metal, data in MATERIALS.items():
        if "ring" in data["forms"] and "rod" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_ring.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": [" R ", "R R", " R "],
                "key": {"R": {"item": f"{MOD_ID}:{metal}_rod"}},
                "result": {"id": f"{MOD_ID}:{metal}_ring"}
            })

    # Hammers
    for metal, data in MATERIALS.items():
        if "hammer" in data["forms"] and "ingot" in data["forms"]:
            write_json(f"{DATA_DIR}/recipes/{metal}_hammer.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["III", "III", " S "],
                "key": {"I": {"item": f"{MOD_ID}:{metal}_ingot"}, "S": {"item": "minecraft:stick"}},
                "result": {"id": f"{MOD_ID}:{metal}_hammer"}
            })
            
    # Manual Plates (Ingot + Hammer)
    for metal, data in MATERIALS.items():
        ingot_item = f"{MOD_ID}:{metal}_ingot" if "ingot" in data["forms"] else f"minecraft:{metal}_ingot"
        if "plate" in data["forms"]:
            # Create a recipe for any hammer
            # Using tags would be better, but for simplicity we list shapeless
            write_json(f"{DATA_DIR}/recipes/{metal}_plate.json", {
                "type": "minecraft:crafting_shapeless",
                "ingredients": [{"item": ingot_item}, {"item": f"{MOD_ID}:iron_hammer"}],
                "result": {"id": f"{MOD_ID}:{metal}_plate"}
            })
            
    # Wrench
    write_json(f"{DATA_DIR}/recipes/engineering_wrench.json", {
        "type": "minecraft:crafting_shaped",
        "pattern": ["I I", " G ", " I "],
        "key": {"I": {"item": f"{MOD_ID}:iron_ingot"}, "G": {"item": f"{MOD_ID}:iron_gear"}},
        "result": {"id": f"{MOD_ID}:engineering_wrench"}
    })
    
    # Bronze Blend
    write_json(f"{DATA_DIR}/recipes/bronze_dust_mix.json", {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [{"item": f"{MOD_ID}:copper_dust"}, {"item": f"{MOD_ID}:copper_dust"}, {"item": f"{MOD_ID}:copper_dust"}, {"item": f"{MOD_ID}:tin_dust"}],
        "result": {"id": f"{MOD_ID}:bronze_dust", "count": 4}
    })

    # Machine Crafting (Basic placeholders so they are craftable)
    for tier in MACHINE_TIERS:
        metal = "bronze" if tier == "bronze" else "steel"
        for mtype in MACHINE_TYPES:
            write_json(f"{DATA_DIR}/recipes/{tier}_{mtype}.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["PPP", "PMP", "PPP"],
                "key": {"P": {"item": f"{MOD_ID}:{metal}_plate"}, "M": {"item": "minecraft:furnace" if "furnace" in mtype else ("minecraft:piston" if "compressor" in mtype else "minecraft:iron_block")}},
                "result": {"id": f"{MOD_ID}:{tier}_{mtype}"}
            })

gen_recipes()
