#include <iostream>

struct Node {
    int data;
    Node* next;
};

// Funcție pentru adăugarea unui nod la sfârșitul listei
void appendNode(Node*& head, int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = nullptr;

    if (head == nullptr) {
        head = newNode;
    } else {
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
    }
}

// Funcție pentru ștergerea primului nod
void deleteFirstNode(Node*& head) {
    if (head == nullptr) return;
    Node* temp = head;
    head = head->next;
    delete temp;
}

// Funcție pentru afișarea listei
void printList(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

int main() {
    Node* head = nullptr;
    int data;

    std::cout << "Numere (0 la final): ";
    while (std::cin >> data && data != 0) {
        appendNode(head, data);
    }

    std::cout << "Lista inițiala: ";
    printList(head);

    deleteFirstNode(head);

    std::cout << "Lista dupa stergerea primului nod: ";
    printList(head);

    return 0;
}