"""
Draw a face with python Graphics library

Author: Gina Lin
Date: 03/04/2025
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply): T2:45 

Requirements:
- Draw a face with at least 5 different features in addition to the main head
  shape. Some features include: eyes, nose, mouth, ears, hair, beard,
  antenna, horns, teeth, etc.

- Your face should use at least 3 different shapes, and 3 different colors
  (background color counts).

- The first mouse click should have your character say something (in text). 
  Please keep the message friendly.

- The second mouse click should exit your program 
  (i.e. make sure that your program does not exit before the user clicks 
   the mouse a second time).
"""

from graphics import * 

def main():
    win = GraphWin("Face", 800, 800)
    win.setBackground("light pink")
    win.setCoords(0,0, 100, 100)
    
    #draw your face 
    center = Point(50,50)          
    circ = Circle(center, 30)
    circ.draw(win)
    facecolor = color_rgb(255, 255, 100)
    circ.setFill(facecolor)
    circ.setOutline(facecolor)

    #eyes (circle)
    cp_eye = Point(37,60)          
    eye = Circle(cp_eye, 5)
    eye.setFill("black")
    eye.setOutline("black")
    eye.draw(win)

    copy_eye = eye.clone()
    copy_eye.setFill("black")
    copy_eye.setOutline("black")
    copy_eye.move(25, 0)
    copy_eye.draw(win)

    #eyebrows (rectangle)
    p1 = Point(32, 67)
    p2 = Point(42, 70)
    brow = Rectangle(p1, p2)
    brow.setFill("brown")
    brow.setOutline("brown")
    brow.draw(win)

    #clone eyebrows
    copy_brow = brow.clone()
    copy_brow.setFill("brown")
    copy_brow.setOutline("brown")
    copy_brow.move(25, 0)
    copy_brow.draw(win)

    #mouth(rectangle)
    p1 = Point(40, 30)
    p2 = Point(60, 35)
    lip = Rectangle(p1, p2)
    lip.setFill("red")
    lip.setOutline("red")
    lip.draw(win)

    #nose (triangle)
    p1 = Point(45,45)
    p2 = Point(50,50)
    p3 = Point(55,45)
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("orange")
    triangle.setOutline("orange")
    triangle.draw(win)

    #hat
    p1 = Point(25, 72)
    p2 = Point(75, 82)
    hat_t = Rectangle(p1, p2)
    hat_t.setFill("blue")
    hat_t.setOutline("blue")
    hat_t.draw(win)
    
    p1 = Point(35, 82)
    p2 = Point(65, 92)
    hat_b = Rectangle(p1, p2)
    hat_b.setFill("blue")
    hat_b.setOutline("blue")
    hat_b.draw(win)

    win.getMouse() 
    message = Text(Point(50,15), "Hasta Luego!")
    message.setSize(24)
    message.setTextColor("green")
    message.draw(win)

    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()
