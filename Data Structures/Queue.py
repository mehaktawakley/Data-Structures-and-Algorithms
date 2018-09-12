"""
Queue is a data structure which follows first in first out methodology i.e. item stored first will be removed first.
One end is used to insert element (enqueue) and other end used to remove data (dequeue).
"""

class Queue: #Creating an class to implement Queue
    arr = [] #Creating an array to store elements of queue

    def enqueue(self,item): #Function to add element in queue
        self.arr.append(item)

    def dequeue(self): #Function to remove element from queue
        if (len(self.arr) > 0):
            ditem = self.arr[0]
            del self.arr[0] #First element is removed in queue, then second and so on
            return ditem
        else:
            return

    def display(self): #Function to display elements of queue
        print(self.arr)

x = Queue() #Object of queue class
x.enqueue(1) #Adding element to queue
x.enqueue(2) #Adding element to queue
x.enqueue(3) #Adding element to queue
x.enqueue(4) #Adding element to queue
x.display() #Displaying elements of queue
x.dequeue() #Removing element from queue
x.enqueue(5) #Adding element to queue
print(x.dequeue()) #Removing element from queue
print(x.dequeue()) #Removing element from queue
x.display() #Displaying elements of queue
