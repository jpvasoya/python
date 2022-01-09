#where and select both us at a time
from pipe import *
tpl=(1,2,3,4,5,6,7,9,8)
x=tuple(tpl|where(lambda x:x%2!=0)
					|select(lambda x:x+1))
print(x)