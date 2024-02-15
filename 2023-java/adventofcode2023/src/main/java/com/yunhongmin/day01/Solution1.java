package com.yunhongmin.day01;

import com.yunhongmin.util.FileReader;

import java.util.List;
import java.util.Objects;

public class Solution1 {
    public static void main(String[] args) {
//        String path = "day01/sample1.txt";
        String path = "day01/input1.txt";
        String absolutePath = Objects.requireNonNull(Solution1.class.getResource("/" + path)).getFile();

        List<String> strings = FileReader.readAll(absolutePath);
        Integer ans = strings.stream()
                .map(Solution1::findCalibrationValue)
                .reduce(0, Integer::sum);

        System.out.println(ans);
    }

    public static int findCalibrationValue(String str) {
        int first = 0;
        int last = 0;

        for (char c : str.toCharArray()) {
            if (Character.isDigit(c)) {
                if (first == 0) {
                    first = Character.getNumericValue(c);
                }
                last = Character.getNumericValue(c);
            }
        }

        return first * 10 + last;
    }
}
