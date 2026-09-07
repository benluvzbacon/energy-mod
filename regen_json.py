MATERIALS = {
    "copper": {"color": (255, 120, 50), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "hammer"]},
    "tin": {"color": (200, 200, 210), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "iron": {"color": (180, 180, 180), "forms": ["crushed", "dust", "plate", "rod", "wire", "gear", "hammer", "ring", "screw", "bolt"]},
    "lead": {"color": (100, 100, 130), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "zinc": {"color": (220, 220, 225), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "gold": {"color": (255, 215, 0), "forms": ["crushed", "dust", "plate", "rod", "wire", "gear"]},
    "silver": {"color": (220, 230, 240), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "nickel": {"color": (160, 160, 150), "forms": ["raw", "ore", "deepslate_ore", "crushed", "dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "coal": {"color": (40, 40, 40), "forms": ["dust"]},
    "charcoal": {"color": (50, 40, 40), "forms": ["dust"]},
    "bronze": {"color": (205, 127, 50), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "ring", "screw", "hammer"]},
    "brass": {"color": (225, 193, 110), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block"]},
    "steel": {"color": (80, 80, 90), "forms": ["dust", "ingot", "nugget", "plate", "rod", "wire", "gear", "block", "ring", "screw", "hammer"]},
    "coal_coke": {"color": (20, 20, 20), "forms": ["dust", "gem", "block"]}
}

MACHINE_TIERS = ["bronze", "steel"]
MACHINE_TYPES = ["furnace", "macerator", "alloy_smelter", "forge_hammer", "compressor", "extractor", "rock_breaker"]
import random

def add_noise(color, variance=15):
    return tuple(max(0, min(255, c + random.randint(-variance, variance))) for c in color[:3]) + (255,)

def gen_colored_rect(path, color, size=(16, 16), outline=None, inner=None):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Background with noise
    for x in range(2, 14):
        for y in range(2, 14):
            d.point((x, y), fill=add_noise(color, 20))
    if inner:
        for x in range(4, 12):
            for y in range(4, 12):
                d.point((x, y), fill=add_noise(inner, 20))
    if outline:
        d.rectangle([2, 2, 13, 13], outline=outline)
    img.save(path)

def gen_ore_texture(path, color, is_deepslate=False):
    base_color = (60, 60, 60, 255) if is_deepslate else (120, 120, 120, 255)
    img = Image.new("RGBA", (16, 16), base_color)
    d = ImageDraw.Draw(img)
    
    # Add stone noise
    for x in range(16):
        for y in range(16):
            d.point((x, y), fill=add_noise(base_color, 15))
            
    # Add ore chunks
    for ox, oy in [(4, 4), (10, 8), (6, 12), (12, 3), (2, 10)]:
        if random.random() > 0.2:
            d.rectangle([ox, oy, ox+1, oy+1], fill=add_noise(color, 30))
            d.point((ox+2, oy), fill=add_noise(color, 40))
            d.point((ox, oy+2), fill=add_noise(color, 40))
            
    img.save(path)

def gen_item_texture(path, color, form):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if form == "ingot":
        d.polygon([(4,10), (12,10), (14,14), (2,14)], fill=color)
        d.polygon([(4,10), (12,10), (10,8), (6,8)], fill=add_noise(color, 40))
    elif form == "dust":
        for _ in range(30):
            d.point((random.randint(4, 12), random.randint(6, 14)), fill=add_noise(color, 30))
    elif form == "plate":
        d.rectangle([2, 2, 14, 14], fill=color, outline=(40,40,40))
        d.rectangle([4, 4, 12, 12], fill=add_noise(color, 20))
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
        for _ in range(20):
            d.point((random.randint(4, 12), random.randint(6, 14)), fill=add_noise(color, 40))
    elif form == "nugget":
        d.ellipse([6,6, 10,10], fill=color)
    elif form == "raw":
        for _ in range(40):
            r = random.randint(3, 12)
            d.point((r, random.randint(3, 12)), fill=add_noise(color, 30))
    else:
        d.rectangle([4,4, 12,12], fill=color)
    img.save(path)

def gen_machine_textures():
    for tier in MACHINE_TIERS:
        color = MATERIALS[tier]["color"]
        for mtype in MACHINE_TYPES:
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_{mtype}_front.png", color, inner=(50,50,50))
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_machine_side.png", color, outline=(30,30,30))
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_machine_top.png", color, outline=(30,30,30))
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{tier}_{mtype}_front_on.png", color, inner=(255,100,0))
    
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/primitive_blast_furnace_front.png", (150,50,50), inner=(50,50,50))
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/primitive_blast_furnace_front_on.png", (150,50,50), inner=(255,150,0))
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/firebrick.png", (150,50,50), outline=(100,30,30))
    
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/coke_oven_front.png", (100,50,50), inner=(30,30,30))
    gen_colored_rect(f"{ASSETS_DIR}/textures/block/coke_oven_front_on.png", (100,50,50), inner=(255,100,0))
    
    for p in ["small_bronze", "bronze", "reinforced_bronze", "steel"]:
        color = MATERIALS["steel"]["color"] if p == "steel" else MATERIALS["bronze"]["color"]
        gen_colored_rect(f"{ASSETS_DIR}/textures/block/{p}_pipe.png", color, inner=(20,20,20))

    for b in ["solid", "liquid", "solar"]:
        for t in ["bronze", "steel"]:
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{t}_{b}_boiler_front.png", MATERIALS[t]["color"], inner=(255,50,50) if b != "solar" else (50,200,255))
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{t}_{b}_boiler_front_on.png", MATERIALS[t]["color"], inner=(255,200,0) if b != "solar" else (255,255,255))
    
    for metal, data in MATERIALS.items():
        if "block" in data["forms"]:
            gen_colored_rect(f"{ASSETS_DIR}/textures/block/{metal}_block.png", data["color"], outline=(40,40,40))

def generate_all_textures():
    for metal, data in MATERIALS.items():
        color = data["color"]
        for form in data["forms"]:
            if form == "ore":
                gen_ore_texture(f"{ASSETS_DIR}/textures/block/{metal}_ore.png", color, is_deepslate=False)
            elif form == "deepslate_ore":
                gen_ore_texture(f"{ASSETS_DIR}/textures/block/deepslate_{metal}_ore.png", color, is_deepslate=True)
            elif form != "block":
                gen_item_texture(f"{ASSETS_DIR}/textures/item/{metal}_{form}.png", color, form)
    gen_machine_textures()
    
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/engineering_wrench.png", (100,100,100), inner=(200,200,200))
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/basic_electrical_circuit.png", (50,150,50), inner=(200,200,0))
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/rubber.png", (20,20,20))
    gen_colored_rect(f"{ASSETS_DIR}/textures/item/raw_rubber_pulp.png", (200,200,150))
    
    img = Image.new("RGBA", (256, 256), (198, 198, 198, 255))
    ImageDraw.Draw(img).rectangle([0, 0, 255, 255], outline=(0,0,0))
    img.save(f"{ASSETS_DIR}/textures/gui/machine.png")
    
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
            if form in ["ore", "deepslate_ore", "block"]:
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
                if "ore" in name:
                    lang[f"block.{MOD_ID}.{name}"] = name.replace("_", " ").title()
                else:
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
