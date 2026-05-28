#include <iostream>
#include <vector>

struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : value(x), left(nullptr), right(nullptr) {}
};

void printInOrder(TreeNode* node) {
    if (node != nullptr) {
        printInOrder(node->left);
        std::cout << node->value << " ";
        printInOrder(node->right);
    }
}

void inOrderTraversal(TreeNode* root, std::vector<int>& vec) {
    if (root != nullptr) {
        inOrderTraversal(root->left, vec);
        vec.push_back(root->value);
        inOrderTraversal(root->right, vec);
    }
}

std::vector<int> merge(const std::vector<int>& vec1, const std::vector<int>& vec2) {
    std::vector<int> merged;
    int i = 0, j = 0;
    while (i < vec1.size() && j < vec2.size()) {
        if (vec1[i] < vec2[j]) {
            merged.push_back(vec1[i++]);
        } else {
            merged.push_back(vec2[j++]);
        }
    }
    while (i < vec1.size()) {
        merged.push_back(vec1[i++]);
    }
    while (j < vec2.size()) {
        merged.push_back(vec2[j++]);
    }
    return merged;
}

TreeNode* sortedArrayToBST(const std::vector<int>& nums, int start, int end) {
    if (start > end) {
        return nullptr;
    }
    int mid = start + (end - start) / 2;
    TreeNode* node = new TreeNode(nums[mid]);
    node->left = sortedArrayToBST(nums, start, mid - 1);
    node->right = sortedArrayToBST(nums, mid + 1, end);
    return node;
}

int main() {
    TreeNode* root1 = new TreeNode(1);
    TreeNode* root2 = new TreeNode(2);

    std::vector<int> vec1, vec2;
    inOrderTraversal(root1, vec1);
    inOrderTraversal(root2, vec2);

    std::vector<int> merged = merge(vec1, vec2);
    TreeNode* mergedTree = sortedArrayToBST(merged, 0, merged.size() - 1);

    std::cout << "In-order traversal of the merged tree: ";
    printInOrder(mergedTree);
    std::cout << std::endl;
    
    return 0;
}