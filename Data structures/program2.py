class Node:

    def __init__(self, data):                  # Constructor to initialize the node object
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):                         # Function to initialize head
        self.head = None

    def sortedInsert(self, new_node):
        if self.head is None:                   # Special case for the empty linked list
            new_node.next = self.head
            self.head = new_node

        elif self.head.data >= new_node.data:   # Special case for head at end
            new_node.next = self.head
            self.head = new_node
        else:                                   # Locate the node before the point of insertion
            current = self.head
            while(current.next is not None and
            current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def search(self, wrd):                  # Function to search for the value in a linked list
        temp = self.head
        while temp:
            if temp.data == wrd:
                return True
            temp = temp.next
        return False

    def push(self, new_data):                     # Function to insert a new node at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, wrd):                   # function to remove  a value from a linked list
        prev = None
        temp = self.head
        while temp:
            if temp.data == wrd:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return True
            prev = temp
            temp = temp.next
        return False

    def printList(self):                          # Utility function to print the linked LinkedList
      temp = self.head
      while temp:
        print(temp.data),
        temp = temp.next


link = LinkedList()                                # assigning the object

with open('/home/admin9/Week1/Data structures/file_num.txt','r') as f2: # open the text file in read mode as f2
    mydata = f2.read().split()
    print(mydata)
    for i in mydata:
        i = int(i)
        newnode = Node(i)                                           # inserting the data in the linked list
        link.sortedInsert(newnode)                                  # functioncall sorting the data into the linked list

link.printList()


User = int(input('Enter a value: '))                         # ask user for a value to check
if link.search(User):                                        # checks the value presen or absent into the sorted linkedlist
    link.remove(User)                                        # removes the value if present in the link list
    mydata.remove(str(User))
    with open('/home/admin9/Week1/Data structures/file_num.txt','w+') as f2: # updating the values into the text file
        for i in mydata:
            f2.write('\n')
            f2.write(i)
else:                                                        # checks value if not present in the link list
    User = int(User)
    link.push(User)                                          # push the value into the link list
    mydata.append(User)
    with open('/home/admin9/Week1/Data structures/file_num.txt','a') as f2: # updating the list in the text file
        f2.write('\n')
        f2.write(str(User))