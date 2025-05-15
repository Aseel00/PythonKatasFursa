
def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise
    """
    if not tree_map:
        return False

        # Step 1: Find all nodes and children



    key_id =[]
    children=[]
    root=[]
    counter = 0
    for key in tree_map.keys():
        if key not in key_id:
            key_id.append(key)

    for child in tree_map.values():
        for id in child:
            if id not in children:
                children.append(id)
        counter+=len(child)
    for id in key_id:
        if id not in children:
            root.append(id)
    #print(f"root len is {len(root)}")
    if len(root)!= 1:
        return False

    if counter >= len(children)+1:
        return False
    return True




if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }
    #false_tree={"A":["B"], "C":["D"], "B":[],"D":[]}
    #print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    #print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False
    print(f"Is valid tree: {is_valid_git_tree(false_tree)}")