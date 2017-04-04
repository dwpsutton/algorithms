'''
    Module to calculate MST of a dense city-city graph.
'''
__author__ = 'David Sutton'

class EDGE:
    def __init__(self,start,end,weight):
        self.start= start
        self.dest= end
        self.length= weight
        return None


def toEdgeList(nodes,distances):
    numNodes= nodes
    numEdges= 0
    edges= []
    for a in nodes:
        for b in nodes:
            if a>b:
                edges.append( EDGE( a, b, distances[a,b]) )
                numEdges += 1
    return numNodes, numEdges, edges

def prims(nodes,distances):
    '''
        Double check that this solution is O(n)
    '''
    numNodes, numEdges, edges= toEdgeList(nodes,distances)
    cost= 0
    explored= {}
    explored[edges[0].start]= 0
    while len(explored) < numNodes:
        mymin= []
        for ctr,e in enumerate(edges):
            if e.start in explored and e.dest not in explored:
                if mymin== []:
                    mymin= e.length
                    mychoice= ctr
                elif e.length < mymin:
                    mymin= e.length
                    mychoice= ctr
            elif e.dest in explored and e.start not in explored:
                if mymin== []:
                    mymin= e.length
                    mychoice= -ctr
                elif e.length < mymin:
                    mymin= e.length
                    mychoice= -ctr
        if mychoice >= 0:
            explored[edges[mychoice].dest]= 0
        else:
            explored[edges[abs(mychoice)].start]= 0
        cost += edges[abs(mychoice)].length
    return cost
