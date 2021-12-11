package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Command struct {
	direction string
	value int
}

func parseInput(filename string) chan Command {
	commandChan := make(chan Command)
	go func() {
		file, err := os.Open(filename)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			commandStr := scanner.Text()
			commandSplit := strings.Split(commandStr, " ")

			direction := commandSplit[0]
			value, err := strconv.Atoi(commandSplit[1])
			if err != nil {
				log.Fatal(err)
			}
			commandChan <- Command{direction: direction, value: value}
		}
		close(commandChan)
	}()
	
	return commandChan
}

func main() {
	filename := os.Args[1]

	position := 0
	depth := 0

	for command := range parseInput(filename) {
		if command.direction == "forward" {
			position += command.value
		} else if command.direction == "down" {
			depth += command.value
		} else if command.direction == "up" {
			depth -= command.value
		}
	}

	fmt.Printf("current position: %d, depth: %d\n", position, depth)
	fmt.Printf("result: %d\n", position * depth)
}
