package com.benluvzbacon.ironworks.registry;

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
