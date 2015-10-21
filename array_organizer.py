#!/usr/bin/python
a = [1,2,4,9,13]
b = [3,4,7,8,20]

def MergeSorted(a,b):
	LA = len(a)
	LB = len(b)
	c = []
	parameter = 0
	
	for i in range(0,len(a)-1):
		
		if a[i] < b[i] and a[i] > parameter:
			c.append(a[i])
			
			if a[i+1]-a[i] <= b[i] - a[i] and a[i] > parameter:
				c.append(a[i+1])
				parameter = a[i+1]
				
			elif a[i+1]-a[i] > b[i] - a[i]:
				c.append(b[i])
				
		
				
				
		elif a[i] > b[i] or a[i] < parameter:
			c.append(b[i])
			if b[i+1]-b[i] <= a[i] - b[i]:
				c.append(b[i+1])
				
			elif b[i+1]-b[i] > a[i]-b[i]:
				c.append(a[i])
				parameter = a[i+1]
	
	if a[len(a)-1] > b[len(b)-1]:
		c.append(b[len(b)-1])
		c.append(a[len(b)-1])
	else:
		c.append(a[len(b)-1])
		c.append(b[len(b)-1])
				
				
			
		
	print(c)
			
MergeSorted(a, b)

[1,2,4,7,8,9,13,20]

#a[i] > b[i] and