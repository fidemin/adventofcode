package com.yunhongmin.day01;

import java.util.HashMap;

public class Trie {
    TrieNode rootNode = new TrieNode();

    public Trie() {
        rootNode = new TrieNode();
    }

    public static Trie digitTrie() {
        Trie trie = new Trie();
        String[] digitList = new String[]{
                "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"
        };

        for (String s : digitList) {
            trie.add(s);
        }

        return trie;
    }

    public void add(String str) {
        TrieNode thisNode = rootNode;

        for (char c : str.toCharArray()) {
            if (thisNode.nextNode(c) == null) {
                thisNode.children.put(c, new TrieNode());
            }

            thisNode = thisNode.children.get(c);
        }

        thisNode.isLeaf = true;
        thisNode.fullWord = str;
    }
}

class TrieNode {
    HashMap<Character, TrieNode> children;
    boolean isLeaf;
    String fullWord;

    public TrieNode() {
        children = new HashMap<>();
    }

    public TrieNode nextNode(char c) {
        return children.getOrDefault(c, null);
    }
}
