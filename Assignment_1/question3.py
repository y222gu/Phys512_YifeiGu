import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

#### f(x)=cos(x)
#polynamial fit
x=np.linspace(-(np.pi/2),np.pi/2,10)
y=np.cos(x)
xx=np.linspace(x[0],x[-1],2000)
y_true=np.cos(xx)
n=5
m=6
pp=np.polyfit(x,y,n+m) #use same number of terms
yy_poly=np.polyval(pp,xx)
error_poly=np.std(y_true-yy_poly)
print('The error of polynomial fit is' , error_poly)

#spline

spln=interpolate.splrep(x,y)
yy_spl=interpolate.splev(xx,spln)
error_spl=np.std(y_true-yy_spl)
print('The error of spline fit is', error_spl)

#rational fit
def rat_eval(p,q,x):
    top=0
    for i in range(len(p)):
        top=top+p[i]*x**i
    bot=1
    for i in range(len(q)):
        bot=bot+q[i]*x**(i+1)
    return top/bot

def rat_fit(x,y,n,m):
    assert(len(x)==n+m-1)
    assert(len(y)==len(x))
    mat=np.zeros([n+m-1,n+m-1])
    for i in range(n):
        mat[:,i]=x**i
    for i in range(1,m):
        mat[:,i-1+n]=-y*x**i
    pars=np.dot(np.linalg.inv(mat),y)
    p=pars[:n]
    q=pars[n:]
    return p,q

n=5
m=6
x=np.linspace(-(np.pi/2),np.pi/2,n+m-1)
y=np.cos(x)
xx=np.linspace(x[0],x[-1],2000)
p,q=rat_fit(x,y,n,m)
yy_rat=rat_eval(p,q,xx)
error_rat=np.std(y_true-yy_rat)
print('The error of rational fit is' , error_rat)

#plot
plt.clf()
plt.plot(x,y,'*',label='choosed modest points')
plt.plot(xx,yy_spl,'b',label='spline')
plt.plot(xx,yy_rat,'g',label='rational fit')
plt.plot(xx,yy_poly,'r',label='polynomial fit')
plt.plot(xx,y_true,'y',label='true')
plt.legend()
plt.savefig('question3_cos_accuracy_comparsion.png')


#### f(x)=1/(1+x^2)
#polynamial fit
n=5
m=6
x=np.linspace(-1,1,n+m)
y=1/(1+x**2)
xx=np.linspace(x[0],x[-1],2000)
y_true=1/(1+xx**2)
pp=np.polyfit(x,y,n+m) #use same number of terms
yy_poly=np.polyval(pp,xx)
error_poly=np.std(y_true-yy_poly)
print('The error of polynomial fit is' , error_poly)

#spline

spln=interpolate.splrep(x,y)
yy_spl=interpolate.splev(xx,spln)
error_spl=np.std(y_true-yy_spl)
print('The error of spline fit is', error_spl)

#rational fit
def rat_eval(p,q,x):
    top=0
    for i in range(len(p)):
        top=top+p[i]*x**i
    bot=1
    for i in range(len(q)):
        bot=bot+q[i]*x**(i+1)
    return top/bot

def rat_fit(x,y,n,m):
    assert(len(x)==n+m-1)
    assert(len(y)==len(x))
    mat=np.zeros([n+m-1,n+m-1])
    for i in range(n):
        mat[:,i]=x**i
    for i in range(1,m):
        mat[:,i-1+n]=-y*x**i
    pars=np.dot(np.linalg.inv(mat),y)
    p=pars[:n]
    q=pars[n:]
    return p,q

n=5
m=6
x=np.linspace(-1,1,n+m-1)
y=1/(1+x**2)
xx=np.linspace(x[0],x[-1],2000)
p,q=rat_fit(x,y,n,m)
yy_rat=rat_eval(p,q,xx)
error_rat=np.std(y_true-yy_rat)
print('The error of rational fit is' , error_rat)

#plot
plt.clf()
plt.plot(x,y,'*',label='choosed modest points')
plt.plot(xx,yy_spl,'b',label='spline')
plt.plot(xx,yy_rat,'g',label='rational fit')
plt.plot(xx,yy_poly,'r',label='polynomial fit')
plt.plot(xx,y_true,'y',label='true')
plt.legend()
plt.savefig('question3_lonrenztian_accuracy_comparsion.png')
