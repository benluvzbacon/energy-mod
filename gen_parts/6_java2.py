import os
from gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, SRC_DIR, DATA_DIR

def gen_item_group():
    items = []
    for metal, data in MATERIALS.items():
        for form in data["forms"]:
            name = f"deepslate_{metal}_ore" if form == "deepslate_ore" else f"{metal}_{form}"
            items.append(name)
            
    items.extend(["engineering_wrench", "basic_electrical_circuit", "rubber", "raw_rubber_pulp"])
    for tier in MACHINE_TIERS:
        for mtype in MACHINE_TYPES:
            items.append(f"{tier}_{mtype}")

    content = f"""package com.benluvzbacon.ironworks.registry;

import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;
import com.benluvzbacon.ironworks.Ironworks;

public class ModItemGroups {{
    public static final ItemGroup IRONWORKS_GROUP = Registry.register(Registries.ITEM_GROUP,
            Identifier.of(Ironworks.MOD_ID, "main"),
            FabricItemGroup.builder()
                    .icon(() -> new ItemStack(ModItems.BRONZE_GEAR))
                    .displayName(Text.translatable("itemGroup.ironworks.main"))
                    .entries((context, entries) -> {{
"""
    for item in items:
        content += f'                        entries.add(ModItems.{item.upper()});\n'

    content += """                    })
                    .build());
                    
    public static void initialize() {}
}
"""
    with open(f"{SRC_DIR}/registry/ModItemGroups.java", "w") as f:
        f.write(content)
        
    with open(f"{SRC_DIR}/Ironworks.java", "r") as f:
        orig = f.read()
    orig = orig.replace("ModItems.initialize();", "ModItems.initialize();\n        com.benluvzbacon.ironworks.registry.ModItemGroups.initialize();")
    with open(f"{SRC_DIR}/Ironworks.java", "w") as f:
        f.write(orig)
        
gen_item_group()
