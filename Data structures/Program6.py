class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashing_func(self, key):
        return int(key) % 11

    def insert(self, key):
        hash_key = self.hashing_func(key)

    def get(self, key):
        startslot = self.hashing_func(key)

        data = key
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # position = self.rehash(position, len(self.slots))
                # if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)
h = HashTable()

with open('/home/admin9/Week2/Data structures/hashfile.txt','r') as f3:
    User = f3.read().split()

    for i in User:
        h.hashing_func(i)
        h.insert(i)
        print(h.__getitem__(i))

