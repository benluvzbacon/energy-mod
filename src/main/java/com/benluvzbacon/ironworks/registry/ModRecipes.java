package com.benluvzbacon.ironworks.registry;

import com.benluvzbacon.ironworks.Ironworks;
import com.benluvzbacon.ironworks.recipe.MachineRecipe;
import com.mojang.serialization.MapCodec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import net.minecraft.item.ItemStack;
import net.minecraft.network.RegistryByteBuf;
import net.minecraft.network.codec.PacketCodec;
import net.minecraft.recipe.Ingredient;
import net.minecraft.recipe.RecipeSerializer;
import net.minecraft.recipe.RecipeType;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public class ModRecipes {

    public static RecipeType<MachineRecipe> MACERATOR_TYPE;
    public static RecipeSerializer<MachineRecipe> MACERATOR_SERIALIZER;
    
    public static RecipeType<MachineRecipe> COMPRESSOR_TYPE;
    public static RecipeSerializer<MachineRecipe> COMPRESSOR_SERIALIZER;
    
    public static RecipeType<MachineRecipe> EXTRACTOR_TYPE;
    public static RecipeSerializer<MachineRecipe> EXTRACTOR_SERIALIZER;

    public static void initialize() {
        MACERATOR_TYPE = Registry.register(Registries.RECIPE_TYPE, Identifier.of(Ironworks.MOD_ID, "macerating"), new RecipeType<MachineRecipe>() {
            @Override
            public String toString() {
                return "macerating";
            }
        });
        MACERATOR_SERIALIZER = Registry.register(Registries.RECIPE_SERIALIZER, Identifier.of(Ironworks.MOD_ID, "macerating"), new MachineRecipeSerializer(MACERATOR_TYPE));

        COMPRESSOR_TYPE = Registry.register(Registries.RECIPE_TYPE, Identifier.of(Ironworks.MOD_ID, "compressing"), new RecipeType<MachineRecipe>() {
            @Override
            public String toString() {
                return "compressing";
            }
        });
        COMPRESSOR_SERIALIZER = Registry.register(Registries.RECIPE_SERIALIZER, Identifier.of(Ironworks.MOD_ID, "compressing"), new MachineRecipeSerializer(COMPRESSOR_TYPE));

        EXTRACTOR_TYPE = Registry.register(Registries.RECIPE_TYPE, Identifier.of(Ironworks.MOD_ID, "extracting"), new RecipeType<MachineRecipe>() {
            @Override
            public String toString() {
                return "extracting";
            }
        });
        EXTRACTOR_SERIALIZER = Registry.register(Registries.RECIPE_SERIALIZER, Identifier.of(Ironworks.MOD_ID, "extracting"), new MachineRecipeSerializer(EXTRACTOR_TYPE));
    }

    public static class MachineRecipeSerializer implements RecipeSerializer<MachineRecipe> {
        private final RecipeType<MachineRecipe> type;
        private final MapCodec<MachineRecipe> codec;
        private final PacketCodec<RegistryByteBuf, MachineRecipe> packetCodec;

        public MachineRecipeSerializer(RecipeType<MachineRecipe> type) {
            this.type = type;
            this.codec = RecordCodecBuilder.mapCodec(instance -> instance.group(
                    Ingredient.DISALLOW_EMPTY_CODEC.fieldOf("ingredient").forGetter(MachineRecipe::getInput),
                    ItemStack.VALIDATED_CODEC.fieldOf("result").forGetter(r -> r.getResult(null))
            ).apply(instance, (ingredient, result) -> new MachineRecipe(ingredient, result, type, this)));
            
            this.packetCodec = PacketCodec.tuple(
                    Ingredient.PACKET_CODEC, MachineRecipe::getInput,
                    ItemStack.PACKET_CODEC, r -> r.getResult(null),
                    (ingredient, result) -> new MachineRecipe(ingredient, result, type, this)
            );
        }

        @Override
        public MapCodec<MachineRecipe> codec() {
            return codec;
        }

        @Override
        public PacketCodec<RegistryByteBuf, MachineRecipe> packetCodec() {
            return packetCodec;
        }
    }
}
