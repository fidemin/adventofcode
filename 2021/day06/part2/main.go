package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func parseInput(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	intList := make([]int, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		strList := strings.Split(scanner.Text(), ",")
		for _, str := range strList {
			i, _ := strconv.Atoi(str)
			intList = append(intList, i)
		}
	}
	return intList
}

var cache = make(map[int64]int64)

func populationForLanternFishWithTimer8(leftdays int64) int64 {
	originalLeft := leftdays
	result, ok := cache[leftdays]
	if ok {
		return result
	}
	// maek timer to 6 by adjusting leftdays
	leftdays -= 2
	result = int64(1)
	for leftdays > 6 {
		// repeated by 7 days: 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> 6(created)
		leftdays -= 7
		// deal with newly created lantern fish (timer is 8)
		result += populationForLanternFishWithTimer8(leftdays)
	}
	cache[originalLeft] = result
	return result
}

func main() {
	// If initial timer is 8 which is same as newly created lanternfish's timer.
	// the population of all lanternfishes has exact same pattern.
	// Therefore, we can use dynamic programmin

	days := 256
	filename := os.Args[1]
	initList := parseInput(filename)

	// make cache from 0 to days + 8
	// +8 is for that initial value of timer is 0
	fullDays := days + 8
	for i := 0; i <= fullDays; i++ {
		populationForLanternFishWithTimer8(int64(i))
	}

	var total int64 = 0

	// initList has initial timers of lantern fishes.
	// because population of one lanternfish is independent to the population of other lanternfish,
	// we can calculate seperately and sum later.
	for _, timer := range initList {
		// make initial value of timer to 8 by adjusting initial days
		// result is same for (initial timer:3, given days: 6) vs (initial timer is 8, given days: 11)
		daysFor8 := days + (8 - timer)
		total += populationForLanternFishWithTimer8(int64(daysFor8))
	}
	fmt.Println(total)
}
