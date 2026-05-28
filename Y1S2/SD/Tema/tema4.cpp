#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>

struct Node {
    std::string key;
    Node* next;

    Node(std::string key) : key(key), next(nullptr) {}
};

class HashTable {
private:
    Node** table;
    int capacity;

    int hashFunction(char key) {
        key = std::toupper(key);
        return key - 'A';
    }

public:
    HashTable(int size) : capacity(size) {
        table = new Node*[capacity];
        for (int i = 0; i < capacity; i++) {
            table[i] = nullptr;
        }
    }

    void insert(std::string key) {
        int index = hashFunction(key[0]);
        Node* newNode = new Node(key);
        if (table[index] == nullptr) {
            table[index] = newNode;
        } else {
            Node* temp = table[index];
            Node* prev = nullptr;
            while (temp != nullptr && temp->key < key) {
                prev = temp;
                temp = temp->next;
            }
            if (prev == nullptr) {
                newNode->next = table[index];
                table[index] = newNode;
            } else {
                newNode->next = prev->next;
                prev->next = newNode;
            }
        }
    }

    void print() {
        for (int i = 0; i < capacity; i++) {
            std::cout << char('A' + i) << " -> ";
            Node* temp = table[i];
            while (temp != nullptr) {
                std::cout << temp->key << " -> ";
                temp = temp->next;
            }
            std::cout << "NULL" << std::endl;
        }
    }

    ~HashTable() {
        for (int i = 0; i < capacity; i++) {
            Node* temp = table[i];
            while (temp != nullptr) {
                Node* prev = temp;
                temp = temp->next;
                delete prev;
            }
        }
        delete[] table;
    }
};

int main() {
    HashTable ht(26);

    ht.insert("ane");
    ht.insert("Are");
    ht.insert("Ana");
    ht.insert("carte");
    ht.insert("caiet");
    ht.insert("cuvinte");
    ht.insert("inteligent");
    ht.insert("inimă");
    ht.insert("imagine");

    ht.print();

    return 0;
}