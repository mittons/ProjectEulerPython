from math import atan, pi
from math import tan
from math import sqrt
from decimal import *

def mathematical((x0,y0),(x1,y1)):
	#dX = direction node1 is in relative to the line passing 
		  #through node0 that is parallel to the x-axis 
	dX = 0
	if x0 == x1:
		if y0 < y1:
			dX = pi/2
		elif y0 > y1:
			dX = 3*pi/2	
		else:
			print "Error, comparing nodes at same coordinates"
	else:
		if x0 > x1:
			dX += pi
		dX += atan((y1-y0)/(x1-x0))
		dX %= (2*pi)
	return dX	


def line2((x1,y1),m):
	return lambda x: m*(x-x1)+y1
#print line((1,1),tan(mathematical((1,1),(2,2))))(2)

def ellipse():
	return lambda x: sqrt(4*x**2-100)

#Ugly as fuck, gotten from wolfram alpha input: 100-4*x^2 - (m*x-m*x1+y1)^2 = 0
def solveX((x1,y1),m):
	x1 = x1
	y1 = y1
	m = m	
	d = 2*sqrt((m**2)*(-(x1)**2)+25*(m**2)+(2*m*x1*y1)-(y1**2)+100)
#	d = 2*sqrt(pow(m,2)*pow(-x1,2)+25*pow(m,2)+2*m*x1*y1-pow(y1,2)+100)
	den = (m**2+4)	
	b = m**2*x1-m*y1
	x1 = (b + d)/den
	x2 = (b - d)/den
	return x1, x2




me = lambda (x,y): atan((-4*x)/y)
"""
print me((1.4,9.6))
print me((-1.4,9.6))
print me((-1.4,-9.6))
print me((1.4,-9.6))

assert False
"""

def mirror(nextLoc, lAng):
	alpha = 0
	delta = 0
	theta = 0
	returnVal = -1
	#Right side
	if nextLoc[0]>0:
		#Upper
		if nextLoc[1]>0:
			alpha = abs(me(nextLoc))
			if lAng < pi:
				theta = lAng
				delta = alpha+theta
			elif lAng > pi:
				theta = 2*pi-lAng	
				delta = alpha-theta
			elif lAng == pi:
				print "ERROR"
			returnVal = 2*pi-(alpha+delta)
		#Lower
		elif nextLoc[1]<0:
			alpha = me(nextLoc)
			if lAng > pi:
				theta = 2*pi-lAng
				delta = alpha+theta
			elif lAng < pi:
				theta = lAng
				delta = alpha-theta
			elif lAng == pi:
				print "ERROR"
			returnVal = alpha+delta
		#Middle
		elif nextLoc[1] == 0:
			if lAng < pi:
				assert lAng < pi/2
				theta = (pi/2)-lAng
				delta = (pi/2)+theta
			elif lAng > pi:
				assert lAng > (3*pi)/2
				theta = lAng-(3*pi)/2
				delta = ((3*pi)/2)-theta
			elif lAng == pi:
				print "ERROR"
			returnVal = delta
	#Left side
	elif nextLoc[0]<0:
		#Upper
		if nextLoc[1]>0:
			alpha = me(nextLoc)
			if lAng <= pi:
				theta = pi-lAng
				delta = alpha+theta
			elif lAng > pi:
				theta = lAng-pi
				delta = alpha-theta
			returnVal = pi+alpha+delta
		#Lower
		elif nextLoc[1]<0:
			alpha = abs(me(nextLoc))
			if lAng <= pi:
				theta = pi-lAng
				delta = alpha-theta
			elif lAng > pi:
				theta = lAng-pi
				delta = alpha+theta
			returnVal = ((pi-alpha)-delta)%(pi*2)
		#Middle
		elif nextLoc[1] == 0:
			if lAng <= pi:
				assert lAng > pi/2
				theta = lAng-(pi/2)
				delta = (pi/2)-theta
			elif lAng > pi:
				assert lAng < ((3*pi)/2)
				theta = ((3*pi)/2)-lAng
				delta = ((3*pi)/2)+theta
			returnVal = delta
	#Middle
	elif nextLoc[0] == 0:
		#Upper
		if nextLoc[1]>0:
			print "VICTORY... {} walls hit".format(hits)
		#Lower
		else:
			assert lAng > pi
			theta = delta = returnVal = (2*pi)-lAng

	return returnVal
		

