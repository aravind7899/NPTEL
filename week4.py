def takesecond(ele):
    return ele[1]
def histogram(l):
    l.sort();list=[]
    for i in l:
        j=l.count(i)
        if (i,j) in list:
            continue
        else:
            list.append((i,j))
    list.sort(key=takesecond)
    return list
  
def transcript(C,S,G):
    for i in range(0,len(S)):
        S[i]=list(S[i]);mylist=[]
        for j in range(0,len(G)):
            G[j]=list(G[j])
            if(S[i][0]==G[j][0]):
                l=[]
                for k in range(0,len(C)):
                    if(G[j][1]==C[k][0]):
                        l.extend(C[k])
                l.append(G[j][2])    
                mylist.append(tuple(l))
        mylist.sort()
        S[i].append(mylist)
        S[i]=tuple(S[i])
    S.sort()
    return S
