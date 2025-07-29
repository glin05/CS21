"""
Make a barchart

Author: Gina Lin
Date: 02/04/2024
Lecture section (delete the two that do not apply): 8:30 
Lab section (delete the three that do not apply):  T2:45 
"""


def main():
    resp = input("Number of rows: ")
    
    row = "*"

    for i in range(int(resp)):
        print(str(i+1) + ": " + row)
        row = row + "**" 
    
main()
