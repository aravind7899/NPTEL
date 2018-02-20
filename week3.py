def ascending(l):
  for i in range(len(l)-1):
    if(l[i]>l[i+1]):
      return False
  return True
def alternating(l):
  f,g=0,0
  for i in range(len(l)-1):
    if(l[i]==l[i+1]):
      return False
  if(len(l)==1):
    return True
  if(len(l)==2):
    if l[0]==l[1]:
      return False
    else:
      return True
  if len(l)==3:
    if l[0]<l[1] and l[1]>l[2]:
      return True
    elif l[0]>l[1] and l[1]<l[2]:
      return True
    else:
      return False
  if len(l)>3:
    if(l[0]>l[1]):
      for i in range(0,len(l),2):
        for j in range(1,len(l)-1,2):
          if(l[i]>l[j]):
            f=1
          else:
            return False
    if f==1:
      return True
  elif l[0]<l[1]:
    for i in range(0,len(l),2):
      for j in range(1,len(l)-1,2):
        if(l[i]<l[j]):
          g=1
        else:
          return False
    if g==1:
      return True
  else:
    return False
                
def matmult(X,Y):
    col= len(Y[0])
    row= len(X)
    result = [[0 for i in range(col)] for j in range(row)]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result
  
