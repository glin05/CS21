"""
Determine the total price of movie tickets for a group of guests based
on their ages.

Author: Gina Lin
Date: 2/11/2025
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45 
"""

def main():
    print("Welcome to the movie theater sales kiosk")
    num_tickets = input("\nHow many movies would you like? ")
    
    price = 0
    total = 0

    for i in range(int(num_tickets)) : 
        age = input("Enter the age of the next guest: ")

        if int(age) >= 60:
            price = 13
            print("A senior ticket is $13 ")
        elif int(age) <= 59 and int(age) >= 13: 
            price = 15
            print( "An adult ticket is $15")
        else:
            price = 10
            print("A child ticket is $10")

        total = price + total 

    print("\nYour total amount for " + num_tickets + " tickets is $" + str(total))
main()   
