import numpy as np

v= range(7)
fa= [0.05,0.4,0.08,0.04,0.1,0.1,0.23]
f={}
for i in range(1,8):
    f[i]= fa[i-1]
print sum(f)



A= np.zeros([7,7])
W= np.zeros([7,7])
for s in range(7):
    for i in range(7-s):
        j= i+s
        if j<7:
            W[i,j]= W[i,j-1]+fa[j]  #Not = fa[k], which is what is implied in the lectures...
            arr= []
            for k in range(i,j+1):
                if k-1 < 0:
                    arr.append( W[i,j] + A[k+1,j] )
                elif k+1 > 7-1:
                    arr.append( W[i,j] + A[i,k-1] )
                else:
                    arr.append( W[i,j] + A[i,k-1] + A[k+1,j] ) #fa[k] + A[i,k-1] + A[k+1,j] )
            A[i,j]= min(arr)
print A

'''
Knuth's optimisation for O(n^2).  Modify the range of considered values of k:
    
    if length=1 then
        m := j
    else
        m := value of k (with r_{i,j-1} ≤ k ≤ r_{i+1,j}) which minimizes (c_{i,k-1}+c_{k,j})
'''