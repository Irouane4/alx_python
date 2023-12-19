from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the Square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size attribute """
        self.width = value
        self.height = value

    def __str__(self):
        """ Override of the __str__ method to return a formatted string """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
