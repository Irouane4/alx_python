""" 1-main """

import sys
sys.path.append('C:/Users/HP/Documents/ISWE PROJECTS/alx_python/python-almost_a_circle/models')

from rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
