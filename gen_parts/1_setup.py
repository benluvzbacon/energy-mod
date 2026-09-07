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
