#include <iostream>

struct Node {
    int data;
    Node* next;
};

Node* createList(int firstData) {
    Node* head = new Node();
    head->data = firstData;
    head->next = nullptr;
    return head;
}

void printList(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

void insertNode(Node*& head, int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

Node* searchKey(Node* head, int key) {
    Node* current = head;
    while (current != nullptr && current->data != key) {
        current = current->next;
    }
    return current;
}

void deleteNode(Node*& head, int key) {
    Node* current = head;
    Node* previous = nullptr;
    while (current != nullptr && current->data != key) {
        previous = current;
        current = current->next;
    }
    if (current == nullptr) return;
    if (previous == nullptr) {
        head = current->next;
    } else {
        previous->next = current->next;
    }
    delete current;
}

int main() {
    Node* myList = createList(10);
    
    insertNode(myList, 20);
    insertNode(myList, 30);
    insertNode(myList, 40);
    
    std::cout << "Lista initiala: ";
    printList(myList);
    
    int keyToSearch = 20;
    Node* foundNode = searchKey(myList, keyToSearch);
    if (foundNode != nullptr) {
        std::cout << "Nodul cu cheia " << keyToSearch << " a fost gasit" << std::endl;
    } else {
        std::cout << "Nodul cu cheia " << keyToSearch << " nu a fost gasit" << std::endl;
    }
    
    int keyToDelete = 30;
    deleteNode(myList, keyToDelete);
    std::cout << "Lista dupa stergerea nodului cu cheia " << keyToDelete << ": ";
    printList(myList);
    
    return 0;
}
