#chain and traverse
from pipe import *
#chain used to iterate at a 1 time
lst=['1','2',['3','4','5',['6','7','8','9'],'10'],'11']
x=list(lst|chain)
print(x)
lst=[1,2,3]
#traverse used to root of the unfold iterate
y=list(lst|traverse)
print(y)