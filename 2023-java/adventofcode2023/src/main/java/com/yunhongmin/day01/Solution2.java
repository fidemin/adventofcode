package com.yunhongmin.day01;

import com.yunhongmin.util.FileReader;

import java.util.*;

public class Solution2 {
    public static TrieNode rootDigitTrieNode = Trie.digitTrie().rootNode;
    public static Map<String, Integer> strToInt = new HashMap<String, Integer>() {
        {
            put("one", 1);
            put("two", 2);
            put("three", 3);
            put("four", 4);
            put("five", 5);
            put("six", 6);
            put("seven", 7);
            put("eight", 8);
            put("nine", 9);
        }
    };

    public static void main(String[] args) {
//        String path = "day01/sample2.txt";
        String path = "day01/input1.txt";

        String absolutePath = Objects.requireNonNull(Solution2.class.getResource("/" + path)).getFile();

        List<String> strings = FileReader.readAll(absolutePath);

        Integer ans = strings.stream()
                .map(Solution2::findCalibrationValue)
                .reduce(0, Integer::sum);

        System.out.println(ans);
    }

    public static int findCalibrationValue(String str) {
        int first = 0;
        int last = 0;

        List<TrieNode> trieNodes = new ArrayList<>();

        for (char c : str.toCharArray()) {
            if (Character.isDigit(c)) {
                if (first == 0) {
                    first = Character.getNumericValue(c);
                }
                last = Character.getNumericValue(c);

                trieNodes = new ArrayList<>();
            } else {
                trieNodes.add(Solution2.rootDigitTrieNode);
                List<TrieNode> newTrieNodes = new ArrayList<>();

                for (TrieNode node : trieNodes) {
                    TrieNode nextNode = node.nextNode(c);
                    if (nextNode == null) {
                        continue;
                    }

                    if (nextNode.isLeaf) {
                        if (first == 0) {
                            first = Solution2.strToInt.get(nextNode.fullWord);
                        }
                        last = Solution2.strToInt.get(nextNode.fullWord);
                    } else {
                        newTrieNodes.add(nextNode);
                    }
                }
                // exchange for next character iteration
                trieNodes = newTrieNodes;
            }
        }

        return first * 10 + last;
    }
}
