import math
a = map(int, raw_input().split(','))
b = map(int, raw_input().split(','))

r = a[0] #radius
h = a[1] #height
s = a[2] #initial height of starting point

d = b[0] #if -ve then on top surface else on cylinder
g = b[1] #angle that the arc forms

def side_t(b, c, angle):
	res = math.sqrt((b*b)+(c*c)-(2*b*c*math.cos(angle)))
	return res

if(g > 180):
	g = 360-g

pi = 3.1415926535897
sum_ = 0
if (d>0):
	if(d>=s):
		sum1 = (d-s) + ((2*pi*r*g)/360)
		s2 = ((2*pi*r*g)/360)
		sum2 = math.sqrt(((d-s)**2)+(s2**2))
		if(sum2>sum1):
			sum_ = sum1
		else:
			sum_ = sum2

	else:
		if(g!=180):
			sum1 = s + d + side_t(r, r, g)
		else:
			sum1 = s + d + 2*r
		s2 = ((2*pi*r*g)/360)
		sum2 = math.sqrt(((s-d)**2)+(s2**2))
		if(sum2>sum1):
			sum_ = sum1
		else:
			sum_ = sum2
		if(g==0):
			sum_ = s-d

else:
	d = -1*d
	if(g==0):
		sum_ = s + (r-d)
	else:
		if(g!=180):
			sum_ = s + side_t(r, d, g)
		else:
			sum_ = s + r + d


fl = int(sum_)
k=sum_ - fl
if(fl<0.5):
	print fl
else:
	print fl + 1