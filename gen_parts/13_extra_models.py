import os, json
ASSETS_DIR="src/main/resources/assets/ironworks"; MOD_ID="ironworks"

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_extra_models():
    extras = ["coke_oven", "primitive_blast_furnace", "treated_wood", "bronze_boiler", "steel_boiler", "large_bronze_boiler", "large_steel_boiler"]
    for e in extras:
        write_json(f"{ASSETS_DIR}/blockstates/{e}.json", {
            "variants": {
                "facing=north,lit=false": {"model": f"{MOD_ID}:block/{e}"},
                "facing=east,lit=false": {"model": f"{MOD_ID}:block/{e}", "y": 90},
                "facing=south,lit=false": {"model": f"{MOD_ID}:block/{e}", "y": 180},
                "facing=west,lit=false": {"model": f"{MOD_ID}:block/{e}", "y": 270},
                "facing=north,lit=true": {"model": f"{MOD_ID}:block/{e}"},
                "facing=east,lit=true": {"model": f"{MOD_ID}:block/{e}", "y": 90},
                "facing=south,lit=true": {"model": f"{MOD_ID}:block/{e}", "y": 180},
                "facing=west,lit=true": {"model": f"{MOD_ID}:block/{e}", "y": 270}
            }
        })
        write_json(f"{ASSETS_DIR}/models/block/{e}.json", {
            "parent": "minecraft:block/cube_all",
            "textures": {"all": f"minecraft:block/iron_block"} # Placeholder texture
        })
        write_json(f"{ASSETS_DIR}/models/item/{e}.json", {
            "parent": f"{MOD_ID}:block/{e}"
        })

gen_extra_models()
