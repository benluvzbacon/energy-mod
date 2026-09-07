package com.benluvzbacon.ironworks;

import net.fabricmc.api.ClientModInitializer;

public class IronworksClient implements ClientModInitializer {
    @Override
    public void onInitializeClient() {
        Ironworks.LOGGER.info("Initializing Ironworks Client");
        net.minecraft.client.gui.screen.ingame.HandledScreens.register(com.benluvzbacon.ironworks.registry.ModScreenHandlers.MACHINE_SCREEN_HANDLER, com.benluvzbacon.ironworks.gui.SteamMachineScreen::new);
    }
}
