def tree(nodes):
    """
    Construct a plan tree with `inputs` references from list of lists form.
    """
    for c in nodes[1:]:
        nodes[0]._inputs.append(tree(c))
    return nodes[0]


def execute(query):
    """
    Given a plan node with references to its children, execute the query.
    """
    for record in query:
        yield record
