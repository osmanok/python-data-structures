import node

class linkedList:
    def __init__(self, data=None):
        self.head = node(data)

    def inserAtBegining(self, newData):
        newNode = node(newData)
        newNode.next = self.head
        self.head = newNode

    def inserEnd(self, newData):
        newNode = node(newData)
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = newData

    def display(self):
        while self.head != None:
            print(self.head.data)