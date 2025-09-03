import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree.setdefault(node, (left, right))


def preorder(root):  # 전위 순회: 루트 - 왼쪽 - 오른쪽
    if root != '.':
        print(root, end='')
        preorder(tree.get(root)[0])
        preorder(tree.get(root)[1])


def inorder(root):  # 중위 순회: 왼쪽 - 루트 - 오른쪽
    if root != '.':
        inorder(tree.get(root)[0])
        print(root, end='')
        inorder(tree.get(root)[1])


def postorder(root):  # 후위 순회: 왼쪽 - 오른쪽 - 루트
    if root != '.':
        postorder(tree.get(root)[0])
        postorder(tree.get(root)[1])
        print(root, end='')


preorder("A")
print()
inorder("A")
print()
postorder("A")
