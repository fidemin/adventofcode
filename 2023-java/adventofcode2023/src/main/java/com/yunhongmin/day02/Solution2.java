package com.yunhongmin.day02;

import com.yunhongmin.util.FileReader;

import java.util.List;
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

            int maxRed = 0;
            int maxGreen = 0;
            int maxBlue = 0;
            for (String cubeSetStringPerGame : cubeSetStrings) {

                // cubeSetStringPerGame: 3 blue, 4 red
                String[] cubeStrings = cubeSetStringPerGame.split(", ");

                for (String cubeString : cubeStrings) {
                    // cubeString: 3 blue
                    String[] cubeCountColorString = cubeString.split(" ");
                    int count = Integer.parseInt(cubeCountColorString[0]);
                    String color = cubeCountColorString[1];

                    if (color.equals("red")) {
                        maxRed = Math.max(maxRed, count);
                    } else if (color.equals("green")) {
                        maxGreen = Math.max(maxGreen, count);
                    } else {
                        maxBlue = Math.max(maxBlue, count);
                    }
                }
            }
            result += maxRed * maxGreen * maxBlue;
        }

        System.out.println("answer: " + result);
    }
}

