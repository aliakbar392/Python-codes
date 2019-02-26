#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import time
start = time.time()

i=0
t=int(input('test case:'))
n=int(input('contestant:'))
p=np.zeros(shape=(t,n))
while(i<t):
    l=[]
    u=[]
    h=[]
    s=[]
    a=[]
    if i>0:
        n=int(input('contestant:'))
    
    j=0
    while(j<n):
        l.append(int(input('lower bound:')))
        
        u.append(int(input('upper bound:')))
        j=j+1
    k=0
    while(k<n):
        m=[]
        s=[]
        h.append(m)
        for q in range(l[k], u[k]+1):
            s.append(q)
        h[k].extend(s)
        print("s=",s)
        k=k+1
    w=0
    while(w<n):
        e=1
        while((w+e)<n):
            if((u[w]-l[w])>=(u[w+e]-l[w+e])):
                if(set(h[w])>=set(h[w+e])):
                    p[i][w]=p[i][w]+2
                    p[i][w+e]=p[i][w+e]+0
                else:
                    p[i][w]=p[i][w]+1
                    p[i][w+e]=p[i][w+e]+1
            else:
                if(set(h[w])<=set(h[w+e])):
                    p[i][w]=p[i][w]+0
                    p[i][w+e]=p[i][w+e]+2
                else:
                    p[i][w]=p[i][w]+1
                    p[i][w+e]=p[i][w+e]+1
                
            e=e+1
        w=w+1
    i+=1
    
print("points:")
for i in range(t):
    print(p[i])
end = time.time()
print(end - start)


# In[ ]:




