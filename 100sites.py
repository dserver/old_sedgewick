import random
f = open("1000sites.txt", "w")
for i in xrange(0,1000):
	print >>f,"%3d %3d" % (i, random.randint(0,100))
f.close()