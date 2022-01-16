from collections import namedtuple

Edge = namedtuple('Edge', ['src', 'dest', 'weight'])

class WeightedGraph:
    def __init__(self, edges):
        self.adj_list = {}

        for Edge in edges:
            if Edge.src not in self.adj_list:
                self.adj_list[Edge.src] = []
            if Edge.dest not in self.adj_list:
                self.adj_list[Edge.dest] = []
            self.adj_list[Edge.src].append((Edge.dest, Edge.weight))
            self.adj_list[Edge.dest].append((Edge.src, Edge.weight))

    def print(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}:", end="")
            for edge in edges:
                print(f" ({edge[0]}, W:{edge[1]})", end="")
            print()

    def BFS(self, root):
        visited = set()
        queue = []
        visited.add(root)
        queue.append(root)

        print("BFS:")
        while len(queue) > 0:
            vertex = queue.pop(0)
            print(f"\t{vertex}")
            for neighbor, _ in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def DFS_recursive(self, node, visited=None):
        if visited is None:
            print("DFS:")
            visited = set()
        visited.add(node)
        print(f"\t{node}")
        for neighbor, _ in self.adj_list[node]:
            if neighbor not in visited:
                self.DFS_recursive(neighbor, visited)

    def DFS_iterative(self):
        pass 

def main():
    edges = [
        Edge("A", "B", 1),
        Edge("A", "C", 2),
        Edge("B", "B2", 3),
        Edge("B", "B3", 3),
    ]

    graph = WeightedGraph(edges)
    graph.print()
    graph.BFS("A")
    graph.DFS_recursive("A")

if __name__ == "__main__":
    main()