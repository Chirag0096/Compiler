import ast
import networkx as nx

class ASTGenerator:
    @staticmethod
    def generate(code):
        try:
            tree = ast.parse(code)
            G = nx.DiGraph()
            ASTGenerator.add_nodes(G, tree)
            return G, None
        except SyntaxError as e:
            return None, str(e)

    @staticmethod
    def add_nodes(G, node, parent=None):
        name = str(id(node))
        G.add_node(name, label=type(node).__name__)
        if parent is not None:
            G.add_edge(parent, name)
        for child in ast.iter_child_nodes(node):
            ASTGenerator.add_nodes(G, child, parent=name)
