

class LinkedList():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse(self):
        temp = self
        while temp != None:
            print(temp.val, end=" ") 
            temp = temp.next

    def append(self,value):
        temp = self
        new = LinkedList(value)
        if temp == None:
            temp.val = value
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = new


    def SumOfElements(self):
        sum = 0
        temp = self
        while temp.next != None:
            sum = (sum + temp.val) * 10
            # print(sum)
            temp = temp.next

        sum = sum + temp.val

        return sum


class SinglyLinkedList():
    def __init__(self):
        self.head = None
    def traverse(self):
        temp = self.head
        if temp == None:
            print("Empty")
        else:
            while temp != None:
                print(temp.val) 
                temp = temp.next
    

def addlinkedlists( l1:LinkedList,l2:LinkedList):
        # l1.SumOfElements()
    temp1 = l1
    temp2 = l2
    t1 = LinkedList(0)
    k = c =0
    s1 = temp1.val
    s2 = temp2.val
    while temp1 != None or temp2 != None:
        print(s1, s2, k)
        sum = s1 + s2 + k
        if sum >= 10 :
            sum = sum % 10
            k = 1
            print("sum",sum, k,s1,s2)
        elif sum < 10 :
            k =0
        if c == 0:
            temp  = LinkedList(sum)
            c = 1

        else:
            temp.append(sum)
        if temp1.next == None:
            s1 = 0
        else:
            temp1 = temp1.next         
            s1 = temp1.val
            
        if temp2.next == None  :
            s2 = 0
        else:
            
            temp2 = temp2.next
            s2 = temp2.val

        if s1==0 and s2 == 0 and k == 0:
            return temp
    return temp

# link1 = SinglulyLinkedList()
# link1.head = LinkedList("Sunday")

d1 = LinkedList(9)
d2 = LinkedList(9)
d3 = LinkedList(9)
d1.next = d2
d2.next = d3
# link1.head = d1
# link1.head.next = d2 
# d2.next = d3

# d1.traverse()

d4 = LinkedList(9)
d5 = LinkedList(9)
d6 = LinkedList(9)
d7 = LinkedList(9)
d8 = LinkedList(9)
d9 = LinkedList(9)

d4.next = d5
d5.next = d6
d6.next = d7
d7.next = d8
d8.next = d9
print(d1.SumOfElements())
print(d4.SumOfElements())

# d4.traverse()

# d = AddLinkList()
n=SinglyLinkedList() 
n = addlinkedlists(d1,d4)
n.traverse()
