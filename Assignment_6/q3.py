import matplotlib.pyplot as plt
import numpy as np
import time


t1=time.time()
n = 10000
v = np.random.rand(n)*0.7
u = np.random.rand(n)
ratio = v/u
accept = u<np.sqrt(np.exp(-1*ratio))
exponential = ratio[accept]
t2=time.time()
fraction=len(exponential)/n
N=n*fraction
fig1, ax1 = plt.subplots()
exponential=exponential[exponential<10]
a,b = np.histogram(exponential,100)
bb = 0.5*(b[:-1]+b[1:])
pred = np.exp(-1*bb)
pred = pred/pred[0]*a[0]

ax1.bar(bb,a,width=1/bb.max(),label="histogram of random number with exponential distribution")
ax1.plot(bb,pred,"r",label="exponential: y=exp(-x)")
plt.legend()
plt.savefig('ratio-of-uniforms generator.png')
plt.show()
print('The accept fraction is', fraction)
print('To generate', N, 'random number with exponential distribution, a ratio-of-uniforms generator takes:', t2-t1,'second')

