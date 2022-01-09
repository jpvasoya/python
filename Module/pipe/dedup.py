#dedup method remove duplicate
from pipe import *
lst=[1,2,1,1,1,1,1,3,4,4,5,56,7,9,1]
#lst=list(set(lst))
x=list(lst|dedup)
print(x)