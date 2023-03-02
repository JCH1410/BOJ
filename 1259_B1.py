def palindrome(num):
    test = list(str(num))
    len_test = len(test) - 1
    for i in range((len_test // 2) + 1):
        if test[i] != test[len_test - i]:
            return 'no'
    return 'yes'


while 1:
    n = int(input())
    if n == 0:
        break
    print(palindrome(n))