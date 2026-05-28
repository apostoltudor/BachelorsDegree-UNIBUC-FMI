package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"strings"
)

func cerinta1(words []string, index int) string {
	result := ""

	for _, w := range words {
		if index < len(w) {
			result += string(w[index])
		} else {
			result += "?"
		}
	}

	return result
}

func cerinta3(values []int) (int, []int) {

	reversedValues := make([]int, len(values))
	totalSum := 0

	for i, v := range values {
		rev := 0
		x := v

		for x > 0 {
			rev = rev*10 + x%10
			x /= 10
		}

		reversedValues[i] = rev
		totalSum += rev
	}

	return totalSum, reversedValues
}

func sumOfDigits(n int) int {
	if n < 0 {
		n = -n
	}
	sum := 0
	for n > 0 {
		sum += n % 10
		n /= 10
	}
	return sum
}

func cerinta4(input []int) (float64, []int) {
	if len(input) < 3 {
		return 0.0, nil
	}

	a := input[0]
	b := input[1]
	numbers := input[2:]

	var validNumbers []int
	sumTotal := 0

	for _, num := range numbers {
		s := sumOfDigits(num)
		if s >= a && s <= b {
			validNumbers = append(validNumbers, num)
			sumTotal += num
		}
	}

	if len(validNumbers) == 0 {
		return 0.0, validNumbers
	}

	media := float64(sumTotal) / float64(len(validNumbers))
	return media, validNumbers
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func countDigits(n int) int {
	if n == 0 {
		return 1
	}
	count := 0
	for n > 0 {
		n /= 10
		count++
	}
	return count
}

func cerinta8(input []int) (int, []int) {
	totalDigits := 0
	var primeNumbers []int

	for _, num := range input {
		if isPrime(num) {
			digits := countDigits(num)
			totalDigits += digits
			primeNumbers = append(primeNumbers, num)
		}
	}
	return totalDigits, primeNumbers
}

func cerinta12(input []int) int {
	totalSum := 0

	for _, num := range input {
		s := fmt.Sprintf("%d", num)

		if len(s) > 0 {
			newS := string(s[0]) + s

			var val int
			fmt.Sscanf(newS, "%d", &val)

			totalSum += val
		}
	}
	return totalSum
}

func handleConn(conn net.Conn) { //aici suntem pe microthread-ul fiecarui client
	defer conn.Close() //amana pana la sf func; ne asiguram ca se inchide gorutina, cum era ls SO

	remote := conn.RemoteAddr().String() //adr remote client
	log.Printf("Conexiune deschisa de la %s", remote)

	reader := bufio.NewScanner(conn)

	if !reader.Scan() {
		log.Printf("[%s] eroare: nu pot citi numele clientului", remote)
		return
	}
	clientName := reader.Text()
	log.Printf("[%s] Nume client: %s", remote, clientName)

	if !reader.Scan() {
		log.Printf("[%s] eroare: nu pot citi cerinta", remote)
		return
	}
	cerintaLine := reader.Text()

	var cerinta int
	fmt.Sscanf(cerintaLine, "%d", &cerinta) //decimal integer
	log.Printf("[%s] Cerinta primita: %d", remote, cerinta)

	if cerinta == 1 {

		if !reader.Scan() {
			conn.Write([]byte("Eroare: nu pot citi indexul i\n"))
			return
		}
		indexLine := reader.Text()
		var index int //lfl ca mai sus din string in int
		fmt.Sscanf(indexLine, "%d", &index)
		log.Printf("[%s] Index i = %d", remote, index)

		if !reader.Scan() {
			conn.Write([]byte("Eroare: nu pot citi stringurile\n"))
			return
		}
		wordsLine := reader.Text()
		words := strings.Split(wordsLine, " ")

		log.Printf("[%s] Vector stringuri: %v", remote, words)

		// Apelăm funcția cerinței 1
		rezultat := cerinta1(words, index)

		// Trimitem răspuns clientului
		reply := fmt.Sprintf("Rezultat cerinta 1: %s\n", rezultat)
		conn.Write([]byte(reply))

		return
	}

	if cerinta == 3 {
		if !reader.Scan() {
			conn.Write([]byte("Eroare: nu pot citi vectorul de numere\n"))
			return
		}
		numbersLine := reader.Text()

		parts := strings.Split(numbersLine, " ")
		var intValues []int

		for _, p := range parts {
			if p == "" {
				continue
			}
			var val int
			fmt.Sscanf(p, "%d", &val)
			intValues = append(intValues, val)
		}

		log.Printf("[%s] Client %s a facut request cu datele: %v", remote, clientName, intValues)

		sum, _ := cerinta3(intValues)

		log.Printf("[%s] Server trimite raspunsul: %d", remote, sum)

		reply := fmt.Sprintf("Suma calculata de server: %d\n", sum)
		conn.Write([]byte(reply))

		return
	}

	if cerinta == 4 {
		if !reader.Scan() {
			conn.Write([]byte("Eroare: nu pot citi datele pentru cerinta 4\n"))
			return
		}
		line := reader.Text()

		parts := strings.Split(line, " ")
		var allInts []int
		for _, p := range parts {
			if p == "" {
				continue
			}
			var val int
			fmt.Sscanf(p, "%d", &val)
			allInts = append(allInts, val)
		}

		log.Printf("[%s] Client %s a facut request cu datele: %v", remote, clientName, allInts)

		media, _ := cerinta4(allInts)

		log.Printf("[%s] Server trimite raspunsul: %.2f", remote, media)

		reply := fmt.Sprintf("Media aritmetica: %.2f\n", media)
		conn.Write([]byte(reply))
		return
	}

	if cerinta == 8 {
		if !reader.Scan() {
			conn.Write([]byte("Eroare: nu pot citi datele pentru cerinta 8\n"))
			return
		}
		line := reader.Text()

		parts := strings.Split(line, " ")
		var intValues []int
		for _, p := range parts {
			if p == "" {
				continue
			}
			var val int
			fmt.Sscanf(p, "%d", &val)
			intValues = append(intValues, val)
		}

		log.Printf("[%s] Client %s a facut request cu datele: %v", remote, clientName, intValues)

		totalCifre, _ := cerinta8(intValues)

		log.Printf("[%s] Server trimite raspunsul: %d", remote, totalCifre)

		reply := fmt.Sprintf("Numarul total de cifre ale numerelor prime: %d\n", totalCifre)
		conn.Write([]byte(reply))
		return
	}

	if cerinta == 12 {
		if !reader.Scan() {
			conn.Write([]byte("Eroare: nu pot citi datele pentru cerinta 12\n"))
			return
		}
		line := reader.Text()

		parts := strings.Split(line, " ")
		var intValues []int
		for _, p := range parts {
			if p == "" {
				continue
			}
			var val int
			fmt.Sscanf(p, "%d", &val)
			intValues = append(intValues, val)
		}

		log.Printf("[%s] Client %s a facut request cu datele: %v", remote, clientName, intValues)

		sum := cerinta12(intValues)

		log.Printf("[%s] Server trimite raspunsul: %d", remote, sum)

		reply := fmt.Sprintf("Suma numerelor cu prima cifra dublata: %d\n", sum)
		conn.Write([]byte(reply))
		return
	}

	conn.Write([]byte("Cerinta nerealizata inca.\n"))
}

func main() {

	addr := "127.0.0.1:9000"

	ln, err := net.Listen("tcp", addr)
	if err != nil { //adr in folosinta
		log.Fatalf("Serverul nu poate asculta pe %s: %v", addr, err)
	}

	log.Printf("Server pornit. Asculta pe %s ...", addr)

	//serverula ccepta conexiuni la infinit
	for {
		conn, err := ln.Accept() //listenerul asteapta sa accepte o conexiune
		if err != nil {
			log.Printf("Eroare la Accept: %v", err)
			continue
		}

		go handleConn(conn) //tirmite un fel de thread(gorutina) si continuna
	}
}
