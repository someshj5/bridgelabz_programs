class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        newnode = Node(new_value)
        newnode.next = self.head
        self.head = newnode

    def insert_at_index (self, index, value):
        if index == 1:
            new_node = Node(value)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def display(self):
        temp = self.head
        while temp:
            print (temp.value),
            temp = temp.next


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

l = LinkedList()


with open('/home/admin9/Week2/Data structures/hashfile.txt','r') as f3:
    User = f3.read().split()
    for i in User:
        rem = int(i) % 11
        l.append(rem)

