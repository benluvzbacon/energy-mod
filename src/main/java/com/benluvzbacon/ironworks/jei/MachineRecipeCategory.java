package com.benluvzbacon.ironworks.jei;

import com.benluvzbacon.ironworks.Ironworks;
import com.benluvzbacon.ironworks.recipe.MachineRecipe;
import mezz.jei.api.gui.builder.IRecipeLayoutBuilder;
import mezz.jei.api.gui.drawable.IDrawable;
import mezz.jei.api.helpers.IGuiHelper;
import mezz.jei.api.recipe.IFocusGroup;
import mezz.jei.api.recipe.RecipeIngredientRole;
import mezz.jei.api.recipe.RecipeType;
import mezz.jei.api.recipe.category.IRecipeCategory;
import net.minecraft.item.ItemStack;
import net.minecraft.text.Text;
import org.jetbrains.annotations.Nullable;

public class MachineRecipeCategory implements IRecipeCategory<MachineRecipe> {
    private final RecipeType<MachineRecipe> recipeType;
    private final Text title;
    private final IDrawable background;
    private final IDrawable icon;

    public MachineRecipeCategory(IGuiHelper guiHelper, RecipeType<MachineRecipe> recipeType, String name, ItemStack iconStack) {
        this.recipeType = recipeType;
        this.title = Text.translatable("category." + Ironworks.MOD_ID + "." + name);
        this.background = guiHelper.createBlankDrawable(82, 34);
        this.icon = guiHelper.createDrawableItemStack(iconStack);
    }

    @Override
    public RecipeType<MachineRecipe> getRecipeType() {
        return recipeType;
    }

    @Override
    public Text getTitle() {
        return title;
    }

    @Override
    public IDrawable getBackground() {
        return background;
    }

    @Override
    public @Nullable IDrawable getIcon() {
        return icon;
    }

    @Override
    public void setRecipe(IRecipeLayoutBuilder builder, MachineRecipe recipe, IFocusGroup focuses) {
        builder.addSlot(RecipeIngredientRole.INPUT, 1, 9).addIngredients(recipe.getInput());
        builder.addSlot(RecipeIngredientRole.OUTPUT, 61, 9).addItemStack(recipe.getResult(null));
    }
}
