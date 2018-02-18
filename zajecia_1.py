import matplotlib.pyplot as plt
import numpy as np
import math as mt

n=5
@np.vectorize
def approx(x,n):
    wartosci = [((-1)**k)*(x**(2*k+1))/mt.factorial(2*k+1) for k in range(n)]
    return sum(wartosci)

x=np.linspace(0,2*np.pi,50)
y=approx(x,n)
[a,b]=plt.plot(x,np.sin(x),'*',x,y,'r')
plt.legend([a,b],['sin(x)','approx {0} terms'.format(n)])

plt.xlim(0,2*np.pi)
axes=plt.gca()
axes.set_xlim([0,2*np.pi])
axes.set_yticks(plt.yticks()[0],minor=False)
axes.set_yticks([0],minor=True)
axes.yaxis.grid(which="minor")

plt.show()