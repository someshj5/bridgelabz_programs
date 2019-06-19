class Node:                                 # creating a node class for linked list head
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:                          # creating a class linked list
    def __init__(self):
        self.head = None                   # assigning the initial value of head as None

    def append(self, new_value):            # function defining to append a value in a linked list
        newnode = Node(new_value)
        newnode.next = self.head
        self.head = newnode

    def display(self):                      # function to display the values in the linked list
        temp = self.head
        while temp:
            print (temp.value),
            temp = temp.next

    def search(self,wrd):                  # Function to search for the value in a linked list
        temp = self.head
        while temp:
            if temp.value == wrd:
                return True
            temp = temp.next
        return False

    def remove(self,wrd):                   # function to remove  a value from a linked list
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


l = LinkedList()                             # assigning the object for the linked list

with open('file_word.txt','r') as file1: # opening the text file in read mode as file1
    mylist = file1.read().split()            # to split the words in the text file

for i in mylist:
    l.append(i)                              # appending the words in a linked list
l.display()

User = input('Enter a name to search')       # ask user for input to search a word
if l.search(User):                           # searching the word in the linked list
    l.remove(User)                           # remove the word if found in the linked list
    mylist.remove(User)                      # remove the word from the text file1
    l.display()
    print(mylist)
    with open('file_word.txt','w+') as file1:  # updating the text file1
        for i in mylist:
            file1.write(i)
else:
    l.append(User)                          # add the word if not in the linked list
    mylist.append(User)                     # add the word to the text file1
    with open('file_word.txt','a+') as f1:  # updating the text file
        f1.write('\n')
        f1.write(User)










