import os, json
DATA_DIR="src/main/resources/data/ironworks"; MOD_ID="ironworks"

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_missing_recipes():
    # Coal Coke / Coke Oven
    write_json(f"{DATA_DIR}/recipes/coke_oven.json", {
        "type": "minecraft:crafting_shaped",
        "pattern": ["BBB", "B B", "BBB"],
        "key": {"B": {"item": "minecraft:bricks"}},
        "result": {"id": f"{MOD_ID}:coke_oven"}
    })
    # Basic circuit
    write_json(f"{DATA_DIR}/recipes/basic_electrical_circuit.json", {
        "type": "minecraft:crafting_shaped",
        "pattern": ["R R", "CCC", "R R"],
        "key": {"R": {"item": "minecraft:redstone"}, "C": {"item": f"{MOD_ID}:copper_wire"}},
        "result": {"id": f"{MOD_ID}:basic_electrical_circuit"}
    })
    # Rubber
    write_json(f"{DATA_DIR}/recipes/rubber.json", {
        "type": "minecraft:smelting",
        "ingredient": {"item": f"{MOD_ID}:raw_rubber_pulp"},
        "result": {"id": f"{MOD_ID}:rubber"},
        "experience": 0.5,
        "cookingtime": 200
    })
    
gen_missing_recipes()
