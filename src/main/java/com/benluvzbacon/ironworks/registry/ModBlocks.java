package com.benluvzbacon.ironworks.registry;

import net.minecraft.block.Block;
import net.minecraft.block.AbstractBlock;
import net.minecraft.block.MapColor;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;
import net.minecraft.sound.BlockSoundGroup;
import com.benluvzbacon.ironworks.Ironworks;

public class ModBlocks {
    public static final Block TIN_ORE = registerBlock("tin_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block DEEPSLATE_TIN_ORE = registerBlock("deepslate_tin_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block TIN_BLOCK = registerBlock("tin_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block LEAD_ORE = registerBlock("lead_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block DEEPSLATE_LEAD_ORE = registerBlock("deepslate_lead_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block LEAD_BLOCK = registerBlock("lead_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block ZINC_ORE = registerBlock("zinc_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block DEEPSLATE_ZINC_ORE = registerBlock("deepslate_zinc_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block ZINC_BLOCK = registerBlock("zinc_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block SILVER_ORE = registerBlock("silver_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block DEEPSLATE_SILVER_ORE = registerBlock("deepslate_silver_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block SILVER_BLOCK = registerBlock("silver_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block NICKEL_ORE = registerBlock("nickel_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block DEEPSLATE_NICKEL_ORE = registerBlock("deepslate_nickel_ore", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block NICKEL_BLOCK = registerBlock("nickel_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_BLOCK = registerBlock("bronze_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRASS_BLOCK = registerBlock("brass_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_BLOCK = registerBlock("steel_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block COAL_COKE_BLOCK = registerBlock("coal_coke_block", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_FURNACE = registerBlock("bronze_furnace", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_MACERATOR = registerBlock("bronze_macerator", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_ALLOY_SMELTER = registerBlock("bronze_alloy_smelter", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_FORGE_HAMMER = registerBlock("bronze_forge_hammer", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_COMPRESSOR = registerBlock("bronze_compressor", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_EXTRACTOR = registerBlock("bronze_extractor", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block BRONZE_ROCK_BREAKER = registerBlock("bronze_rock_breaker", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_FURNACE = registerBlock("steel_furnace", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_MACERATOR = registerBlock("steel_macerator", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_ALLOY_SMELTER = registerBlock("steel_alloy_smelter", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_FORGE_HAMMER = registerBlock("steel_forge_hammer", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_COMPRESSOR = registerBlock("steel_compressor", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_EXTRACTOR = registerBlock("steel_extractor", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_ROCK_BREAKER = registerBlock("steel_rock_breaker", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));

    private static Block registerBlock(String name, Block block) {
        return Registry.register(Registries.BLOCK, Identifier.of(Ironworks.MOD_ID, name), block);
    }
    public static void initialize() {}
}
