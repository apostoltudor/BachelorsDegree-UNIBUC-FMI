#include <iostream>

struct CNode {
    int data;
    CNode* next;
};

CNode* createCircularList(int firstData) {
    CNode* head = new CNode();
    head->data = firstData;
    head->next = head; // Point to itself to maintain circularity
    return head;
}

void printCircularList(CNode* head) {
    if (head == nullptr) return;
    CNode* current = head;
    do {
        std::cout << current->data << " ";
        current = current->next;
    } while (current != head);
    std::cout << std::endl;
}

void insertCircularNode(CNode*& head, int data) {
    CNode* newNode = new CNode();
    newNode->data = data;
    if (head == nullptr) {
        newNode->next = newNode;
        head = newNode;
    } else {
        CNode* tail = head;
        while (tail->next != head) {
            tail = tail->next;
        }
        tail->next = newNode;
        newNode->next = head;
        head = newNode;
    }
}

CNode* searchCircularKey(CNode* head, int key) {
    if (head == nullptr) return nullptr;
    CNode* current = head;
    do {
        if (current->data == key) return current;
        current = current->next;
    } while (current != head);
    return nullptr;
}

void deleteCircularNode(CNode*& head, int key) {
    if (head == nullptr) return;
    CNode* current = head;
    CNode* previous = nullptr;
    do {
        if (current->data == key) {
            if (previous == nullptr) {
                if (current->next == head) {
                    delete current;
                    head = nullptr;
                    return;
                } else {
                    previous = head;
                    while (previous->next != head) {
                        previous = previous->next;
                    }
                    previous->next = head->next;
                    head = head->next;
                    delete current;
                    return;
                }
            } else {
                previous->next = current->next;
                if (current == head) head = current->next;
                delete current;
                return;
            }
        }
        previous = current;
        current = current->next;
    } while (current != head);
}

int main() {
    CNode* circularList = createCircularList(10);

    insertCircularNode(circularList, 20);
    insertCircularNode(circularList, 30);
    insertCircularNode(circularList, 40);

    std::cout << "Initial circular list: ";
    printCircularList(circularList);

    int keyToSearch = 20;
    CNode* foundNode = searchCircularKey(circularList, keyToSearch);
    if (foundNode != nullptr) {
        std::cout << "Nodul cu cheia " << keyToSearch << " a fost gasit" << std::endl;
    } else {
        std::cout << "Nodul cu cheia " << keyToSearch << " nu a fost gasit" << std::endl;
    }

    int keyToDelete = 30;
    deleteCircularNode(circularList, keyToDelete);
    std::cout << "Lista circulara dupa stergerea nodului cu cheia " << keyToDelete << ": ";
    printCircularList(circularList);

    return 0;
}