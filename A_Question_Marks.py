from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    answer = input()

    ct = Counter(answer)
    marks = 0
    for char in ct:
        if char == '?':
            continue
        if ct[char] > n:
            marks += n
        else:
            marks += ct[char]

    print(marks)