package com.yunhongmin.day02;

import com.yunhongmin.util.FileReader;

import java.util.List;
import java.util.Objects;

public class Solution1 {
    public static void main(String[] args) {
//        String path = "day02/sample1.txt";
        String path = "day02/input.txt";
        String absolutePath = Objects.requireNonNull(
                com.yunhongmin.day02.Solution1.class.getResource("/" + path)).getFile();
        List<String> strings = FileReader.readAll(absolutePath);

        CubeDeterminant cubeDeterminant = new CubeDeterminant(12, 13, 14);
        int possibleGameNumberSum = 0;

        for (String str : strings) {
            // str: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            String[] gameCubeSetsSplit = str.split(": ");

            int gameNumber = Integer.parseInt(gameCubeSetsSplit[0].split(" ")[1]);

            // cubeSetsString: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            String cubeSetsString = gameCubeSetsSplit[1];
            String[] cubeSetStrings = cubeSetsString.split("; ");

            boolean isPossible = true;
            for (String cubeSetString : cubeSetStrings) {
                CubeSet cubeSet = CubeSet.fromString(cubeSetString);

                for (CubeColor cubeColor : CubeColor.values()) {
                    if (!cubeDeterminant.isPossible(cubeColor, cubeSet.get(cubeColor))) {
                        isPossible = false;
                        break;
                    }
                }

                if (!isPossible) {
                    break;
                }
            }
            if (isPossible) {
                possibleGameNumberSum += gameNumber;
            }
        }

        System.out.println("answer: " + possibleGameNumberSum);
    }
}

