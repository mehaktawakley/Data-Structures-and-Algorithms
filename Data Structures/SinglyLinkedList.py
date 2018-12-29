class Node:
    def __init__(self, data = None):
            self.data = data
            self.next = None

class SLinkedList:
    def __init__(self):
            self.head = Node()

    def append(self, data):
            new_node = Node(data)
            cur = self.head
            while cur.next != None:
                    cur = cur.next
            cur.next = new_node

    def length(self):
            cur = self.head
            count = 0
            while cur.next != None:
                    count += 1
                    cur = cur.next
            return count

    def display(self):
            elements = []
            cur = self.head
            while cur != None:
                    elements.append(cur.data)
                    cur = cur.next
            return elements

    def get(self, index):
            if index >= self.length():
                    return "ERROR : index out of range!"
            idx = 0
            cur = self.head
            while cur.next != None:
                    cur = cur.next
                    if idx == index:
                            return cur.data
                    idx += 1

    def delete(self, index):
            if index >= self.length():
                    return "ERROR : index out of range!"
            idx = 0
            cur = self.head
            while cur.next != None:
                    last_node = cur
                    cur = cur.next
                    if idx == index:
                            last_node.next = cur.next
                            return "Node Deleted"
                    idx += 1

    def insert(self, index, value):
            if index > self.length():
                    return "ERROR : index out of range!"
            elif index == self.length():
                    self.append(value)
                    return "Node Added"
            new_node = Node(value)
            idx = 0
            cur = self.head
            while cur.next != None:
                    last_node = cur
                    cur = cur.next
                    if idx == index:
                            last_node.next = new_node
                            new_node.next = cur
                            return "Node Added"
                    idx += 1

#Creating linked list
l1 = SLinkedList()

#Adding head value and elements
l1.head = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
e5 = Node("Friday")

#Linking first node to second node
l1.head.next = e2

#Linking second node to third node and third node to forth node
e2.next = e3
e3.next = e5

#Displaying List
print("Initial Elements: ",*l1.display())

#Inserting an element at end
l1.append("Sunday")
print("After Appending An Element In List: ",*l1.display())

#Inserting an element in middle and at the end of linked list
l1.insert(2,"Thursday")
l1.insert(4,"Saturday")

print("After Adding Elements In List At Specified Positions: ",*l1.display())

#Getting an element
print("Display Element At Specified Position: ",l1.get(3))

#Deleting an element
l1.delete(1)
print("After Deleting An Element: ",*l1.display())
