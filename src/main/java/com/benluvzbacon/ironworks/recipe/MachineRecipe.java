package com.benluvzbacon.ironworks.recipe;

import net.minecraft.item.ItemStack;
import net.minecraft.recipe.Ingredient;
import net.minecraft.recipe.Recipe;
import net.minecraft.recipe.RecipeSerializer;
import net.minecraft.recipe.RecipeType;
import net.minecraft.recipe.input.SingleStackRecipeInput;
import net.minecraft.registry.RegistryWrapper;
import net.minecraft.world.World;

public class MachineRecipe implements Recipe<SingleStackRecipeInput> {
    private final Ingredient input;
    private final ItemStack output;
    private final RecipeType<?> type;
    private final RecipeSerializer<?> serializer;

    public MachineRecipe(Ingredient input, ItemStack output, RecipeType<?> type, RecipeSerializer<?> serializer) {
        this.input = input;
        this.output = output;
        this.type = type;
        this.serializer = serializer;
    }

    public Ingredient getInput() { return input; }

    @Override
    public boolean matches(SingleStackRecipeInput inventory, World world) {
        return input.test(inventory.item());
    }

    @Override
    public ItemStack craft(SingleStackRecipeInput inventory, RegistryWrapper.WrapperLookup lookup) {
        return output.copy();
    }

    @Override
    public boolean fits(int width, int height) {
        return true;
    }

    @Override
    public ItemStack getResult(RegistryWrapper.WrapperLookup lookup) {
        return output;
    }

    @Override
    public RecipeSerializer<?> getSerializer() {
        return serializer;
    }

    @Override
    public RecipeType<?> getType() {
        return type;
    }
}
