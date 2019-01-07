class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, data=None):
        self.head = node(data)

    def append(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while (last.next):
                last = last.next
            last.next = newNode

    def display(self):
        curNode = self.head
        while (curNode):
            print(curNode.data)
            curNode = curNode.next


list1 = linkedList(0)

list1.append(10)
list1.append(20)

list1.display()
