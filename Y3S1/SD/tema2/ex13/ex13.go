package main

import (
	"fmt"
	"strings"
	"sync"
)

type InputData [][]string

func mapWorker(names []string, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()

	count := 0
	for _, name := range names {
		if strings.HasSuffix(name, "escu") {
			count++
		}
	}
	results <- count
}

func reduce(results <-chan int, totalLists int) float64 {
	totalMatches := 0
	for partialCount := range results {
		totalMatches += partialCount
	}

	if totalLists == 0 {
		return 0.0
	}
	return float64(totalMatches) / float64(totalLists)
}

func main() {
	input := InputData{
		{"Popescu", "Ionescu", "Pop", "aaastrfb", ""},
		{"Nicolae", "Dumitrescu", "ddanube", "jahfjksgfjhs", "ajsdas", "urs"},
		{"Dumitru", "Angelescu", "arac", "karnak"},
	}

	fmt.Println("Ex 13")

	results := make(chan int, len(input))
	var wg sync.WaitGroup

	for _, list := range input {
		wg.Add(1)
		go mapWorker(list, results, &wg)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	average := reduce(results, len(input))

	fmt.Printf("Rezultat final: %.2f\n", average)
}
