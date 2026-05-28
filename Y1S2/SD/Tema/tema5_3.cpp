//Găsirea celui mai mic strămoș comun (LCA) într-un BST
#include <iostream>

struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) : value(x), left(nullptr), right(nullptr) {}
};

TreeNode* findLCA(TreeNode* root, int n1, int n2) {
    if (root == nullptr) return nullptr;

    if (root->value < n1 && root->value < n2) {
        return findLCA(root->right, n1, n2);
    }

    if (root->value > n1 && root->value > n2) {
        return findLCA(root->left, n1, n2);
    }

    return root;
}




bool isBSTUtil(TreeNode* node, TreeNode* left, TreeNode* right) {
    if (node == nullptr) return true;

    if (left != nullptr && node->value <= left->value) return false;
    if (right != nullptr && node->value >= right->value) return false;

    return isBSTUtil(node->left, left, node) && isBSTUtil(node->right, node, right);
}

bool isBST(TreeNode* root) {
    return isBSTUtil(root, nullptr, nullptr);
}



int main() {
    TreeNode* root = new TreeNode(20);
    root->left = new TreeNode(10);
    root->right = new TreeNode(30);
    root->left->left = new TreeNode(5);
    root->left->right = new TreeNode(15);

    std::cout << "Is BST: " << isBST(root) << std::endl;

    TreeNode* lca = findLCA(root, 5, 15);
    if (lca != nullptr) {
        std::cout << "LCA of 5 and 15: " << lca->value << std::endl;
    } else {
        std::cout << "No LCA found." << std::endl;
    }

    return 0;
}