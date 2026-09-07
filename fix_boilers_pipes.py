import os, json
from gen_parts.gen_json import MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_extra_recipes():
    # Pipes
    for p in ["small_bronze", "bronze", "reinforced_bronze", "steel"]:
        metal = "steel" if p == "steel" else "bronze"
        write_json(f"{DATA_DIR}/recipes/{p}_pipe.json", {
            "type": "minecraft:crafting_shaped",
            "pattern": ["PPP", "   ", "PPP"],
            "key": {"P": {"item": f"{MOD_ID}:{metal}_plate"}},
            "result": {"id": f"{MOD_ID}:{p}_pipe", "count": 6}
        })
        
    # Boilers
    for b in ["solid", "liquid", "solar"]:
        for t in ["bronze", "steel"]:
            write_json(f"{DATA_DIR}/recipes/{t}_{b}_boiler.json", {
                "type": "minecraft:crafting_shaped",
                "pattern": ["PPP", "PWP", "PFP"],
                "key": {
                    "P": {"item": f"{MOD_ID}:{t}_plate"},
                    "W": {"item": "minecraft:water_bucket"},
                    "F": {"item": "minecraft:furnace"}
                },
                "result": {"id": f"{MOD_ID}:{t}_{b}_boiler"}
            })
            
    # Treated wood
    write_json(f"{DATA_DIR}/recipes/treated_wood.json", {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [{"item": "minecraft:oak_planks"}, {"item": "minecraft:coal"}],
        "result": {"id": f"{MOD_ID}:treated_wood", "count": 1}
    })

gen_extra_recipes()
