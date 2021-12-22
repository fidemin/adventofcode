package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func parseInput(filename string) chan string {
	stringChan := make(chan string)
	go func() {
		file, err := os.Open(filename)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			bitString := scanner.Text()
			stringChan <- bitString
		}
		close(stringChan)
	}()

	return stringChan
}

func findCommon(isMostCommon bool, bitsArr []string, pos int) []string {
	if len(bitsArr) == 1 {
		return bitsArr
	}
	var arrFor0bit []string
	var arrFor1bit []string

	for _, bits := range bitsArr {
		if bits[pos] == 49 {
			arrFor1bit = append(arrFor1bit, bits)
		} else {
			arrFor0bit = append(arrFor0bit, bits)
		}
	}

	nextPos := pos + 1

	if isMostCommon {
		if len(arrFor1bit) >= len(arrFor0bit) {
			return findCommon(isMostCommon, arrFor1bit, nextPos)
		} else {
			return findCommon(isMostCommon, arrFor0bit, nextPos)
		}
	} else {
		if len(arrFor1bit) >= len(arrFor0bit) {
			return findCommon(isMostCommon, arrFor0bit, nextPos)
		} else {
			return findCommon(isMostCommon, arrFor1bit, nextPos)
		}
	}
}

func main() {
	filename := os.Args[1]

	var arr []string
	for bits := range parseInput(filename) {
		arr = append(arr, bits)
	}
	mostCommonBits := findCommon(true, arr, 0)[0]
	leastCommonBits := findCommon(false, arr, 0)[0]

	oxyGenRate, _ := strconv.ParseInt(mostCommonBits, 2, 64)
	co2ScrRate, _ := strconv.ParseInt(leastCommonBits, 2, 64)
	fmt.Println(oxyGenRate * co2ScrRate)
}
