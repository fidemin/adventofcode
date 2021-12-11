package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

func depths(filename string) <-chan int {
	depthChannel := make(chan int)
	go func() {
		file, err := os.Open(filename)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)

		for scanner.Scan() {
			depthStr := scanner.Text()
			depth, err := strconv.Atoi(depthStr)
			if err != nil {
				log.Fatal(err)
			}
			depthChannel <- depth
		}
		defer close(depthChannel)
	}()
	return depthChannel
}

func main() {
	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// window length
	const length = 3

	// initialize with math.MaxInt
	depthsStore := [length]int{}
	for i := range depthsStore {
		depthsStore[i] = math.MaxInt
	}

	counter := 0
	increased := 0

	for depth := range depths(filename) {
		position := counter  % length
		if depthsStore[position] < depth {
			increased += 1
		}
		depthsStore[position] = depth
		counter += 1
	}

	fmt.Printf("result: %d\n", increased)
}
