import numpy as np

def lorentz(x):
    return 1/(1+x**2)

def non_match_elements(list_a, list_b):
    non_match = []
    for i in list_a:
        if i not in list_b:
            non_match.append(i)
    return non_match

def integrate_step(fun,x1,x2,tol,x_tot,y_tot):
    print('integrating from ',x1,' to ',x2)
    if len(x_tot)<5:
        x=np.linspace(x1,x2,5)
        x_add=non_match_elements(x_tot,x)
        x_tot=x_tot+x_add
        y_add=fun(x_add)
        y_tot=y_tot+y_add 
    
    area1=(x2-x1)*(y_add[0]+4*y_add[2]+y_add[4])/6
    area2=(x2-x1)*( y_add[0]+4*y_add[1]+2*y_add[2]+4*y_add[3]+y_add[4])/12

    else:
        x=np.linspace(x1,x2,5)
        x_add=non_match_elements(x_tot,x)
        x_tot=x_tot+x_add
        y_add=fun(x_add)
        y_tot=y_tot+y_add 
    
        area1=(x2-x1)*(y_add[0]+4*y_add[2]+y_add[4])/6
        area2=(x2-x1)*( y_add[0]+4*y_add[1]+2*y_add[2]+4*y_add+y_add[4])/12
        
    myerr=np.abs(area1-area2)
    if myerr<tol:
        return area2
    else:
        xm=0.5*(x1+x2)
        a1=integrate_step(fun,x1,xm,tol/2,x_tot,y_tot)
        a2=integrate_step(fun,xm,x2,tol/2,x_tot,y_tot)
        return a1+a2


x0=-10
x1=10
ans1=integrate_step(lorentz,x0,0,0.001)
ans2=integrate_step(lorentz,0,x1,0.001)
ans=ans1+ans2
print('area is ',ans)
