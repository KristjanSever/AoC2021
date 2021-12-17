##
##def astar(labirint, size):
##    visited = {}
##    queue = {}
##    queue['0,0'] = [0,0]
##    while len(queue) > 0:
##        key = min(queue, key=queue.get)
##        val = queue[key]
##        visited[key] = queue[key]
##        del queue[key]
##        cur = key.split(',')
##        print(cur)
##        if int(cur[0]) == size - 1 and int(cur[1]) == size - 1:
##            print('found the path, cost = ' , val)
##        #za vse sosede
##        children = []
##        x, y = int(cur[0]), int(cur[1])
##        if inBounds(x + 1,size):
##            children.append([x + 1, y, val[1] + labirint[x][y] + manhatten(x + 1, y, size), val[1] + labirint[x+1][y]])
##        if inBounds(x - 1,size):
##            children.append([x - 1, y, val[1] + labirint[x][y] + manhatten(x - 1, y, size), val[1] + labirint[x-1][y]])
##        if inBounds(y + 1,size):
##            children.append([x, y + 1, val[1] + labirint[x][y] + manhatten(x, y + 1, size), val[1] + labirint[x][y+1]])
##        if inBounds(y - 1,size):
##            children.append([x, y - 1 , val[1] + labirint[x][y] + manhatten(x, y - 1, size), val[1] + labirint[x][y-1]])
##        for v in children:
##            if str(v[0])+','+str(v[1]) in visited:
##                continue
##            if str(v[0])+','+str(v[1]) in queue:
##                if queue[str(v[0])+','+str(v[1])][1] < v[3]:
##                    queue[str(v[0])+','+str(v[1])] = [v[2],v[3]]
##                    continue
##            queue[str(v[0])+','+str(v[1])] = [v[2],v[3]]
##            
##            
##
##def manhatten(x,y,size):
##    return (size - x) + (size - y)
##
##def inBounds(x, size):
##    return (x >= 0 and x < size)
import math
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):


    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        print(len(open_list))
        # Get the current node
        current_node = open_list[0]
        print(current_node.position)
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(1, 0), (-1,0),(0,-1) , (0, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) * 5 - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) * 5 -1) or node_position[1] < 0:
                continue


            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)
    
        # Loop through children
        for child in children:
            # Child is on the closed list
            tmp = False
            for closed_child in closed_list:
                if child == closed_child:
                    tmp = True
                    continue
            if tmp:
                continue
            child.g = current_node.g + maze[child.position[0]][child.position[1]]
            child.h = ((child.position[0]-end_node.position[0])**2 + (child.position[1]-end_node.position[1])**2)**(0.5)
            child.f = child.g + child.h

            # Child is already in the open list
            tmp = False
            for open_node in open_list:
                if child == open_node and child.g >= open_node.g:
                    tmp = True
                    continue
            if tmp:
                continue
            # Add the child to the open list
            open_list.append(child)


best = float('inf')
f = open('input.txt','r')
labirint = [[int(n) for n in line.strip()] for line in f]
size = len(labirint)

start = (0,0)
end = (size-1, size -1)
path = astar(labirint, start,end)

risk = 0
for i, el in enumerate(path):
    if i != 0:
        x,y = el
        risk += labirint[x][y]
print(path)
print(risk)


