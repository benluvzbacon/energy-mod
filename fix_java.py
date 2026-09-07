SRC_DIR='src/main/java/com/benluvzbacon/ironworks'; DATA_DIR='src/main/resources/data/ironworks'; MOD_ID='ironworks'
import os
from gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, SRC_DIR

def gen_java():
    items = []
    blocks = []
    
    for metal, data in MATERIALS.items():
        for form in data["forms"]:
            name = f"deepslate_{metal}_ore" if form == "deepslate_ore" else f"{metal}_{form}"
            if form in ["ore", "deepslate_ore", "block"]:
                blocks.append(name)
            else:
                items.append(name)
                
    misc_items = ["engineering_wrench", "basic_electrical_circuit", "rubber", "raw_rubber_pulp"]
    items.extend(misc_items)

    # ModItems.java
    mod_items_content = f"""package com.benluvzbacon.ironworks.registry;

import net.minecraft.item.Item;
import net.minecraft.item.BlockItem;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;
import com.benluvzbacon.ironworks.Ironworks;

public class ModItems {{
"""
    for item in items:
        mod_items_content += f'    public static final Item {item.upper()} = registerItem("{item}", new Item(new Item.Settings()));\n'
        
    for block in blocks:
        mod_items_content += f'    public static final Item {block.upper()} = registerItem("{block}", new BlockItem(ModBlocks.{block.upper()}, new Item.Settings()));\n'

    for tier in MACHINE_TIERS:
        for mtype in MACHINE_TYPES:
            name = f"{tier}_{mtype}"
            mod_items_content += f'    public static final Item {name.upper()} = registerItem("{name}", new BlockItem(ModBlocks.{name.upper()}, new Item.Settings()));\n'

    mod_items_content += """
    private static Item registerItem(String name, Item item) {
        return Registry.register(Registries.ITEM, Identifier.of(Ironworks.MOD_ID, name), item);
    }
    public static void initialize() {}
}
"""
    with open(f"{SRC_DIR}/registry/ModItems.java", "w") as f:
        f.write(mod_items_content)


    # ModBlocks.java
    mod_blocks_content = f"""package com.benluvzbacon.ironworks.registry;

import net.minecraft.block.Block;
import net.minecraft.block.AbstractBlock;
import net.minecraft.block.MapColor;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;
import net.minecraft.sound.BlockSoundGroup;
import com.benluvzbacon.ironworks.Ironworks;

public class ModBlocks {{
"""
    for block in blocks:
        mod_blocks_content += f'    public static final Block {block.upper()} = registerBlock("{block}", new Block(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));\n'
        
    for tier in MACHINE_TIERS:
        for mtype in MACHINE_TYPES:
            name = f"{tier}_{mtype}"
            # TODO: We need real MachineBlocks. For now we use placeholder MachineBlock class.
            mod_blocks_content += f'    public static final Block {name.upper()} = registerBlock("{name}", new com.benluvzbacon.ironworks.block.MachineBlock(AbstractBlock.Settings.create().mapColor(MapColor.IRON_GRAY).requiresTool().strength(3.0f, 3.0f).sounds(BlockSoundGroup.METAL)));\n'

    mod_blocks_content += """
    private static Block registerBlock(String name, Block block) {
        return Registry.register(Registries.BLOCK, Identifier.of(Ironworks.MOD_ID, name), block);
    }
    public static void initialize() {}
}
"""
    os.makedirs(f"{SRC_DIR}/block", exist_ok=True)
    with open(f"{SRC_DIR}/registry/ModBlocks.java", "w") as f:
        f.write(mod_blocks_content)

gen_java()
