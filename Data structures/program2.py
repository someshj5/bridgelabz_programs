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



    def ordered(self):
        for i in range(0, 8):
            if self.head is None:
                newnode = Node
                self.head = newnode
                temp = self.head
                while temp != None:
                    if temp.value > temp.next.value:
                        newnode.next = temp
                        self.head = newnode
                        # temp.value, temp.next.value = temp.next.value , temp.value
                    # temp = temp.next
                else:
                    prev = self.head
                    while temp != None:
                        if temp.value > value:
                            newnode.next = prev.next
                            prev.next = newnode
                        prev = temp
                        temp = temp.next
                        prev.next = newnode


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
            return temp.value

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

with open('/home/admin9/Week1/Data structures/file_num.txt','r') as f2:
    mydata = f2.read().split()
    print(mydata)
    for i in mydata:
        link.insert(i)
        # print(i)
        link.ordered()
    link.display()
# link.pop()
# link.display()
# mylist = link.sort()