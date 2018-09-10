#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 09-09-2018
## Assignment: Linked List
## Question 3. Modify Q1 such that one can add a new element after any specified element.
#################################################################################################
import user_ds as uds

class AddAfterList(uds.Slist):

    def __init__(self):
        super().__init__()
    
    def AddAfter(self,key,ele):
        nn = self._Node(ele)
        cur = self.head
        while cur != None:
            if cur.data == key:
                nn.next = cur.next
                cur.next = nn
                break
            cur = cur.next
        self.count += 1

def test3():
    sl = AddAfterList()
    sl.AddFirst(10)
    sl.AddLast(20)
    sl.AddFirst(50)
    sl.AddLast(40)
    sl.AddAfter(20,30)
    assert(sl.length() == 5)