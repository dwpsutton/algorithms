#!/Users/davidsutton/usr/canopy/bin/python
import sys, random, copy, gzip, resource
from datetime import datetime, timedelta
import SSC


def DFSr(graph,inode):
    '''
        Beautiful and elegant recursive algorithm.  Not for large graphs due to python recursion
        limits. Instead of determining finishing time for a node, we push the node onto an ordering
        stack (avoids having to sort the finishing time array).
    '''
    node= graph.nodeSet[inode]
    node.explored= True
    node.leader= s
    #print inode,node.outList()
    for jnode in node.outList():
        if not graph.nodeSet[jnode].explored:
            DFSr(graph,jnode)
    graph.order.push(inode)
    return None

def DFSRecursive(graph,ordering ):
    global s
    s= None
    for i in range(len(ordering)):
        inode= ordering[ len(ordering)-1-i ]
        node= graph.nodeSet[inode]
        if not node.explored:
            s = inode
            DFSr(graph,inode)
    return None


def DFSIterative(graph,ordering):
    '''
        Iterative version of depth first search.  Only way to search large graphs, due to python's
        limitations with recursion.  Replaces recursion with a while loop and a stack.  Includes a
        trick for determining when a node's children have been thoroughly explored.  In the recursive
        version, this trivial: you mark it after the recursive call on all children.  Here, you have
        to push the current node onto the stack again before adding its children.  When children have
        been finished, you see the node again and can mark it.
    '''
    stack= []
    s= None
    finished= {}
    explored= {}
    #    kalaboos= 0
    
    for i in range(len(ordering)):
        stack= []
        inode= ordering[ len(ordering)-1-i ]
        #        kalaboos += len(graph.nodeSet[inode].outEntities)+1
        #        print i,inode,kalaboos
        
        counter= 0
        if inode not in explored:
            stack= [inode] + stack
            counter += 1
        
        while counter > 0:
            jnode= stack[0]
            del stack[0]
            counter -= 1
            if jnode not in explored:
                explored[jnode]= 1
                graph.nodeSet[jnode].leader= inode
                stack = [jnode] + stack
                counter += 1
                for knode in graph.nodeSet[jnode].outEntities:
                    if knode not in explored:
                        stack = [knode] + stack
                        counter += 1
            elif jnode not in finished:
                finished[jnode]= 1
                graph.order.push(jnode)

            #if i==7113:
            #    print 'explored=',len(explored)
    return None




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
    sscs= {}
    for i,node in graph.nodeSet.items():
        if node.leader not in sscs:
            sscs[node.leader]= 1
        else:
            sscs[node.leader] += 1
    return sscs

if __name__ == '__main__':
    '''
        This took 3h and 40mins to run, even with pypy!!
    '''
    
    fname= 'homework_data.txt.gz'
    graph= SSC.DIRECTEDGRAPH( SSC.generateEdgeList(fname) )
    sscs= kosaraju(graph)
    print ''
    print sorted(sscs.values(),reverse=True)[0:5]