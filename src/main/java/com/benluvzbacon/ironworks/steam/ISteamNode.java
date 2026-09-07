package com.benluvzbacon.ironworks.steam;

import net.minecraft.util.math.Direction;

public interface ISteamNode {
    long getSteamCapacity();
    long getSteamAmount();
    long insertSteam(long maxAmount, boolean simulate);
    long extractSteam(long maxAmount, boolean simulate);
    boolean canConnect(Direction dir);
}
