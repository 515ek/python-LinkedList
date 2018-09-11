#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 10-09-2018
## Assignment: Linked List
## Question 7. Write a method which creates the union of elements from two lists.
#################################################################################################
import user_ds as uds 

def union(sl1,sl2):
    sl1.tail.next = sl2.head
    sl1.tail = sl2.tail
    sl1.count = sl1.length() + sl2.length()

def test7():
    sl1 = uds.Slist()
    sl2 = uds.Slist()
    assert(sl1.isEmpty())
    assert(sl2.isEmpty())
    uds.seedlist(sl1)
    uds.seedlist(sl2)
    print(sl1.length(),sl2.length())
    union(sl1,sl2)
    print(sl1.length())

if __name__ == '__main__':
    test7()