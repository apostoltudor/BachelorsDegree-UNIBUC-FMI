package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"os"
)

// structura pentru fisierul config.json
type Config struct {
	ArraySize int `json:"arraySize"`
}

// func pentru incarcare JSON
func loadConfig(filename string) (Config, error) {
	file, err := os.Open(filename)
	if err != nil {
		return Config{}, fmt.Errorf("eroare la deschiderea config.json: %v", err)
	}
	defer file.Close()

	var cfg Config
	decoder := json.NewDecoder(file)
	if err := decoder.Decode(&cfg); err != nil {
		return Config{}, fmt.Errorf("eroare la decodarea config.json: %v", err)
	}

	return cfg, nil
}

func main() {

	cfg, err := loadConfig("config.json")
	if err != nil {
		log.Fatalf("Nu pot incarca configuratia: %v", err)
	}

	clientName := "Client4"

	cerinta := 4

	fmt.Println("=== CONFIGURATIE ===")
	fmt.Println("Client:", clientName)
	fmt.Println("Cerinta:", cerinta)
	fmt.Println("Dimensiune vector din JSON:", cfg.ArraySize)
	fmt.Println()

	addr := "127.0.0.1:9000"
	conn, err := net.Dial("tcp", addr)
	if err != nil {
		log.Fatalf("Nu ma pot conecta la server: %v", err)
	}
	defer conn.Close()

	fmt.Println("Client conectat la server:", addr)
	writer := bufio.NewWriter(conn) //le trimitem oe toate odata

	fmt.Fprintf(writer, "%s\n", clientName)
	fmt.Fprintf(writer, "%d\n", cerinta)

	if cerinta == 1 {

		index := 4

		words := []string{"trd3w", "675ft", "0000i", "ppppp", "zqzqt"}

		fmt.Println("=== DATE TRIMISE PENTRU CERINTA 1 ===")
		fmt.Println("Index i:", index)
		fmt.Println("Stringuri:", words)
		fmt.Println()

		fmt.Fprintf(writer, "%d\n", index)

		for i, w := range words {
			if i == len(words)-1 {
				fmt.Fprintf(writer, "%s\n", w)
			} else {
				fmt.Fprintf(writer, "%s ", w)
			}
		}

	} else if cerinta == 3 {

		dataToSend := []int{12, 13, 14}

		fmt.Println("=== DATE TRIMISE PENTRU CERINTA 3 ===")
		fmt.Println("Vector:", dataToSend)
		fmt.Println()

		for i, val := range dataToSend {
			if i == len(dataToSend)-1 {
				fmt.Fprintf(writer, "%d\n", val)
			} else {
				fmt.Fprintf(writer, "%d ", val)
			}
		}

	} else if cerinta == 4 {

		mixedData := []int{2, 10, 11, 39, 32, 80, 84}

		fmt.Println("=== DATE TRIMISE PENTRU CERINTA 4 ===")
		fmt.Printf("Vector complet: %v\n", mixedData)
		fmt.Printf(" -> Interval [a, b]: [%d, %d]\n", mixedData[0], mixedData[1])
		fmt.Printf(" -> Valori de procesat: %v\n", mixedData[2:])
		fmt.Println()

		for i, val := range mixedData {
			if i == len(mixedData)-1 {
				fmt.Fprintf(writer, "%d\n", val)
			} else {
				fmt.Fprintf(writer, "%d ", val)
			}
		}
	} else if cerinta == 8 {
		dataToSend := []int{21, 17, 15, 3, 18}

		fmt.Println("=== DATE TRIMISE PENTRU CERINTA 8 ===")
		fmt.Println("Vector:", dataToSend)
		fmt.Println()

		for i, val := range dataToSend {
			if i == len(dataToSend)-1 {
				fmt.Fprintf(writer, "%d\n", val)
			} else {
				fmt.Fprintf(writer, "%d ", val)
			}
		}
	} else if cerinta == 12 {

		dataToSend := []int{23, 43, 26, 74}

		fmt.Println("=== DATE TRIMISE PENTRU CERINTA 12 ===")
		fmt.Println("Vector:", dataToSend)
		fmt.Println()

		for i, val := range dataToSend {
			if i == len(dataToSend)-1 {
				fmt.Fprintf(writer, "%d\n", val)
			} else {
				fmt.Fprintf(writer, "%d ", val)
			}
		}
	} else {

		fmt.Printf("\nCerinta %d nu este implementata in client.\n", cerinta)
		fmt.Println("Nu se trimit date catre server. Inchid executia.")

		return
	}

	writer.Flush()

	reader := bufio.NewReader(conn) //citim ce raspnude serverul
	reply, err := reader.ReadString('\n')
	if err != nil {
		log.Fatalf("Eroare la citirea raspunsului: %v", err)
	}

	fmt.Println("=== RASPUNS SERVER ===")
	fmt.Println(reply)
}
