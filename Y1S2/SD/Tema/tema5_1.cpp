#include <iostream>
#include <vector>

struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : value(x), left(nullptr), right(nullptr) {}
};

TreeNode* sortedArrayToBST(std::vector<int>& nums, int start, int end) {
    if (start > end) {
        return nullptr;
    }

    int mid = start + (end - start) / 2;
    TreeNode* node = new TreeNode(nums[mid]);

    node->left = sortedArrayToBST(nums, start, mid - 1);
    node->right = sortedArrayToBST(nums, mid + 1, end);

    return node;
}

void printInOrder(TreeNode* node) {
    if (node != nullptr) {
        printInOrder(node->left);
        std::cout << node->value << " ";
        printInOrder(node->right);
    }
}

int main() {
    std::vector<int> nums;
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(4);
    nums.push_back(5);
    nums.push_back(6);
    nums.push_back(7);

    TreeNode* root = sortedArrayToBST(nums, 0, nums.size() - 1);

    std::cout << "In-order traversal of the constructed BST: ";
    printInOrder(root);
    std::cout << std::endl;

    return 0;
}