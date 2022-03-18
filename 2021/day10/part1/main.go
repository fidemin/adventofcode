package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type LineStatus string

const (
	LineStatusCorrupted  LineStatus = "Corrupted"
	LineStatusInComplete LineStatus = "InComplete"
)

type Line struct {
	str    string
	len    int
	cursor int
}

var charSetPair map[uint8]uint8 = map[uint8]uint8{
	'[': ']',
	'{': '}',
	'<': '>',
	'(': ')',
}

var charPoint map[uint8]int = map[uint8]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

func NewLine(str string) *Line {
	return &Line{
		str: str,
		len: len(str),
	}
}

func (l *Line) FindStatus() LineStatus {
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
				return LineStatusCorrupted
			}
		}

		l.cursor += 1
	}
	return LineStatusInComplete
}

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

func (l *Line) CharPoint() int {
	return charPoint[l.str[l.cursor]]
}

func main() {
	filename := os.Args[1]
	lines := parseInput(filename)

	sum := 0
	for _, line := range lines {
		lineStatus := line.FindStatus()
		if lineStatus == LineStatusCorrupted {
			sum += line.CharPoint()
		}
	}

	fmt.Println(sum)
}
