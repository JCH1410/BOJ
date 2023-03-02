import sys

input = sys.stdin.readline

st1 = list(input().rstrip())
st2 = list(input().rstrip())
len1, len2 = len(st1), len(st2)
solution = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if st1[i - 1] == st2[j - 1]:
            solution[i][j] = solution[i - 1][j - 1] + 1
        else:
            solution[i][j] = max(solution[i - 1][j], solution[i][j - 1])

print(solution[-1][-1])