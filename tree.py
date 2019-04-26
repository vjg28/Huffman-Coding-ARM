
'''
eg> nodes
value - key
a     - 5
b     - 15
c     - 3
d     - 10
e     - 25

in huffing tree:
Each node is either a leaf with one of the key and value specified or has 2 children with value '*' and key with value addition of both children node.
This important property will be exploited to make an easy tree

There will be total n leaf nodes and n-1 non-leaf nodes (in our case 5 leaf and 4 non-leaf nodes)

eg. of formed tree

						58
					    (*)				
				33			25
				(*)			(E)
		18			15
		(*)			(B)
10			8
(D)		    (*)
		5		3	
		(A)		(C)

Array Structure:
	0    1    2    3    4    5    6    7    8
    *    *    E    *    B    D    *    A    C
    58   33   25   18   15   10   8    5    3	

'''

data=[
	('a',5),
	('b',15),
	('c',3),
	('d',10),
	('e',25),
]

from operator import itemgetter
data = sorted(data, key = itemgetter(1))
print('INPUT DATA:')
print (data)

data2=[]

while(len(data)>1):
	a=data[0]
	b=data[1]
	c=('*',a[1]+b[1])
	data.pop(0)
	data.pop(0)
	data.append(c)
	data = sorted(data, key = itemgetter(1))
	if(a[0]!='*'):
		data2.append(a)
	if(b[0]!='*'):	
		data2.append(b)
	data2.append(c)
#a=data[0]
data.pop(0)
#data2.append(a)
print('\nTREE DATA:')
print(data2)
data2=sorted(data2, key = itemgetter(1))
data2=data2[::-1]
print('\nSORTED TREE DATA or TREE STRUCTURE')
print(data2)

'''
In assembly code this can be achieved by storing all the elements in array and finally sorting them as mentioned in previous assembly functions.

Achieved Array Structure:
	0    1    2    3    4    5    6    7    8
    *    *    E    *    B    D    *    A    C
    58   33   25   18   15   10   8    5    3	
'''

###TREE PERCOLATION and CREATING NEW BINARIES
indexes=[1]
for i in range(len(data2)):
	if(data2[i][0]=='*'):
		indexes.append(2*indexes[i])
		indexes.append(2*indexes[i]+1)
print('\nINDICES')
print(indexes)

'''
Data Structures:

	0    1    2    3    4    5    6    7    8

ARRAY
    *    *    E    *    B    D    *    A    C
    58   33   25   18   15   10   8    5    3	

INDICES
	1	 2	  3    4	5	 8	  9    18   19


These indices are what should be the actual indices is this was a complete(balanced) binary tree.

						58
					    (*)				
						(1)				
				33			25
				(*)			(E)
				(2)			(3)
		18			15
		(*)			(B)
		(4)			(5)	
10			8
(D)		    (*)
(8)			(9)
		5		3	
		(A)		(C)
		(18)	(19)

Now only step left is to find out the frequencies.

Compressed representations will simply be the binary representation of these numbers with the significant bit removed.
eg (For this tree)
letters    freq    index   binary repr.   compressed repr.
a 			5 		18       10010          0010
b 			15      5        101            01
c 			3       19       10011          0011
d 			10      8        1000           000
e 			25      3        11             1

'''
print('\nCompressed bit representations')
for i in range(len(data2)):
	if(data2[i][0]!='*'):
		print(str(data2[i][0])+': '+bin(indexes[i])[3:])

'''
Thanks
~~Work originally done by ANIKET AGRAWAL
~~NOT COPIED FROM ANY SOURCES
'''

