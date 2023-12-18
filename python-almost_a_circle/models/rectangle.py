"""
Module documentation here.
"""

import sys
sys.path.append('C:/Users/HP/Documents/ISWE PROJECTS/alx_python/python-almost_a_circle/models')


if __name__ == "__main__":
    from base import Base

class Rectangle(Base):
    """
    Class documentation here.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor documentation here.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
