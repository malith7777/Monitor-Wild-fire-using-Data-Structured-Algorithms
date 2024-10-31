class DSAHashEntry:
    class State:
        FREE = 0
        USED = 1
        PREVIOUSLY_USED = 2
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.state = DSAHashEntry.State.USED
    
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state


class DSAHashTable:
    def __init__(self, maxSize):
       self.maxSize = maxSize
       self.hashArray = [None] * maxSize
       self.count = 0
       self.loadFactorThreshold = 0.75
       self.shrinkFactorThreshold = 0.25
    
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def next_prime(self, num):
        next_num = num + 1
        while not self.is_prime(next_num):
            next_num += 1
        return next_num   
    
    def hash(self, key):
        hash_val = 0
        for char in key:
            hash_val = 37 * hash_val + ord(char)
        hash_val %= self.maxSize
        if hash_val < 0:
            hash_val += self.maxSize
        return hash_val
    
    def put(self, key, value):
        if self.count >= self.loadFactorThreshold * self.maxSize:
            self.resize(self.maxSize * 2)
        hashVal = self.hash(key)
        index = hashVal % self.maxSize
        stepSize = 1 + (hashVal % (self.maxSize - 2))
        while self.hashArray[index] is not None and self.hashArray[index].getState() != DSAHashEntry.State.FREE:
            if self.hashArray[index].getState() == DSAHashEntry.State.USED and self.hashArray[index].getKey() == key:
                self.hashArray[index].setValue(value)
                return
            index = (index + stepSize) % self.maxSize
        self.hashArray[index] = DSAHashEntry(key, value)
        self.count += 1

    def get(self, key):
        index = self.find(key)
        if index == -1:
            return None
        return self.hashArray[index].getValue()

    def hasKey(self, key):
        hash_val = self.hash(key)
        while self.hashArray[hash_val] is not None:
            if (
               self.hashArray[hash_val].getKey() == key
               and self.hashArray[hash_val].getState() == DSAHashEntry.State.USED
            ):
               return True
            hash_val = (hash_val + 1) % len(self.hashArray)
        return False

    
    def remove(self, key):
        index = self.find(key)
        if index == -1:
            return
        self.hashArray[index].setState(DSAHashEntry.State.PREVIOUSLY_USED)
        self.count -= 1
        if self.count < self.shrinkFactorThreshold * self.maxSize:
            self.resize(self.maxSize // 2)

    def find(self, key):
        hashVal = self.hash(key)
        index = hashVal % self.maxSize
        stepSize = 1 + (hashVal % (self.maxSize - 2))
        while self.hashArray[index] is not None:
            if self.hashArray[index].getState() == DSAHashEntry.State.USED and self.hashArray[index].getKey() == key:
                return index
            index = (index + stepSize) % self.maxSize
        return -1


    def export(self):
        export_list = []
        for entry in self.hashArray:
            if entry is not None and entry.getState() == DSAHashEntry.State.USED:
                export_list.append(entry.getKey())
        return export_list
    

    
    def resize(self, newMaxSize):
        newTable = DSAHashTable(newMaxSize)
        for entry in self.hashArray:
            if entry is not None and entry.getState() == DSAHashEntry.State.USED:
                newTable.put(entry.getKey(), entry.getValue())

        self.maxSize = newTable.maxSize
        self.hashArray = newTable.hashArray

    
