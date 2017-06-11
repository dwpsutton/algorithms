import SSC
from kosaraju_main import *
from datetime import datetime, timedelta

def kosaraju(graph):
    tc= datetime.now()
    graph= graph.reverse()
    print 'Reversed graph ',(datetime.now()-tc).total_seconds()
    DFSIterative( graph, graph.nodeSet.keys() )
    print 'First DFS call ',(datetime.now()-tc).total_seconds()
    graph= graph.reverse()
    ordering= copy.deepcopy( graph.order.values )
    graph.order= SSC.STACK()
    DFSIterative(graph, ordering )
    return graph
    
def verifySAT(graph):
    sscs= {}
    for i,node in graph.nodeSet.items():
        ii= -1 * i  # disjoint of literal i
        # Add literal i into ssc checker
        if node.leader not in sscs:
            sscs[node.leader]= set( [i] )
        else:
            sscs[node.leader].add( i )
        # check if disjoint of literal i exists in set (node labels are positive integers)
        if ii in sscs[node.leader]:
            # Here we have found a literal and its disjoint in same SSC, so exit
            return False
    return True

def readImplicationGraph(fname):
    '''
        Reads a file of normal conjunctive constraints and constructs implication graph.
        Input file: first line is total number of constraints (= number of literals). Then 2 cols for the two
        literals in constraint, negative denoting 'not'.
        Implication graph has two nodes per literal (for true and false), and two edges per constraint indicating
        implied disjunction (ie: for (`x1 V x2) would be a directed edge from +1 to +2 and -2 to -1.
    '''
    with open(fname,'rb') as f:
        ctr= 0
        edgeList= []
        for line in f:
            if len(line.split()) == 1:
                n= len(line.split())
            else:
                thisTuple= [int(e) for e in str(line).strip().split()]
                edgeList.append( [-thisTuple[0] , thisTuple[1]] )
                edgeList.append( [-thisTuple[1] , thisTuple[0]] )
            ctr+=1
                #if ctr==1E4:
                #break
    return SSC.DIRECTEDGRAPH( edgeList)

def twoSAT(fname):
    graph= readImplicationGraph(fname)
    graph= kosaraju( graph )
    return verifySAT(graph)

def main():
    #fnames= ['test1_true.txt','test2_false.txt']
    fnames= ['2SAT'+str(i+1)+'.txt' for i in range(4,6)]
    print fnames
    for f in fnames:
        print f
        print twoSAT(f)

if __name__ == '__main__':
    main()