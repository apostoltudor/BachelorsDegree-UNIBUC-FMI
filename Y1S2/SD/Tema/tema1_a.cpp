#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        std::swap(arr[i], arr[minIndex]);
    }
}

void printArray(const std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> arr;
    int x;

    std::cout<<"Numere: ";
    while (std::cin>>x)
    {
        arr.push_back(x);
    }

    std::cout << "Array-ul nesortat: ";
    printArray(arr);

    selectionSort(arr);

    std::cout << "Array-ul sortat: ";
    printArray(arr);

    return 0;
}
