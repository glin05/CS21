"""
Represents a single photo in the album
"""

class Photo:
    def __init__(self, filename, creator, description, tags):    
        self.filename = filename
        self.creator = creator
        self.description = description
        
        new_tags = []
        for item in tags:
            item = item.lower()
            new_tags.append(item)
        self.tags = new_tags
    def get_filename(self):
        """ returns the name of the .gif file for photo """
        return self.filename
    
    def get_creator(self):
        """ 
        returns string with name of person who created the photo"""
        return self.creator
    
    def get_description(self):
        """return a string containing the description of the photo """
        return self. description
    
    def get_tags(self):
        return self.tags
        """ return a list of strings that are the tags for this photo"""
   
    def __str__(self):
        tags = ''
        for item in self.get_tags():
            tags = tags + " #" + item 

        return "Desription: %s; Creator: %s; Tags:%s" %  (self.description,
         self.creator, tags)

def main():
    print("Testing Photo class")
    photo = Photo("test.gif", "Test Creator", "Test Description", ["Tag1", 
    "tag2"])
    print(photo)
    print(photo.get_filename())
    print(photo.get_creator())
    print(photo.get_description())
    print(photo.get_tags())

if __name__ == "__main__":
    main()
