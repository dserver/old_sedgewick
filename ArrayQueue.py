
''' A simple array queue class I wrote that operates entirely
on a fixed size array. Methods add and remove seem to work fine'''
class ArrayQueue:

    def __init__(self, size):
        self.q = [None for x in range(0, size)]
        self.fp = 0 # front pointer
        self.e = 0 # end pointer
        self.n = 0 # queue size

    @classmethod
    def fromnothing(cls):
        return cls(3) # initialize class with buffer size of 3

    
    # uses the elementary resize operation when the buffer is full
    def add(self, val):
        #print "inside add"
        #print "%d %d" % (self.n, len(self.q))
        if self.n == len(self.q):
            self.resize_elementary()
            
        # one way is to decrement end
        #self.e = (self.e - 1) % len(self.q)
        # another way is to add n to fp and take modulo (fp + n) mod len
        self.e = (self.fp + self.n) % len(self.q)
        self.q[self.e] = val
        self.n += 1

    def remove(self):
        ret_val = self.q[self.fp]
        self.q[self.fp] = None
        self.fp = (self.fp + 1) % len(self.q)
        self.n -= 1
        return ret_val

    
    # my own implemenation of resize which is simple but
    # inefficient since it requires n removes and n adds, thus 2*n modulo ops
    # and 3*n memory ops. Compare this to resize_efficient
    def resize_elementary(self):
        #print "resize"
        b = ArrayQueue(self.n * 2)
        n = self.n
        while self.n > 0:
            b.add(self.remove())
        self.q = b.q
        self.n = b.n
        self.fp = b.fp
        self.e = b.e

    # requires n memory ops and n modulo ops
    def resize_efficient(self):
        b = ArrayQueue(self.n * 2)
        k = 0
        for k in range(0, self.n):
            b.q[k] = self.q[(self.fp + k) % len(self.q)]
        self.q = b
        self.fp = 0
        self.e = self.fp + self.n-1
        
        
    def __str__(self):
        s = ""
        for x in range(0, len(self.q)):
            s += " " + str(self.q[x])

        return s
            

def test():
    q = ArrayQueue.fromnothing()
    q.add("1")
    q.add("2")
    q.add("3")
    print len(q.q)
    print q.n
    q.add("8")
    print len(q.q)
    print q
    q.remove()
    print q
    q.remove()
    print q
    q.remove()
    print q
    q.add("4")
    print q
    q.remove()
    print q
    q.add("5")
    print q
