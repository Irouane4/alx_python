"""Module defining the Base class for managing ids in the project."""

class Base:
    """Base class for managing ids.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects.
        id (int): A public instance attribute representing the id of an object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object with a unique id.

        Args:
            id (int, optional): The id to assign to the object. If not provided, a unique id
                will be automatically generated.

        Note:
            If id is provided, it will be assigned to the object. If id is not provided,
            __nb_objects will be incremented, and the new value will be assigned to the id
            attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
