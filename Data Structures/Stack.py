class stack: #Class 
    arr = [] #member item

    def push(self, item): #Member function to add an element to stack
        self.arr.append(item)

    def spop(self): #Member function to remove an element from stack
        if(len(self.arr) > 0):
            return self.arr.pop() #It will return the element removed
        else:
            return #If stack is empty then it will return 'None'

    def display(self): #Member function to display items in stack
        print(self.arr)


x = stack() #Object of class Stack
x.push(1) #Pushing 1 to Stack
x.push(2) #Pushing 2 to stack
x.display() #Displaying items in stack
x.spop() #Popping last element, here 2, from stack
x.display() 
print(x.spop()) #Popping last element, here 1, from stack
print(x.spop()) #As no element is present in stack now, it will return 'None'
