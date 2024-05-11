class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None
def insert(node, data):
    if not node:
        return Node(data)
    if node.n > data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data) 
    return node
tree = Node(int(input()))

while True:
    try:
        n = int(input())
    except:
        break
    tree = insert(tree, n)

def post(tree):
    if not tree:
        return
    post(tree.left)
    post(tree.right)
    print(tree.n)
    return
post(tree)