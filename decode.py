def decode(E):
    l = ""
    b = len(E)
    for d in range(0,b):
        x = E[d][1]
        for c in range(0,x):
            l = l + E[d][0]
    return(l)




def stretches(S):
    char = []
    a = 0
    x = len(S) 
    while (a < x):
        c = 1
        y = S[a]
        while (a < x-1) and (y == S[a+1]):
            c = c + 1
            a = a + 1      
        a = a + 1 
        char.append(c)
    return(char)




def shrivel(S):
    char = [S[0]]
    x = len(S)
    y = S[0]
    for i in range(1,x):
        if  S[i] != y:
            char. append(S[i])
            y = S[i]
    return(char)    



def encode(D):
    l = []
    v = shrivel(D)
    n = stretches(D)
    for k in range(0,len(n)):
        l.append((v[k],n[k]))
    return l 