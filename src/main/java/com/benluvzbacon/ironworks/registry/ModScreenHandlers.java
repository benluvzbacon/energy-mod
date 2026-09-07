package com.benluvzbacon.ironworks.registry;

import net.fabricmc.fabric.api.screenhandler.v1.ExtendedScreenHandlerType;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.screen.ScreenHandlerType;
import net.minecraft.util.Identifier;
import com.benluvzbacon.ironworks.Ironworks;
import com.benluvzbacon.ironworks.gui.SteamMachineScreenHandler;

public class ModScreenHandlers {
    public static final ScreenHandlerType<SteamMachineScreenHandler> MACHINE_SCREEN_HANDLER = Registry.register(
            Registries.SCREEN_HANDLER,
            Identifier.of(Ironworks.MOD_ID, "machine"),
            new ScreenHandlerType<>(SteamMachineScreenHandler::new, net.minecraft.resource.featuretoggle.FeatureFlags.VANILLA_FEATURES)
    );

    public static void initialize() {}
}
