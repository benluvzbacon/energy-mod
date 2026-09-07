import os
from PIL import Image, ImageDraw

ASSETS_DIR = "src/main/resources/assets/ironworks"

def gen_gui():
    img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    # Background panel
    d.rectangle([0, 0, 175, 165], fill=(198, 198, 198, 255), outline=(0, 0, 0, 255))
    
    # Title space
    d.rectangle([8, 6, 168, 16], fill=(198, 198, 198, 255))
    
    # Input slot
    d.rectangle([55, 34, 73, 52], fill=(139, 139, 139, 255), outline=(55, 55, 55, 255))
    
    # Output slot (larger)
    d.rectangle([115, 30, 141, 56], fill=(139, 139, 139, 255), outline=(55, 55, 55, 255))
    
    # Progress Arrow Outline (empty)
    d.polygon([(79, 34), (103, 34), (103, 41), (111, 41), (111, 43), (103, 43), (103, 50), (79, 50)], outline=(100, 100, 100, 255))
    
    # Fire/Fuel slot area
    d.rectangle([55, 53, 73, 71], fill=(139, 139, 139, 255), outline=(55, 55, 55, 255))
    
    # Inventory slots
    for row in range(3):
        for col in range(9):
            x = 7 + col * 18
            y = 83 + row * 18
            d.rectangle([x, y, x + 18, y + 18], fill=(139, 139, 139, 255), outline=(55, 55, 55, 255))
            
    # Hotbar
    for col in range(9):
        x = 7 + col * 18
        y = 141
        d.rectangle([x, y, x + 18, y + 18], fill=(139, 139, 139, 255), outline=(55, 55, 55, 255))
        
    img.save(f"{ASSETS_DIR}/textures/gui/machine.png")

gen_gui()
