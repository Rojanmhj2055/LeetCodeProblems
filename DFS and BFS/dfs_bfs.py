## demo of Depth First Search(DFS) and Breadth First Search(BFS)

graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited =[]
queue =[]
#BFS uses a Queue Data structure -> First in First Out
def bfs(visited,graph,node)->None:
    print("BFS: ")
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m,end="-")
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


#BFS uses a Stack Data structure, Last In First Out
stack=[]
def dfs(visited,graph,node)->None:
    print("")
    print("DFS: ")
    visited.append(node)
    stack.append(node)
    
    while stack:
        m = stack.pop()
        print(m,end="-")
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

bfs(visited,graph,'5')

visited=[]
dfs(visited,graph,'5')
    
    