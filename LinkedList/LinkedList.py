
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    
    # Add new data in LinkedList
    def append(self, data):
        # if LinkedList is empty
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        # if LinkedList is not empty
        else:
            self.last.next = Node(data)
            self.last  = self.last.next
        
    # Print the LinkedList
    def display(self):
        current = self.head
        counter = 0
        while current is not None:
            print(current.data,"---",end='')
            current = current.next
            counter += 1
        print()
        print("Total data point: ", counter)
# Driver Code 
linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.display()