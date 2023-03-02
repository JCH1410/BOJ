import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_name = dict()
pokemon_num = dict()
for i in range(n):
    name = input().rstrip()
    pokemon_name[name] = str(i + 1)
    pokemon_num[str(i + 1)] = name

result = []
for _ in range(m):
    insert = input().rstrip()
    if insert.isdigit():
        result.append(pokemon_num[insert])
    else:
        result.append(pokemon_name[insert])

print('\n'.join(result))