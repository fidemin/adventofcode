package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Diagram [1000][1000]int

func (d *Diagram) drawLine(line Line) {
	p1 := line.p1
	p2 := line.p2

	if p1[0] == p2[0] {
		x := p1[0]
		//vertical
		max := Max(p1[1], p2[1])
		min := Min(p1[1], p2[1])

		for ; max >= min; min++ {
			d[min][x] += 1
		}
	} else {
		// horizontal
		x := p1[1]
		//vertical
		max := Max(p1[0], p2[0])
		min := Min(p1[0], p2[0])

		for ; max >= min; min++ {
			d[x][min] += 1
		}
	}
}

type Line struct {
	p1 [2]int
	p2 [2]int
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func parseInput(filename string) []Line {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	lines := make([]Line, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		// e.g. lineStr := "313,561 -> 121,753"
		lineStr := scanner.Text()

		xyStrList := strings.Split(lineStr, " -> ")

		x1y1StrList := strings.Split(xyStrList[0], ",")
		x2y2StrList := strings.Split(xyStrList[1], ",")

		x1, _ := strconv.Atoi(x1y1StrList[0])
		y1, _ := strconv.Atoi(x1y1StrList[1])
		x2, _ := strconv.Atoi(x2y2StrList[0])
		y2, _ := strconv.Atoi(x2y2StrList[1])

		// only horizontal or vertical line is valid
		if !((x1 == x2) || (y1 == y2)) {
			continue
		}

		p1 := [2]int{x1, y1}
		p2 := [2]int{x2, y2}

		line := Line{
			p1: p1,
			p2: p2,
		}
		lines = append(lines, line)
	}
	return lines
}

func main() {
	filename := os.Args[1]
	diagram := Diagram{}
	lines := parseInput(filename)
	for _, line := range lines {
		diagram.drawLine(line)
	}

	count := 0
	for _, row := range diagram {
		for _, value := range row {
			if value > 1 {
				count += 1
			}

		}
	}
	fmt.Println(count)
}
