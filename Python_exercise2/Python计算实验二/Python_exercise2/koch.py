"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

# see if Swampy is installed as a package
from swampy.TurtleWorld import *


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 3:
        fd(t, n)
        return
    m = n / 3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        rt(t, 120)


def f(t, n):
    for i in range(3):
        koch(t, n)
        lt(t, 120)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -150
bob.y = -75
bob.redraw()

f(bob, 300)


world.mainloop()
