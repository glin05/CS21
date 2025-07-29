"""
This program reads a data set of earthquake statistics that contain
a unique ID, magintude, location, longitude and latitude, and 
the date and time of each earthquake. Then then program prompts the user
to search by location, ID, or magnitude; and also provides a Quit option. 
Functions perform input validation and then uses linear or binary search 
based on which option is chosen. 

Authors: Gina Lin
Date: 04/01/2025
Lab section (delete the three that do not apply): T2:45
Lecture section: 8:30
"""

from earthquakes_lab import *

def main():
    data = open_file()
    search = True 
    while search:
        selection = menu()
        resp = more_info(selection, data) 
        if int(selection) in [1, 2, 3, 4, 5]:    
            display = output(resp)
        elif int(selection) == 6: 
            search = False
        else:
            search = False
        
def open_file():
    """
    Reads the given file and returns a list of earthquake objects.
    
    Parameter:
    none
    
    Returns:
    data (list): list of earthquake objects.
    """
    fp = open("/usr/local/doc/earthquakes.txt", 'r')
    data = []
    for line in fp:
        line = line.strip()
        info = line.split(";")
        
        ID = info[0]
        mag = float(info[1])
        loc = info[2]
        lat = float(info[3])
        longt = float(info[4])
        s_loc = info[5]
        time = info[6]

        stats = Earthquake(ID,mag,loc,lat,longt,s_loc,time)
        data.append(stats)
    fp.close()
    return data

def menu():
    """
    Performs input validation that continuosly prompts user 
    for correct menu option and returns user input to main if input valid.
    
    Parameters: none

    Returns:
    selection(str): user input from menu options
    """
    print(" ")
    print("Please select one of the following choices:")
    print("(1) Find by location")
    print("(2) Find by ID")
    print("(3) Find by magnitude")
    print("(4) Find quakes by magnitude and sort by largest")
    print("(5) Find quakes by location and sort by largest ")
    print("(6) Find quakes by location and sort by most recent")
    print("(7) Quit")
    print("")
    selection = input("Choice? ")
    not_valid = True
    while not_valid:
        if not selection.isdigit() or int(selection) < 1 or int(selection) > 7:  
            print("Choice is not valid") 
            selection = input("Choice? ")
        else:
            return selection
            not_valid = False
            
def more_info(selection, data): 
    """
    Based on user's selection from menu, this function will prompt
    them to provide more information to search dataset by location,
    ID, minimum and maximum magnitudes, or exit the program.
    
    Parameters:
    selection(str): user input from menu options
    data (list): list of earthquake objects.
   
    Returns:
    selc_loc (lst): user location search results
    selc_id (str) : user id search results
    selc_mag (str): user magnitude search results
    m_sort(str): sorted earthquake objects in decresing
    """
    
    if int(selection) == 1:
        enter_loc = input("Enter location: ")
        loc_cap = enter_loc.capitalize()
        selc_loc = search_loc(loc_cap, data)
        if len(selc_loc) == 0:
            print("No records match entered location.")
        return selc_loc
        
    if int(selection) == 2:
        enter_id = input("Enter ID: ")
        selc_id = search_id(enter_id, data)
        return selc_id 

    if int(selection) == 3:
        is_mag = False 
        while is_mag == False:
            minm = input("Enter minimum magnitude: ")
            if is_float(minm) == False: 
                print("Invalid input. Please try again")
            if is_float(minm) == True:
                is_mag = True
        is_magmax = False 

        while is_magmax == False:
            maxm = input("Enter maximum magnitude: ")
            if is_float(maxm) == False or float(maxm) <= float(minm): 
                print("Invalid input. Please try again")
            elif is_float(maxm) == True:
                is_magmax = True
        selc_mag = search_mag(minm, maxm, data) 
        return selc_mag
        
    if int(selection) ==  4:
        is_mag = False 
        while is_mag == False:
            minm = input("Enter minimum magnitude: ")
            if is_float(minm) == False: 
                print("Invalid input. Please try again")
            if is_float(minm) == True:
                is_mag = True
        is_magmax = False 

        while is_magmax == False:
            maxm = input("Enter maximum magnitude: ")
            if is_float(maxm) == False or float(maxm) <= float(minm): 
                print("Invalid input. Please try again")
            elif is_float(maxm) == True:
                is_magmax = True
        to_report = input("How many earthquakes do you want to report? ")
        rep_int = int(to_report)
        m_sort = mag_sort(minm, maxm, data, rep_int) 
        return m_sort

    if int(selection) == 5:
        enter_loc = input("Enter location: ")
        loc_cap = enter_loc.capitalize()
        selc_loc = loc_sort(loc_cap, data)
        if len(selc_loc) == 0:
            print("No records match entered location.")
        return selc_loc

    if int(selection) == 6:
        enter_loc = input("Enter location: ")
        loc_cap = enter_loc.capitalize()
        selc_loc = loc_sort(loc_cap, data)
        if len(selc_loc) == 0:
            print("No records match entered location.")
        to_report = input("How many earthquakes do you want to report? ")
        rep_int = int(to_report)
        loc_sort_recent(selc_loc, data, rep_int) 

    if int(selection) == 7:
        print("Goodbye!")
        return 123

