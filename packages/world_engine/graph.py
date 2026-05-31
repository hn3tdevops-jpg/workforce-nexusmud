import networkx as nx

class WorldGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self._initialize_graph()

    def _initialize_graph(self):
        # Add initial nodes and edges
        self.graph.add_node("town_square")
        self.graph.add_node("north_gate")
        self.graph.add_node("south_alley")
        
        self.graph.add_edge("town_square", "north_gate")
        self.graph.add_edge("town_square", "south_alley")

    def get_neighbors(self, node_id: str) -> list:
        return list(self.graph.neighbors(node_id))
