package com.benluvzbacon.ironworks.registry;

import net.minecraft.block.Block;
import net.minecraft.block.AbstractBlock;
import net.minecraft.block.MapColor;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;
import net.minecraft.sound.BlockSoundGroup;
import com.benluvzbacon.ironworks.Ironworks;

public class ModExtraBlocks {
    public static final Block COKE_OVEN = registerBlock("coke_oven", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.RED).requiresTool().strength(3.0f).sounds(BlockSoundGroup.STONE)));
    public static final Block PRIMITIVE_BLAST_FURNACE = registerBlock("primitive_blast_furnace", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.RED).requiresTool().strength(3.0f).sounds(BlockSoundGroup.STONE)));
    public static final Block TREATED_WOOD = registerBlock("treated_wood", new Block(AbstractBlock.Settings.create().mapColor(MapColor.BROWN).requiresTool().strength(2.0f).sounds(BlockSoundGroup.WOOD)));
    
    public static final Block BRONZE_BOILER = registerBlock("bronze_boiler", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.BROWN).requiresTool().strength(3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block STEEL_BOILER = registerBlock("steel_boiler", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f).sounds(BlockSoundGroup.METAL)));
    
    public static final Block LARGE_BRONZE_BOILER = registerBlock("large_bronze_boiler", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.BROWN).requiresTool().strength(3.0f).sounds(BlockSoundGroup.METAL)));
    public static final Block LARGE_STEEL_BOILER = registerBlock("large_steel_boiler", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f).sounds(BlockSoundGroup.METAL)));

    private static Block registerBlock(String name, Block block) {
        return Registry.register(Registries.BLOCK, Identifier.of(Ironworks.MOD_ID, name), block);
    }
    public static void initialize() {}
}
