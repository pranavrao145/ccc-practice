# J5

from collections import deque

graph = dict()
pages = list()
visited = list()
q = deque(list())
path_lengths = []


class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = None
        self.depth = None

def all_visited():
    for node in pages:
        if node not in visited:
            return False
    return True

def bfs():
    global path_lengths, q, visited, pages
    while len(q) > 0:
        elem = q.pop()
        if elem.adjacent == []:
            path_lengths.append(elem.depth)
        else:
            for page in elem.adjacent:
                if pages[page - 1] not in visited:
                    node = pages[page - 1]
                    node.depth = elem.depth + 1
                    visited.append(node)
                    q.appendleft(node)
                

if __name__ == "__main__":
    numpages = int(input())

    for i in range(1, numpages + 1):
        pages.append(Node(data=i))

    for i in range(1, numpages + 1):
        graph[i] = list(map(int, input().strip().split()[1:]))
    
    for key in graph:
        pages[key - 1].adjacent = graph.get(key)

    pages[0].depth = 1
    q.appendleft(pages[0])
    visited.append(pages[0])

    bfs()
    
    path_lengths.sort()
    
    if all_visited():
        print("Y")
        print(path_lengths[0])
    else:
        print("N")
        print(path_lengths[0])
