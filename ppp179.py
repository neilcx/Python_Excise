###########################################################
#
#	program: triangle.py
#
#
###########################################################
import math
from graphics import *

def square(x):
	return x*x

def distance(p1,p2):

	dist=math.sqrt(square(p2.getX()-p1.getX())+square(p2.getY()-p1.getY()))

	return dist

def main():

	win = GraphWin("Draw a Triangle")
	win.setCoords(0.0,0.0,10.0,10.0)
	message = Text(Point(5,0.5),"Click on three points")
	message.draw(win)

	#get and draw three vertivals of the triangle 

	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)
	p3 = win.getMouse()
	p3.draw(win)

	#use polygon object to draw the triangle

	triangle = Polygon(p1,p2,p3)
	triangle.setFill("peachpuff")
	triangle.setOutline("cyan")
	triangle.draw(win)
	

	#claculate the perimeter of the triangle

	perim = distance(p1,p2) + distance(p2,p3)+distance(p3,p1)

	message.setText("The perimeter is %0.2f" % perim)

	#wait for another click to exit

	win.getMouse()
	win.close()

main()





	


