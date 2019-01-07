import node

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child == node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        return False

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node:
            return cur_node
        elif value<cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if node == None or self.find(node, value) == None:
            return None

        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0
            if n.left_child != None: num_children += 1
            if n.right_child != None: num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        if node_children == 0:
            if node_parent != None :
                if node_parent.left_child == node:
                    node_parent.left_child = None
                if node_parent.right_child == node:
                    node_parent.right_child = None
            else:
                self.root = None

        if node_children == 1:
            if node.left_child != None:
                child = node.left_child
            if node.right_child != None:
                child = node.right_child

            if node_parent != None:
                if node_parent.left_child == node:
                    node_parent.left_child = child
                if node_parent.right_child == node:
                    node_parent.right_child = child

            else:
                self.root = child

            child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right_child)
            node.value = successor.value
            self.delete_node(successor)