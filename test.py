        # sum1 = sum2  = 0 
        # a,b = len(l1), len(l2)

        # if a == b:
        #     for i in range(a -1):
        #         sum1 = sum1 + (l1[i] * 10)
        #         sum2 = sum2 + (l2[i] * 10)
            
        #     sum1 = sum1 + l1[a-1]
        #     sum2 = sum2 + l2[a-1]


'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        if head == None:
            temp = Node(x)
            head = temp
        else:
            temp = Node(x)
            temp.next = head
            head = temp

        
        # code here 
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        temp = head
        if head == None:
            temp = Node(x)
            head = temp
            
        else:
                
            while temp.next != None:
                temp.next = temp
            temp.data = x

# Driver Code Starts
class Node:
    def _init_(self, data):
        self. data=data
        self.next=None
class LinkedList:
    def _init_(self):
        self.head=None
def printList (head):
    while head:
        print (head. data, end=' ')
        head=head. next
    print()
if __name__ == '__main__':
    t=int(input ())
    for cases in range(t):
        n=int(input())
        a=LinkedList()
        nodes_info = list(map(int, input().split()))
        for i in range(0, len (nodes_info)-1,2):
            if(nodes_info[i+1]==0):
                a.head = solution().insertAtBegining(a.head, nodes_info[i])
            else:
                a.head = solution().insertAtEnd(a.head, nodes_info[i])
        printList(a.head)
