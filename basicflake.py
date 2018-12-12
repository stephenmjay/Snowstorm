import random
from random import randint
def basicflake(foo,colours,flakesize):
    for i in range(10):
        foo.color('black',random.choice(colours))
        foo.begin_fill()
        for j in range(2):
            if (i==9) and (j==1):
                foo.forward(.72*flakesize)
                foo.right(95)
                foo.forward(.27*flakesize)
                foo.left(59)
                foo.forward(flakesize)
                break
            else:
                foo.forward(flakesize)
            foo.right(60)
            foo.forward(flakesize)
            foo.right(120)
        foo.end_fill()
        foo.right(36)
