#include <iostream>

struct DNode {
    int data;
    DNode* prev;
    DNode* next;
};

DNode* createDList(int firstData) {
    DNode* head = new DNode();
    head->data = firstData;
    head->prev = nullptr;
    head->next = nullptr;
    return head;
}

void printDList(DNode* head) {
    DNode* current = head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

void insertDNode(DNode*& head, int data) {
    DNode* newNode = new DNode();
    newNode->data = data;
    newNode->prev = nullptr;
    newNode->next = head;
    if (head != nullptr) {
        head->prev = newNode;
    }
    head = newNode;
}

DNode* searchDKey(DNode* head, int key) {
    DNode* current = head;
    while (current != nullptr && current->data != key) {
        current = current->next;
    }
    return current;
}

void deleteDNode(DNode*& head, int key) {
    DNode* current = searchDKey(head, key);
    if (current == nullptr) return; // Key not found

    if (current->prev != nullptr) {
        current->prev->next = current->next;
    } else {
        head = current->next; // Update head if needed
    }
    if (current->next != nullptr) {
        current->next->prev = current->prev;
    }

    delete current;
}

int main() {
    DNode* dList = createDList(10);

    insertDNode(dList, 20);
    insertDNode(dList, 30);
    insertDNode(dList, 40);

    std::cout << "Lista dublu inlantuita initiala: ";
    printDList(dList);

    int keyToSearch = 20;
    DNode* foundNode = searchDKey(dList, keyToSearch);
    if (foundNode != nullptr) {
        std::cout << "Node cu cheia " << keyToSearch << " a fost gasita" << std::endl;
    } else {
        std::cout << "Node cu cheia " << keyToSearch << " nu a fost gasita" << std::endl;
    }

    int keyToDelete = 30;
    deleteDNode(dList, keyToDelete);
    std::cout << "Lista dubla inlantuita dupa stergerea nodului cu cheia " << keyToDelete << ": ";
    printDList(dList);

    return 0;
}