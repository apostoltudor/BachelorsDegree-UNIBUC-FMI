#include <iostream>
#include <string>

struct Node {
    char data;
    Node* next;
};

class Stack {
public:
    Node* top;

    Stack() : top(nullptr) {}

    void push(char value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = top;
        top = newNode;
    }

    char pop() {
        if (top == nullptr) {
            return '\0';
        }
        Node* temp = top;
        char poppedValue = top->data;
        top = top->next;
        delete temp;
        return poppedValue;
    }

    char peek() {
        return (top != nullptr) ? top->data : '\0';
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

bool areBracketsBalanced(const std::string& expression) {
    Stack stack;
    for (char ch : expression) {
        if (ch == '(' || ch == '{' || ch == '[') {
            stack.push(ch);
        } else if (ch == ')' || ch == '}' || ch == ']') {
            if (stack.isEmpty()) {
                return false;
            }
            char top = stack.pop();
            if ((ch == ')' && top != '(') ||
                (ch == '}' && top != '{') ||
                (ch == ']' && top != '[')) {
                return false;
            }
        }
    }
    return stack.isEmpty();
}

int main() {
    std::string expression;
    std::cout << "Introdu o expresie cu paranteze: ";
    std::cin >> expression;

    if (areBracketsBalanced(expression)) {
        std::cout << "Este corect." << std::endl;
    } else {
        std::cout << "Nu este corect." << std::endl;
    }

    return 0;
}