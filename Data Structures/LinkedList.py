#Creating Node
class node :
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    
#Singly Linked List
class slinkedlist():
    def __init__(self):
        self.head = node()

    def append(self, data):
        NewNode = node(data)
        cur = self.head
        while cur.nextval != None:
            cur = cur.nextval
        cur.nextval = NewNode

    def length(self):
        cur = self.head
        count = 0
        while cur.nextval != None:
            count += 1
            cur = cur.nextval
        return count

    def display(self):
        datalist = []
        cur = self.head
        while cur.nextval != None:
            cur = cur.nextval
            datalist.append(cur.dataval)
        return datalist

    def getdata(self, index):
        if index >= self.length():
            return "Index out of range"
        
        i = 0
        cur = self.head
        while cur.nextval != None:
            cur = cur.nextval
            if i == index:
                return cur.dataval
            i = i+1

    def insert(self, index, data):
        if index > self.length():
            return "Index out of range."
        
        elif index == self.length():
            self.append(data)
            return "Node Added"

        NewNode = node(data)
        i = 0
        cur = self.head
        while cur.next != None:
            LastNode = cur
            cur = cur.nextval
            if i == index:
                LastNode.next = NewNode
                NewNode.nextval = cur
                return "Node Added"
            i += 1

    def remove(self, index):
        if index >= self.length():
            return "Index out of range."
        i = 0
        cur = self.head
        while cur.next != None:
            LastNode = cur
            cur = cur.nextval
            if index == i:
                LastNode.nextval = cur.nextval
                return "Node Removed"
            i += 1



        





