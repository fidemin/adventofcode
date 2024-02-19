package com.yunhongmin.day02;

import com.yunhongmin.util.FileReader;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

public class Solution2 {
    public static void main(String[] args) {
//        String path = "day02/sample2.txt";
        String path = "day02/input.txt";
        String absolutePath = Objects.requireNonNull(
                com.yunhongmin.day02.Solution2.class.getResource("/" + path)).getFile();
        List<String> strings = FileReader.readAll(absolutePath);

        int result = 0;

        for (String str : strings) {
            // str: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            String[] gameCubeSetsSplit = str.split(": ");

            // cubeSetsString: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            String cubeSetsString = gameCubeSetsSplit[1];
            String[] cubeSetStrings = cubeSetsString.split("; ");

            Map<CubeColor, Integer> maxSet = new HashMap<CubeColor, Integer>() {
                {
                    put(CubeColor.RED, 0);
                    put(CubeColor.GREEN, 0);
                    put(CubeColor.BLUE, 0);
                }
            };

            for (String cubeSetStringPerGame : cubeSetStrings) {
                // cubeSetStringPerGame: 3 blue, 4 red
                CubeSet cubeSet = CubeSet.fromString(cubeSetStringPerGame);

                for (CubeColor cubeColor : CubeColor.values()) {
                    maxSet.put(cubeColor, Math.max(maxSet.get(cubeColor), cubeSet.get(cubeColor)));
                }
            }

            int multiply = 1;
            for (int value : maxSet.values()) {
                multiply *= value;
            }
            result += multiply;
        }

        System.out.println("answer: " + result);
    }
}

