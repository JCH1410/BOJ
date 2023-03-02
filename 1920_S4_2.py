import sys
input = sys.stdin.readline


n = input()
nums = set(input().split())
m = input()

result = ""
for num in input().split():
    result += "1\n" if num in nums else "0\n"
print(result)