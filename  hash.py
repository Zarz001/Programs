def hash(d):
    """given a list d of instructions to add or delete keys to a hash table 
    returns the hash table after these instructions have been applied using
    hash function h(k) = 2k + 4 mod 13 
    
    the instructions are either '+k' or '-k' for some positive integer k to indicate
    that k is to be added or deleted
        
    separate chaining is used for collision handling
    """
    h = HashTable(13)
    newlist = LinkedList()
    for i in range(0,len(d)):
        s = d[i]
        sign = d[i][0]
        k = ""
        for l in range(1,len(s)):
            k = k + s[l]
        k = int(k) 
        point = ((2*k)+4)%13
        newlist = h.lookup(point)
        current = newlist.head
        found =  False
        while current:
            if current.data == k:
                found = True
            current = current.next        
        if (sign == "+") and (found == False):
            if newlist.size == 0:
                newlist.head = Node(k)
                newlist.next = None
                newlist.size += 1
            else:
                current = newlist.head
                while current.next:
                    current = current.next
                current.next = Node(k)
                newlist.size+=1
        else:
            if (sign == "-") and  (found == True):
                if newlist.size == 1:
                    newlist.head = None
                    newlist.size = 0
                else: 
                    current = newlist.head
                    lastitem = None
                    if current.data == k:
                        newlist.head = current.next
                    else:
                        while current.next:
                            lastitem = current
                            current = current.next
                            if current.data == k:
                                lastitem.next = current.next
                        newlist.size -= 1
    h.print_table()
    return h 