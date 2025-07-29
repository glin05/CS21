from photo import Photo
from album import Album
from graphics import *

def main():
    album = initialize("photos.txt", "Heeler family")
    show_album = True 
    while show_album:
        choice = print_menu()
        if int(choice) == 1:
            list_photos = photos_list(album)
        if int(choice) == 2:
            add = add_photo(album)
        if int(choice) == 3:
            search = search_tags(album)
        if int(choice) == 4:
            view = view_photos(album)
        if int(choice) == 5:
            slides = view_slideshow(album)
        if int(choice) == 6:
            print("Goodbye!")
            show_album = False 

def initialize(filename, title):
    """
    Reads the file and creates Photos for each line and puts them
    into an Album.

    Parameters:
    * filename (str): name of file containing info about photos
    * title (str): title of the Album

    Returns: (Album) an Album consisting of Photos created from data
    in the file.
    """
    fp = open(filename,'r')
    album = Album(title)
    for line in fp: 
        line = line.strip()
        info = line.split(",")
        tags = []
        for i in range(len(info)):
            if i > 2:
                tags.append(info[i])

        album.add_photo(Photo(info[0], info[1], info[2], tags))
    return album

def print_menu():
    """
    This function print out menu options and performs input validation
    """
    print("")
    print("================== Menu ======================")
    print("1: list all photos")
    print("2: add a photo")
    print("3: search photos by tag")
    print("4: view a photo")
    print("5: slideshow")
    print("6: quit")
    print("")
    choice = input("Choose a menu option: ")
    invalid_resp = True
    while invalid_resp: 
        if int(choice) < 1 or int(choice) > 6:
            print("Invalid input")
            choice = input("Choose a menu option: ")
        else:
            return choice
            invalid_resp == False
           
    
def photos_list(album):
    """
    This function shows the description, creator, and tags for all 
    the photos in the album.
    Param:
    (Album) an Album consisting of Photos created from data
    in the file.

    Return: None
    """
    photos = album.get_photos()

    sorting = True
    while sorting == True: 
        sorting = False
        for i in range(len(photos)-1):
            if photos[i].get_description() > photos[i+1].get_description():
                swap(photos, i, i+1)
                sorting = True 

    print("Here are the photos in this album: ")
    for item in photos:
        print(item)

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
      return 

    item1 = lst[i]
    lst[i] = lst[j]
    lst[j] = item1

def add_photo(album):
    """
    This function allows users to add photos to the album
    Params:
    (Album) an Album consisting of Photos created from data
    in the file.

    Returns:
    None
    """
    name = input("Enter name of the file: ")
    creator = input("Enter creator of the image: ")
    descrip = input("Enter description of the image: ")
    tags = input("Enter tags: ")
    new_tags = tags.split()  
    new_photo = Photo(name, creator, descrip, new_tags)
   
    if album.add_photo(new_photo):
        print(album)
        print("Successfully added photo.")
    else:
        print("Could not add photo to album.")

def search_tags(album):
    """
    This function should display the tags of all photos in the album and 
    then ask the user to enter a tag.
    """
    print("")
    print("Here are the tags: ")
    tags = album.get_tags()
    for line in tags: 
        print(line)
    print("")
    
    to_search = input("Search for a tag: ")

    descriptions = []
    for photos in album.get_photos():
        if to_search.lower() in photos.get_tags():
            descriptions.append(photos) 
    if len(descriptions) == 0:
        print("\nNo tags found in the album.")
    else:  
        sorting = True
        while sorting == True: 
            sorting = False
            for i in range(len(descriptions)-1):
                if descriptions[i].get_description() > descriptions[i+1].get_description():
                    swap(descriptions, i, i+1)
                    sorting = True 
        print("\nHere are the phtotos with that tag:")
        for photos in descriptions:
            print(photos.get_description())

def view_photos(album):
    """
    This program should show an enumerated list (starting at 1) of the
    descriptions of the photos in the album and then prompt the user 
    to select one of the photos by using the corresponding number.
    """
    photos = album.get_photos()

    if len(photos) == 0:
        print("There are no photos in the album.")
        return

    while True:
        for i in range(len(photos)):
            number = i + 1
            description = photos[i].get_description()
            print(str(number) + ": " + description)

        choice = input("Choose a photo: ")

        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(photos):
                selec_photo = photos[number - 1]
                display_image(selec_photo.get_filename())
                break
            else:
                print("Please enter a valid number.")
        else:
            print("Please enter a valid number.")


def view_slideshow(album):
    """
    This program iterates over all photos in the album and use the
    display_image function to show each photo one at a time.
    """
    photos = album.get_photos()

    if len(photos) == 0:
        print("There are no photos in the album.")
        return

    print("Slideshow in progress. Click screen to see next picture.")

    for photo in photos:
        display_image(photo.get_filename())

    print("All photos have been shown!")

def display_image(filename):
    """
    This function displays the image with the specified filename.
    YOU SHOULD NOT NEED TO CHANGE IT!
    Please contact a member of the Instruction Staff if you think
    a change is necessary.
    """
    try:
        image = Image(Point(250, 250), filename)
        win = GraphWin(filename, image.getWidth(), image.getHeight())
        win.setCoords(0, 0, 500, 500)
        image.draw(win)
        try:
            win.getMouse()
            win.close()
        except:
            pass
    except:
        print("An error occurred trying to open %s" % filename)
        
if __name__ == "__main__":
    main()
