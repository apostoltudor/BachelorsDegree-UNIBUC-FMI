#include <iostream>
#include <vector>

struct StackNode {
    int index;
    StackNode* next;
};

struct QueueNode {
    std::pair<int, int> indexPair;
    QueueNode* next;
};

class Stack {
public:
    StackNode* top = nullptr;

    void push(int idx) {
        StackNode* newNode = new StackNode();
        newNode->index = idx;
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (top == nullptr) return -1;
        StackNode* temp = top;
        int idx = temp->index;
        top = top->next;
        delete temp;
        return idx;
    }

    bool isEmpty() {
        return top == nullptr;
    }

    ~Stack() {
        while (!isEmpty()) {
            pop();
        }
    }
};

class Queue {
public:
    QueueNode* front = nullptr;
    QueueNode* rear = nullptr;

    void enqueue(std::pair<int, int> idxPair) {
        QueueNode* newNode = new QueueNode();
        newNode->indexPair = idxPair;
        newNode->next = nullptr;
        if (rear == nullptr) {
            front = rear = newNode;
            return;
        }
        rear->next = newNode;
        rear = newNode;
    }

    std::pair<int, int> dequeue() {
        if (front == nullptr) return std::make_pair(-1, -1);
        QueueNode* temp = front;
        std::pair<int, int> idxPair = temp->indexPair;
        front = front->next;
        if (front == nullptr) rear = nullptr;
        delete temp;
        return idxPair;
    }

    bool isEmpty() {
        return front == nullptr;
    }

    ~Queue() {
        while (!isEmpty()) {
            dequeue();
        }
    }
};

void processVector(const std::vector<int>& vec) {
    Stack stack;
    Queue queue;
    int n = vec.size();

    for (int i = 0; i < n - 1; i++) {
        while (!stack.isEmpty() && vec[stack.top->index] < vec[i + 1]) {
            int idx = stack.pop();
   queue.enqueue(std::make_pair(idx, i + 1));
        }
        if (vec[i] < vec[i + 1]) {
   queue.enqueue(std::make_pair(i, i + 1));
        } else {
            stack.push(i);
        }
    }

    while (!queue.isEmpty()) {
        std::pair<int, int> p = queue.dequeue();
        std::cout << "(" << p.first << ", " << p.second << ") ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> vec;
    vec.push_back(5);
    vec.push_back(3);
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(4);
    processVector(vec);
    return 0;
}