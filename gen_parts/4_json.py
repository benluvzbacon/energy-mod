import os, json
from gen_assets import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, ASSETS_DIR, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_models_and_blockstates():
    lang = {}
    
    # Items & Blocks
    for metal, data in MATERIALS.items():
        for form in data["forms"]:
            name = f"deepslate_{metal}_ore" if form == "deepslate_ore" else f"{metal}_{form}"
            if form in ["ore", "deepslate_ore", "block"]:
                # Blockstate
                write_json(f"{ASSETS_DIR}/blockstates/{name}.json", {
                    "variants": {"": {"model": f"{MOD_ID}:block/{name}"}}
                })
                # Block Model
                write_json(f"{ASSETS_DIR}/models/block/{name}.json", {
                    "parent": "minecraft:block/cube_all",
                    "textures": {"all": f"{MOD_ID}:block/{name}"}
                })
                # Item Model
                write_json(f"{ASSETS_DIR}/models/item/{name}.json", {
                    "parent": f"{MOD_ID}:block/{name}"
                })
                if "ore" in name:
                    lang[f"block.{MOD_ID}.{name}"] = name.replace("_", " ").title()
                else:
                    lang[f"block.{MOD_ID}.{name}"] = name.replace("_", " ").title()
            else:
                # Item Model
                write_json(f"{ASSETS_DIR}/models/item/{name}.json", {
                    "parent": "minecraft:item/generated",
                    "textures": {"layer0": f"{MOD_ID}:item/{name}"}
                })
                lang[f"item.{MOD_ID}.{name}"] = name.replace("_", " ").title()
                
    # Machines
    for tier in MACHINE_TIERS:
        for mtype in MACHINE_TYPES:
            name = f"{tier}_{mtype}"
            lang[f"block.{MOD_ID}.{name}"] = f"{tier.title()} {mtype.replace('_', ' ').title()}"
            
            # Blockstate
            write_json(f"{ASSETS_DIR}/blockstates/{name}.json", {
                "variants": {
                    "facing=north,lit=false": {"model": f"{MOD_ID}:block/{name}"},
                    "facing=east,lit=false": {"model": f"{MOD_ID}:block/{name}", "y": 90},
                    "facing=south,lit=false": {"model": f"{MOD_ID}:block/{name}", "y": 180},
                    "facing=west,lit=false": {"model": f"{MOD_ID}:block/{name}", "y": 270},
                    "facing=north,lit=true": {"model": f"{MOD_ID}:block/{name}_on"},
                    "facing=east,lit=true": {"model": f"{MOD_ID}:block/{name}_on", "y": 90},
                    "facing=south,lit=true": {"model": f"{MOD_ID}:block/{name}_on", "y": 180},
                    "facing=west,lit=true": {"model": f"{MOD_ID}:block/{name}_on", "y": 270}
                }
            })
            
            # Models
            for state, tex in [("", "front"), ("_on", "front_on")]:
                write_json(f"{ASSETS_DIR}/models/block/{name}{state}.json", {
                    "parent": "minecraft:block/orientable",
                    "textures": {
                        "top": f"{MOD_ID}:block/{tier}_machine_top",
                        "front": f"{MOD_ID}:block/{name}_{tex}",
                        "side": f"{MOD_ID}:block/{tier}_machine_side"
                    }
                })
                
            write_json(f"{ASSETS_DIR}/models/item/{name}.json", {
                "parent": f"{MOD_ID}:block/{name}"
            })

    # Misc Items
    misc_items = ["engineering_wrench", "basic_electrical_circuit", "rubber", "raw_rubber_pulp"]
    for i in misc_items:
        write_json(f"{ASSETS_DIR}/models/item/{i}.json", {
            "parent": "minecraft:item/generated",
            "textures": {"layer0": f"{MOD_ID}:item/{i}"}
        })
        lang[f"item.{MOD_ID}.{i}"] = i.replace("_", " ").title()
        
    write_json(f"{ASSETS_DIR}/lang/en_us.json", lang)

gen_models_and_blockstates()
