money = int(input())
notes = [1,5,10,20,100]
ct = 0
for note in notes[::-1]:

    if money >= note:
        ct += money // note
        money = money % note

print(ct)