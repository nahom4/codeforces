s = input()
word = "hello"

left,right = 0,0

while left < len(word) and right < len(s):
    if word[left] == s[right]:
        left += 1
        right += 1

    else:
        right += 1


if left == len(word):
    print('YES')
else:
    print('NO')