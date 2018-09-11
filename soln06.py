#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 10-09-2018
## Assignment: Linked List
## Question 6. Create two separate single lists. Check two list are same. If the two lists have the same number of elements in the same order, then they are treated as same.
#################################################################################################

import user_ds as uds 

def check(sl1,sl2):
    if sl1.length() != sl2.length():
        return False
    
    c1 = sl1.head
    c2 = sl2.head

    while c1 != None and c2 != None:
        if c1.data != c2.data:
            return False
        c1 = c1.next
        c2 = c2.next
    
    else:
        return True

def samelist(sl):
    ls = [2,4,5,6,7,8]
    for l in ls:
        sl.AddFirst(l)


def test6():
    sl1 = uds.Slist()
    sl2 = uds.Slist()
    uds.seedlist(sl1)
    uds.seedlist(sl2)
    """ samelist(sl1)
    samelist(sl2)
    print(sl1.length())
    print(sl2.length()) """
    print(check(sl1,sl2))

if __name__ == '__main__':
    test6()
