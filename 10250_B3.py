t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        first = h
        second = n // h
    else:
        first = n % h
        second = n // h + 1
    result = first * 100 + second
    print(result)