package com.yunhongmin.day02;

import java.util.HashMap;
import java.util.Map;

public class CubeSet {
    public static CubeSet fromString(String str) {
        CubeSet cubeSet = new CubeSet();

        // cubeString: 3 blue, 4 red
        String[] cubeStrings = str.split(", ");

        for (String cubeString : cubeStrings) {
            // cubeString: 3 blue
            String[] cubeCountColorString = cubeString.split(" ");
            int count = Integer.parseInt(cubeCountColorString[0]);
            String colorStr = cubeCountColorString[1];
            CubeColor cubeColor = CubeColor.valueOf(colorStr.toUpperCase());
            cubeSet.increase(cubeColor, count);
        }
        return cubeSet;
    }

    Map<CubeColor, Integer> set;


    public CubeSet() {
        this.set = new HashMap<>();

        for (CubeColor cubeColor : CubeColor.values()) {
            this.set.put(cubeColor, 0);
        }
    }

    public void increase(CubeColor color, int amount) {
        this.set.put(color, this.set.get(color) + amount);
    }

    public int get(CubeColor color) {
        return this.set.get(color);
    }
}
