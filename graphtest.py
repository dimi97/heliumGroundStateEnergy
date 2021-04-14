import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from myCons import myCons
from main import main  

# Data for plotting

myCons.n=2

a = np.arange(0.65, 2.0, 0.005)
vmainf = np.vectorize(main.f);
data = vmainf(a)

myCons.n=3

a = np.arange(0.65, 2.0, 0.005)
vmainf = np.vectorize(main.f);
data2 = vmainf(a)

myCons.n=5

a = np.arange(0.65, 2.0, 0.005)
vmainf = np.vectorize(main.f);
data3 = vmainf(a)

fig, ax = plt.subplots()
ax.plot(a,data,'-b',label='n=3')
ax.plot(a,data2,'-g',label='n=4')
ax.plot(a,data3,'-r',label='n=8')

ax.legend(loc='upper right', frameon=True)
fig


ax.set(xlabel='a parameter', ylabel='Energy',
       title='Energy-a diagramm')
ax.grid()

fig.savefig("test.png")
plt.show()