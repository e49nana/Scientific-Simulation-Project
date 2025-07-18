import numpy as np
import matplotlib.pyplot as plt

nx, ny = .3, .3
x=np.arange(-3,3,nx)
y=np.arange(-2,2,ny)

X,Y=np.meshgrid(x,y)


dy=X*X+Y*Y
#dy=-X/Y
dx=np.ones(dy.shape)

plt.quiver(X,Y,dx,dy,color='purple')
plt.show()
