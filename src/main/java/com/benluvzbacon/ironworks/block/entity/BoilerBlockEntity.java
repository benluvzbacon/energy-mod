package com.benluvzbacon.ironworks.block.entity;

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
