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

with open('/home/admin9/Week2/Data structures/file_word.txt','r') as file1:
    mylist = file1.read().split()

for i in mylist:
    l.append(i)
l.display()

User = input('Enter a name to search')
if l.search(User):
    l.remove(User)
    mylist.remove(User)
    l.display()
    print(mylist)
    with open('/home/admin9/Week2/Data structures/file_word.txt','w+') as file1:
        for i in mylist:
            file1.write(i)
else:
    l.append(User)
    mylist.append(User)
    with open('/home/admin9/Week2/Data structures/file_word.txt','a+') as f1:
        f1.write('\n')
        f1.write(User)










