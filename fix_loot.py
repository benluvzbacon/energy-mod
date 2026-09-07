DATA_DIR='src/main/resources/data/ironworks'; MOD_ID='ironworks'; ASSETS_DIR='src/main/resources/assets/ironworks'
MATERIALS = {
    "copper": {"color": (255, 120, 50), "forms": ["crushed", "dust", "nugget", "plate", "rod", "wire", "gear", "hammer"]},
    "tin": {"color": (200, 200, 210), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "iron": {"color": (180, 180, 180), "forms": ["crushed", "dust", "plate", "rod", "wire", "gear", "hammer", "ring", "screw", "bolt"]},
    "lead": {"color": (100, 100, 130), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "zinc": {"color": (220, 220, 225), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "gold": {"color": (255, 215, 0), "forms": ["crushed", "dust", "plate", "rod", "wire", "gear"]},
    "silver": {"color": (220, 230, 240), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "nickel": {"color": (160, 160, 150), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "coal": {"color": (40, 40, 40), "forms": ["dust"]},
    "charcoal": {"color": (50, 40, 40), "forms": ["dust"]},
    "bronze": {"color": (205, 127, 50), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "ring", "screw", "hammer"]},
    "brass": {"color": (225, 193, 110), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "steel": {"color": (80, 80, 90), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "ring", "screw", "hammer"]},
    "coal_coke": {"color": (20, 20, 20), "forms": ["dust", "gem", "block"]}
}

MACHINE_TIERS = ["bronze", "steel"]
MACHINE_TYPES = ["furnace", "macerator", "alloy_smelter", "forge_hammer", "compressor", "extractor", "rock_breaker"]
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
