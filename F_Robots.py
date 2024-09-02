def min_moves(locations,n):
    current = 1
    left = 0 
    
    moves = n

    for right in range(1,n):#[4,7,9] 3  
        current += locations[right] - locations[right - 1]

        if current >= n:
            spaces = current - (right - left + 1) # 

            moves = min(moves,min(spaces,max(2,n - right + left)))

            current -= locations[left + 1] - locations[left]
            left += 1

    return moves

def solve():
    n = int(input())

    locations = [0] * n

    for i in range(n):
        locations[i] = int(input())

    locations.sort()

    min_move = min_moves(locations,n)
    max_move = max(locations[-2] - locations[0], locations[-1] - locations[1]) - (n - 2)

    print(min_move)
    print(max_move)
if __name__ == "__main__":
    solve()