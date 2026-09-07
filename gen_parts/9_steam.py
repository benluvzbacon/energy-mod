import os

def gen_steam_api():
    os.makedirs("src/main/java/com/benluvzbacon/ironworks/steam", exist_ok=True)
    content = """package com.benluvzbacon.ironworks.steam;

import net.minecraft.util.math.Direction;

public interface ISteamNode {
    long getSteamCapacity();
    long getSteamAmount();
    long insertSteam(long maxAmount, boolean simulate);
    long extractSteam(long maxAmount, boolean simulate);
    boolean canConnect(Direction dir);
}
"""
    with open("src/main/java/com/benluvzbacon/ironworks/steam/ISteamNode.java", "w") as f:
        f.write(content)

gen_steam_api()
