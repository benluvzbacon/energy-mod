import os
SRC_DIR = "src/main/java/com/benluvzbacon/ironworks"

def gen_block_entities():
    os.makedirs(f"{SRC_DIR}/block/entity", exist_ok=True)
    
    boiler_be = """package com.benluvzbacon.ironworks.block.entity;

import net.minecraft.block.BlockState;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.util.math.BlockPos;
import com.benluvzbacon.ironworks.registry.ModBlockEntities;
import net.minecraft.world.World;

public class BoilerBlockEntity extends BlockEntity {
    public BoilerBlockEntity(BlockPos pos, BlockState state) {
        super(ModBlockEntities.BOILER_BLOCK_ENTITY, pos, state);
    }
    
    public static void tick(World world, BlockPos pos, BlockState state, BoilerBlockEntity blockEntity) {
        // Simple tick logic for now
    }
}
"""
    machine_be = """package com.benluvzbacon.ironworks.block.entity;

import net.minecraft.block.BlockState;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.util.math.BlockPos;
import com.benluvzbacon.ironworks.registry.ModBlockEntities;
import net.minecraft.world.World;

public class MachineBlockEntity extends BlockEntity {
    public MachineBlockEntity(BlockPos pos, BlockState state) {
        super(ModBlockEntities.MACHINE_BLOCK_ENTITY, pos, state);
    }
    
    public static void tick(World world, BlockPos pos, BlockState state, MachineBlockEntity blockEntity) {
        // Simple tick logic for now
    }
}
"""
    registry = """package com.benluvzbacon.ironworks.registry;

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
"""
    with open(f"{SRC_DIR}/block/entity/BoilerBlockEntity.java", "w") as f: f.write(boiler_be)
    with open(f"{SRC_DIR}/block/entity/MachineBlockEntity.java", "w") as f: f.write(machine_be)
    with open(f"{SRC_DIR}/registry/ModBlockEntities.java", "w") as f: f.write(registry)

gen_block_entities()
