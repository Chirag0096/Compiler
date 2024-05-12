class Token:
    def __init__(self, type, value, lineno, index, end):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.index = index
        self.end = end

class Node:
    def __init__(self, token=None, children=None):
        self.token = token
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)

    def to_graphviz(self, dot=None):
        if dot is None:
            dot = Digraph()

        if self.token:
            dot.node(str(id(self)), self.token.value)
        else:
            dot.node(str(id(self)), "<empty>")

        for child in self.children:
            child_node = child.to_graphviz(dot)
            dot.edge(str(id(self)), str(id(child_node)))

        return dot

class SemanticNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return self.value

def build_semantic_tree(parse_tree):
    semantic_root = SemanticNode(parse_tree.token.value)
    for child in parse_tree.children:
        if child.token:
            semantic_root.add_child(SemanticNode(child.token.value))
        else:
            semantic_root.add_child(build_semantic_tree(child))
    return semantic_root

def build_ast(parse_tree):
    if parse_tree.token and parse_tree.token.value in ['+', '-', '*', '/']:
        operator = parse_tree.token.value
        left = build_ast(parse_tree.children[0])
        right = build_ast(parse_tree.children[1])
        return SemanticNode(operator, [left, right])
    elif parse_tree.token and parse_tree.token.value == 'print':
        return build_ast(parse_tree.children[0])
    else:
        return SemanticNode(parse_tree.token.value)

def main():
    # Parse tree obtained from the example
    parse_tree = Node(Token(type='IDENTIFIER', value='print', lineno=1, index=0, end=5))
    parse_tree.add_child(Node(Token(type='LPAREN', value='(', lineno=1, index=5, end=6)))
    plus_node = Node(Token(type='PLUS', value='+', lineno=1, index=7, end=8))
    plus_node.add_child(Node(Token(type='IDENTIFIER', value='a', lineno=1, index=6, end=7)))
    plus_node.add_child(Node(Token(type='IDENTIFIER', value='b', lineno=1, index=8, end=9)))
    parse_tree.add_child(plus_node)
    parse_tree.add_child(Node(Token(type='RPAREN', value=')', lineno=1, index=9, end=10)))

    # Build semantic tree
    semantic_tree = build_semantic_tree(parse_tree)
    print("Semantic Tree:")
    print(semantic_tree)

    # Build AST
    ast = build_ast(parse_tree)
    print("\nAbstract Syntax Tree:")
    print(ast)

if __name__ == "__main__":
    main()
