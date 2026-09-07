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
    "copper": {"color": (255, 120, 50), "forms": ["crushed", "dust", "nugget", "plate", "rod", "wire", "gear", "hammer"]},
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
