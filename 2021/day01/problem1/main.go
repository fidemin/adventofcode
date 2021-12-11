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

	previousDepth := math.MaxInt
	increased := 0

	for depth := range depths(filename) {
		if previousDepth < depth {
			increased += 1
		}
		previousDepth = depth
	}

	fmt.Printf("result: %d\n", increased)
}
