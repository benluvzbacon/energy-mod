import os, json
from gen_parts.gen_json import MOD_ID, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_pbf():
    # Firebrick item/block
    write_json(f"{DATA_DIR}/recipes/firebrick.json", {
        "type": "minecraft:crafting_shaped",
        "pattern": ["BB ", "BB ", "   "],
        "key": {"B": {"item": "minecraft:brick"}},
        "result": {"id": f"{MOD_ID}:firebrick", "count": 1}
    })

    write_json(f"{DATA_DIR}/recipes/primitive_blast_furnace.json", {
        "type": "minecraft:crafting_shaped",
        "pattern": ["FFF", "F F", "FFF"],
        "key": {"F": {"item": f"{MOD_ID}:firebrick"}},
        "result": {"id": f"{MOD_ID}:primitive_blast_furnace"}
    })

gen_pbf()
