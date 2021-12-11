package main

import (
	"bufio"
	"fmt"
	"log"
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

	scanner := bufio.NewScanner(file)

	previousDepth := 123456789
	increased := 0
	for scanner.Scan() {
		depthStr := scanner.Text()
		depth, err := strconv.Atoi(depthStr)
		if err != nil {
			log.Fatal(err)
		}

		if previousDepth < depth {
			increased += 1
		}
		previousDepth = depth
	}

	fmt.Printf("result: %d\n", increased)
}
