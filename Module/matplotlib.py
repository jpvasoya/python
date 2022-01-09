import matplotlib.pyplot as mp
import numpy as np

x=np.array([0,6,3])
x1=[5,2,8,4,1]
y=np.array([0,250,300])
y1=[5,20,40,256,33]
mp.plot(x,y,'--or',ms=20)
mp.plot(x1,y1,'--og',ms=20)
mp.title("Simple Chart")
mp.xlabel("x-axis")
mp.ylabel("y-axis")
mp.grid()
mp.show()