package main

import (
	"bufio"
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

type Point struct {
	x int
	y int
}

type Stack struct {
	stack []Point
}

func NewStack() *Stack {
	stack := &Stack{}
	stack.stack = make([]Point, 0)

	return stack
}

func (s *Stack) Push(value Point) {
	s.stack = append(s.stack, value)
}

func (s *Stack) Pop() Point {
	point := s.stack[len(s.stack)-1]
	s.stack = s.stack[:len(s.stack)-1]
	return point
}

func (s *Stack) Len() int {
	return len(s.stack)
}

type OctopusMatrix struct {
	matrix [][]int
	rowLen int
	colLen int
}

func NewOctopusMatrix(matrix [][]int) *OctopusMatrix {
	rowLen := len(matrix)
	colLen := len(matrix[0])
	return &OctopusMatrix{
		matrix: matrix,
		rowLen: rowLen,
		colLen: colLen,
	}
}

func (m *OctopusMatrix) Step() {
	flashPoints := NewStack()
	for y, row := range m.matrix {
		for x, value := range row {
			if value < 9 {
				value += 1
			}

			if value == 9 {
				flashPoints.Push(Point{x, y})
			}

			m.matrix[y][x] = value
		}
	}

	for flashPoints.Len() > 0 {
		point := flashPoints.Pop()

	}

}

func main() {
	filename := os.Args[1]
	matrix := parseInput(filename)
	octopuxMatrix := NewOctopusMatrix(matrix)
}
