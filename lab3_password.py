"""
Given a phrase, create a possible password by replacing vowels with
special characters.

Author: Gina Lin
Date: 02/11/2025
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45 
"""
def main(): 

    string = input("Enter string: ")
    
    newstring = ""
   
    for letter in string:
        if letter == 'A' or letter == 'a':
            newstring += "@"
    
        elif letter == 'E' or letter == 'e':
            newstring += "3"

        elif letter == 'I' or letter == 'i':
            newstring += "1" 

        elif letter == 'O' or letter == 'o':
            newstring += "0" 

        elif letter == 'U' or letter == 'u':
            newstring += "^"
        
        elif letter == " ":
            newstring = newstring + ""

        else:
            newstring = newstring + letter

    print("Possible password: " +  newstring)
    
    if string == newstring:
        print("Your encoded phrase is the same as the original--try something else!")

main()
