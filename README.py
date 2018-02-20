def sumofsquares(n):
    if n<0:
        return False
    for i in range(1, int(n**0.5)  + 1 ):
        for j in range(1, int(n**0.5) + 1 ):
            m = i**2 + j**2
            if m == n:
                return True
            elif m > n:
                break
    return False
def wellbracketed(ss):
    depth=0
    for i in range(len(ss)):
        char = ss[i]
        if char=="(":
            depth+=1
        elif char==")":
            if depth>0:
                depth-=1
            else:
                return False
    return depth==0
def rotatelist(ll, shft):
    l = len(ll)
    shft = shft % l
    ans = ll[l-shft:] + ll[:l-shft]
    return ans
