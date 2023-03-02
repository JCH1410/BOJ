import sys

input = sys.stdin.readline
n = int(input())
alphabet = dict()
alphabet['A'] = ['', '']
for _ in range(n):
    a, b, c = input().rstrip().split(' ')
    alphabet[a][0] = b
    alphabet[b] = ['', '']
    alphabet[a][1] = c
    alphabet[c] = ['', '']

def preorder(l):
    if l == '.':
        return ''
    result = []
    result.append(l)
    result.append(preorder(alphabet[l][0]))
    result.append(preorder(alphabet[l][1]))
    return ''.join(result)

def inorder(l):
    if l == '.':
        return ''
    result = []
    result.append(inorder(alphabet[l][0]))
    result.append(l)
    result.append(inorder(alphabet[l][1]))
    return ''.join(result)

def postorder(l):
    if l == '.':
        return ''
    result = []
    result.append(postorder(alphabet[l][0]))
    result.append(postorder(alphabet[l][1]))
    result.append(l)
    return ''.join(result)

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))