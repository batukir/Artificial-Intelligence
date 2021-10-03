# graph input is adjacency list

graph = {
    'a' : ['b', 'c', 'd'],
    'b' : ['e', 'f', 'g'],
    'c' : ['h', 'i'],
    'd' : ['n', 'j'],
    'e' : ['k','l'],
    'f': [],
    'g': ['m'],
    'h': [],
    'i': [],
    'j': [],
    'n': [],
    'k': ['n'],
    'l': [],
    'm': [],
    'n': []
}
tmpGraph = list()
def DLS(start,goal,tmpGraph,depth):
    #add root node (with children)
    tmpGraph.append(start)
    currDepth = 0
    #check if root = goal
    if start == goal:
        return tmpGraph
    #check if current depth is negative
    #if negative, path may exist but not for desired depth
    if depth <= 0:
        return False
    #loop through children of currNode
    for currNode in graph[start]:
        #changes start parameter to currNode
        #checks if goal is found recursively
        if DLS(currNode,goal,tmpGraph,depth-1):
            return tmpGraph
        else:
            #pop to check next parent
            tmpGraph.pop()
    return False
def IDS(start,goal,tmpGraph): 
    #loop through current root
    for i in range(len(graph)-1):
        #checks if current node is goal
        if DLS(start,goal,tmpGraph,i):
            t = ' - '.join(tmpGraph)
            print("IDS: path from " + start + " to " + goal + " [depth " + str(i) + "]:found [" + t + "]")  
            return tmpGraph
        else:
            
            if(i > 0):
                print("IDS: path from " + start + " to " + goal + " [depth " + str(i) + "]:not found")
            tmpGraph.pop()
    return False
    
    
choice = '0'
while choice == '0':
    print('Choose one of the following: ')
    print('1. Find DLS')
    print('2. Find IDS')
    print('3. Exit')
    choice = input ('Please make a choice: ')
            
    if choice =='1':
        start = input('Enter start value: ')
        goal = input('Enter goal value: ')
        depth = int(input('Enter desired depth: '))
        print()
        function = DLS(start,goal,tmpGraph,depth)
        if(function):
            s = ' - '.join(tmpGraph)
            print("DLS: path from " + start + " to " + goal + " is " + s)    
        else:
            print("DLS path not found")
        tmpGraph.clear()
        choice = '0'
        print()
    elif choice =="2":
        start = input('Enter start value: ')
        goal = input('Enter goal value: ')
        print()
        function = IDS(start,goal,tmpGraph)
        function
        choice = '0'
        tmpGraph.clear()
        print()
    elif choice =="3":
        print("exiting...")
        break
    else:
        print("I don't understand your choice.")
        choice = '0'
        print()
        
