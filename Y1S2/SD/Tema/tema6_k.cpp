#include <iostream>
#include <vector>
#include <algorithm>

struct Edge {
    int src, dest, weight;
};

struct Graph {
    int V, E;
    std::vector<Edge> edges;

    Graph(int V, int E) : V(V), E(E) {}

    void addEdge(int src, int dest, int weight) {
        edges.push_back({src, dest, weight});
    }
};

struct DisjointSets {
    std::vector<int> parent, rank;

    DisjointSets(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int u) {
        if (u != parent[u])
            parent[u] = find(parent[u]);
        return parent[u];
    }

    void merge(int x, int y) {
        x = find(x), y = find(y);
        if (rank[x] > rank[y])
            parent[y] = x;
        else
            parent[x] = y;
        if (rank[x] == rank[y])
            rank[y]++;
    }
};

void KruskalMST(Graph& graph) {
    std::vector<Edge> result;
    int V = graph.V;
    sort(graph.edges.begin(), graph.edges.end(), [](Edge a, Edge b) {
        return a.weight < b.weight;
    });

    DisjointSets ds(V);

    for (auto& e : graph.edges) {
        int u = ds.find(e.src);
        int v = ds.find(e.dest);
        if (u != v) {
            result.push_back(e);
            ds.merge(u, v);
        }
    }

    std::cout << "Edges in MST:\n";
    for (auto& e : result) {
        std::cout << e.src << " -- " << e.dest << " == " << e.weight << std::endl;
    }
}