from collections import defaultdict

import sys, threading
def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())

        graph = defaultdict(list)
        node = None
        for _ in range(n - 1):
            u,v = map(int,input().split())

            graph[u].append(v)
            graph[v].append(u)
            node = u

        def countComponents(node,size):

            visited = set()
            components = 0
            def dfs(node,size):
                nonlocal components
                if node in visited:
                    return 0 

                visited.add(node)

                count = 1
                for neighbor in graph[node]:
                    count += dfs(neighbor,size)

                if count >= size:
                    components += 1
                    return 0

                return count


            dfs(node,size)
            
            return components


        left,right = 1,n

        while left + 1 < right:
            md = left + (right - left) // 2

            if countComponents(node,md) >= k + 1:
                left = md

            else:
                right = md

        print(left)           

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


 

    

    