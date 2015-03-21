class ArrayDequeue:
    def __init__(self, size):
        self.q = [None for x in range(0, size)] # the array buffer to store elements
        self.fp = 0 # points to the front element
        self.e = 0 # points to the last element
        self.n = 0 # the number of items in the buffer

    @classmethod
    def fromnothing(cls):
        cls(3) # initialize buffer of size 3
