#!/Users/davidsutton/usr/canopy/bin/python
import quickSort_demo
import copy,sys

# Read the data
data= []
with open('homework_data.txt','rb') as fin:
    for l in fin:
        data.append(int(l))

sorted, ctr= quickSort_demo.quickSort( copy.deepcopy(data), method= 'first' )
print quickSort_demo.tester(sorted)
print 'first: ', ctr, len(sorted)


sorted, ctr= quickSort_demo.quickSort( copy.deepcopy(data), method= 'last' )
print quickSort_demo.tester(sorted)
print 'last: ', ctr, len(sorted)


sorted, ctr= quickSort_demo.quickSort( copy.deepcopy(data), method= 'median-of-three' )
print quickSort_demo.tester(sorted)
print 'median-of-three: ', ctr, len(sorted)


sorted, ctr= quickSort_demo.quickSort( copy.deepcopy(data), method= 'random' )
print quickSort_demo.tester(sorted)
print 'random: ', ctr, len(sorted)