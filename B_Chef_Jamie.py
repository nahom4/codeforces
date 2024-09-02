n = int(input())
array = list(map(int,input().split()))

inc = []
dec = []
incSet = set()
decSet = set()

#2 5 8 8 10 10 11 4 12 12

for i in range(n):
    while inc and inc[-1] > array[i]:
        incSet.add(inc.pop())


    inc.append(array[i])

array = array[::-1]

for i in range(n):
    while dec and dec[-1] < array[i]:
        decSet.add(dec.pop())

    dec.append(array[i])

print(max(len(incSet),len(decSet)))


