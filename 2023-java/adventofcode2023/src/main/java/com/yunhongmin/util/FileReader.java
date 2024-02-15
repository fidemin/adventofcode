package com.yunhongmin.util;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class FileReader {
    public static List<String> readAll(String filepath) {
        File file = new File(filepath);
        Scanner scanner;
        try {
            scanner = new Scanner(file);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

        List<String> strList = new ArrayList<>();

        while (scanner.hasNextLine()) {
            String str = scanner.nextLine();
            strList.add(str);
        }
        return strList;
    }
}
