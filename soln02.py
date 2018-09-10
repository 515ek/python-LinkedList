#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 09-09-2018
## Assignment: Linked List
## Question 2. Add methods to Q1 to find maximum and minimum elements in the list.
#################################################################################################
import user_ds as uds

class MaxMinList(uds.Slist):

    def __init__(self):
        super().__init__()
    
    def getMaxMin(self):
        max = self.head.data
        min = self.head.data
        cur = self.head
        while cur != None:
            if max < cur.data:
                max = cur.data
            if min > cur.data:
                min = cur.data
            cur = cur.next
        return(max,min)

def test2():
    sl = MaxMinList()
    sl.AddFirst(10)
    sl.AddLast(20)
    sl.AddFirst(50)
    sl.AddLast(40)
    print(sl.getMaxMin())

if __name__ == '__main__':
    test2()