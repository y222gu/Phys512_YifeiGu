import numpy as np

expvals=np.linspace(-16,-0.5,30)
x0=1

#for f(x)=exp(x): 
print("The result for f(x)=exp(x) are :")
truth=np.exp(x0)
f=np.exp(x0)
for myexp in expvals:
    dx=10**myexp
    f1=np.exp(x0+dx)
    f2=np.exp(x0-dx)
    f3=np.exp(x0+2*dx)
    f4=np.exp(x0-2*dx)
    deriv1=[8*(f1-f2)-(f3-f4)]/(12*dx) #make the derivative according with the given four points 
   
    print(myexp,deriv1,np.abs(deriv1-truth))

#for f(x)=exp(0.01x):
print("The result for f(x)=exp(0.01x) are :")
truth= np.exp(0.01*x0)*0.01
f=np.exp(0.01*x0)
for myexp in expvals:
    dx=10**myexp
    f1=np.exp(0.01*(x0+dx))
    f2=np.exp(0.01*(x0-dx))
    f3=np.exp(0.01*(x0+2*dx))
    f4=np.exp(0.01*(x0-2*dx))
    deriv2=[8*(f1-f2)-(f3-f4)]/(12*dx) #make the derivative according with the given four points 
    
    print(myexp,deriv2,np.abs(deriv2-truth))