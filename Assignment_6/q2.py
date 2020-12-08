import matplotlib.pyplot as plt
import numpy as np
import time

def random_power_law(n,a):
    r=np.random.rand(n)
    alpha = a
    x = (1-r)**(1/(1+alpha))
    return x

def pl_to_exp(power_law):
    accpt_prob=1/1.5*np.exp(-power_law)/(power_law**-3)
    assert(np.max(accpt_prob<=1))
    accept=np.random.rand(len(accpt_prob))<accpt_prob
    exponential=power_law[accept]
    accpt_fraction=len(exponential)/len(power_law)
    return exponential,accpt_fraction

def random_exp(tau,n):
    r=np.random.rand(n)
    exponential = -tau*np.log(1-r)
    return exponential

#make power laws
alpha=-3
N=100000
fig1, ax1 = plt.subplots()
x=random_power_law(N,alpha)
xx=x[x<10] #easier to make nice plot
a,b = np.histogram(xx,100)
bb = 0.5*(b[:-1]+b[1:]) # middle value of each bin


#the power law needs to be normalized and scaled so it's above the exponitial
ax1.bar(bb,1.5*a,width=1/bb.max(),label="histogram of random number with power laws distribution")
#plot the expect random power laws curve
pred = bb**alpha
pred_power_law=pred/pred[0]*a[0]
ax1.plot(bb,1.5*pred_power_law,"k",label="power laws: y=1.5x^-3")
plt.legend()
plt.savefig('random power laws.png')
plt.show()


#from power laws to exponential
exponential,fraction = pl_to_exp(x)
exponential=exponential[exponential<10] #easier to make nice plot
c,d = np.histogram(exponential,100)
dd = 0.5*(d[:-1]+d[1:])
fig2, ax2 = plt.subplots()
ax2.bar(dd,c,width=1/dd.max(),label="histogram of random number with exponential distribution")
#plot the expect exponential curve
pred = np.exp(-1*dd)
pred_exp= pred/pred[0]*c[0]
ax2.plot(dd,pred_exp,"r",label="exponential: y=exp(-x)")
ax2.plot(bb,1.5*pred_power_law,"k",label="power laws: y=1.5x^-3")
plt.legend()
plt.savefig('exponential from power laws.png')
plt.show()

#efficient
t_1 = time.time()
p = random_power_law(N,-3)
e_1,fraction = pl_to_exp(p)
t_2 = time.time()
N=int(N*fraction)
t_3= time.time()
e_2 = random_exp(1,N)
t_4= time.time()
print('To generate', N ,'random number,')
print('The rejection method takes:', t_2-t_1,'and the accept fraction is', fraction)
print("The transformation method takes:", t_4-t_3)

