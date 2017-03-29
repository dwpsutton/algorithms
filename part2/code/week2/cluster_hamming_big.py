#!/Users/davidsutton/usr/canopy/bin/python
#import numpy as np
import copy,sys



class UF(object):
    def __init__(self,node_labels):
        self.ctr= len(node_labels)
        self.leader= {}
        self.size= {}
        self.followers= {}
        for i in node_labels:
            self.leader[i]= i
            self.size[i]= 1
            self.followers[i]= [i]
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
    nodes= []
    header= map(int,f.readline().split())
    num_nodes= header[0]
    nbits= header[1]
    for line in f:
        linestr= line.split()[0]
        for i in range(1,nbits):
            linestr += line.split()[i]
        nodes.append( linestr )
        #print linestr
    return num_nodes,nbits,nodes

def hammingDistance(x,y):
    return sum([ abs( int(z[0]) - int(z[1]) ) for z in zip(x,y) ])

def permutationIterator(x):
    # Finds all candidate strings that would be distance 1 or 2 away
    xvec= [int(i) for i in x]
    nbits= len(xvec)
    yield x
    for i in range(nbits):
        xtemp= copy.deepcopy(xvec)
        xtemp[i]= abs( xvec[i] - 1 )
        for j in range(i,nbits):
            xtemp2= copy.deepcopy(xtemp)
            if j!=i:
                xtemp2[j]= abs( xtemp[j] -1 )
            yield ''.join(str(e) for e in xtemp2)


if __name__ == '__main__':
    dave= '0001'
    perms= permutationIterator(dave)
    ctr= 0
    for i in perms:
        print i, hammingDistance(dave,i)
        ctr+=1
    print ctr


    fname= 'clustering_big.txt'  # 2_1 should be 6, 2_2 should be 4
    num_nodes, nbits, nodes= readData(fname)
    print num_nodes,len(nodes)
    checker= {}
    ndups=0
    for i in nodes:
        if i in checker:
            checker[i] += 1
            ndups+=1
        else:
            checker[i]= 1
    print 'found ',ndups,' duplicates'
    #
    # Now create list of viable short edges
    ll= []
    n1= []
    n2= []
    ctr= 0
    processed={}
    for inode in nodes:
#        for jnode in nodes:
#            dd= hammingDistance(inode,jnode)
#            if dd < 3:
#                ll.append(dd)
#                n1.append(inode)
#                n2.append(jnode)
#                ctr+=1
        if inode not in processed:
            processed[inode]= 1
            perms= permutationIterator(inode)
            for p in perms:
                if p in checker:
                    #if p not in processed:
                    #processed[p]= 1
                    #for i in range(checker[p]):
                    ll.append( hammingDistance(inode,p) )
                    n1.append( inode )
                    n2.append( p )
                    ctr+=1
    print ctr,' edges found'
    #
    # Now do the clustering
    #
    isort= sorted(range(len(ll)),key=lambda x:ll[x]) #isort= np.argsort(ll)
    ufo= UF(processed.keys())
    k= ufo.ctr
    i_ctr= 0
    bobo =0
    while k>1:
        if i_ctr/1000 > bobo:
            bobo+=1
            print bobo
        # check edge node 1 and node 2 are not in same cluster, unioning if not, skipping if so
        i_edge= isort[i_ctr]
        if ufo.leader[n1[i_edge]] == ufo.leader[n2[i_edge]]:
            i_ctr+=1
        else:
            ufo.union(n1[i_edge], n2[i_edge])
            i_ctr+=1
            k -= 1
        if i_ctr >= len(isort):
            print 'Found ',k,'disconnected components!'
            sys.exit()
    print 'Found ',k,' clusters'