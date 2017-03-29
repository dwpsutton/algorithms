#!/Users/davidsutton/usr/canopy/bin/python
import numpy as np,copy



class UF(object):
    def __init__(self,num_nodes):
        self.ctr= num_nodes
        self.leader= {}
        self.size= {}
        self.followers= {}
        for i in range(num_nodes):
            self.leader[i+1]= i+1
            self.size[i+1]= 1
            self.followers[i+1]= [i+1]
        return None

    def find(self,x):
        return self.leader[x]

    def union(self,px,py):
        x= self.leader[px]
        y= self.leader[py]
        if self.size[x] < self.size[y]:
            # Reassign leader of smaller cluster and adjust size
            self.leader[x]= self.leader[y]
            self.size[y] += self.size[x]
            # Keep track of clusters new members
            self.followers[y] += copy.deepcopy( self.followers[x] )
            self.followers[x]= []
            for i in self.followers[y]:
                self.leader[i]= self.leader[y]
        else:
            self.leader[y]= self.leader[x]
            self.size[x] += self.size[y]
            self.followers[x] += copy.deepcopy( self.followers[y] )
            self.followers[y]= []
            for i in self.followers[x]:
                self.leader[i]= self.leader[x]
        self.ctr -=1 #reduce number of clusters
        return None


def readData(fname):
    f= open(fname)
    lengths= []
    node1s= []
    node2s= []
    num_nodes= int(f.readline())
    for line in f:
        node1s.append( int(line.split()[0]) )
        node2s.append( int(line.split()[1]) )
        lengths.append( int(line.split()[2]) )
    return num_nodes,np.array(node1s),np.array(node2s),np.array(lengths)

if __name__ == '__main__':
    fname= 'clustering_small.txt'
    num_nodes, n1,n2,ll= readData(fname)
    #
    isort= np.argsort(ll)
    ufo= UF(num_nodes)
    k= ufo.ctr
    i_ctr= 0
    while k>4:
        # check edge node 1 and node 2 are not in same cluster, unioning if not, skipping if so
        i_edge= isort[i_ctr]
        if ufo.leader[n1[i_edge]] == ufo.leader[n2[i_edge]]:
            i_ctr+=1
        else:
            ##print '--',ufo.followers[ufo.leader[n1[i_edge]]],ufo.followers[ufo.leader[n2[i_edge]]]
            ufo.union(n1[i_edge], n2[i_edge])
            ##print '++',ufo.followers[ufo.leader[n1[i_edge]]],ufo.followers[ufo.leader[n2[i_edge]]]
            i_ctr+=1
            k -= 1
    i_edge= isort[i_ctr]
    #
    # print the next non-cycle edge, which is the max spacing
    while ufo.leader[n1[i_edge]] == ufo.leader[n2[i_edge]]:
        i_ctr += 1
        i_edge= isort[i_ctr]
    print ll[i_edge]