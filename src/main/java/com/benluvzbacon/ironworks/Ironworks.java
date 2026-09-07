package com.benluvzbacon.ironworks;

import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.benluvzbacon.ironworks.registry.*;

public class Ironworks implements ModInitializer {
    public static final String MOD_ID = "ironworks";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    @Override
    public void onInitialize() {
        LOGGER.info("Initializing Ironworks: Steam Engineering");
        ModBlocks.initialize();
        ModExtraBlocks.initialize();
        ModItems.initialize();
        ModExtraItems.initialize();
        ModRecipes.initialize();
        ModItemGroups.initialize();
        ModBlockEntities.initialize();
        ModCommands.initialize();
        ModFluids.initialize();
        ModWorldGen.initialize();
        ModScreenHandlers.initialize();
    }
}
