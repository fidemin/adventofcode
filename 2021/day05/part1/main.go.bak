package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Diagram struct {
	horizontalLines   map[int][]Line
	verticalLines     map[int][]Line
	horizontalOveraps map[int][][2]int
	verticalOveraps   map[int][][2]int
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

// find intersect of two lines (x1, x2), (x3, x4)
func intersectTwoLines(line1 [2]int, line2 [2]int) ([]int, bool) {
	sort.Ints(line1[:])
	sort.Ints(line2[:])

	firstLine := line1
	secondLine := line2

	if line1[0] > line2[0] {
		firstLine = line2
		secondLine = line1
	}

	if secondLine[0] > firstLine[1] {
		// no intersect
		return make([]int, 0), false
	} else {
		result := make([]int, 2)
		result[0] = Max(firstLine[0], secondLine[0])
		result[1] = Min(firstLine[1], secondLine[1])
		return result, true
	}
}

func findCrossPoint(line1 Line, line2 Line) ([]int, bool) {
	hLine := line1
	vLine := line2

	if !line1.isHorizontal {
		vLine = line1
		hLine = line2
	}

	if !(hLine.x1 <= vLine.x1 && hLine.x2 >= vLine.x1 && vLine.y1 <= hLine.y1 && vLine.y2 >= hLine.y2) {
		return make([]int, 0), false
	}

	result := make([]int, 2)
	result[0] = vLine.x1
	result[1] = hLine.y1
	return result, true
}

func findOverlaps(linesMap map[int][]Line) map[int][][2]int {
	overlapsMap := make(map[int][][2]int)

	for sameValue, lines := range linesMap {
		length := len(lines)
		if length <= 1 {
			continue
		}
		for i := 0; i < length-1; i++ {
			thisLine := lines[i]
			for j := i + 1; j < length; j++ {
				thatLine := lines[j]
				overlapLine := make([]int, 0)
				overlapped := false
				if thisLine.isHorizontal {
					overlapLine, overlapped = intersectTwoLines([2]int{thisLine.x1, thisLine.x2}, [2]int{thatLine.x1, thatLine.x2})
				} else {
					overlapLine, overlapped = intersectTwoLines([2]int{thisLine.y1, thisLine.y2}, [2]int{thatLine.y1, thatLine.x2})
				}

				if !overlapped {
					continue
				}
				overlapsMap[sameValue] = append(overlapsMap[sameValue], [2]int{overlapLine[0], overlapLine[1]})
			}
		}
	}
	return overlapsMap
}

func main() {
	filename := os.Args[1]
	lines := parseInput(filename)

	diagram := Diagram{
		horizontalLines:   make(map[int][]Line),
		verticalLines:     make(map[int][]Line),
		horizontalOveraps: make(map[int][][2]int),
		verticalOveraps:   make(map[int][][2]int),
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

	for _, hLines := range diagram.horizontalLines {
		for _, hLine := range hLines {
			for _, vLines := range diagram.verticalLines {
				for _, vLine := range vLines {
					point, crossed := findCrossPoint(hLine, vLine)
					if !crossed {
						continue
					}
					// adds horizontal overlaps (whatever!)
					diagram.horizontalOveraps[point[1]] = append(diagram.horizontalOveraps[point[1]], [2]int{point[0], point[0]})
					fmt.Println(point)
				}
			}
		}
	}

	fmt.Println(diagram)
}
