import random

class UnionFind:
	def __init__(self):
		self._id = []
		self._count = 0 # number of components
	
	# Initializes each component id[i] with node i
	def UF(self, N):
		self._count = N
		self._id = [i for i in xrange(N)]
	
	def count(self):
		return self._count
	
	# retuns true of false if p is connected to q
	def connected(self, p, q):
		return self.find(p) == self.find(q)
	
	# returns the component identifier for p.
	def find(self, p):
		return self._id[p]
	
	
	# joins the components that p and q belong to
	def union_slow(self, p, q):
		if self.connected(p, q): # 2 array reads
			return # nothing to do if p and q are in the same component
		else:
			# 2 array reads
			pCom = self.find(p) # get p's component id.
			qCom = self.find(q) # get q's component id
			
			# loops N-1 times, 2 array accesses each time
			for i in xrange(0, len(self._id)):
				if self._id[i] == qCom: # if the i'th site equals q's component
					self._id[i] = pCom # switch it to p's component
			self._count -= 1 # decrement the number of components
			return
	
	# returns the component identifier for p.
	def find_quick(self, p):
		while (self._id[p] != p):
			p = self._id[p]
		return p
	
	# joings the components that p and q belong to
	def union_quick(self, p, q):
		if (self._id[p] == q):
			return # nodes are already connected
		
		pRoot = self.find_quick(p)
		qRoot = self.find_quick(q)
		
		self._id[pRoot] = qRoot
		self._count -= 1
		return
		
# tests UnionFind on a number of sites specified by size.
# Uses random to create [p,q] q for each p
def union_test(size):
	uf = UnionFind()
	uf.UF(100)
	components = []
	for i in xrange(0,size):
		c = [i, random.randint(0,size)]
		components.append(c)
		
	for component in components:
		uf.union_slow(component[0], component[1])
	
	print uf._count

def union_quick_test():
	pass
	

if __name__ == "__main__":
	uf = UnionFind()
	uf.UF(100)
	components = []
	for i in xrange(0,100):
		c = [i, random.randint(0,100)]
		components.append(c)
		
	for component in components:
		uf.union_slow(component[0], component[1])
	
	print uf._count
	i = raw_input()