def search_loc(loc_cap, data):
    """
    This function uses linear search to search for locations that match 
    loc_cap and data. 

    Parameters:
        loc_cap(str): user inputed location 
        data (list): list of earthquake objects
    
    Returns: 
        loc_lst(list): search results based loc_cap
    """
    loc_lst = []
    for i in range(len(data)):
        new_data = data[i].get_location_full()
        if loc_cap in new_data:
            loc_lst.append(data[i])
    return loc_lst
   
def search_id(enter_id, data):
    """
    This function uses binary search to search for ID's that match 
    enter_id and data. Notifies user if ID wasn't found.

    Parameters:
        enter_id(string): user inputed eqarthquate ID
        data (list): list of earthquake objects.

    Returns:
        result(str): search results based on enter_id or if not found
        
    """
    lo = 0
    hi = len(data)-1
    while  lo <= hi :
     mid = (lo + hi) // 2
     if data[mid].get_id() == enter_id:
         return [data[mid]]
     elif data[mid].get_id() > enter_id:
         hi = mid -1
     else:
         lo = mid + 1
    return []

def search_mag(minm, maxm, data):
    """
    This function ensures that a valid float for magnitudes are entered and will
    keep prompting until valid responses are entered. 
    
    Parameters:
        minm(float): user inputed minimum magnitude
        maxm(float): user inputed minimum magnitude
        data(list): list of earthquake objects.
        to_report (str): how many earthquakes the user wants displayed

    Returns:
        result(float): search results based on minm and maxm and to_report
    """  
    mag_lst = []

    for i in range(len(data)):
        mag_data = data[i].get_magnitude()
        if float(minm) <= mag_data and float(maxm) >= mag_data:
            mag_lst.append(data[i])
    return mag_lst

    action = print("Invalid input. Please try again.")
    return action
 
def swap(lst, i, j):
    """
    Swap items in list at positions i and j 

    Args:
       lst (list): a list of items to sort 
       i,j (int): positions in list to swap. 
         assumes  0 <= i,j < len(lst)

    Return: None. Swaps items in place and modifies list
    """
    if i==j:
      return #nothing to do 

    item1 = lst[i]
    lst[i] = lst[j]
    lst[j] = item1

def mag_sort(minm, maxm, data, rep_int):
    """
    This function uses bubble sort to sort earthquake magnitudes in decreasing
    order

    Parameters:
        minm(float): user inputed minimum magnitude
        maxm(float): user inputed minimum magnitude
        data(list): list of earthquake objects.
        rep_int(int): The number of eqarthquake objects that the user wants displayed

    Returns:
    mag_lst (lst): sorted earthquake data in decreasing order
    """
    mag_lst = []
    for i in range(len(data)):
        mag_data = data[i].get_magnitude()
        if float(minm) <= mag_data and float(maxm) >= mag_data:
            mag_lst.append(data[i])
    
    sorting = True
    while sorting == True: 
        sorting = False 
        for i in range(len(mag_lst)-1):
            if mag_lst[i].get_magnitude() < mag_lst[i+1].get_magnitude(): 
                swap(mag_lst, i, i+1)
                sorting = True  
    if len(mag_lst) > rep_int:
        mag_lst = mag_lst[:rep_int]
    return mag_lst

    action = print("Invalid input. Please try again.")
    return action
def loc_sort(loc_cap, data):
    """
    This function uses bubble sort to sort earthquake magnitudes in decreasing
    order given location.

    Parameters:
        loc_cap(str): user inputed location 
        data(list): list of earthquake objects.
        
    Returns:
    loc_lst (lst): sorted earthquake data in decreasing order of magnitude
    """
    loc_lst = []
    for i in range(len(data)):
        new_data = data[i].get_location_full()
        if loc_cap in new_data:
            loc_lst.append(data[i])
    sorting = True
    while sorting == True: 
        sorting = False 
        for i in range(len(loc_lst)-1):
            if loc_lst[i].get_magnitude() < loc_lst[i+1].get_magnitude(): 
                swap(loc_lst, i, i+1)
                sorting = True  

    return loc_lst

def loc_sort_recent(selc_loc, data, rep_int):
    """
    This function uses bubble sort to sort earthquakes by date/time

    Parameters:
        selc_loc (lst): user location search results 
        data(list): list of earthquake objects.
        rep_int(int): The number of eqarthquake objects that the user wants displayed

    Returns:
        None
    """
    keep_going = True
    while keep_going == True: 
        keep_going = False 
        for i in range(len(selc_loc)-1):
            if is_more_recent(selc_loc[i + 1], selc_loc[i]): 
                swap(selc_loc, i, i+1)
                keep_going = True
    for i in range(rep_int):
        print("%d. %s" % (i, selc_loc[i + 1]))

def output(resp):
    """
    Prints list of earthquake search results

    Parameters:
        resp(lst): are the earthquake search results 
   
    Returns: None
    """
    print("")
    print("Found " + str(len(resp)) + " results:")
    for i in range(len(resp)):
        print("%d. %s" % (i + 1, resp[i]))

main()
