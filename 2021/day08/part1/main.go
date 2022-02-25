package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type Entry struct {
	Patterns   []string
	fourDigits []string
}

func (e Entry) uniqueNumberSegmentPatterns() (string, string, string, string) {
	oneStr := ""
	fourStr := ""
	sevenStr := ""
	eightStr := ""

	for _, p := range e.Patterns {
		switch length := len(p); length {
		case 2:
			oneStr = p
		case 4:
			fourStr = p
		case 3:
			sevenStr = p
		case 7:
			eightStr = p
		default:
			continue
		}
	}
	return oneStr, fourStr, sevenStr, eightStr
}

func (e Entry) numberOfOnlyDigits() int {
	count := 0
	for _, d := range e.fourDigits {
		switch length := len(d); length {
		case 2:
			count += 1
		case 4:
			count += 1
		case 3:
			count += 1
		case 7:
			count += 1
		default:
			continue
		}
	}
	return count
}

func parseInput(filename string) []Entry {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	entries := make([]Entry, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		str := scanner.Text()
		initSplits := strings.Split(str, " | ")
		patterns := strings.Split(initSplits[0], " ")
		fourDigits := strings.Split(initSplits[1], " ")

		entries = append(entries, Entry{patterns, fourDigits})
	}
	return entries
}

func main() {
	filename := os.Args[1]
	entries := parseInput(filename)
	totalCount := 0
	for _, entry := range entries {
		totalCount += entry.numberOfOnlyDigits()
	}
	fmt.Println(totalCount)
}
