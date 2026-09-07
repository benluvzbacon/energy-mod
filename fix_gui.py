import os
from PIL import Image, ImageDraw

ASSETS_DIR = "src/main/resources/assets/ironworks"

def draw_beveled_rect(d, box, base_color, highlight_color, shadow_color, border_color=None):
    x0, y0, x1, y1 = box
    if border_color:
        d.rectangle([x0-1, y0-1, x1+1, y1+1], fill=border_color)
    d.rectangle([x0, y0, x1, y1], fill=base_color)
    
    # Highlight (Top, Left)
    d.line([(x0, y0), (x1, y0)], fill=highlight_color, width=1)
    d.line([(x0, y0), (x0, y1)], fill=highlight_color, width=1)
    
    # Shadow (Bottom, Right)
    d.line([(x0, y1), (x1, y1)], fill=shadow_color, width=1)
    d.line([(x1, y0), (x1, y1)], fill=shadow_color, width=1)

def draw_slot(d, x, y, size=18):
    # Vanilla slot: dark top/left, white bottom/right
    draw_beveled_rect(d, [x, y, x+size-1, y+size-1], base_color=(139, 139, 139, 255), 
                      highlight_color=(55, 55, 55, 255), 
                      shadow_color=(255, 255, 255, 255))

def gen_gui():
    os.makedirs(f"{ASSETS_DIR}/textures/gui", exist_ok=True)
    img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    # Main Panel (176x166 is vanilla standard)
    draw_beveled_rect(d, [0, 0, 175, 165], base_color=(198, 198, 198, 255), 
                      highlight_color=(255, 255, 255, 255), 
                      shadow_color=(85, 85, 85, 255),
                      border_color=(0, 0, 0, 255))
    
    # Title space (no visual box, just space)
    
    # Input slot
    draw_slot(d, 55, 34)
    
    # Output slot (26x26)
    draw_beveled_rect(d, [115, 30, 115+25, 30+25], base_color=(139, 139, 139, 255), 
                      highlight_color=(55, 55, 55, 255), 
                      shadow_color=(255, 255, 255, 255))
    
    # Progress Arrow Outline (Empty)
    # Just draw a simple arrow
    arrow = [(79, 34), (103, 34), (103, 41), (111, 41), (111, 43), (103, 43), (103, 50), (79, 50)]
    d.polygon(arrow, outline=(85, 85, 85, 255), fill=(150, 150, 150, 255))
    
    # Fire/Fuel slot area
    draw_slot(d, 55, 53)
    
    # Player Inventory slots
    for row in range(3):
        for col in range(9):
            x = 7 + col * 18
            y = 83 + row * 18
            draw_slot(d, x, y)
            
    # Hotbar slots
    for col in range(9):
        x = 7 + col * 18
        y = 141
        draw_slot(d, x, y)
        
    img.save(f"{ASSETS_DIR}/textures/gui/machine.png")

gen_gui()
