package com.benluvzbacon.ironworks.jei;

import com.benluvzbacon.ironworks.Ironworks;
import com.benluvzbacon.ironworks.recipe.MachineRecipe;
import com.benluvzbacon.ironworks.registry.ModBlocks;
import com.benluvzbacon.ironworks.registry.ModRecipes;
import mezz.jei.api.IModPlugin;
import mezz.jei.api.JeiPlugin;
import mezz.jei.api.helpers.IGuiHelper;
import mezz.jei.api.recipe.RecipeType;
import mezz.jei.api.registration.IRecipeCategoryRegistration;
import mezz.jei.api.registration.IRecipeRegistration;
import mezz.jei.api.registration.IRecipeCatalystRegistration;
import net.minecraft.item.ItemStack;
import net.minecraft.recipe.RecipeEntry;
import net.minecraft.recipe.RecipeManager;
import net.minecraft.util.Identifier;
import java.util.List;
import java.util.ArrayList;

@JeiPlugin
public class IronworksJeiPlugin implements IModPlugin {
    public static final RecipeType<MachineRecipe> MACERATING = RecipeType.create(Ironworks.MOD_ID, "macerating", MachineRecipe.class);
    public static final RecipeType<MachineRecipe> COMPRESSING = RecipeType.create(Ironworks.MOD_ID, "compressing", MachineRecipe.class);
    public static final RecipeType<MachineRecipe> EXTRACTING = RecipeType.create(Ironworks.MOD_ID, "extracting", MachineRecipe.class);

    @Override
    public Identifier getPluginUid() {
        return Identifier.of(Ironworks.MOD_ID, "jei_plugin");
    }

    @Override
    public void registerCategories(IRecipeCategoryRegistration registration) {
        IGuiHelper guiHelper = registration.getJeiHelpers().getGuiHelper();
        registration.addRecipeCategories(
            new MachineRecipeCategory(guiHelper, MACERATING, "macerating", new ItemStack(ModBlocks.BRONZE_MACERATOR)),
            new MachineRecipeCategory(guiHelper, COMPRESSING, "compressing", new ItemStack(ModBlocks.BRONZE_COMPRESSOR)),
            new MachineRecipeCategory(guiHelper, EXTRACTING, "extracting", new ItemStack(ModBlocks.BRONZE_EXTRACTOR))
        );
    }

    @Override
    public void registerRecipes(IRecipeRegistration registration) {
        // JEI 1.20+ provides getIngredientManager() and possibly getVanillaRecipeManager() or getRecipeManager()
        // Wait, let's just use MinecraftClient.getInstance().world.getRecipeManager() but carefully.
        RecipeManager rm;
        try {
            rm = net.minecraft.client.MinecraftClient.getInstance().world.getRecipeManager();
        } catch (Exception e) {
            // Fallback for title screen etc
            return;
        }
        
        if (rm != null) {
            registration.addRecipes(MACERATING, getRecipes(rm, ModRecipes.MACERATOR_TYPE));
            registration.addRecipes(COMPRESSING, getRecipes(rm, ModRecipes.COMPRESSOR_TYPE));
            registration.addRecipes(EXTRACTING, getRecipes(rm, ModRecipes.EXTRACTOR_TYPE));
        }
    }

    private List<MachineRecipe> getRecipes(RecipeManager rm, net.minecraft.recipe.RecipeType<MachineRecipe> type) {
        List<MachineRecipe> list = new ArrayList<>();
        for (RecipeEntry<?> entry : rm.values()) {
            if (entry.value().getType() == type && entry.value() instanceof MachineRecipe) {
                list.add((MachineRecipe) entry.value());
            }
        }
        return list;
    }

    @Override
    public void registerRecipeCatalysts(IRecipeCatalystRegistration registration) {
        registration.addRecipeCatalyst(new ItemStack(ModBlocks.BRONZE_MACERATOR), MACERATING);
        registration.addRecipeCatalyst(new ItemStack(ModBlocks.STEEL_MACERATOR), MACERATING);
        
        registration.addRecipeCatalyst(new ItemStack(ModBlocks.BRONZE_COMPRESSOR), COMPRESSING);
        registration.addRecipeCatalyst(new ItemStack(ModBlocks.STEEL_COMPRESSOR), COMPRESSING);
        
        registration.addRecipeCatalyst(new ItemStack(ModBlocks.BRONZE_EXTRACTOR), EXTRACTING);
        registration.addRecipeCatalyst(new ItemStack(ModBlocks.STEEL_EXTRACTOR), EXTRACTING);
    }
}
