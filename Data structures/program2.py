class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, nw_value):
        newnode = Node(nw_value)
        newnode.next = self.head
        self.head = newnode



    # def append(self, new_value):
    #     newnode = Node(new_value)
    #     newnode.next = self.head
    #     self.head = newnode

    def display(self):
        temp = self.head
        while temp:
            print (temp.value),
            temp = temp.next

    def pop(self):
        temp = self.head
        if temp is None:
            return
        else:
            popped = temp.value
            temp = temp.next
        # prev = None
        # temp = self.head
        # while temp:
        #     prev = temp
        #     temp = temp.next
        # if pos == None:
        #     self.head = temp.next
        # # else:
        # #     prev.next = temp.next


    def search(self,wrd):
        temp = self.head
        while temp:
            if temp.value == wrd:
                return True
            temp = temp.next
        return False

    def remove(self,wrd):
        prev = None
        temp = self.head
        while temp:
            if temp.value == wrd:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return True
            prev = temp
            temp = temp.next
        return False

link = LinkedList()

with open('/home/admin9/Week2/Data structures/file_num.txt','r') as f2:
    mydata = f2.read().split()
    link.insert(mydata)
    link.pop()
    link.display()