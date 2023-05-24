# Python
from random import randint as r

t=0
n=0
for x in range(5):
    t=r(0,16)
    n+=t**2
print(n)
