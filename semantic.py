def type_check(node):
    if node[0] == 'assignment':
        expr_type = type_check(node[2])
        if expr_type != 'integer':
            raise TypeError(f"Expression should be of type 'integer', got '{expr_type}'")
    elif node[0] == 'identifier':
        # Look up the type of the identifier in the symbol table
        ...
    # Handle other node types...