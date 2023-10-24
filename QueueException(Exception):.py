class EmptyQueueException(Exception):
    pass

class FullQueueException(Exception):
    pass



class ArrayDeque:
    CAPACITY = 16
    
    def __init__(self):
        self._data = [None] * ArrayDeque.CAPACITY
        self._r = 0
        self._f = 0
        
    def __str__(self):
        return self._data.__str__()
    
    def size(self):
        return (self._r - self._f) % self.CAPACITY
        
    
    def isEmpty(self):
        return self._r == self._f
        

    def rear(self):
        if self.isEmpty():
            raise EmptyQueueException
        
        return self._data[self._r]
    
                  
    def front(self):
        if self.isEmpty():
            raise EmptyQueueException
        
        return self._data[self._f]
    

    def addRear(self, element):
        if self.size() == self.CAPACITY - 1:
            raise FullQueueException
        
        self._data[self._r] = element
        self._r = (self._r + 1) % self.CAPACITY

    def removeRear(self):
        if self.isEmpty():
            raise EmptyQueueException

        self._r = (self._r - 1) % self.CAPACITY
        value = self._data[self._r]
        self._data[self._r] = None
        return value

    def addFront(self, element):
        if self.size() == self.CAPACITY - 1:
            raise FullQueueException
        
        self._f = (self._f - 1) % self.CAPACITY
        self._data[self._f] = element

    def removeFront(self):
        if self.isEmpty():
            raise EmptyQueueException

        value = self._data[self._f]
        self._data[self._f] = None
        self._f = (self._f + 1) % self.CAPACITY
        return value



##b)
def check_palindrome_deque(S):
    d = ""
    a = ArrayDeque()
    for x in range(0,len(S)):
        a.addFront(S[x])
    while a.isEmpty() == False:
        d = d + a.removeFront()
    if S == d:
        return True
    else: 
        return False