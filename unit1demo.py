import math 
def dist2pt(x1, y1, x2, y2):
	x_dist = x2 - x1 
	y_dist = y2 - y1
	return math.sqrt(x_dist**2 + y_dist**2)

print(dist2pt(0, 0, 5, 5)) 

def harmonicmean4(a, b, c, d): 
	n = 4
	sum = (1/a) + (1/b) + (1/c) + (1/d)
	return n/sum 
print(harmonicmean4(8, 9, 10, 11))
