package main

import (
	"bufio"
	"fmt"
	"log"
	"math/bits"
	"os"
	"strings"
)

var charIntToBitsInt = map[int32]int{
	97:  1 << 6, // a
	98:  1 << 5, // b
	99:  1 << 4, // c
	100: 1 << 3, // d
	101: 1 << 2, // e
	102: 1 << 1, // f
	103: 1,      // g
}

func strToBitInt(str string) int {
	// abcdefg -> 1111111
	// abc -> 1110000
	// ba -> 1100000

	result := 0
	for _, charInt := range str {
		result += charIntToBitsInt[charInt]
	}
	return result
}

type Entry struct {
	bitIntPatterns  []int
	bitIntDigits    []int
	lengthToBitInts map[int][]int
	bitIntToInt     map[int]int
}

func NewEntry(strPatterns []string, strDigits []string) *Entry {
	entry := new(Entry)

	bitIntPatterns := make([]int, 0)
	bitIntDigits := make([]int, 0)
	lengthToBitInts := make(map[int][]int)

	for _, pattern := range strPatterns {
		bitInt := strToBitInt(pattern)
		bitIntPatterns = append(bitIntPatterns, bitInt)
		length := len(pattern)
		lengthToBitInts[length] = append(lengthToBitInts[length], bitInt)
	}

	for _, digit := range strDigits {
		bitInt := strToBitInt(digit)
		bitIntDigits = append(bitIntDigits, bitInt)
	}

	entry.bitIntPatterns = bitIntPatterns
	entry.bitIntDigits = bitIntDigits
	entry.lengthToBitInts = lengthToBitInts
	entry.bitIntToInt = make(map[int]int)
	return entry
}

func (e *Entry) Decode() {
	// unique numbers: 1, 4, 7, 8
	oneBitInt := e.lengthToBitInts[2][0]
	fourBitInt := e.lengthToBitInts[4][0]
	sevenBitInt := e.lengthToBitInts[3][0]
	eightBitInt := e.lengthToBitInts[7][0]

	e.bitIntToInt[oneBitInt] = 1
	e.bitIntToInt[fourBitInt] = 4
	e.bitIntToInt[sevenBitInt] = 7
	e.bitIntToInt[eightBitInt] = 8

	// 6 length numbers: 0, 6, 9
	nineBitInt := 0
	zeroBitInt := 0
	sixBitInt := 0

	sixLengthBitInts := e.lengthToBitInts[6]
	for _, bitInt := range sixLengthBitInts {
		if bits.OnesCount(uint(bitInt&oneBitInt)) == 1 {
			sixBitInt = bitInt
		} else {
			// 0 or 9
			if bits.OnesCount(uint(bitInt&fourBitInt)) == 4 {
				nineBitInt = bitInt
			} else {
				zeroBitInt = bitInt
			}
		}
	}

	e.bitIntToInt[nineBitInt] = 9
	e.bitIntToInt[zeroBitInt] = 0
	e.bitIntToInt[sixBitInt] = 6

	// 5 length numbers: 2, 3, 5
	cc := oneBitInt ^ (oneBitInt & sixBitInt)
	fiveBitInt := cc ^ nineBitInt
	threeBitInt := 0
	twoBitInt := 0

	fiveLengthBitInts := e.lengthToBitInts[5]
	for _, bitInt := range fiveLengthBitInts {
		if fiveBitInt == bitInt {
			continue
		} else if bits.OnesCount(uint(bitInt&oneBitInt)) == 2 {
			threeBitInt = bitInt
		} else {
			twoBitInt = bitInt
		}
	}

	e.bitIntToInt[fiveBitInt] = 5
	e.bitIntToInt[threeBitInt] = 3
	e.bitIntToInt[twoBitInt] = 2
	//fmt.Println(zeroBitInt, oneBitInt, twoBitInt, threeBitInt, fourBitInt, fiveBitInt, sixBitInt, sevenBitInt, eightBitInt, nineBitInt)
}

func (e *Entry) OutputValue() int {
	result := 0
	multiplier := 1

	for i := len(e.bitIntDigits) - 1; i >= 0; i-- {
		realInt := e.bitIntToInt[e.bitIntDigits[i]]
		//fmt.Println(e.bitIntDigits[i], realInt)
		result += realInt * multiplier
		multiplier *= 10
	}

	return result
}

func parseInput(filename string) []*Entry {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	entries := make([]*Entry, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		str := scanner.Text()
		initSplits := strings.Split(str, " | ")
		patterns := strings.Split(initSplits[0], " ")
		fourDigits := strings.Split(initSplits[1], " ")

		entries = append(entries, NewEntry(patterns, fourDigits))
	}
	return entries
}

func main() {
	filename := os.Args[1]
	entries := parseInput(filename)
	totalCount := 0
	for _, entry := range entries {
		entry.Decode()
		totalCount += entry.OutputValue()
	}
	fmt.Println(totalCount)
}
