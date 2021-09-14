import networkx as nx

"""
Build the corresponding nondirected graph without weight from an input.
"""

# ---------------------------------------------------------------------------------

first_line = input().split() # First line from input, we need to introduce the number of nodes and the number of edges.

node = int(first_line[0]) # Nodes
edge = int(first_line[1]) # Edges

# ---------------------------------------------------------------------------------

graph = nx.Graph() # Create the graph

for i in range(node):
    graph.add_node(i+1) # Insert the nodes
    
# ---------------------------------------------------------------------------------

visible_nodes = 0

while visible_nodes != edge:

    linea = input().split() # We input the edges of the graph

    node_1 = int(linea[0])
    node_2 = int(linea[1])

    graph.add_edge(node_1, node_2)

    visible_nodes += 1
    
# ---------------------------------------------------------------------------------
# Check the results

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges())

# ---------------------------------------------------------------------------------
