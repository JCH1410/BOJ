n, k = map(int, input().split())
nums = []
nums2 = [True] * (n + 1)
for num in range(n + 1):
    nums.append(num)

count = 0
result = 0
for i in range(2, n + 1):
    if nums2[i]:
        for j in range(i, n + 1, i):
            if nums2[j]:
                nums2[j] = False
                count += 1
            if count == k:
                result = j
                break

print(result)