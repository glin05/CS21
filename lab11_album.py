"""
Represents a photo album, i.e. a collection of photos
"""

from photo import Photo

class Album:
    def __init__(self, name):
        self.name = name
        self.photos = []

    def get_name(self):
        """return string that was passed to constructor as name of album. """  
        return self.name
   
    def add_photo(self, photo):
        """ 
        Adds Photo object to album if not present in album.
        """
        for album_photo in self.photos:
            if album_photo.get_filename() == photo.get_filename() or album_photo.get_description() == photo.get_description(): 
                return False

        self.photos.append(photo)
        return True
    
    def get_photos(self):
        """
        Returns list of Photo objects in this album or empty list if no photos
        """
        if len(self.photos) < 0:
            return []
        else: 
            return self.photos
    
    def get_count(self):
        """ return the number of photos in the album """
    
        return len(self.photos)
    
    def get_tags(self):
        """ 
        Return a list of the distinct tags of all the
        Photo objects in the album. 
        """
        distinct_tags = []
        for photo in self.get_photos(): 
            for tags in photo.get_tags():
                if tags not in distinct_tags: 
                    distinct_tags.append(tags)
        
        distinct_tags.sort()
        return distinct_tags

    def __str__(self):
        tags = ''
        for item in self.get_tags():
            tags = tags + " #" + item 

        return "Album Name: %s ; Number of photos: %d; Tags: %s" % (self.name, 
        self.get_count(), tags)
   
def main():
    print("Testing Album class")
    album = Album("Test Album")
    print(album)
    album.add_photo(Photo("test1.gif", "Test Creator 1", "Test Description 1", ["tag1", "tag2"]))
    album.add_photo(Photo("test2.gif", "Test Creator 2", "Test Description 2", ["tag2", "tag3"]))
    photo = Photo("pic.jpg", "Bob", "test pic", ["picnic", "pick"])
    album.add_photo(photo)
    print(photo)
    
    print(album.get_count())
    print(album.get_photos())
    print(photo.get_creator())
    print(photo.get_tags())

if __name__ == "__main__":
    main()
