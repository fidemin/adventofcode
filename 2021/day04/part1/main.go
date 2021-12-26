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

type Game struct {
	Boards         [][5][5]int
	NumToPositions map[int][][3]int
}

func (g Game) CheckRowAndColMarkedAtPos(pos [3]int) bool {
	board := g.Boards[pos[0]]
	// check all row values are marked
	rowMarked := 0
	for _, num := range board[pos[1]] {
		if num == math.MaxInt {
			rowMarked += 1
		}
	}
	if rowMarked == 5 {
		return true
	}

	// check all column values are marked
	colMarked := 0
	for i := 0; i < 5; i++ {
		if board[i][pos[2]] == math.MaxInt {
			colMarked += 0
		}
	}
	if colMarked == 5 {
		return true
	}
	return false
}

func parseInput(filename string) ([]int, Game) {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	drawnString := scanner.Text()
	numStrings := strings.Split(drawnString, ",")
	drawnNumbers := make([]int, len(numStrings))

	for i, numberString := range numStrings {
		drawnNumbers[i], _ = strconv.Atoi(numberString)
	}

	// skip blank
	scanner.Scan()

	// initialize game
	boardPos := 0
	rowPos := 0
	boards := Game{}
	boards.NumToPositions = make(map[int][][3]int)
	board := [5][5]int{}

	for scanner.Scan() {
		thisLine := scanner.Text()
		if thisLine != "" {
			numberStrings := strings.Split(thisLine, " ")
			colPos := 0
			for _, numberString := range numberStrings {
				if numberString != "" {
					num, _ := strconv.Atoi(numberString)

					if _, exists := boards.NumToPositions[num]; !exists {
						boards.NumToPositions[num] = make([][3]int, 0)
					}

					pos := [3]int{boardPos, rowPos, colPos}
					boards.NumToPositions[num] = append(boards.NumToPositions[num], pos)
					board[rowPos][colPos] = num
					colPos += 1
				}
			}
			rowPos += 1
		} else {
			// next line starts new board
			boardPos += 1
			// append board to boards
			boards.Boards = append(boards.Boards, board)
			// initialize new board
			board = [5][5]int{}
			rowPos = 0
		}
	}
	// append board to boards
	boards.Boards = append(boards.Boards, board)
	return drawnNumbers, boards
}

func main() {
	filename := os.Args[1]
	drawnNumbers, game := parseInput(filename)

	finalPos := [3]int{}
	finalNum := 0

Outer:
	for _, num := range drawnNumbers {
		positions := game.NumToPositions[num]

		for _, pos := range positions {
			game.Boards[pos[0]][pos[1]][pos[2]] = math.MaxInt
			if game.CheckRowAndColMarkedAtPos(pos) {
				finalPos = pos
				finalNum = num
				break Outer
			}
		}
	}
	fmt.Println("pos:", finalPos)
	fmt.Println("num:", finalNum)
	sum := 0
	board := game.Boards[finalPos[0]]
	for i := range board {
		for _, num := range board[i] {
			if num != math.MaxInt {
				sum += num
			}
		}
	}
	fmt.Println("sum:", sum)
	fmt.Println("result:", finalNum*sum)
}
