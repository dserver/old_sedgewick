
def isnumber(c):
	try:
		int(c)
	except (ValueError, TypeError):
		return False
	return True

def parse_sites(line):
	start = 0
	end = 0
	i=0
	number = False
	prev_char = None
	numbers = []
	for char in line:
		print "i: %3d\t start:%2d\t end:%2d\t char:%c" % (i, start, end, char)
		if (i>0):
			prev_char = line[i-1]
		
		if (isnumber(char)):
			if prev_char == ' ' or prev_char is None:
				start = i
				end = start
			else:
				end += 1
		elif (isnumber(prev_char)):
			numbers.append(line[start:end+1])
		else:
			pass
		i += 1
	if isnumber(prev_char):
		numbers.append(line[start:end+1])
	return numbers
if __name__ == "__main__":
	test_line = "  30  900"
	nums = []
	p= parse_sites(test_line)	
	print p