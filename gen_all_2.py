import os
import json
from PIL import Image, ImageDraw

MOD_ID = "ironworks"
SRC_DIR = "src/main/java/com/benluvzbacon/ironworks"
RES_DIR = "src/main/resources"
ASSETS_DIR = f"{RES_DIR}/assets/{MOD_ID}"
DATA_DIR = f"{RES_DIR}/data/{MOD_ID}"

def create_dirs():
    dirs = [
        f"{SRC_DIR}/registry",
        f"{SRC_DIR}/item",
        f"{SRC_DIR}/block/entity",
        f"{SRC_DIR}/recipe",
        f"{SRC_DIR}/steam",
        f"{SRC_DIR}/gui",
        f"{SRC_DIR}/network",
        f"{ASSETS_DIR}/models/item",
        f"{ASSETS_DIR}/models/block",
        f"{ASSETS_DIR}/blockstates",
        f"{ASSETS_DIR}/textures/block",
        f"{ASSETS_DIR}/textures/item",
        f"{ASSETS_DIR}/textures/gui",
        f"{ASSETS_DIR}/lang",
        f"{DATA_DIR}/recipes",
        f"{DATA_DIR}/tags/items",
        f"{DATA_DIR}/tags/blocks",
        f"{RES_DIR}/data/c/tags/items",
        f"{RES_DIR}/data/c/tags/blocks"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

create_dirs()
MATERIALS = {
    "copper": {"color": (255, 120, 50), "forms": ["raw", "ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "hammer"]},
    "tin": {"color": (200, 200, 210), "forms": ["raw", "ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "iron": {"color": (180, 180, 180), "forms": ["crushed", "dust", "plate", "rod", "wire", "gear", "hammer", "ring", "screw", "bolt"]},
    "lead": {"color": (100, 100, 130), "forms": ["raw", "ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "zinc": {"color": (220, 220, 225), "forms": ["raw", "ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "gold": {"color": (255, 215, 0), "forms": ["crushed", "dust", "plate", "rod", "wire", "gear"]},
    "silver": {"color": (220, 230, 240), "forms": ["raw", "ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "nickel": {"color": (160, 160, 150), "forms": ["raw", "ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "coal": {"color": (40, 40, 40), "forms": ["dust"]},
    "charcoal": {"color": (50, 40, 40), "forms": ["dust"]},
    "bronze": {"color": (205, 127, 50), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "ring", "screw", "hammer"]},
    "brass": {"color": (225, 193, 110), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "steel": {"color": (80, 80, 90), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "ring", "screw", "hammer"]},
    "coal_coke": {"color": (20, 20, 20), "forms": ["dust", "gem", "block"]}
}

MACHINE_TIERS = ["bronze", "steel"]
MACHINE_TYPES = ["furnace", "macerator", "alloy_smelter", "forge_hammer", "compressor", "extractor", "rock_breaker"]
def gen_colored_rect(path, color, size=(16, 16), outline=None, inner=None):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Simple base shape
    d.rectangle([2, 2, 13, 13], fill=color)
    if inner:
        d.rectangle([4, 4, 11, 11], fill=inner)
    if outline:
        d.rectangle([2, 2, 13, 13], outline=outline)
    img.save(path)

def gen_ore_texture(path, color):
    img = Image.new("RGBA", (16, 16), (100, 100, 100, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([4, 4, 6, 6], fill=color)
    d.rectangle([10, 8, 12, 10], fill=color)
    d.rectangle([6, 12, 8, 14], fill=color)
    img.save(path)

def gen_item_texture(path, color, form):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if form == "ingot":
        d.polygon([(4,10), (12,10), (14,14), (2,14)], fill=color)
    elif form == "dust":
        d.ellipse([4, 10, 12, 16], fill=color)
        d.ellipse([6, 6, 10, 10], fill=color)
    elif form == "plate":
        d.rectangle([2, 2, 14, 14], fill=color, outline=(40,40,40))
    elif form == "gear":
        d.ellipse([2, 2, 14, 14], fill=color, outline=(40,40,40))
        d.ellipse([6, 6, 10, 10], fill=(0,0,0,0))
    elif form == "rod":
        d.line([(4,14), (12,2)], fill=color, width=3)
    elif form == "ring":
        d.ellipse([4, 4, 12, 12], outline=color, width=2)
    elif form == "screw":
        d.line([(8,14), (8,6)], fill=color, width=2)
        d.rectangle([6,2, 10,4], fill=color)
    elif form == "wire":
        d.arc([2,2, 14,14], start=0, end=180, fill=color, width=2)
    elif form == "hammer":
        d.rectangle([2,2, 10,6], fill=color)
        d.line([(6,6), (6,14)], fill=(139,69,19), width=2)
    elif form == "crushed":
        d.ellipse([4,8, 10,14], fill=color)
        d.ellipse([8,6, 12,12], fill=color)
    elif form == "nugget":
        d.ellipse([6,6, 10,10], fill=color)
    elif form == "raw":
        d.ellipse([3,3, 13,13], fill=color)
    else:
        d.rectangle([4,4, 12,12], fill=color)
    img.save(path)

def gen_machine_textures():
    for tier in MACHINE_TIERS:
        color = MATERIALS[tier]["color"]
        for mtype in MACHINE_TYPES:
            # Front, side, top
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_{mtype}_front.png", color, inner=(50,50,50))
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_machine_side.png", color, outline=(30,30,30))
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_machine_top.png", color, outline=(30,30,30))
            # Active front
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_{mtype}_front_on.png", color, inner=(255,100,0))
    
    # Primitive Blast Furnace
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/primitive_blast_furnace_front.png", (150,50,50), inner=(50,50,50))
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/primitive_blast_furnace_front_on.png", (150,50,50), inner=(255,150,0))
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/firebrick.png", (150,50,50), outline=(100,30,30))
    
    # Coke Oven
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/coke_oven_front.png", (100,50,50), inner=(30,30,30))
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/coke_oven_front_on.png", (100,50,50), inner=(255,100,0))
    
    # Pipes
    for p in ["small_bronze", "bronze", "reinforced_bronze", "steel"]:
        color = MATERIALS["steel"]["color"] if p == "steel" else MATERIALS["bronze"]["color"]
        gen_colored_rect(f"{ASSETS_DIR}/textures/block/{p}_pipe.png", color, inner=(20,20,20))

    # Boilers
    for b in ["solid", "liquid", "solar"]:
        for t in ["bronze", "steel"]:
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{t}_{b}_boiler_front.png", MATERIALS[t]["color"], inner=(255,50,50) if b != "solar" else (50,200,255))
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{t}_{b}_boiler_front_on.png", MATERIALS[t]["color"], inner=(255,200,0) if b != "solar" else (255,255,255))
    
    # Blocks
    for metal, data in MATERIALS.items():
        if "block" in data["forms"]:
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{metal}_block.png", data["color"], outline=(40,40,40))

def generate_all_textures():
    for metal, data in MATERIALS.items():
        color = data["color"]
        for form in data["forms"]:
            if form == "ore":
                gen_ore_texture(f"{ASSETS_DIR}/textures/block/{metal}_ore.png", color)
            elif form != "block":
                gen_item_texture(f"{ASSETS_DIR}/textures/item/{metal}_{form}.png", color, form)
    gen_machine_textures()
    
    # Misc
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/engineering_wrench.png", (100,100,100), inner=(200,200,200))
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/basic_electrical_circuit.png", (50,150,50), inner=(200,200,0))
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/rubber.png", (20,20,20))
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/raw_rubber_pulp.png", (200,200,150))
    
    # GUI
    img = Image.new("RGBA", (256, 256), (198, 198, 198, 255))
    ImageDraw.Draw(img).rectangle([0, 0, 255, 255], outline=(0,0,0))
    img.save(f"{ASSETS_DIR}/textures/gui/machine.png")
    
    # Icon
    gen_item_texture(f"{ASSETS_DIR}/icon.png", MATERIALS["bronze"]["color"], "gear")

generate_all_textures()
import os, json
from gen_assets import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, ASSETS_DIR, DATA_DIR

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def gen_models_and_blockstates():
    lang = {}
    
    # Items & Blocks
    for metal, data in MATERIALS.items():
        for form in data["forms"]:
            name = f"{metal}_{form}"
            if form in ["ore", "block"]:
                # Blockstate
                write_json(f"{ASSETS_DIR}/blockstates/{name}.json", {
                    "variants": {"": {"model": f"{MOD_ID}:block/{name}"}}
                })
                # Block Model
                write_json(f"{ASSETS_DIR}/models/block/{name}.json", {
                    "parent": "minecraft:block/cube_all",
                    "textures": {"all": f"{MOD_ID}:block/{name}"}
                })
                # Item Model
                write_json(f"{ASSETS_DIR}/models/item/{name}.json", {
                    "parent": f"{MOD_ID}:block/{name}"
                })
                lang[f"block.{MOD_ID}.{name}"] = name.replace("_", " ").title()
            else:
                # Item Model
                write_json(f"{ASSETS_DIR}/models/item/{name}.json", {
                    "parent": "minecraft:item/generated",
                    "textures": {"layer0": f"{MOD_ID}:item/{name}"}
                })
                lang[f"item.{MOD_ID}.{name}"] = name.replace("_", " ").title()
                
    # Machines
    for tier in MACHINE_TIERS:
        for mtype in MACHINE_TYPES:
            name = f"{tier}_{mtype}"
            lang[f"block.{MOD_ID}.{name}"] = f"{tier.title()} {mtype.replace('_', ' ').title()}"
            
            # Blockstate
            write_json(f"{ASSETS_DIR}/blockstates/{name}.json", {
                "variants": {
                    "facing=north,lit=false": {"model": f"{MOD_ID}:block/{name}"},
                    "facing=east,lit=false": {"model": f"{MOD_ID}:block/{name}", "y": 90},
                    "facing=south,lit=false": {"model": f"{MOD_ID}:block/{name}", "y": 180},
                    "facing=west,lit=false": {"model": f"{MOD_ID}:block/{name}", "y": 270},
                    "facing=north,lit=true": {"model": f"{MOD_ID}:block/{name}_on"},
                    "facing=east,lit=true": {"model": f"{MOD_ID}:block/{name}_on", "y": 90},
                    "facing=south,lit=true": {"model": f"{MOD_ID}:block/{name}_on", "y": 180},
                    "facing=west,lit=true": {"model": f"{MOD_ID}:block/{name}_on", "y": 270}
                }
            })
            
            # Models
            for state, tex in [("", "front"), ("_on", "front_on")]:
                write_json(f"{ASSETS_DIR}/models/block/{name}{state}.json", {
                    "parent": "minecraft:block/orientable",
                    "textures": {
                        "top": f"{MOD_ID}:block/{tier}_machine_top",
                        "front": f"{MOD_ID}:block/{name}_{tex}",
                        "side": f"{MOD_ID}:block/{tier}_machine_side"
                    }
                })
                
            write_json(f"{ASSETS_DIR}/models/item/{name}.json", {
                "parent": f"{MOD_ID}:block/{name}"
            })

    # Misc Items
    misc_items = ["engineering_wrench", "basic_electrical_circuit", "rubber", "raw_rubber_pulp"]
    for i in misc_items:
        write_json(f"{ASSETS_DIR}/models/item/{i}.json", {
            "parent": "minecraft:item/generated",
            "textures": {"layer0": f"{MOD_ID}:item/{i}"}
        })
        lang[f"item.{MOD_ID}.{i}"] = i.replace("_", " ").title()
        
    write_json(f"{ASSETS_DIR}/lang/en_us.json", lang)

gen_models_and_blockstates()
import os
from gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, SRC_DIR

def gen_java():
    items = []
    blocks = []
    
    for metal, data in MATERIALS.items():
        for form in data["forms"]:
            name = f"{metal}_{form}"
            if form in ["ore", "block"]:
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
import os
from gen_json import MATERIALS, MACHINE_TIERS, MACHINE_TYPES, MOD_ID, SRC_DIR, DATA_DIR

def gen_item_group():
    items = []
    for metal, data in MATERIALS.items():
        for form in data["forms"]:
            items.append(f"{metal}_{form}")
            
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
