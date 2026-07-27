class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)

print("루트: ", root.data)
print("왼쪽 자식: ",root.left.data)
print("오른쪽 자식: ", root.right.data)

class TreeNode2:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode2(10)
root.left = TreeNode2(20)
root.right = TreeNode2(30)
root.left.left = TreeNode2(40)
root.left.right = TreeNode2(50)
root.right.left = TreeNode2(60)
root.right.right = TreeNode2(70)

print("\n","="*50,"\n")
print("루트: ", root.data)
print("왼쪽 자식: ",root.left.data)
print("오른쪽 자식: ", root.right.data)
print("왼쪽의 왼쪽 자식: ", root.left.left.data)
print("왼쪽의 오른쪽 자식: ",root.left.right.data)
print("오른쪽의 왼쪽 자식: ", root.right.left.data)
print("오른쪽의 오른쪽 자식: ",root.right.right.data)


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

print("전위순회")
preorder(root)
print()

def inorder(node):
    preorder(node.left)
    print(node.data, end=" ")
    preorder(node.right)

print("중위순회")
inorder(root)
print()

def postorder(node):
    preorder(node.left)
    preorder(node.right)
    print(node.data, end=" ")

print("후위순회")
postorder(root)
print()