import math
import heapq
import sys
class Node():

    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.x = x
        self.y = y

        self.dist = sys.maxsize

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __lt__(self, other):
        return self.dist < other.dist

def inBounds(x,y , size):
    return x >= 0 and x < size and y >= 0 and y < size

def successors(node, size):
    global nodes
    pos = [[1,0], [0,1], [-1,0], [0,-1]]
    res = []
    for p in pos:
        tmpX = node.x + p[0]
        tmpY = node.y + p[1]
        if inBounds(tmpX, tmpY, size):
            res.append(nodes[tmpX][tmpY])
    return res

def newLt(self, other):
    return self.dist < other.dist


def dijsktra(maze, start, end):
    heap = [start]
    heapq.heapify(heap)
    a = 1
    while len(heap) > 0:
        u = heapq.heappop(heap)
        if u.x == end.x and u.y == end.y:
            dist = 0
            return u.dist
        
        for v in successors(u, 5 * len(maze)):
            add = math.floor(v.x / len(maze)) + math.floor(v.y / len(maze))
            add = add + maze[v.x % len(maze)][v.y % len(maze)]
            add = add % 9
            add = add if add != 0 else 9
            alt =  u.dist + add
            if alt < v.dist:
                v.dist = alt
                v.parent = u
                heapq.heappush(heap, v)
            
    return u.dist


f = open('input.txt','r')
maze = [[int(n) for n in line.strip()] for line in f]
nodes = [[Node(None, x,y) for y in range(0,5 * len(maze))] for x in range(0, 5* len(maze))]
size = len(maze)

start = Node(None, 0,0)
start.dist = 0
end = Node(None, 5 * size - 1, 5 * size - 1)

res = dijsktra(maze , start,end)

print(res)



