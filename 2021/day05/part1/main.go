package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Diagram struct {
	horizontalLines   map[int][]Line
	verticalLines     map[int][]Line
	horizontalOveraps map[int][][2]int
	verticalOveraps   map[int][][2]int
	crossOveraps      [][2]int
}

type Line struct {
	x1, y1, x2, y2 int
	isHorizontal   bool
	sameValue      int
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

		isHorizontal := false
		sameValue := x1

		if y1 == y2 {
			isHorizontal = true
			sameValue = y1
			// make x1 smaller value
			if x1 > x2 {
				temp := x2
				x2 = x1
				x1 = temp
			}
		} else {
			// make y1 smaller value
			if y1 > y2 {
				temp := y2
				y2 = y1
				y1 = temp
			}

		}

		line := Line{
			x1:           x1,
			y1:           y1,
			x2:           x2,
			y2:           y2,
			isHorizontal: isHorizontal,
			sameValue:    sameValue,
		}
		lines = append(lines, line)
	}
	return lines
}

func findOverlaps(linesMap map[int][]Line) map[int][][2]int {
	overlapsMap := make(map[int][][2]int)

	for sameValue, horizontalLines := range linesMap {
		fmt.Println(sameValue)
		length := len(horizontalLines)
		if length <= 1 {
			continue
		}
		for i := 0; i < length-1; i++ {
			thisLine := horizontalLines[i]
			for j := i + 1; j < length; j++ {
				thatLine := horizontalLines[j]
				if thisLine.isHorizontal {
					// y value is same
					firstLine := thisLine
					secondLine := thatLine

					if thisLine.x1 > thatLine.x1 {
						firstLine = thatLine
						secondLine = thisLine
					}

					if secondLine.x1 > firstLine.x2 {
						// no overap
						continue
					} else {
						overapX1 := Max(firstLine.x1, secondLine.x1)
						overapX2 := Min(firstLine.x2, secondLine.x2)
						overlapsMap[sameValue] = append(overlapsMap[sameValue], [2]int{overapX1, overapX2})
					}

				} else {
					// x value is same
					firstLine := thisLine
					secondLine := thatLine

					if thisLine.y1 > thatLine.y1 {
						firstLine = thatLine
						secondLine = thisLine
					}

					if secondLine.y1 > firstLine.y2 {
						// no overap
						continue
					} else {
						overapY1 := Max(firstLine.y1, secondLine.y1)
						overapY2 := Min(firstLine.y2, secondLine.y2)
						overlapsMap[sameValue] = append(overlapsMap[sameValue], [2]int{overapY1, overapY2})
					}
				}
			}
		}
	}
	return overlapsMap
}

func main() {
	filename := os.Args[1]
	lines := parseInput(filename)
	fmt.Println(lines)

	diagram := Diagram{
		horizontalLines:   make(map[int][]Line),
		verticalLines:     make(map[int][]Line),
		horizontalOveraps: make(map[int][][2]int),
		verticalOveraps:   make(map[int][][2]int),
		crossOveraps:      make([][2]int, 0),
	}

	for _, line := range lines {
		if line.isHorizontal {
			diagram.horizontalLines[line.sameValue] = append(diagram.horizontalLines[line.sameValue], line)
		} else {
			diagram.verticalLines[line.sameValue] = append(diagram.verticalLines[line.sameValue], line)
		}
	}
	diagram.horizontalOveraps = findOverlaps(diagram.horizontalLines)
	diagram.verticalOveraps = findOverlaps(diagram.verticalLines)

	fmt.Println(diagram)
}
