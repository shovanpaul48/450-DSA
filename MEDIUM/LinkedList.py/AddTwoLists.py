# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def traverse(self):
        temp = self
        if temp == None:
            print("Empty")
        else:
            while temp != None:
                print(temp.val) 
                temp = temp.next

class Solution:
    def append(self,head,value):
        t = head
        new = ListNode(value)
        if t == None:
            t = new
            head = t
        else:
            while t.next != None:
                t = t.next
            t.next = new

    def addTwoNumbers(self, l1: ListNode, l2:ListNode):
      # l1.SumOfElements()
        temp1,temp2 = l1,l2
        t1 = ListNode(0)
        k = c =0
        s1 ,s2 = temp1.val ,temp2.val
        head = None
        while temp1 != None or temp2 != None:
            # print(s1, s2, k)
            sum = s1 + s2 + k
            if sum >= 10 :
                sum = sum % 10
                k = 1
                # print("sum",sum, k,s1,s2)
            elif sum < 10 :
                k = 0
            
            # Solution().append(head,sum)
            if c == 0:
                temp  = ListNode(sum)
                c = 1
                head=temp

            else:
                Solution().append(head,sum)
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



l1=ListNode(2)
l2= ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

s = Solution()
l = s.addTwoNumbers(l1,l4)
l.traverse()