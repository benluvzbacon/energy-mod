import os
import json
from gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, DATA_DIR

def gen_loot_tables_and_tags():
    os.makedirs(f"{DATA_DIR}/loot_table/blocks", exist_ok=True)
    os.makedirs(f"{DATA_DIR}/tags/block", exist_ok=True)
    os.makedirs(f"{DATA_DIR}/tags/item", exist_ok=True)
    
    mineable_pickaxe = []
    needs_stone = []
    needs_iron = []
    
    # Blocks
    for metal, data in MATERIALS.items():
        for form in data["forms"]:
            if form in ["ore", "deepslate_ore", "block"]:
                name = f"deepslate_{metal}_ore" if form == "deepslate_ore" else f"{metal}_{form}"
                mineable_pickaxe.append(f"{MOD_ID}:{name}")
                if metal in ["lead", "silver", "gold"]:
                    needs_iron.append(f"{MOD_ID}:{name}")
                else:
                    needs_stone.append(f"{MOD_ID}:{name}")
                    
                # Loot table
                if form == "block":
                    loot = {
                      "type": "minecraft:block",
                      "pools": [
                        {
                          "rolls": 1,
                          "entries": [ { "type": "minecraft:item", "name": f"{MOD_ID}:{name}" } ],
                          "conditions": [ { "condition": "minecraft:survives_explosion" } ]
                        }
                      ]
                    }
                else:
                    drop = f"{MOD_ID}:{metal}_raw" if "raw" in data["forms"] else (f"minecraft:raw_{metal}" if metal in ["copper", "iron", "gold"] else f"{MOD_ID}:{metal}_dust")
                    loot = {
                      "type": "minecraft:block",
                      "pools": [
                        {
                          "rolls": 1,
                          "entries": [
                            {
                              "type": "minecraft:item",
                              "name": drop
                            }
                          ],
                          "conditions": [
                            {
                              "condition": "minecraft:survives_explosion"
                            }
                          ]
                        }
                      ]
                    }
                with open(f"{DATA_DIR}/loot_table/blocks/{name}.json", "w") as f:
                    json.dump(loot, f, indent=2)

    # Machines
    for tier in MACHINE_TIERS:
        for mtype in MACHINE_TYPES:
            name = f"{tier}_{mtype}"
            mineable_pickaxe.append(f"{MOD_ID}:{name}")
            needs_stone.append(f"{MOD_ID}:{name}")
            loot = {
              "type": "minecraft:block",
              "pools": [
                {
                  "rolls": 1,
                  "entries": [ { "type": "minecraft:item", "name": f"{MOD_ID}:{name}" } ],
                  "conditions": [ { "condition": "minecraft:survives_explosion" } ]
                }
              ]
            }
            with open(f"{DATA_DIR}/loot_table/blocks/{name}.json", "w") as f:
                json.dump(loot, f, indent=2)
                
    # Extra Blocks
    extras = ["coke_oven", "primitive_blast_furnace", "treated_wood", "bronze_boiler", "steel_boiler", "large_bronze_boiler", "large_steel_boiler"]
    for e in extras:
        mineable_pickaxe.append(f"{MOD_ID}:{e}")
        needs_stone.append(f"{MOD_ID}:{e}")
        loot = {
          "type": "minecraft:block",
          "pools": [
            {
              "rolls": 1,
              "entries": [ { "type": "minecraft:item", "name": f"{MOD_ID}:{e}" } ],
              "conditions": [ { "condition": "minecraft:survives_explosion" } ]
            }
          ]
        }
        with open(f"{DATA_DIR}/loot_table/blocks/{e}.json", "w") as f:
            json.dump(loot, f, indent=2)

    # Tags
    with open(f"{DATA_DIR}/tags/block/mineable_with_pickaxe.json", "w") as f:
        json.dump({"replace": False, "values": mineable_pickaxe}, f, indent=2)
        
    with open(f"{DATA_DIR}/tags/block/needs_stone_tool.json", "w") as f:
        json.dump({"replace": False, "values": needs_stone}, f, indent=2)

    with open(f"{DATA_DIR}/tags/block/needs_iron_tool.json", "w") as f:
        json.dump({"replace": False, "values": needs_iron}, f, indent=2)
        
gen_loot_tables_and_tags()
