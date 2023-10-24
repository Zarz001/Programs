def linz_ordering_eight():
    import  random
    l = []
    lists = [0,1,2,3,4,5,6,7]
    random.shuffle(lists)
    for i in range(1,8):
        k = (lists[i] - lists[i-1])%8
        l.append(k)
    if len(set(l)) == len(l):
        return lists
    else:
        return linz_ordering_eight()
        

##b)
def linz_ordering_k(k):
    import  random
    l = []
    lists = random.sample(range(0,k),k)
    random.shuffle(lists)
    for i in range(1,len(lists)):
        b = (lists[i] - lists[i-1])%k
        l.append(b)
    if len(set(l)) == len(l):
        return lists
    else:
        return linz_ordering_k(k)