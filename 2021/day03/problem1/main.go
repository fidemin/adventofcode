package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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

func main() {
	filename := os.Args[1]

	bitChan := parseInput(filename)
	firstBitString := <-bitChan
	bitLength := len(firstBitString)
	count := 1

	var bitCounter = make([]int, bitLength)

	for i, bit := range firstBitString {
		if bit == 49 {
			bitCounter[i] += 1
		}
	}
	fmt.Println(bitCounter)

	for bitString := range bitChan {
		count += 1
		for i, bit := range bitString {
			if bit == 49 {
				bitCounter[i] += 1
			}
		}
	}
	fmt.Println(bitCounter)

	halfCount := count / 2
	currentBase := 1
	gammaRate := 0
	epsilonRate := 0

	for i := range bitCounter {
		reverseI := bitLength - i - 1
		currentCounter := bitCounter[reverseI]
		if currentCounter == halfCount {
			panic(fmt.Sprintf("currentCount == halfCount for %d th", reverseI))
		}
		if currentCounter > halfCount {
			gammaRate += currentBase
		} else {
			epsilonRate += currentBase
		}

		currentBase *= 2
	}
	fmt.Println(gammaRate)
	fmt.Println(epsilonRate)
	fmt.Println(fmt.Sprintf("result: %d", gammaRate*epsilonRate))

}
