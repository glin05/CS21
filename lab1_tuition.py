"""
This program calculates a tuition bill based on the number
of credits, any existing balance, and a general fee.

Author: Gina Lin
Date: 01/28/2025
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45 
"""
def main():
    #ask how many courses and then multiple it with tuition
    course = input("This program calculates the tuition bill How many courses is the student taking? " )
    exist= input("What is the exisiting balance? ") 
    n = int(course)
    n2= float(exist)
    tu= n * 3456.78
    bal = tu + n2 + 876.54

    print("\nThe total bill is $" + str(bal))
    
    
main()
