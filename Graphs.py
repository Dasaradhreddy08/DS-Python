class Graphsds:
    def __init__(self, edges):
        self.edges = edges
        self.graphs_dict = {}
        self.starts = []
        self.ends = []
        for start, end in self.edges:
            if start in self.graphs_dict:
                self.graphs_dict[start].append(end)
            else:
                self.graphs_dict[start] = [end]
            if end not in self.ends:
                self.ends.append(end.strip())
        self.starts = list(self.graphs_dict.keys())

        print(self.graphs_dict)

    def getpath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphs_dict:
            return []
        paths = []
        for node in self.graphs_dict[start]:
            if node not in path:
                new_paths = self.getpath(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths




    def get_nodes(self):
        return set(self.starts+self.ends)


if __name__ == "__main__":
    routes = [
        ("Hyderabad", "Delhi"),
        ("Hyderabad", "Mumbai"),
        ("Delhi", "Kolkata"),
        ("Delhi", "Amritsar"),
        ("Vijayawada", "Delhi"),
        ("Vijayawada", "Hyderabad"),
        ("Mumbai", "Delhi"),
        ("Mumbai", "Kolkata"),
        ("Pune", "Mumbai")
    ]

    route_graph = Graphsds(routes)
    print(route_graph.get_nodes())
    print(route_graph.getpath("Hyderabad","Kolkata"))
    print(route_graph.getpath("Amritsar","Kolkata"))


