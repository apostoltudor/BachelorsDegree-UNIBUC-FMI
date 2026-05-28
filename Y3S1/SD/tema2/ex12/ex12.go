package main

import (
	"fmt"
	"strings"
	"sync"
)

// def date
type InputData [][]string

// mapWorker proceseaza o singura lista de cai
func mapWorker(paths []string, results chan<- int, wg *sync.WaitGroup) { //mecanismul prin care se sincron gorroutine
	defer wg.Done() //se asigura ca se termina gorotuinele

	count := 0
	for _, path := range paths {
		if strings.HasPrefix(path, "/") {
			count++
		}
	}
	results <- count
}

func reduce(results <-chan int, totalLists int) float64 {
	totalMatches := 0

	//trecem prin canal pana cand e golit si inchis
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
		{"/dev/null", "/bin", "saar", "teme/scoala/2020", ""},
		{"proiect/tema", "/dev", "ddanube", "jahfjksgfjhs", "ajsdas", "urs"},
		{"scoica", "/teme/repos/git", "arac", "karnak"},
	}

	fmt.Println("Ex 12")

	results := make(chan int, len(input))

	var wg sync.WaitGroup

	for _, list := range input {
		wg.Add(1) //adauga muncitori, goroutines pt cati sunt
		go mapWorker(list, results, &wg)
	}

	go func() { //ruleaza in paralel si verifica sa inchida canalul ca sa se opreasca bucla
		wg.Wait()
		close(results)
	}()

	average := reduce(results, len(input))

	fmt.Printf("Media: %.2f\n", average)
}
