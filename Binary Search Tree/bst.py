import binary_search_tree

def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()

tree.insert(3)
tree.insert(5)
tree.insert(10)


