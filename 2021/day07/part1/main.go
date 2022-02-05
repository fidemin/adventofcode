package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
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

func parseInput(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	intList := make([]int, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		str := scanner.Text()
		if strings.Trim(str, " ") == "" {
			continue
		}

		strList := strings.Split(str, ",")
		for _, str := range strList {
			i, _ := strconv.Atoi(str)
			intList = append(intList, i)
		}
	}
	return intList
}

type PositionFinder struct {
	counts map[int]int
	maxPos int
	minPos int
}

func NewPositionFinder(positions []int) *PositionFinder {
	f := &PositionFinder{}
	f.counts = make(map[int]int)
	f.maxPos = 0
	f.minPos = math.MaxInt

	for _, pos := range positions {
		f.counts[pos] += 1
		f.maxPos = max(f.maxPos, pos)
		f.minPos = min(f.minPos, pos)
	}
	return f
}

func (f *PositionFinder) Find() (int, int) {
	minFuel := math.MaxInt
	pos := 0
	for target := f.minPos; target <= f.maxPos; target++ {
		fuel := f.fuel(target)
		if minFuel > fuel {
			pos = target
			minFuel = fuel
		}
	}

	return pos, minFuel
}

func (f *PositionFinder) fuel(target int) int {
	fuel := 0
	for pos, count := range f.counts {
		if target == pos {
			continue
		} else if target > pos {
			fuel += (target - pos) * count
		} else {
			fuel += (pos - target) * count
		}
	}
	return fuel
}

func main() {
	filename := os.Args[1]
	positions := parseInput(filename)
	finder := NewPositionFinder(positions)
	pos, minFuel := finder.Find()
	fmt.Printf("pos: %d, min fuel: %d\n", pos, minFuel)
}
