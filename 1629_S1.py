import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
nums = []
while b > 1:
    if b % 2 == 1:
        b -= 1
        nums.append(a % c)
    a = (a * a) % c
    b //= 2
for num in nums:
    a *= num
print(a % c)