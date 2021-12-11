package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)


func main() {
	filename := os.Args[1]
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	const length = 3
	depths := [length]int{}
	// initialize with math.MaxInt
	for i := range depths {
		depths[i] = math.MaxInt
	}
	counter := 0
	increased := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		depthStr := scanner.Text()
		depth, err := strconv.Atoi(depthStr)
		if err != nil {
			log.Fatal(err)
		}

		position := counter  % length
		if depths[position] < depth {
			increased += 1
		}
		depths[position] = depth
		counter += 1
	}

	fmt.Printf("result: %d\n", increased)
}
