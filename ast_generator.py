import ast
from graphviz import Digraph

class ASTGenerator:
    @staticmethod
    def generate(code):
        try:
            tree = ast.parse(code)
            dot = Digraph()
            ASTGenerator.add_nodes(dot, tree)
            return dot, None
        except SyntaxError as e:
            return None, str(e)

    @staticmethod
    def add_nodes(dot, node, parent=None):
        name = str(id(node))
        label = type(node).__name__
        dot.node(name, label)
        if parent is not None:
            dot.edge(parent, name)
        for child in ast.iter_child_nodes(node):
            ASTGenerator.add_nodes(dot, child, parent=name)
