package com.benluvzbacon.ironworks.registry;

import net.minecraft.item.Item;
import net.minecraft.item.BlockItem;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;
import com.benluvzbacon.ironworks.Ironworks;

public class ModExtraItems {
    public static final Item COKE_OVEN = registerItem("coke_oven", new BlockItem(ModExtraBlocks.COKE_OVEN, new Item.Settings()));
    public static final Item PRIMITIVE_BLAST_FURNACE = registerItem("primitive_blast_furnace", new BlockItem(ModExtraBlocks.PRIMITIVE_BLAST_FURNACE, new Item.Settings()));
    public static final Item TREATED_WOOD = registerItem("treated_wood", new BlockItem(ModExtraBlocks.TREATED_WOOD, new Item.Settings()));
    public static final Item BRONZE_BOILER = registerItem("bronze_boiler", new BlockItem(ModExtraBlocks.BRONZE_BOILER, new Item.Settings()));
    public static final Item STEEL_BOILER = registerItem("steel_boiler", new BlockItem(ModExtraBlocks.STEEL_BOILER, new Item.Settings()));
    public static final Item LARGE_BRONZE_BOILER = registerItem("large_bronze_boiler", new BlockItem(ModExtraBlocks.LARGE_BRONZE_BOILER, new Item.Settings()));
    public static final Item LARGE_STEEL_BOILER = registerItem("large_steel_boiler", new BlockItem(ModExtraBlocks.LARGE_STEEL_BOILER, new Item.Settings()));

    private static Item registerItem(String name, Item item) {
        return Registry.register(Registries.ITEM, Identifier.of(Ironworks.MOD_ID, name), item);
    }
    public static void initialize() {}
}
