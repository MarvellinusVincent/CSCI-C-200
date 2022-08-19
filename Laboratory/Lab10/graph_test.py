from Graph import Graph
import numpy as np

### DO NOT MODIFY
nodes = [1, 2, 3, 4, 5, 6]

### DO NOT MODIFY
pairs = [(1, 2), (3, 4), (4, 6), (1, 6), (2, 3)]

### DO NOT MODIFY
TEST_CASES = [[1, [2, 6]], [2, [3]], [3, [4]], [4, [6]], [5, []], [6, []]]
TEST_CASES_BIGRAPH = [[1, [2, 6]], [2, [1, 3]], [3, [2, 4]], [4, [3, 6]], [5, []], [6, [1, 4]]]




###############################################################################
# Complete the tasks using the Graph Class (Directional)
print("" + "="*30 + " Directional Graph " + "="*30 + "")
print("Comment out this print statement ONCE the error is fixed  (Error below) ")
g = Graph(nodes) # TODO: Should be a directional graph

# Adds all the edges to the graph
for p in pairs:
    g.add_edge(p)

# Children for a given node
print("Testing if children are correct (Order does not matter)")
for t in TEST_CASES:
    l = g.children(t[0])
    print("\tNode: {0}, Result: {1}, Wanted: {2}".format(t[0], l, t[1]))

print("\nDettached Nodes Test")
result = g.dettachedNodes()
if result != [5, 6]:
    print("\tDid not pass test, found {0} dettached".format(result))
else:
    print("\tCorrect, only {0} is dettached".format(result))


# Prints the graph out
print("Graph human representation")
print(g)

###############################################################################
# Complete the tasks using the Graph Class (Undirected graph)
print("\n" + "" + "="*35 + " Undirected " + "="*35 + "")
print("Comment out this print statement ONCE the error is fixed  (Error below) ")
g = Graph(nodes) # Should be a undirected graph

# Adds all the edges to the graph
for p in pairs:
    g.add_edge(p)

# Children for a given node
print("Testing if children are correct (Order does not matter)")
for t in TEST_CASES_BIGRAPH:
    l = g.children(t[0])
    print("\tNode: {0}, Result: {1}, Wanted: {2}".format(t[0], l, t[1]))

#Dettached Nodes
print("\nDettached Nodes Test")
result = g.dettachedNodes()
if result != [5]:
    print("\tDid not pass test, found {0} dettached".format(result))
else:
    print("\tCorrect, only {0} is dettached".format(result))


# Prints the graph out
print("Graph human representation")
print(g)


###############################################################################
# Complete the above task with adjacency lists here (Do not use the Graph class)
# All code for this part will be in this part, you will not use the Graph class
print("\n" + "" +  "="*30 + " Adjacency List (Undirected graph)" + "="*30 + "")

# TODO: Create the graph as list of lists (No dictionaries)
# HINT: Notice how the nodes don't start at zero, how can you make them start at zero? (Don't change nodes list)
# HINT: DO NOT USE THE Graph Class

adj_lst = []
for i in nodes:
    adj_lst.append([i, {}])

for src,dest in pairs:
    adj_lst[src-1].append(dest)
    adj_lst[dest-1].append(src-1)



# TODO: Add all the pairs
print("TODO") # TODO: Complete and remove this line


# TODO: Get all children for a node (Print test statements)
print("Testing if children are correct (Order does not matter)")
for t in TEST_CASES_BIGRAPH:
    pass

print("TODO") # TODO: Complete and remove this line





# TODO: Find dettached nodes (Print test statements)
det = None
print("TODO") # TODO: Complete and remove this line 

print("\nDettached nodes: [5] =? {0}".format(det))




# TODO: Print the adjacency list (Print test statements)
print("\nGraph human representation")
print("TODO") # TODO: Complete and remove this line

###############################################################################
# Complete the above task with adjacency matrix here (Do not use the Graph class)
# All code for this part will be in this part, you will not use the Graph class
# HINT: Might have to look at numpy documentation
print("\n" +  "="*30 + " Adjacency Matrix (Undirected graph)" + "="*30 + "")

graph  = [[[0 for i in range(len(nodes))] for j in range(len(nodes))]]
graph = []
for j in range(len(nodes)):
    line = []
    for i in range(len(nodes)):
        line+= [0]
    graph += [line]

for src, dest in pairs:
    graph[src - 1][dest - 1] = 1
    graph[dest - 1][src - 1] = 1
print (graph)




# TODO: Create the graph as 2-dimensional list (Numpy)
# HINT: Do not use the Graph class
print("TODO") # TODO: Complete and remove this line

graph_np = np.zeros(len(nodes), len(nodes))

for p in pairs:
    graph_np[p[0]-1][p[1]- -1] = 1
    graph_np[p[1]-1][p[0]- -1] = 1

print("adj_lst: ", adj_lst)



# TODO: Add all the pairs
print("TODO") # TODO: Complete and remove this line





# TODO: Get all children for a node (Print test statements)
# Children for a given node
print("\nTesting if children are correct (Order does not matter)")
print("NOTE: It is okay if the result is off by 1 for each node")
print("TODO") # TODO: Complete and remove this line
for t in TEST_CASES_BIGRAPH:
    l = [] # FIXME
    print("\tNode: {0}, Result: {1}, Wanted: {2}".format(t[0], l, t[1]))





# CHALLENGE: Find dettached nodes (Print test statements) 
# HINT: Might have to look at numpy documentation




# TODO: Print the adjacency matrix (Print test statements)
# HINT: Might have to look at numpy documentation
print("\nGraph human representation")
print("NOTE: It is okay if the result is off by 1 for each node")
print("TODO") # TODO: Complete and remove this line
