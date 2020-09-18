import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

#load data file
data = np.loadtxt("lakeshore.txt")

#read the first and second colunm, and give the vaule to true data
x_true=data[:,0]
y_true=data[:,1]

#extract the elements with even indexes and use as known data points
x_even=x_true[::2]
y_even=y_true[::2]

#extract the elements with odd indexes and use as known data points
x_odd=x_true[1::2]
y_odd=y_true[0::2]

#interpolate using the method of spline with even data points
spln=interpolate.splrep(x_even,y_even)
yy_even=interpolate.splev(x_true,spln)
plt.clf();
plt.plot(x_even,y_even,'*g',label='Given Data Points (Even Index) ')
plt.plot(x_true,yy_even,'r',label='Interpolated Value')
plt.plot(x_true,y_true,'b',label='True Vaule')
plt.legend()
plt.savefig('question2_lakeshore_interpolation_with_even_data_points.png')


#compare the interpolation with odd data points and even data points
spln=interpolate.splrep(x_odd,y_odd)
yy_odd=interpolate.splev(x_true,spln)
plt.clf();
plt.plot(x_true,yy_odd,'r',label='Interpolated Value(Odd Index)')
plt.plot(x_true,yy_even,'b',label='Interpolated Vaule(Even Index)')
plt.legend()
plt.savefig('question2_interpolation_comparsion_between_even_odd.png')

#pint the error of spline interpolation
print('my rms error of interpolation with even data point is ',np.std(y_true-yy_even))
print('my rms error of interpolation with odd data point is ',np.std(y_true-yy_odd))
