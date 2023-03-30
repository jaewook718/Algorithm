def preorder(node):
    print(chr(node+65), end = '')
    if tree[node][0]!=0:
        preorder(tree[node][0])
    if tree[node][1]!=0:
        preorder(tree[node][1])


def inorder(node):
    if tree[node][0] != 0:
        inorder(tree[node][0])
    print(chr(node + 65), end='')
    if tree[node][1] != 0:
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] != 0:
        postorder(tree[node][0])
    if tree[node][1] != 0:
        postorder(tree[node][1])
    print(chr(node + 65), end='')

N = int(input())
tree = [[0]*2 for _ in range(N)]
for _ in range(N):
    a, b, c = input().split()
    if b != '.':
        tree[ord(a)-65][0] = ord(b)-65
    if c != '.':
        tree[ord(a)-65][1] = ord(c)-65

preorder(0)
print()
inorder(0)
print()
postorder(0)