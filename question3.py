from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_excel
from sklearn.metrics import r2_score


t=0
i=0
numdat = pd.read_excel (r'/home/hk/Desktop/bionluk/TimeSeries.xlsx')
numdat2 = pd.read_excel (r'/home/hk/Desktop/bionluk/TimeSeries2.xlsx')
numdat_1=numdat[0:150]
numdat_2=numdat[0:len(numdat):3]
numdat2_1=numdat2[0:150]
numdat2_2=numdat2[0:len(numdat):3]

# print(numdat[1,3])

interpolated = numdat_2.interpolate(method='linear')
interpolated_1 = numdat_2.interpolate(method='cubic')
MSE_linear=np.sum(np.square(np.subtract(numdat2_2,interpolated)))/(2*len(numdat2_2))
MSE_cubic=np.sum(np.square(np.subtract(numdat2_2,interpolated_1)))/(2*len(numdat2_2))
print(len(numdat_2))
plt.subplot(141)
plt.title("raw")
plt.scatter(np.linspace(0,3098,num=len(numdat_2)),numdat_2)

plt.subplot(142)
plt.title("linear")
plt.scatter(np.linspace(0,1000,num=len(interpolated)),interpolated)

plt.subplot(143)
plt.title("cubic")
plt.scatter(np.linspace(0,1000,num=len(interpolated)),interpolated_1 )

number_of_nan=numdat_2.count()
numdat_2.dropna(inplace=True)
x_domain=np.linspace(0,986,num=len(numdat_2),endpoint=True)
print(len(x_domain),len(numdat_2))
plt.subplot(144)
plt.title("polyfit result")
plt.scatter(x_domain,numdat_2)
numdat_2 = np.squeeze(numdat_2)
model=np.polyfit(x_domain,numdat_2,4)
predict = np.poly1d(model)


model2=np.polyfit(x_domain,numdat_2,5)
predict2 = np.poly1d(model2)

o=np.polyval(np.linspace(0,1000,num=len(interpolated)),numdat_2)
    
MSE_polyfit=r2_score(numdat_2, predict(x_domain))
MSE_polyfit2=r2_score(numdat_2, predict2(x_domain))


plt.plot(x_domain, predict(x_domain), c = 'y')
plt.plot(x_domain, predict2(x_domain), c = 'r')
plt.legend(["order4","order5"])


plt.show()


#e: polyfit is the best choice to predict some value if the order 
#is increased MSE of the result would be increased that means more accurate 