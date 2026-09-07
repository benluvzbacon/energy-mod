import os

def gen_pipes_boilers():
    os.makedirs("src/main/java/com/benluvzbacon/ironworks/block", exist_ok=True)
    pipe = """package com.benluvzbacon.ironworks.block;

import net.minecraft.block.Block;
import net.minecraft.block.BlockEntityProvider;
import net.minecraft.block.BlockState;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.util.math.BlockPos;

public class PipeBlock extends Block implements BlockEntityProvider {
    public PipeBlock(Settings settings) { super(settings); }
    @Override public BlockEntity createBlockEntity(BlockPos pos, BlockState state) { return null; }
}
"""
    boiler = """package com.benluvzbacon.ironworks.block;

import net.minecraft.block.Block;
import net.minecraft.block.BlockEntityProvider;
import net.minecraft.block.BlockState;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.util.math.BlockPos;

public class BoilerBlock extends Block implements BlockEntityProvider {
    public BoilerBlock(Settings settings) { super(settings); }
    @Override public BlockEntity createBlockEntity(BlockPos pos, BlockState state) { return null; }
}
"""
    with open("src/main/java/com/benluvzbacon/ironworks/block/PipeBlock.java", "w") as f: f.write(pipe)
    with open("src/main/java/com/benluvzbacon/ironworks/block/BoilerBlock.java", "w") as f: f.write(boiler)

gen_pipes_boilers()
