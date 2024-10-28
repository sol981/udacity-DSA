import math
import heapq 

class Intersection:
    # constructor 
    def __init__(self, pos):
        self.parent = None 
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
        
    # override the comparison operator, use for heapq, lowest f is on the top
    def __lt__(self, nxt): 
        return self.f < nxt.f 
        
    # operator == to know it is the same position 
    def __eq__(self, other):
        if not isinstance(other, Intersection):
            return False
        return self.pos == other.pos

# calculate distance between 2 point
def distance(M, point_1, point_2):
    return math.sqrt((M.intersections[point_1][0] - M.intersections[point_2][0]) ** 2 + (M.intersections[point_1][1] - M.intersections[point_2][1]) ** 2)

# find the path from destination node
# I use link list to store path so traversing back take O(n): n is number of intersection in path
def findPath(node):
    path = []
    while node is not None:
        path.append(node.pos)
        node = node.parent
    path.reverse()
    return path

def shortest_path(M, start, goal):
    # 1. Initialize the Open and Closed Lists:
    # Open List contains nodes to be evaluated.
    # Closed List contains intersection that have already been evaluated.
    open_list = [] #(node intersection)
    # close_list is save integer number as intersection to save momory instead of saving as a node such as open_list     
    close_list = []

    # 2. Add the start node to the Open List.
    # Use heapq to save nodes, the node with lowest f will on the top   
    # Pushing and popping a heap is O(log n).
    start_node = Intersection(start)
    heapq.heappush(open_list, start_node)

    # 3. Loop until the Open List is empty or the goal is reached:
    # Select the node from the Open List with the lowest f(n), where f(n) = g(n) + h(n).
    # If the current node is the goal, reconstruct the path and return it.
    while len(open_list) > 0:
    # 4. For the selected node:
        # Remove it from the Open List and add it to the Closed List.
        current_intersection_node = heapq.heappop(open_list)
        if current_intersection_node.pos == goal:
            return findPath(current_intersection_node)
     
        close_list.append(current_intersection_node.pos)
        
        # Evaluate all neighboring nodes:
        # If a neighbor is in the Closed List, skip it.
        # If a neighbor is in the Open List, check if this path is better (lower g(n)); update if necessary.
        for intersection in M.roads[current_intersection_node.pos]:
            if intersection in close_list:
                continue

            g = current_intersection_node.g + distance(M, current_intersection_node.pos, intersection)
            h = distance(M, intersection, goal)
            f = g + h

            # if node in open list and has lower g -> update 
            for node in open_list:
                if node.pos == intersection and g < node.g:
                    node.g = g 
                    node.f = f
                    node.parent = current_intersection_node
                    continue
                    
            # Otherwise, calculate g(n), h(n), and f(n), then add the neighbor to the Open List.
            neighbor = Intersection(intersection)
            neighbor.parent = current_intersection_node
            neighbor.g = g 
            neighbor.h = h
            neighbor.f = f 
            heapq.heappush(open_list, neighbor)

    return []