import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
nums = [True] * (n + 1)
nums[1] = False
k = int(n ** 0.5)
for i in range(2, k + 1):
    if nums[i]:
        for j in range(i + i, n + 1, i):
            nums[j] = False


primes = []
for i in range(m, n + 1):
    if nums[i]:
        primes.append(i)
if not primes:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])