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

type ThreeMaxInts [3]int

func (ints *ThreeMaxInts) Insert(num int) {
	minValue := math.MaxInt
	minLoc := -1
	for i, v := range *ints {
		if v < minValue {
			minLoc = i
			minValue = v
		}
	}

	if num > minValue {
		ints[minLoc] = num
	}
}

var usedPointMat [100][100]bool

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

type Point struct {
	x int
	y int
}

func findLowPoints(mat [][]int) []Point {
	rowLen := len(mat)
	columnLen := len(mat[0])

	lowPoints := make([]Point, 0)

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

			p := Point{j, i}

			// value is the row point
			lowPoints = append(lowPoints, p)
		}
	}

	return lowPoints
}

func basinSizeAtPoint(mat *[][]int, point Point) int {
	if usedPointMat[point.y][point.x] {
		return 0
	}

	x := point.x
	y := point.y
	rowLen := len(*mat)
	columnLen := len((*mat)[0])

	// check point as used
	usedPointMat[y][x] = true

	val := (*mat)[y][x]

	if val == 9 {
		return 0
	}

	sum := 1

	if point.y > 0 {
		sum += basinSizeAtPoint(mat, Point{point.x, point.y - 1})
	}

	if point.x < columnLen-1 {
		sum += basinSizeAtPoint(mat, Point{point.x + 1, point.y})
	}

	if point.y < rowLen-1 {
		sum += basinSizeAtPoint(mat, Point{point.x, point.y + 1})
	}

	if point.x > 0 {
		sum += basinSizeAtPoint(mat, Point{point.x - 1, point.y})
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
	//fmt.Println(lowPoints)

	topThree := ThreeMaxInts{}
	for _, point := range lowPoints {
		size := basinSizeAtPoint(&mat, point)
		topThree.Insert(size)
	}

	fmt.Println(topThree)
	fmt.Println(topThree[0] * topThree[1] * topThree[2])
}
