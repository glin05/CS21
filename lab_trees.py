"""
This program lets users interactively draw trees by clicking three points on
the screen p1, p2, p3. The points will be assigned as the center, edge of the 
canopy, and the length of the trunk respectivley. The user will be allowed to 
create as many trees as they like and can exit the window by clicking on 
the sun.

Author: Gina Lin
Date: 03/03/2025
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply): T2:45
"""


leaf_colors = ["white", "violet", "SpringGreen1", "SpringGreen2", "yellow"]

trunk_colors=["brown", "snow1", "SaddleBrown", "DarkGoldenRod4", "khaki4"]


from graphics import *
from math import sqrt 
from random import choice 

def main():
    """
    This function asks user to click the screen to assign three points p1, p2, 
    and p3. Before the function can proceed to create trees, it checks to see 
    if the point is iside the sun using a boolean condition, which allows for 
    the user to exit the window. Otherwise, the program will prompt the user to 
    click for two more points and create a trees in the draw_tree() function.
    The while loop allows for the user to keep creating trees until they choose
    to exit the window by clicking the sun. 
    """

    width = 800
    height = 600
    aspect = width / height
    win = GraphWin("Trees", width, height)
    win.setBackground("sky blue")
   
    w = 100 * aspect
    win.setCoords(0,0, w, 100)

    circ = make_sun(win, width)
    rec_g = make_ground(win, width)

    click = True
    center_circle = circ.getCenter()
    message = Text(Point(60,10), "Click the screen for the center point")
    message.draw(win)

    while click == True: 
        p1 = win.getMouse()
        distance_from_p1_r = distance(p1, center_circle)
        if circ.getRadius() > distance_from_p1_r:
            click = False 
        
        else:
            message.setText("Click for canopy of the tree.")
            p2 = win.getMouse()
            message.setText("Click for the length of the trunk.")
            p3 = win.getMouse()
            tree = draw_tree(win, p1, p2, p3)
    win.close()

def make_sun(win, width):
    """
    Draws the sun in the top right hand corner of window
    """
    circ = Circle(Point(120, 90), 5)
    circ.setFill("yellow")
    circ.setOutline("yellow")
    circ.draw(win)
    return circ

def make_ground(win, width): 
    """
    Draws the ground
    """
    p1_g = Point(0, 0)
    p2_g = Point(133, 50)
    rec_g = Rectangle(p1_g, p2_g)
    rec_g.setFill("green")
    rec_g.setOutline("green")
    rec_g.draw(win)
    return rec_g

def draw_tree(win, p1, p2, p3):
    """
    This function compute the distance r between p1 and p2
    using the distance() and creates a circle for the tree canopy tree_top. 
    Then it creates the tree trunk tree_trunk centered around p1.x and 
    extending vertically from p1.y to b. The trunk is drawn first and then 
    the canopy using colors from leaf_colors and trunk_colors.
    """
    r = distance(p1, p2)
    tree_top = Circle(p1, r)
    tree_top.setFill(choice(leaf_colors))  
    trunk = sqrt(r)
    tree_trunk1 = Point(p1.getX()- trunk/2, p3.getY())
    tree_trunk2 = Point(p1.getX()+ trunk/2, p1.getY())
    tree_trunk = Rectangle(tree_trunk1, tree_trunk2)
    tree_trunk.setFill(choice(trunk_colors))
    
    tree_trunk.draw(win)
    tree_top.draw(win)

def distance(p1, p2): 
    """
    Distance formula required to perform calculations from other functions
    """
    return sqrt((p1.getX() - p2.getX())**2 + (p1.getY()- p2.getY())**2)
    


if __name__ == "__main__":
    main()
