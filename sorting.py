def selection_sort(L):
    for i in range(0,len(L)):
        pos = i
        for j in range(i+1,len(L)):
            if L[j] < L[pos]:
                pos = j
        (L[i],L[pos]) = (L[pos],L[i])        
        


def get_pivot(L):
    import random
    a = []
    c = []
    n = random.randint(0,len(L)-1)
    for i in range(0,5):
        while n in c:
            n = random.randint(0,len(L)-1)
        c.append(n)
        a.append(L[n])
    selection_sort(a)
    return a[2]
   


   
    
  
def three_partition(L, pivot):
    l0 = []
    l1 = []
    l2 = []
    for m in range(0,len(L)):
        if L[m] < pivot:
            l0.append(L[m])
        elif L[m] == pivot:
            l1.append(L[m])
        else:
            l2.append(L[m])
    return(l0,l1,l2)
          


def quick_sort(L):
   if len(L) <= 10:
    selection_sort(L)
    return(L)
   else:
    pivot = get_pivot(L)
    l0,l1,l2 = three_partition(L,pivot)
    if len(l0) == 1:
        return(l0[1]+l1+quick_sort(l2))
    elif len(l2) == 1:
        return(quick_sort(l0)+l1+l2[1])
    return(quick_sort(l0)+l1+quick_sort(l2)) 
  