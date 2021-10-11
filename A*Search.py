#resubmit 
import math
board = [ 
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ],
    [ '#', 'A', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
    [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', '#' ],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ]]

#start from 0 for 20x20
import math
#The max row and col for the board
ROW = 19
COL = 19

# To store matrix cell coordinates
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
 
 # A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, g:float, parent):
        self.pt = pt  # coordinates
        self.f = 0
        self.g = g
        self.parent = parent

# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
 
# Function to find the shortest path between
# a given source cell to a destination cell.
# Informed Search
def IS(mat, src: Point, dest: Point, type):
    # check source and destination cell
    # of the matrix have value #
    if mat[src.x][src.y]== '#' or mat[dest.x][dest.y]=='#':
        return -1
    
    visited = [[False for i in range(COL)] for j in range(ROW)]
     
    # Mark the source cell as visited
    visited[src.x][src.y] = True
     
    # Create a queue
    q = []
     
    # Distance of source cell is 0
    s = queueNode(src,0, None)
    q.append(s)

    if type == 'Euclidean':
        rowNum = [-1, 1, 1, 0, 0, -1]
        colNum = [-1, 1, 0, 1, -1, 0]
        elength = len(rowNum)
    elif type == "Manhattan":
        rowNum = [1, 0, 0, -1]
        colNum = [0, 1, -1, 0]
        mlength = len(rowNum)
    else:
        print('Error: Type not recognized')
        exit()

    while q:
        curr = q.pop(0) # pop the front cell

        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            tmpArray = []
            currNode = curr
            while currNode is not None:
                tmpArray.append(currNode.pt)
                currNode= currNode.parent
            return tmpArray[::-1]

        # Otherwise enqueue its adjacent cells
        if type == 'Euclidean':
            neighborRange = elength
        elif type == 'Manhattan':
            neighborRange = mlength
        for i in range(neighborRange):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            # if adjacent cell is valid, has path 
            # and not visited yet, append it. 
            if (isValid(row,col) and board[row][col] != '#' and not visited[row][col]):
                visited[row][col] = True
                h = abs(row - dest.x) + abs(col - dest.y)
                if type == 'Euclidean':
                    g = math.sqrt((row - curr.pt.x)**2 + (col - curr.pt.y)**2)
                elif type == "Manhattan":
                    g = 1
                Adjcell = queueNode(Point(row,col), curr.g + g,curr)
                # Calculate f(n) for current neighbor
                Adjcell.f = g + h
                q.append(Adjcell)
                
        front = q[0]
        fs = front.f
        for node in q:
            if node.f < fs:
                fs = node.f
                q.remove(front)
                front = node
        
        q.insert(0, front)        
           
    # Return -1 if goal cannot be reached
    return -1
 
# Driver code
def main():
    start_x= 1
    start_y= 1
    goal_x= 18 # Remember that array indexing starts from 0 in python
    goal_y= 18
    mat = board
    source = Point(start_x, start_y)
    dest = Point(goal_x, goal_y)
    print()
    print('(the agent can move to up, down, left and right)')
    output = IS(mat,source,dest,"Manhattan")
    for i in output[1:-1]:
        mat[i.x][i.y] = '*'
    for i in mat:
        print (' '.join(i))
    print()
    print('(the agent can move to up, down, left and right, as well as in diagonal)')
    output= IS(mat,source,dest,"Euclidean")
    for j in output[1:-1]:
        mat[j.x][j.y] = '*'
    for j in mat:
        print (' '.join(j))
main()
 


