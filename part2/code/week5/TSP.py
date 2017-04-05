from itertools import combinations
from copy import deepcopy
from math import sqrt
from prims import prims

__author__= 'David Sutton'


fname= 'test2.txt'

def read_nodes(fname):
    x= []
    y= []
    with open(fname,'rb') as f:
        n= int(f.next())
        #ctr=0
        for line in f:
            fields= map(float, line.split(' '))
            x.append( fields[0] )
            y.append( fields[1] )
                #if ctr > 18:
                #break
                #ctr+=1
    #n=18
    return x,y,n

def distances(x,y):
    distance= {}
    for i in range(len(x)):
        for j in range(len(x)):
            distance[i,j]= sqrt( (x[i]-x[j])**2 + (y[i]-y[j])**2)
    return distance

def tsp_naive(distance,n):
    '''
        Implementation of the lecture's dynamic programming algorithm.
    '''
    # Initialise
    A= {}
    A[ str([ [0], 0]) ]= 0
    #
    # Iterate
    for m in range(1,n):
        print m
        for S in combinations( range(1,n), m ):
            S= [0]+list(S)
            for j in S[1:]:
                SmJ= deepcopy(S)
                SmJ.remove(j)
                if SmJ is not None:
                    thing= [] # rename this
                    for k in SmJ:
                        if k==0 and SmJ != [0]:
                            continue
                        thing.append( A[str([SmJ,k])] + distance[k,j] )
                    if len(thing) > 0:
                        A[str([S,j])]= min(thing)
    #
    # Get minimal tour over possible endpoints
    finalSet= []
    for j in range(1,n):
        finalSet.append( A[str([range(n), j])] + distance[j,0] )
    return min(finalSet)




def lower_bound(sp,distance):
    '''
        Uses Prim's algorithm to return cost of MST of remainder of tour.  This is added to
        minimum cost edge from current vertex to remainder of tour, and the minimum cost edge
        from the remainder of tour to the end point node (0).
        input is of structure (remainder of tour, current vertex, cost of tour to vertex), and distance matrix
    '''
    return prims(sp[0],distance) + min( [ distance[sp[1],i] for i in sp[0] ] ) + min( [distance[0,i] for i in sp[0] ] )

def branch_and_bound(distance,n):
    '''
        Implementation of a branch and bound approach, as in page 287 of:
        http://www.cse.iitd.ernet.in/~naveen/courses/CSL630/all.pdf
        The text here is a little confusing.  The TSP description actually considers
        a sub-problem Pi to be the completion of the tour. You bring in potential next
        steps into active sub-problems, only if it is possible for the solution to be 
        better than one you already have.  This way you avoid useless sub-trees and 
        reduce the space being explored relative to brute-force search.
        TODO: debug prims module.  Without lower bound, this algo is numerically identical to naive on test data.
    '''
    # Data structure: stack of subproblems, each containing:
    #  (remainder of tour, current vertex, cost of tour to vertex)
    subProblems= [ (range(1,n), 0, 0.) ]
    #
    bestSoFar= sum(distance.values())+1
    while len(subProblems) > 0:
        print subProblems
        if lower_bound( subProblems[-1], distance ) > bestSoFar:
            # Unnecessary sub-tree, remove from stack
            del subProblems[-1]
        else:
            # worth exploring sub-tree
            toExplore= subProblems[-1][0]
            parentNode= subProblems[-1][1]
            parentCost= subProblems[-1][2]
            del subProblems[-1]
            #
            if len(toExplore) == 1:
                # Base case: is a complete solution, update best solution if its been improved
                childNode= toExplore[0]
                cost= parentCost + distance[parentNode,childNode] + distance[childNode,0]
                if cost < bestSoFar:
                    bestSoFar= cost
            else:
                # Add children of subtree root to active sub-problem stack
                for childNode in toExplore:
                    newSubProblem= deepcopy(toExplore)
                    newSubProblem.remove(childNode)
                    subProblems.append( ( newSubProblem,
                                          childNode,
                                          parentCost + distance[parentNode,childNode] )
                                       )
    return bestSoFar


def main():
    x,y,n= read_nodes(fname)
    distance= distances(x,y)
    minDist= branch_and_bound(distance,n)
    print minDist

if __name__=='__main__':
    main()