import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
visited_vertices = []

def process(vertex) :
    visited_vertices.append ( vertex )


def graphTraversal(G, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            process(vertex)
            for neighbor in G[vertex]:
                stack.append(neighbor)

G =  {
    'A':['B','C'],
    'B':['A', 'D', 'E'],
    'C':['A', 'F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

graphTraversal(G, 'A')
nx.draw(G)
plt.savefig("C:\\USERS\\KAREN\\abc.jpeg")
print(visited_vertices)

# ['A', 'C', 'F', 'E', 'B', 'D']