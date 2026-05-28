package main

import (
	"fmt"
	"math"
	"math/rand"
	"sync"
	"time"
)

const (
	NumNodes       = 10000
	ConstTolerance = 0.0001
)

type Node struct {
	Id      int
	Alive   bool
	Value   float64
	Cluster *Cluster
	mu      sync.Mutex
}

type Cluster struct {
	Nodes []*Node
}

func NewNode(id int, value float64, cluster *Cluster) *Node {
	return &Node{
		Id:      id,
		Alive:   true,
		Value:   value,
		Cluster: cluster,
	}
}

func NewCluster(size int) *Cluster {
	cluster := &Cluster{}
	for i := 0; i < size; i++ {
		node := NewNode(i, float64(i)*10.0, cluster)
		cluster.Nodes = append(cluster.Nodes, node)
	}
	return cluster
}

// luam starea nodului
func (n *Node) GetSnapshot() (float64, bool) {
	n.mu.Lock()
	defer n.mu.Unlock()
	return n.Value, n.Alive
}

func (n *Node) ToggleStatus() {
	n.mu.Lock()
	defer n.mu.Unlock()
	n.Alive = !n.Alive
	if n.Alive {
		fmt.Printf("->Node %d has recovered (Back online).\n", n.Id)
		//resetam valoarea cand revine online
		n.Value = float64(n.Id) * 10.0
	} else {
		fmt.Printf("-> Node %d has crashed (Offline).\n", n.Id)
	}
}

func ReadValuesFromCluster(cluster *Cluster) []float64 {
	values := []float64{}
	for _, node := range cluster.Nodes {
		val, alive := node.GetSnapshot()
		if alive {
			values = append(values, val)
		} else {
			values = append(values, -1.0)
		}
	}
	return values
}

func Gossip(n1 *Node, n2 *Node) {
	//le ordonam dupa id pentru a evita deadlock-uri (sa nu se blochereze reciproc)
	first, second := n1, n2
	if n1.Id > n2.Id {
		first, second = n2, n1
	}

	first.mu.Lock()
	second.mu.Lock()

	defer second.mu.Unlock()
	defer first.mu.Unlock()

	//verificare daca sunt vii
	if n1.Alive && n2.Alive {
		avgValue := (n1.Value + n2.Value) / 2
		n1.Value = avgValue
		n2.Value = avgValue
	}
}

func pickRandomNeighbor(n *Node, nodes []*Node) *Node {
	//luam un nod random dintre vecinii lui ca sa nu parcurgem tot clusterul
	limit := 5
	for i := 0; i < limit; i++ {
		idx := rand.Intn(len(nodes))
		candidate := nodes[idx]

		//exceptie
		if candidate.Id == n.Id {
			continue
		}
		return candidate
	}
	return nil
}

func (n *Node) run() {
	ticker := time.NewTicker(100 * time.Millisecond)
	defer ticker.Stop()

	for range ticker.C {
		n.mu.Lock()
		alive := n.Alive
		n.mu.Unlock()

		if !alive {
			continue
		}

		other := pickRandomNeighbor(n, n.Cluster.Nodes)
		if other == nil {
			continue
		}

		Gossip(n, other)
	}
}

func RandomToggle(cluster *Cluster) {
	for {
		time.Sleep(500 * time.Millisecond)
		targetIndex := rand.Intn(len(cluster.Nodes))
		cluster.Nodes[targetIndex].ToggleStatus()
	}
}

// verificam daca valorile sunt convergente
func valuesConverged(v1, v2 []float64) bool {
	if len(v1) != len(v2) {
		return false
	}

	diffCount := 0
	for i := range v1 {
		if v1[i] == -1.0 || v2[i] == -1.0 {
			continue
		}

		if math.Abs(v1[i]-v2[i]) > ConstTolerance {
			diffCount++
		}
	}

	return diffCount == 0
}

func displayValues(cluster *Cluster) {
	currentValues := ReadValuesFromCluster(cluster)
	fmt.Println("Current values:", currentValues)
}

func main() {
	cluster := NewCluster(NumNodes)

	fmt.Println("Network started. Initializing gossip...")

	for _, node := range cluster.Nodes {
		go node.run()
	}

	go RandomToggle(cluster)

	prevValues := make([]float64, len(cluster.Nodes))

	displayValues(cluster)

	for {
		time.Sleep(100 * time.Millisecond)

		// displayValues(cluster)

		currentValues := ReadValuesFromCluster(cluster)

		//afisam doar primele cateva valori
		displayLimit := 10
		if len(currentValues) < 10 {
			displayLimit = len(currentValues)
		}
		fmt.Printf("Current state (first %d): %v ... \n", displayLimit, currentValues[:displayLimit])

		if valuesConverged(currentValues, prevValues) {
			fmt.Println(">>> SYSTEM STABLE (Converged) <<<")
		} else {
			fmt.Println("... system converging ...")
		}

		copy(prevValues, currentValues)
		prevValues = append([]float64(nil), currentValues...)
	}
}
