import matplotlib.pyplot as plt
import os
clear = lambda: os.system('cls')
clear()
import numpy as np
import random
np.random.seed(10)
import math
import statistics
import pandas as pd
from scipy import stats
from scipy.stats import genpareto

def fun () :
    lst1=[]
    lst2=[]
    sig=[0.5];
    qmu=0;
    q=0.25
    beta=1
    N=10000
    #z=np.zeros(N)
    y2=np.zeros(N)
    d=1
    #pi=3.14159265358979324
    pi=3.1416
    #k1=np.zeros((25,2))

    #k_hat1=np.empty(25, dtype=np.float64)
    #sig_hat1=np.zeros(25)
    #k_hat2=np.zeros(25)
    #sig_hat2=np.zeros(25)
    #MSE_1=np.zeros(25)

    #k_hat_po=np.zeros(len(sig))
    #k_hat_ne=np.zeros(len(sig))
    #k_hat_2_po=np.zeros(len(sig))
    #k_hat_2_ne=np.zeros(len(sig))
    #sig_hat_po=np.zeros(len(sig))
    #sig_hat_ne=np.zeros(len(sig))
    #MSE_sig_hat=np.zeros(len(sig))

    # Loop for q value


    #for ia1 in range(0,len(sig)):
        #a1=sig[ia1]
    y2 = stats.genpareto.rvs(q, loc=0, scale=sig,size=N)

    y3=y2

    ww=np.concatenate((np.ones(int(np.size(y2)/2)),-np.ones(np.size(y2)-int(np.size(y2)/2))))

    y3=y2*random.choices(ww,k=np.size(y2))
    rng = np.random.default_rng(12345)
    vals=rng.integers(low=np.size(y2)*0,high=np.size(y2),size=np.size(y3))


    ss=y3[random.choices(vals, k=len(y3)-len(y3)%3)]


    A=np.reshape(ss,(-1,3))


    A[:,2] = A[:,2] *-1

    sig_hat= stats.genpareto.fit(y2)[2]
    sig_hat1=sig_hat
    z1=len(A[:,2])

    D=np.amax(A, axis=1)-np.amin(A, axis=1)

    # Find index and sort the D vector.
    ix=np.argsort(D) 

    minD=D.sort()
    #sort A matrix based on index from small to large number.
    SS = A[ix,:]
    #Choosing (0.5%) from smallest data

    #============================
    condition = True
    step = 1
    flag = 1
    nn0=100
    nnf=2250
    tol = 1e-4
    #-----------
  
    while condition and nn0 < nnf:
        #np.any(error > tol) and i3 < max_iter:
        lst1.append(nn0)
        S=SS[0:math.floor(nn0),:]
        x=abs(np.median(S, axis=1))
        #nn=len(x)
        m=0.0
        for i in range(nn0):
            m=m+(x[i])**2;
        M_2=(1/nn0)*m;
        M_3 = stats.moment(x, moment=2)
        sig_hat2=np.sqrt((M_2*(9+3*q))/4)
        sig_hat_ne=np.mean(sig_hat2)
        error=sig_hat_ne-sig[0]
        lst2.append(sig_hat_ne)
        print('Iteration-%d, nn0 = %d, sig_hat_ne = %0.6f, error = %0.6f' % (step, nn0, sig_hat_ne,error))
        #nn0=S
        nn0 = nn0 + 1
        step = step + 1
                
        if nn0 > nnf:
            flag = 0
      
    
        condition = abs(error) > tol
    return [lst1,lst2]    
        
    # if flag==1 and condition == False:
    #     print('\n sig_hat_ne is: %0.8f' % sig_hat_ne)
    #     dic_vals={"sig_hat_ne":sig_hat_ne,"nn0":nn0}
    #     return dic_vals
   
    # else:
    #     print('\nNot Convergent.')
    #     return False
   
#============================ #

lst = fun()
nn0_lst=lst[0]
sig_hat_ne_lst=lst[1]
plt.plot(nn0_lst,sig_hat_ne_lst) 
plt.show()   
# sig_list= []
# number_list=[]
# while len(sig_list) <= 10 :
#     value = fun()
#     if (value):
#         sig_list.append(value['sig_hat_ne'])
#         number_list.append(value["nn0"])
# plt.plot(sig_list,number_list) 
# plt.show()