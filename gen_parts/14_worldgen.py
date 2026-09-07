import os
import json

DATA_DIR = "src/main/resources/data/ironworks"
SRC_DIR = "src/main/java/com/benluvzbacon/ironworks"

ORES = ["tin", "lead", "silver", "zinc", "nickel"]

def gen_worldgen():
    os.makedirs(f"{DATA_DIR}/worldgen/configured_feature", exist_ok=True)
    os.makedirs(f"{DATA_DIR}/worldgen/placed_feature", exist_ok=True)
    os.makedirs(f"{DATA_DIR}/tags/worldgen/biome", exist_ok=True)
    
    for ore in ORES:
        # Configured feature
        with open(f"{DATA_DIR}/worldgen/configured_feature/{ore}_ore.json", "w") as f:
            json.dump({
              "type": "minecraft:ore",
              "config": {
                "size": 9,
                "discard_chance_on_air_exposure": 0.0,
                "targets": [
                  {
                    "target": {
                      "predicate_type": "minecraft:tag_match",
                      "tag": "minecraft:stone_ore_replaceables"
                    },
                    "state": { "Name": f"ironworks:{ore}_ore" }
                  },
                  {
                    "target": {
                      "predicate_type": "minecraft:tag_match",
                      "tag": "minecraft:deepslate_ore_replaceables"
                    },
                    "state": { "Name": f"ironworks:deepslate_{ore}_ore" }
                  }
                ]
              }
            }, f, indent=2)

        # Placed feature
        with open(f"{DATA_DIR}/worldgen/placed_feature/{ore}_ore.json", "w") as f:
            json.dump({
              "feature": f"ironworks:{ore}_ore",
              "placement": [
                { "type": "minecraft:count", "count": 10 },
                { "type": "minecraft:in_square" },
                { "type": "minecraft:height_range", "height": { "type": "minecraft:trapezoid", "min_inclusive": { "absolute": -64 }, "max_inclusive": { "absolute": 64 } } },
                { "type": "minecraft:biome" }
              ]
            }, f, indent=2)

    worldgen_java = """package com.benluvzbacon.ironworks.registry;

import net.fabricmc.fabric.api.biome.v1.BiomeModifications;
import net.fabricmc.fabric.api.biome.v1.BiomeSelectors;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.util.Identifier;
import net.minecraft.world.gen.GenerationStep;
import com.benluvzbacon.ironworks.Ironworks;

public class ModWorldGen {
    public static void initialize() {
        String[] ores = {"tin_ore", "lead_ore", "silver_ore", "zinc_ore", "nickel_ore"};
        for (String ore : ores) {
            BiomeModifications.addFeature(
                BiomeSelectors.foundInOverworld(),
                GenerationStep.Feature.UNDERGROUND_ORES,
                RegistryKey.of(RegistryKeys.PLACED_FEATURE, Identifier.of(Ironworks.MOD_ID, ore))
            );
        }
    }
}
"""
    with open(f"{SRC_DIR}/registry/ModWorldGen.java", "w") as f:
        f.write(worldgen_java)
        
gen_worldgen()
