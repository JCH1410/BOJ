def vps(word):
    input_word = list(word)
    output_word = []
    while input_word:
        letter = input_word.pop(0)
        if letter == '(':
            output_word.append(letter)
        else:
            if not output_word:
                return "NO"
            output_word.pop()
    if output_word:
        return "NO"
    else:
        return "YES"


n = int(input())
for _ in range(n):
    print(vps(input()))