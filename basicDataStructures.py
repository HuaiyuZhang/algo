# Array
# all must be homogeneous
from array import *
array1 = array('i', [10, 20, 30, 40, 50])
for x in array1:
    print(x)

array1[2] = 40
for x in array1:
    print(x)
array1.index(40)
array1.insert(1,20)
array1.remove(40)
array2 = array('i', [10,20])
array1 + array2 

# List
# can have heterogeneous entries
list1 = ['Physics', 'Chemistry', 20, 4]
list2 = ['John', 'mike', 'a', 'c']
print(list1[0])
print(list2[1:4])
list2[3] = 2001
print(list2)
list2.remove('a')
del list2[1]
del list2[list2.index('John')]
list3 = [1,2,3,4,5]
len(list3)
list3[0:2] + list3[3:5]
list3 *2
3 in list3
for x in list3: print(x)

# Tuple
# tuples cannot be changed unlike lists and tuples use parentheses
# immutable: strings, numbers, tuples...
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1,2,3,4,5)
tup3 = 1,2,3,4,5
tup2 == tup3
tup1 = ()
tup2 = (50,)
tup3[2]
tup1 + tup2 + tup3
del tup1

# Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']", dict['Name']
dict['School'] = 'Mension High School'
del dict['Age']

# 2D array
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[0])
print(T[1][2])
T.insert(2, [0,5,11,13,6])
del T[3]

# Matrix
from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
m = reshape(a, (7,5))
print m
m[2][3]
m_r = append(m, [['Avg', 12, 14, 13, 11]], 0) # append also an array
m_c = append(m, [[1],[2], [3], [4], [5], [6], [7]], 1)
m1 = delete(m_r, [0],0)
m2 = delete(m_c, s_[3], 1)
m[3] = ['Thu',0,0,0,0]

# Set
# elements do not duplicate; elements immutable; no index
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
for d in Days: print d
Days.add("JohnDay")
Days.discard("Sun")
Day1 = {'Mon','Tue', 'Sha'}
Day1|Days
Day1&Days
Day1 - Days
Days - Day1
Day1 <= Days

# LinkedList
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    # traversing
    def listprint(self):
        printval = self.headval  # a node
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    # Insert at begining
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    # Insert at the end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode
    # Insert after a specified node
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print('Missing node.')
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    # Remove
    def Remove(self, removeKey):
        HeadVal = self.headval
        if (HeadVal.dataval is not None):
            if(HeadVal.dataval == removeKey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == removeKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        if (HeadVal == None):
            return
        
        prev.nextval = HeadVal.nextval
        HeadVal = None


list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

list1.listprint()
list1.AtBegining('Sun')
list1.listprint()
list1.AtEnd('Thursday')
list1.listprint()
list1.InBetween(list1.headval.nextval.nextval, 'between')
list1.listprint()
list1.Remove('between')
list1.listprint()


# Stack
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):     
	    return self.stack[0]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())