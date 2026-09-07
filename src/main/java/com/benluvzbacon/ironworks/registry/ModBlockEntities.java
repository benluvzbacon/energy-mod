package com.benluvzbacon.ironworks.registry;

import net.minecraft.block.entity.BlockEntityType;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;
import net.fabricmc.fabric.api.object.builder.v1.block.entity.FabricBlockEntityTypeBuilder;
import com.benluvzbacon.ironworks.Ironworks;
import com.benluvzbacon.ironworks.block.entity.BoilerBlockEntity;
import com.benluvzbacon.ironworks.block.entity.MachineBlockEntity;

public class ModBlockEntities {
    public static final BlockEntityType<BoilerBlockEntity> BOILER_BLOCK_ENTITY = Registry.register(
            Registries.BLOCK_ENTITY_TYPE,
            Identifier.of(Ironworks.MOD_ID, "boiler_block_entity"),
            FabricBlockEntityTypeBuilder.create(BoilerBlockEntity::new, ModExtraBlocks.BRONZE_BOILER, ModExtraBlocks.STEEL_BOILER).build()
    );

    public static final BlockEntityType<MachineBlockEntity> MACHINE_BLOCK_ENTITY = Registry.register(
            Registries.BLOCK_ENTITY_TYPE,
            Identifier.of(Ironworks.MOD_ID, "machine_block_entity"),
            FabricBlockEntityTypeBuilder.create(MachineBlockEntity::new, 
                ModBlocks.BRONZE_MACERATOR, ModBlocks.BRONZE_FURNACE, ModBlocks.BRONZE_ALLOY_SMELTER,
                ModBlocks.STEEL_MACERATOR, ModBlocks.STEEL_FURNACE, ModBlocks.STEEL_ALLOY_SMELTER
            ).build()
    );

    public static void initialize() {}
}
