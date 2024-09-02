from collections import defaultdict


import sys, threading
def main():
    n,m = map(int,input().split())
    people = []
    for _ in range(n):
        people.append(input())

    graph = defaultdict(list)
    for _ in range(m):
        u,v = input().split()
        graph[u].append(v)
        graph[v].append(u)


    ans = []
    def backTracking(temp,removed,mask):
        if len(temp) + len(removed) >= n:
            ans.append(temp.copy())

        for i,p in enumerate(people):
            if not (1 << i) & mask and not removed[p]:
                mask |= (1 << i)
                for nei in graph[p]:
                    removed[nei] += 1
                
                temp.append(p)
                backTracking(temp,removed,mask)
                temp.pop()
                for nei in graph[p]:
                    removed[nei] -= 1
                
                mask &= ~(1 << i)

            if removed[p] == 0:
                removed.pop(p)

    backTracking([],defaultdict(int),0)
    ans.sort(key= lambda x : len(x))
    print(len(ans[-1]))
    for p in sorted(ans[-1]):
        print(p)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
