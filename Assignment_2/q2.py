import numpy as np
from matplotlib import pyplot as plt

#define the function extract the coefficient matrix
def chebyshev_mat(x,order):
    mat= np.zeros([len(x),order+1])
    mat[:,0]=1
    mat[:,1]=x
    for i in range(1,order):
        mat[:,i+1]=2*x*mat[:,i]-mat[:,i-1]
    return mat

def lin(mat,y):
    u,s,v=np.linalg.svd(mat,0)
    fitp=v.T@(np.diag(1/s)@(u.T@y))
    return fitp

def chebyshev_fit(x,y,order):
    mat=chebyshev_mat(x, order)
    for ncoeffs in range(0,order):
            mat_ncoeffs=mat[:,:ncoeffs]
            fitp=lin(mat_ncoeffs,y)
            #pred are only calculated to the terms that gives an error smaller than 10**-6
            pred=mat_ncoeffs@fitp
            e=np.sqrt(np.mean((pred-y)**2))
            if e <= 10**-6:
                #the first coefficient term starts with a index of 0
                #so the terms number should plus 1
                return pred, ncoeffs  
                break

#rescale the x to the range of Chebyshev
x= np.linspace(-1,1,51)
y_true = np.log2((x+3)/4)

#To get the order we need:
pred1,terms=chebyshev_fit(x,y_true,50)

#legendre poly with same number of terms
mat_2=np.polynomial.legendre.legvander(x,terms)
pred2 = mat_2@lin(mat_2,y_true)


#print the results
print('The terms we need is ',terms+1,'to reach an accuracy in the region better than 10^-6.')

print('RMS error of Chebyshev poly fit is ' ,np.sqrt(np.mean((pred1-y_true)**2)))
print('RMS error of legendre poly fit is ' ,np.sqrt(np.mean((pred2-y_true)**2)))

print('max error of Chebyshev poly fit is ' , np.max(np.abs(pred1-y_true)))
print('max error of legendre poly fit is ' ,np.max(np.abs(pred2-y_true)))

#plot the scatter plot
plt.clf();
plt.scatter(x,pred1-y_true,label="Chebyshev poly fit", s=12)
plt.scatter(x,pred2-y_true,label="legendre poly fit",s=12)
plt.legend()
plt.savefig('cheb_lss_resids.png')

    
