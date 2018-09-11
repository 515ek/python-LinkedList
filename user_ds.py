#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 09-09-2018
## Assignment: Implementing the Linked List DataStructure
## Question: Create a Class Slist to implement the working of Single Linked List DataStructure.
#################################################################################################
import random

class Slist:

    class _Node:

        def __init__(self,ele):
            self.data = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def length(self):
        return self.count

    def AddFirst(self,ele):
        nn = self._Node(ele)
        if not self.isEmpty():
            nn.next = self.head
            self.head = nn
        else:
            self.head = self.tail = nn
        self.count += 1
    
    def AddLast(self,ele):
        nn = self._Node(ele)
        if not self.isEmpty():
            self.tail.next = nn
            self.tail = nn
        else:
            self.head = self.tail = nn
        self.count += 1
    
    def DelFirst(self):
        if not self.isEmpty():
            self.head = self.head.next
            if self.head == None:
                self.tail = self.head
            self.count -= 1
    
    def DelLast(self):
        if not self.isEmpty():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                cur = self.head
                tail = self.tail
                while cur.next != tail:
                    cur = cur.next
                self.tail = cur
                self.tail.next = None
            self.count -= 1

def test_class():
    sl = Slist()
    assert(sl.isEmpty())
    sl.AddFirst(10)
    sl.AddLast(20)
    sl.AddFirst(30)
    sl.AddLast(40)
    assert(sl.length() == 4)
    sl.DelFirst()
    assert(sl.length() == 3)
    sl.DelLast()
    assert(sl.length() == 2)
    sl.DelFirst()
    assert(sl.length() == 1)
    sl.DelLast()
    assert(sl.length() == 0)


def seedlist(sl):
    for i in range(5):
        sl.AddFirst(random.randint(i*3,(i+1)*3))
        sl.AddLast(random.randint(2*i*6,2*(i+1)*6))

if __name__ == '__main__':
    test_class()