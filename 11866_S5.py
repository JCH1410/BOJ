n, k = map(int, input().split())
people = [i + 1 for i in range(n)]

index = 0
result = []
output = "<"
while len(people) > 0:
    index = (index + (k - 1)) % len(people)
    result.append(people.pop(index))
for i in range(len(result) - 1):
    output += (str(result[i]) + ', ')
output += (str(result[-1]) + '>')
print(output)
