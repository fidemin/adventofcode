package com.yunhongmin.day02;

import java.util.HashMap;
import java.util.Map;

public class CubeDeterminant {
    Map<CubeColor, Integer> cubes;

    public CubeDeterminant(int red, int green, int blue) {
        cubes = new HashMap<>();
        cubes.put(CubeColor.RED, red);
        cubes.put(CubeColor.GREEN, green);
        cubes.put(CubeColor.BLUE, blue);
    }

    public boolean isPossible(CubeColor color, int count) {
        return cubes.get(color) >= count;
    }
}
