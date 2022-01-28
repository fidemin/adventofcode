package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type LanternFishSchool struct {
	school []int
}

func NewLanternFishSchool(initSchool []int) *LanternFishSchool {
	return &LanternFishSchool{
		school: initSchool,
	}
}

func (s *LanternFishSchool) PassOneDay() {
	for i := range s.school {
		if s.school[i] == 0 {
			s.school = append(s.school, 8)
			s.school[i] = 6
		} else {
			s.school[i] -= 1
		}
	}
}

func (s *LanternFishSchool) NumOfFishes() int {
	return len(s.school)
}

func (s *LanternFishSchool) String() string {
	return fmt.Sprintf("%v", s.school)
}

func parseInput(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	intList := make([]int, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		strList := strings.Split(scanner.Text(), ",")
		for _, str := range strList {
			i, _ := strconv.Atoi(str)
			intList = append(intList, i)
		}
	}
	return intList
}

func main() {
	days := 80
	filename := os.Args[1]
	initList := parseInput(filename)
	s := NewLanternFishSchool(initList)
	//fmt.Println(s)

	for i := 0; i < days; i++ {
		s.PassOneDay()
		//fmt.Println(s)
	}

	fmt.Println(s.NumOfFishes())
}
