
import random

def ToReducedRowEchelonForm( M):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
		
def print_matrix(mtx):
	for rw in mtx:
		print ', '.join( (str(rv) for rv in rw) )

def add_rows(m, r1, r2):
	for k in range(0, len(m[r1])):
		m[r1][k] += m[r2][k]
		
def multiply_row(row, factor):
	for x in xrange(0, len(row)):
		row[x] = row[x] * factor
		
# assume minimum of two rows
def RREFtoREF(mtx):
	for k in range(0, len(mtx[0])-1):
		add_rows(mtx, k, k+1)
		multiply_row(mtx[k], random.randint(2,10))
	multiply_row(mtx[k], random.randint(2,13))
	
	
def visualize_matrix(m):
	print_matrix(m)
	ToReducedRowEchelonForm(m)
	RREFtoREF(m)
	print "First Row Echelon Form"
	print_matrix(m)
	
	ToReducedRowEchelonForm(m)
	print "Reduced Echelon Form"
	print_matrix(m)