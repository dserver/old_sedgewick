
try:
	''' list indices when splitting the list in two '''
	# To help remember bounds checking when splitting a list using n/2 and floor
	for x in range(0, 30):
		l = [y for y in range(0, x)]
		print "#############################"
		print l
		print str(len(l)/2) + "    n = " + str(len(l))
		print "0..."+str(len(l)/2 - 1) + "    " + str(len(l)/2) + "..." + str(len(l)-1)
		


	''' Circular array indices visualization '''
	# Sets a dictionary with key values as 'memory addresses' and values as list indices
	max_len = 6
	d = {}
	for x in range(0,max_len):
		d[x] = (x-4) % max_len

	front_pointer = None
	back_pointer = None
	for s in d:
		st = "memory address: " + str(s)
		st += "     list index: " + str(d[s])
		if d[s] == 0:
			st += " <-- Front pointer"
			front_pointer = s
		if d[s] == max_len-1:
			st += " <-- Back pointer"
			back_pointer = s
		print st
		st = ""
		
	for x in range(0, max_len):
		st = "list index: " + str(d[(front_pointer+x) % max_len])
		st += "     memory address: " + str((front_pointer+x) % max_len)
		st += "     modulo operation = front_pointer+x) % max_len = " + str((front_pointer+x) % max_len)
		print st

except Exception as e:
	print e
	stop = raw_input()
	
stop = raw_input()