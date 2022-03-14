package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func parseInput(filename string) [][]int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	matrix := make([][]int, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		str := scanner.Text()
		row := make([]int, 0)
		splits := strings.Split(str, "")
		for _, strInt := range splits {
			integer, _ := strconv.Atoi(strInt)
			row = append(row, integer)
		}
		matrix = append(matrix, row)
	}
	return matrix
}

func findLowPoints(mat [][]int) []int {
	rowLen := len(mat)
	columnLen := len(mat[0])

	lowPoints := make([]int, 0)

	for i, row := range mat {
		for j, value := range row {
			if i > 0 {
				top := mat[i-1][j]
				if value >= top {
					continue
				}
			}

			if j < columnLen-1 {
				right := mat[i][j+1]
				if value >= right {
					continue
				}
			}

			if i < rowLen-1 {
				bottom := mat[i+1][j]
				if value >= bottom {
					continue
				}
			}

			if j > 0 {
				left := mat[i][j-1]
				if value >= left {
					continue
				}
			}

			// value is the row point
			lowPoints = append(lowPoints, value)
		}
	}

	return lowPoints
}

func sumOfRiskLevels(lowPoints []int) int {
	sum := 0

	for _, point := range lowPoints {
		sum += point + 1
	}

	return sum
}

func main() {
	filename := os.Args[1]
	mat := parseInput(filename)
	//for _, row := range mat {
	//	fmt.Println(row)
	//}

	lowPoints := findLowPoints(mat)
	fmt.Println(lowPoints)

	fmt.Println(sumOfRiskLevels(lowPoints))
}
