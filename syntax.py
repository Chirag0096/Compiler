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

def parse_print_statement(tokens):
    """
    Parses a single print statement from a list of tokens.

    Args:
        tokens (list[Token]): A list of tokens representing the code.

    Returns:
        Node: The root node of the parse tree.
    """

    if len(tokens) < 3 or tokens[0].value != 'print':
        raise SyntaxError("Invalid print statement")

    root = Node(tokens[0])  # Node for 'print'

    # Check for parentheses
    if tokens[1].value != '(':
        raise SyntaxError("Missing '(' in print statement")

    lparen_node = Node(tokens[1])  # Node for '('
    root.children.append(lparen_node)

    # Parse the expression (a + b)
    expr_node = parse_expression(tokens[2:])  # Pass remaining tokens
    root.children.append(expr_node)

    # Check for closing parenthesis
    if tokens[-1].value != ')':
        raise SyntaxError("Missing ')' in print statement")

    rparen_node = Node(tokens[-1])  # Node for ')'
    root.children.append(rparen_node)

    return root

def parse_expression(tokens):
    """
    Parses a simple arithmetic expression (a + b).

    Args:
        tokens (list[Token]): A list of tokens representing the expression.

    Returns:
        Node: The root node of the parse tree for the expression.
    """

    if len(tokens) < 3:
        raise SyntaxError("Invalid expression")

    left_node = Node(tokens[0])  # Node for 'a' (or any left operand)
    root = Node(tokens[1])  # Node for '+' (or any operator)
    right_node = Node(tokens[2])  # Node for 'b' (or any right operand)

    root.children.append(left_node)
    root.children.append(right_node)

    return root

def print_parse_tree(node, indent=0):
    """
    Prints the parse tree structure in a readable format.

    Args:
        node (Node): The root node of the parse tree.
        indent (int, optional): The indentation level for printing. Defaults to 0.
    """
    print(" " * indent, end="")
    if node.token:
        print(node.token.value)
    else:
        print("<empty>")
    for child in node.children:
        print_parse_tree(child, indent + 2)

def main():
    code = "print(a+b)"  # Assuming input is taken elsewhere
    tokens = [
        Token(type='IDENTIFIER', value='print', lineno=1, index=0, end=5),
        Token(type='LPAREN', value='(', lineno=1, index=5, end=6),
        Token(type='IDENTIFIER', value='a', lineno=1, index=6, end=7),
        Token(type='PLUS', value='+', lineno=1, index=7, end=8),
        Token(type='IDENTIFIER', value='b', lineno=1, index=8, end=9),
        Token(type='RPAREN', value=')', lineno=1, index=9, end=10),
    ]

    try:
        parse_tree = parse_print_statement(tokens)
        print("Parse Tree:")
        print_parse_tree(parse_tree)
    except SyntaxError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
