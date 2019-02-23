#Maria F. Fiscal
#CS 2302 - Spring 2019
#UTEP 
#Instructor: Olac Fuentes
#LAB2
#Purpose: implement several sort algorithms to find the median of 
#a list of random generated items. Data generated is used to test  methods
#sorting algorithms used: bubble sort, merge sort and quick sort.  


from random import randint
#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None 

def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()    

def Prepend(L,x):
    #Adds item to the first position of the list
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        temp = Node(x)
        temp.next = L.head
        L.head = temp
        
#getting the length using List object, this method will be called to find the middle point of the sorting algorithms          
def getLength(L):
    #if the head of the list is empty return value of 0
    if L.head == None:
     return 0
 
    else:
        temp = L.head
        counter = 0
        #if the list is not empty
        while temp.next is not None:
            #increase counter 
            counter = counter + 1
            #move to the next node in the list
            temp = temp.next
        #return the counter (length of the list) 
        return counter

#ALGORITHM 
#visit all nodes in the list, starting with the head. If that note is a match returns the node position.
#else move to the next node (.next)
def ListSearch(L,k):
    #pointer at head
    currentPosition = L.head
    counter=0
    #while list is not null
    while currentPosition  is not None:
        counter+=1
        if currentPosition.item == k:
            
            return counter
        else:
            #continue moving forward to the next node element 
            currentPosition = currentPosition.next
    #if key is not in the list return null 
    return counter


#ALGORITHM
#case 1: insert as list first node. If list is empty and we are adding a new node, head and tail points to the new added node
#case 2: insert after tail node: if list is not null, and currNode porint to the list tail, the algorithm points the tail node's next pointer 
#and the list's tail pointer to the new added node(x)
#case 3: insert in the middle of the list. New node(x).next pointer to currNode.next node, and then points currNode next pointer to the new node
def insertAfter(L,currNode,x):
    #case 1
    if L.head is None:
        L.head = Node(x)
        L.tail = L.head
    #case 2
    elif currNode == L.tail:
        L.tail.next = Node(x)
        L.tail = Node(x)
    #case 3
    else:
        Node(x).next = currNode.next
        currNode.next = Node(x)

#return TRUE is list is sorted
#otherwise FALSE
def listIsSorted(L):
    #if list is empty is sorted
    if L.head == None:
        return True
    temp = L.head
    while temp.next is not None:
        if temp.item > temp.next.item:
            return False
        temp = temp.next
    return True

def listCopy(L):
    currentPosition = L.head
    newCopyList = List()
    
    while currentPosition is not None:
        Append(newCopyList, currentPosition.item)
        currentPosition = currentPosition.next
    
    return newCopyList

def ElementAt(L,i):
    currentPointer = L.head
    counter = 0; 
    
    while counter !=i:
        currentPointer = currentPointer.next
        counter = counter + 1
    return currentPointer

#BUBBLE SORT ALGORITHM 
#repeatedly swapping the adjacent elements if the are 
#in the wrong order. 
def bubbleSort(L):
    temp = L.head
    temp2 = L.head
    #while list 1,2 is not empty
    while temp != None:
        while temp2 != None:
            if temp2.item > temp2.next.item:
                temp3 = temp2.item
                temp2.item = temp2.next.item
                temp2.next.item = temp3
            temp2 = temp2.next
        temp = temp.next
        temp2 = L.head

#METHOD USED FOR mergeSort last step; merge the 2 sorted lists
def LastMerger(L, List1,List2):
    temp = List1.head
    temp2 = List2.head
    #while lists are not null 
    while temp != None and temp2 != None:
        if temp.item < temp2.item:
            Append(L, temp.item)
            temp = temp.next
        else:
            Append(L, temp2.item)
            temp2.temp2.next
    
    while temp != None:
        Append (L, temp.item)
        temp = temp.net
    while temp2 != None:
        Append (L.temp2.item)
        temp2 = temp2.next
    
     
#MERGE SORT ALGORITHM 
#Divide and conquer. First find the middle point to divede the list in two halves
#call mergesort for first half (left)
#call mergesort for second halg (right)
#merge 2 sorted halved in prev. steps using LastMerger method call 
def mergeSort(L):
    if getLength(L) > 1:
        List1 = List()
        List2 = List()
        temp = L.head
        halves = 0
        while halves < getLength(L)//2:
            Append(List1, temp.item)
            Remove(L, temp.item)
            halves = halves + 1
        while temp != None:
            Append(List2, temp.item)
            Remove(L, temp.item)
            temp = temp.next
            
        mergeSort(List1)
        mergeSort(List2)
        LastMerger(L, List1, List2)

#QUICK SORT ALGORITHM 
#pivot first elment and move the next element and separate if next value is greater of lesser than pivot.  
def QuickSort(L):
    if getLength(L) >1:
        pivotValue = L.head.item
        temp = L.head.next
        greaterValue = List()
        lesserValue = List()
        #while list is not null
        while temp != None:
            #compare against pivot lesser or greater value 
            if pivotValue > temp.item:
                Append(lesserValue, temp.item)
            else:
                Append(greaterValue, temp.item)
            temp = temp.next
        #continue doing the same process by recursive calls
        QuickSort(greaterValue)
        QuickSort(lesserValue)
        if lesserValue.head != None:
                L.head = lesserValue.head
                L.tail = greaterValue.tail
                lesserValue.tail.next = greaterValue.head
        else:
                #if empty value becomes head and tail
                L.head = greaterValue.head
                L.tail = greaterValue.tail
    
        
#MEDIAN VALUES returning middle element
#BubbleSort
def medianBS(L):
    c = listCopy(L)
    bubbleSort(c)
    return ElementAt(c, getLength(c) // 2)
#MergeSort
def medianMS(L):
    c = listCopy(L)
    mergeSort(c)
    return ElementAt(c, getLength(c) // 2)
#QuickSort
def medianQS(L):
    c = listCopy(L)
    QuickSort(c)
    return ElementAt(c, getLength(c) // 2)

#Method to generate the list with n elements
def listCreation(n,x):
    L = List()
    for i in range (n):
        Append(L, randint(0,x))
    return L 

#MAIN 
# testing values 

n = 7
x = 7

L = listCreation(n,x)
print('List created...')
print(L)


print('Create list using bubble sort:')
bubbleSort(L)
Print(L)

print('Return element in the the middle (bubble sort):')
print(medianBS(L)) 

print('Create list using merge sort:')
mergeSort(L)
print(L)
print('Return element in the the middle (merge sort):')
print(medianMS(L)) 

print('Create list using quick sort:')
QuickSort(L)
print(L)
print('Return element in the the middle (quick sort):')
print(medianQS(L)) 

#other testing methods
print('Printing list using recursive method: ')
PrintRec(L)

print('Printing list in reverse:')
PrintReverse(L)


print('Is the list sorted?')
print(listIsSorted(L))

print('The length of the list is:', end = " ")
print(getLength(L))

#testing emptylist 
#print('Is list empty?', end =" ")
#print(IsEmpty(L))


#testing sorting list methods 
#print('Adding values in the list..')
#for i in range(5):
#    Append(L,i)
#print('New list: ', end = " ")
#Print(L)










