"""
Create a survey based on four topics and compare the user's answers
to your preferences. 

Author: Gina Lin
Date: 02/22/2025
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45 
"""


def main():
    print("Let's take a compatibility survey.")
    category = ["color", "food", "season", "holiday"]
    resp = ["teal", "ice cream", "spring", "thanksgiving"]
    n = len(category)

    compatibility = 0

    for i in range(n): 
        ans = input("\nWhat is your favorite " + category[i]+ "? ")
        if ans == resp[i]:
            print("That is my favorite " + category[i] + " too!")
            compatibility = compatibility + 1
        else: 
            print(ans + " is nice but I prefer " + resp[i])

    print("\nOur compatability is: " + str(compatibility) + " out of 4")
    if compatibility == 4:
        print("We are really in synch!")
    elif compatibility == 0:
        print("Difference is the spice of life!")
    else: 
        print("We have some faves in common.")
main()
