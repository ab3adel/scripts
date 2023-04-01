# -*- coding: utf-8 -*-
"""location_estemator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CckqDieXMu-JdiU8dazbHh-DLVcDKlHw
"""

# -*- coding: utf-8 -*-
import numpy as np
import random
np.random.seed(10)
import math
import statistics
from scipy import stats
import pandas as pd


sig=1;
qmu=[0.5,50,100];
q=0.25
N=10000
beta=1
#z=np.zeros(N)
y2=np.zeros(N)
d=1
#pi=3.14159265358979324
pi=3.1416
#k1=np.zeros((25,2))

k_hat1=np.empty(25, dtype=np.float64)
sig_hat1=np.zeros(25)
k_hat2=np.zeros(25)
sig_hat2=np.zeros(25)
MSE_1=np.zeros(25)

k_hat_po=np.zeros(len(qmu))
k_hat_ne=np.zeros(len(qmu))
k_hat_2_po=np.zeros(len(qmu))
k_hat_2_ne=np.zeros(len(qmu))
sig_hat_po=np.zeros(len(qmu))
sig_hat_ne=np.zeros(len(qmu))
MSE_sig_hat=np.zeros(len(qmu))

# Loop for q value
for ia1 in range(0,len(qmu)):
    a1=qmu[ia1]
    for it in range(0,25):
        for i in range(0,N):
            u1= np.random.uniform()
            u2= np.random.uniform()
            u1= u1**(-2)
            lnq= ((u1**q-1)/q)
            z2= np.sqrt(lnq)*np.cos(2*pi*u2)
            y2[i]=  a1 + sig*z2
        y3=y2
    #print("The Array is : ")
    #for k in y3:
        #print(k, end = ' ')
    
      #Divided vector y3 in to three vectors but randomly
        ss=y3[np.random.choice(np.random.permutation(len(y3)), size=len(y3)-len(y3)%3, replace=False)]
        A=np.reshape(ss,(-1,3))
       
        z1=len(A[:,1])
        
        #I take maximum number from each row - minimum number from each row. 
        D=np.amax(A, axis=1)-np.amin(A, axis=1)
        # Find index and sort the D vector.
        ix=np.argsort(D) 
        minD=D.sort()
        #sort A matrix based on index from small to large number.
        SS = A[ix,:]
        #Choosing (0.5%) from smallest data
        S=SS[0:math.floor(0.05*z1),:]
        #take median
        x=np.mean(S, axis=1)
        #x=x1.T
        #estimate parameter using maximum likelihood method for generalize pareto distribution.
        
        # Fit Student’s t continuous random variable
        
        #L=stats.t.fit(x)
        #print('L',L)
        sig_hat  = stats.t.fit(y3)[1]
        sig_hat1[it]=sig_hat

        #print('K_hat11',k_hat11)


        #estimate parameter using different method
        nn=len(x)
        m=0.0
        for i in range(nn):
            m=m+(x[i])**2;

        M_2=(1/nn)*m;
        M_3 = stats.moment(x, moment=2)
        
        sig_hat2[it]=np.sqrt((3*M_2-(sig)**2)/3)
        #MSE_1[it]=(np.sqrt((3*M_2-(sig)**2)/3)-a1)**2
        #sig_tr[it]=np.sqrt(4*M_2+1*M_2)
    
    
    #k_hat_po[ia1]=np.mean(sig_hat2)+2*np.std(sig_hat2)   # std=standard deviation
    #k_hat_ne[ia1]=np.mean(sig_hat2)-2*np.std(sig_hat2)
    #k_hat_2_po[ia1]=np.mean(k_hat2)+2*np.std(k_hat2)
    #k_hat_2_ne[ia1]=np.mean(k_hat2)-2*np.std(k_hat2)
    #sig_hat_po[ia1]=np.mean(sig_tr)+2*np.std(sig_tr)
    #sig_hat_ne[ia1]=np.mean(sig_tr)-2*np.std(sig_tr)
    #sig_hat_po[ia1]=np.mean(sig_hat1)+2*np.std(sig_hat1)
    #sig_hat_ne[ia1]=np.mean(sig_hat1)-2*np.std(sig_hat1)
    #MSE_sig_hat[ia1]=np.mean(MSE_1)
    k_hat_2_po[ia1]=np.square(np.subtract(sig_hat1,a1)).mean()
    k_hat_2_ne[ia1]=np.square(np.subtract(sig_hat2,a1)).mean()
    sig_hat_po[ia1]=np.mean(sig_hat1)
    sig_hat_ne[ia1]=np.mean(sig_hat2)
    k_hat_po[ia1]=np.std(sig_hat1)   # std=standard deviation
    k_hat_ne[ia1]=np.std(sig_hat2)
    #import seaborn as sns

    #sns.set_style('darkgrid')
    #sns.distplot(G,100)

#print('MSE_sig_hat',MSE_sig_hat)
True_AI_sig=[0.5,50,100]
No=range(len(True_AI_sig))
#ML_sig_hat_1=sig_hat_po
#ML_sig_hat_2=sig_hat_ne
#AI_sig_hat_1=k_hat_po
#AI_sig_hat_2=k_hat_ne

ML_sig_hat_ms_1=k_hat_2_po
ML_sig_hat_ms_2=k_hat_2_ne
ML_sig_hat_1=sig_hat_po
AI_sig_hat_1=sig_hat_ne
ML_sig_hat_2=k_hat_po
AI_sig_hat_2=k_hat_ne
df_T = pd.DataFrame({'True_value': True_AI_sig,'Maximum_likelihood(ML)': ML_sig_hat_1,'Independent_approximates(IA)': AI_sig_hat_1,'std of ML':ML_sig_hat_2,'std of IA':AI_sig_hat_2,'MSE of ML':ML_sig_hat_ms_1,'MSE of IA':ML_sig_hat_ms_2})

#df_T = pd.DataFrame({'No': No, 'True_IA_sig': True_IA_sig,'ML_k_hat_1': ML_sig_hat_1,'ML_sig_hat_2': ML_sig_hat_2,'AI_sig_hat_1': AI_sig_hat_1,'AI_sig_hat_2': AI_sig_hat_2})
print(df_T)