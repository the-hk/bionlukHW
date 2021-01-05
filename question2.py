import math
import numpy as np
from matplotlib import pyplot as plt
import scipy as sp
from scipy import signal

increment = 0.001
upper_bound = 10
lower_bound = 0
timeDomain = np.arange(lower_bound, upper_bound, increment)
f=np.zeros(10000)
g=np.zeros(10000)
i=0
print(len(timeDomain) )

for i in range(len(timeDomain)):
    
     f[i]= 3*math.exp(-1*3*timeDomain[i])*math.cos(2*timeDomain[i]*math.pi/3)-5*timeDomain[i]*math.exp(-1*timeDomain[i])-2*math.exp(-1*timeDomain[i])






for i in range(len(timeDomain)):
    if timeDomain[i]<=4 and timeDomain[i]>=0:
        g[i]= 3*math.exp(-1*3*timeDomain[i])*math.cos(2*timeDomain[i]*math.pi/3)-5*timeDomain[i]*math.exp(-1*timeDomain[i])-2*math.exp(-1*timeDomain[i])
    else:
        g[i]= -(3*math.exp(-1*3*timeDomain[i])*math.cos(2*timeDomain[i]*math.pi/3)-5*timeDomain[i]*math.exp(-1*timeDomain[i])-2*math.exp(-1*timeDomain[i]))
       

y1 = sp.signal.medfilt(f,21)
        
plt.subplot(131),plt.plot(timeDomain,f),plt.title('f(t)')
plt.subplot(132),plt.plot(timeDomain,g),plt.title('g(t)')
plt.subplot(133),plt.plot(timeDomain,y1),plt.title('medium filtering')

plt.show()   

