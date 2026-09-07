import os
from gen_json import SRC_DIR

def gen_gui():
    os.makedirs(f"{SRC_DIR}/gui", exist_ok=True)
    os.makedirs(f"{SRC_DIR}/network", exist_ok=True)
    
    handler = """package com.benluvzbacon.ironworks.gui;

import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.entity.player.PlayerInventory;
import net.minecraft.inventory.Inventory;
import net.minecraft.inventory.SimpleInventory;
import net.minecraft.item.ItemStack;
import net.minecraft.screen.ScreenHandler;
import net.minecraft.screen.ScreenHandlerType;
import net.minecraft.screen.slot.Slot;

public class SteamMachineScreenHandler extends ScreenHandler {
    private final Inventory inventory;

    public SteamMachineScreenHandler(int syncId, PlayerInventory playerInventory) {
        this(syncId, playerInventory, new SimpleInventory(2));
    }

    public SteamMachineScreenHandler(int syncId, PlayerInventory playerInventory, Inventory inventory) {
        // null for type for now, will register properly
        super(null, syncId);
        this.inventory = inventory;
        inventory.onOpen(playerInventory.player);

        this.addSlot(new Slot(inventory, 0, 56, 35));
        this.addSlot(new Slot(inventory, 1, 116, 35));

        for (int m = 0; m < 3; ++m) {
            for (int l = 0; l < 9; ++l) {
                this.addSlot(new Slot(playerInventory, l + m * 9 + 9, 8 + l * 18, 84 + m * 18));
            }
        }
        for (int m = 0; m < 9; ++m) {
            this.addSlot(new Slot(playerInventory, m, 8 + m * 18, 142));
        }
    }

    @Override
    public ItemStack quickMove(PlayerEntity player, int index) {
        return ItemStack.EMPTY;
    }

    @Override
    public boolean canUse(PlayerEntity player) {
        return this.inventory.canPlayerUse(player);
    }
}
"""
    with open(f"{SRC_DIR}/gui/SteamMachineScreenHandler.java", "w") as f: f.write(handler)
    
    screen = """package com.benluvzbacon.ironworks.gui;

import net.minecraft.client.gui.DrawContext;
import net.minecraft.client.gui.screen.ingame.HandledScreen;
import net.minecraft.entity.player.PlayerInventory;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;
import com.benluvzbacon.ironworks.Ironworks;

public class SteamMachineScreen extends HandledScreen<SteamMachineScreenHandler> {
    private static final Identifier TEXTURE = Identifier.of(Ironworks.MOD_ID, "textures/gui/machine.png");

    public SteamMachineScreen(SteamMachineScreenHandler handler, PlayerInventory inventory, Text title) {
        super(handler, inventory, title);
    }

    @Override
    protected void drawBackground(DrawContext context, float delta, int mouseX, int mouseY) {
        int x = (width - backgroundWidth) / 2;
        int y = (height - backgroundHeight) / 2;
        context.drawTexture(TEXTURE, x, y, 0, 0, backgroundWidth, backgroundHeight);
    }

    @Override
    public void render(DrawContext context, int mouseX, int mouseY, float delta) {
        super.render(context, mouseX, mouseY, delta);
        drawMouseoverTooltip(context, mouseX, mouseY);
    }
}
"""
    with open(f"{SRC_DIR}/gui/SteamMachineScreen.java", "w") as f: f.write(screen)
    
gen_gui()
