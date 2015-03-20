from ParseSites import parse_sites
import random
import time

def swap(a_list, pos1, pos2):
	temp = a_list[pos1]
	a_list[pos1] = a_list[pos2]
	a_list[pos2] = temp
	return a_list
	

def selection_sort(a_list):
	for l in xrange(len(a_list)):
		for m in xrange(l, len(a_list)):
			if a_list[m]<a_list[l]:
				swap(a_list, l, m)

def insertion_sort(a_list):
	sorted_start = 0
	while (sorted_start != len(a_list)-1):
		j = sorted_start + 1
		number = a_list[j] # number is the value to insert in the list
		while (number < a_list[j] and j > 0):
			j -= 1
		
		sorted_start += 1

def create_numbers(size):
	f = open(str(size) + "numbers.txt", "w")
	for i in xrange(0, size):
		print >>f, "%6d" % (random.randint(0, 10000))

# shift a_list one to the right starting from b to c
def shift_list(a_list, b, c):
	print a_list
	print "b: %3d \t c: %3d" % (b, c)
	for x in range(b, c-1, -1):
		temp = a_list[x+1]
		a_list[x+1] = a_list[x]
	return a_list
		
if __name__ == "__main__":
	# ln = []
	# with open("10000numbers.txt", "r") as f:
		# line = f.readline()
		# n = parse_sites(line)
		# ln.append(n[0])
	# start = time.time()
	# selection_sort(ln)
	# print "%d seconds for 10,000 numbers" % (time.time() - start)
	
	ln = [8, 7, 5, 30, 1]
	insertion_sort(ln)
	print ln

	