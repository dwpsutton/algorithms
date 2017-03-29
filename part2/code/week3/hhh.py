#-*- coding: utf-8 -*-
import sys, time
gk = lambda i,j:str(i)+','+str(j)

def optimal_BST(p, q, n):   #pæåéåçæç(nä)， qæäåéåçæç(n+1ä)， næåéåçäæ
    MAX = (max(p)>max(q) and max(p) or max(q))*(n+1)*(len(p)+len(q))  #èçæåå ååpåqäçæåçääæçå，
                                                                      #ään+1(æå)，åælen(p)+len(q)äèç，
                                                                      #æçæçææäåèæèäåå
    e, w, root = {}, {}, {} #eåæææ wåææçå rootåæåæçæèç
    for i in xrange(1, n+2): #åååeåw iåä[1,n+1]
        e[gk(i, i-1)] = q[i-1]
        w[gk(i, i-1)] = q[i-1]
    for l in xrange(1, n+1):   #läèçæåæçéå låä[1,n]
        for i in xrange(1, n-l+2): # iæéåälçæäåæçåéåçæåççåå iåä[1,n-l+1]
            j = i+l-1        #iæåæåéåçååå，jæçæåçåæ，åéççåæä1ååç，èpæä0ååç，éèå+1æä
            e[gk(i, j)] = MAX
            w[gk(i, j)] = w[gk(i, j-1)]+p[j-1]+q[j]
            for r in xrange(i, j+1): #råä[i,j]
                t = e[gk(i, r-1)]+e[gk(r+1, j)]+w[gk(i, j)]
                if t<e[gk(i, j)]:
                    e[gk(i, j)] = t
                    root[gk(i, j)] = r
    return e, root

def main():
    p = [0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    e, root = optimal_BST(p, q, len(p))
    print e[gk(1,len(p))]
    
if __name__ == '__main__':
    main()
