# J5 - doesn't work for some inputs

from queue import Queue

graph = dict()
numpages = int()
bfsQueue = Queue()
depthQueue = Queue()
visited = list()
valid_paths = []

def BFS():
    while not bfsQueue.empty():
        elem = bfsQueue.get()
        depth = depthQueue.get()
        if visited[elem - 1] == True:
            if all(visited):
                return depth
            else:
                continue
        else:
            visited[elem - 1] = True
            if all(visited):
                return depth
            if graph.get(elem) == []:
                valid_paths.append(depth)
            for page in graph.get(elem):
                bfsQueue.put(page)
                depthQueue.put(depth + 1)
        
    return -1

if __name__ == "__main__":
    numpages = int(input())
    visited = [False] * numpages

    for i in range(1, numpages + 1):
        graph[i] = list(map(int, input().strip().split()[1:]))
    
    bfsQueue.put(1)
    depthQueue.put(1)

    result = BFS()

    if result == -1:
        print("N")
        valid_paths.sort()
        print(valid_paths[0])
    else:
        print("Y")
        print(result)