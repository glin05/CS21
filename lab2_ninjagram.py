"""

TODO: This program calculates the price of sending ninjagrams by using 
accumulator patterns to allow the user to input multple messages and also 
calculates the price for the grams by using mathematical functions to 
calculate price relative to length of the characters of the message.

Author: Gina Lin
Date: 02/04/2024
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45 
"""
def main():
    num = input("\nNumber of ninjagrams to send: ")
    
    total = 0

    for i in range(int(num)):
        let = input("\nEnter message: ")
        price = len(let) * 0.15
        print("This message will cost: " + str(price))
        total = total + price 
    print("\nTotal amount: " + str(total))
   
main()
