package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
)

func parseInput(filename string) []*Line {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	lines := make([]*Line, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		str := scanner.Text()
		line := NewLine(str)
		lines = append(lines, line)
	}

	return lines
}

type LineStatus string

const (
	LineStatusCorrupted  LineStatus = "Corrupted"
	LineStatusInComplete LineStatus = "InComplete"
)

var charSetPair map[uint8]uint8 = map[uint8]uint8{
	'[': ']',
	'{': '}',
	'<': '>',
	'(': ')',
}

var charPoint map[uint8]int = map[uint8]int{
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}

type Line struct {
	str    string
	len    int
	cursor int
	stack  []uint8
}

func NewLine(str string) *Line {
	return &Line{
		str: str,
		len: len(str),
	}
}

func (l *Line) CheckStatus() LineStatus {
	//defer fmt.Println()
	stack := make([]uint8, 0)
	for l.cursor < l.len {
		char := l.str[l.cursor]
		//fmt.Printf("%s", string(char))
		if _, ok := charSetPair[char]; ok {
			// char = [, {, <, (
			stack = append(stack, char)
		} else {
			// char = ], }, >, )
			poped := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if charSetPair[poped] != char {
				l.stack = stack
				return LineStatusCorrupted
			}
		}

		l.cursor += 1
	}
	l.stack = stack
	return LineStatusInComplete
}

func (l *Line) Score() int {
	score := 0
	length := len(l.stack)

	for i := length - 1; i >= 0; i-- {
		leftChar := l.stack[i]
		point := charPoint[charSetPair[leftChar]]
		score = score*5 + point
	}

	return score
}

func main() {
	filename := os.Args[1]
	lines := parseInput(filename)

	scores := make([]int, 0)
	for _, line := range lines {
		lineStatus := line.CheckStatus()
		if lineStatus == LineStatusInComplete {
			scores = append(scores, line.Score())
		}
	}

	// sort and find mid score
	sort.Slice(scores, func(i, j int) bool {
		return scores[i] < scores[j]
	})
	fmt.Println(scores[len(scores)/2])
}
