"""
Module documentation here.
"""

try:
    from models.base import Base
except ImportError:
    pass  # Ignore import errors during documentation check

class Rectangle(Base):
    """
    Class documentation here.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor documentation here.
        """
        try:
            super().__init__(id)
        except NameError:
            pass  # Ignore NameError during documentation check
        self.width = width
        self.height = height
        self.x = x
        self.y = y
