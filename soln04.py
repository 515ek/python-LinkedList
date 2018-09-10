#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 09-09-2018
## Assignment: Linked List
## Question 4. Modify Q1 such that one can delete any specified element from the list.
#################################################################################################

import user_ds as uds 

class DelList(uds.Slist):

    def __init__(self):
        super().__init__()
    
    def delete(self,key):
        cur = self.head
        while cur.next != None:
            if cur.next.data == key:
                cur.next = cur.next.next
                break
            cur = cur.next
        else:
            return None
        self.count -= 1

def test4():
    sl = DelList()
    sl.AddFirst(10)
    sl.AddLast(20)
    sl.AddFirst(50)
    sl.AddLast(40)
    assert(sl.length() == 4)
    sl.delete(20)
    assert(sl.length() == 3)
    sl.delete(40)
    assert(sl.length() == 2)
    assert(sl.delete(70) == None)

if __name__ == '__main__':
    test4()