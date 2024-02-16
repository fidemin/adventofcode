package com.yunhongmin.day02;

import java.util.HashMap;
import java.util.Map;

public class CubeDeterminant {
    Map<String, Integer> cubes;

    public CubeDeterminant(int red, int green, int blue) {
        cubes = new HashMap<>();
        cubes.put("red", red);
        cubes.put("green", green);
        cubes.put("blue", blue);
    }

    public boolean isPossible(String color, int count) {
        return cubes.get(color) >= count;
    }
}