def funcX():
	loc = (0.0,10.1)
	nextLoc = (1.4,-9.6)
	lAng = mathematical(nextLoc,loc)

	hits = 0
	po = [loc,nextLoc]

	while ((nextLoc[1]<0 or abs(nextLoc[0])>0.01)):
		hits += 1
		lAng = mirror(nextLoc,lAng)
		lm = tan(lAng)
		print hits, loc, lm
		loc = nextLoc

		x1,x2 = solveX(loc,lm)
		if abs(x1-loc[0])<abs(x2-loc[0]):
			nextLoc = (x2,line2(loc,lm)(x2))
		else:
			nextLoc = (x1,line2(loc,lm)(x1))
		po.append(nextLoc)
	print nextLoc
	print hits

funcX()

#SOLVE FUNCTION DERIVATION

#100-4*x**2 = (m*x-m*x1+y1)^2 = (m*x)**2-(m*x*m*x1)+m*x*y1-(m*x1*m*x)+(m*x1)**2-(m*x1*y1)+m*x*y1-m*x1*y1+y1**2


#100-4*x**2 = (m*x)**2-(m*x*m*x1)+m*x*y1-(m*x1*m*x)+(m*x1)**2-(m*x1*y1)+m*x*y1-m*x1*y1+y1**2

#100-4*x**2 = ((m**2)*(x**2))-((m**2)*x*x1)+m*x*y1-((m**2)*x1*x)+(m*x1)**2-(m*x1*y1)+m*x*y1-m*x1*y1+y1**2

#- 4*x**2 - ((m**2)*(x**2)) + ((m**2)*x*x1) - m*x*y1 + ((m**2)*x1*x) - m*x*y1 = (m*x1)**2-(m*x1*y1)-m*x1*y1+y1**2 - 100


#(x**2)*(-4-m**2) + ((m**2)*x*x1) - m*x*y1 + ((m**2)*x1*x) - m*x*y1 = (m*x1)**2-(m*x1*y1)-m*x1*y1+y1**2 - 100

#(x**2)*(-4-m**2) + x*((m**2)*x1) - x*(m*y1) + x*((m**2)*x1) - x*(m*y1) = (m*x1)**2-(m*x1*y1)-m*x1*y1+y1**2 - 100

#(x**2)*(-4-m**2) + x*(2*(m**2)*x1) - x*(2*m*y1)= (m*x1)**2-(m*x1*y1)-m*x1*y1+y1**2 - 100

#(x**2)*(-4-m**2) + x*((2*(m**2)*x1) - (2*m*y1))= (m*x1)**2-(m*x1*y1)-m*x1*y1+y1**2 - 100

#(x**2)*(-4-m**2) + x*(2*m*(m*x1 - y1))= (m*x1)**2-(m*x1*y1)-m*x1*y1+y1**2 - 100

#(x**2)*(-4-m**2) + x*(2*m*(m*x1 - y1)) = (m*x1)**2 - 2*m*x1*y1 + y1**2 - 100

#(x**2)*(-4-m**2) + x*(2*m*(m*x1 - y1)) - (m*x1)**2 + 2*m*x1*y1 - y1**2 + 100 = 0

#a = (-4-m**2)
#b = (2*m*(m*x1 - y1))
#c = -(m*x1)**2 + 2*m*x1*y1 - y1**2 + 100

#d = sqrt(b**2-4*a*c) 
#x1 = (-b + d)/2*a
#x2 = (-b - d)/2*a
