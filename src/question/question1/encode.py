from sage.all import *
import random


#CREATION OF LINEAR CODE
def generateCode(n,k):
    g=[]
    col=[]
    #CREATION OF GENERATION MATRIX
    for i in range(0,k):
        for j in range(0,k):
            if(i==j):
                col.append(1)
            else:
                col.append(0)
        g.append(col)
        col=[]
    for i in range(0,k):
        for j in range(0,n-k):
            g[i].append(random.randint(0,1))
    G=matrix(GF(2),g)
    C=codes.LinearCode(G)
    return C
    
#MODIFYING EACH LETTER TO AN 8 BIT BINARY FORMAT    
def messageConverter(msg):
    m=list(msg)
    mNumbers=[]
    for i in m:
        mNumbers.append(ord(i))
    mBin=[]
    for i in mNumbers:
        l=bin(i)
        l=l[2:]
        l="00000000"+l
        mBin.append(l[-8:])
    #print(m)
    #print(mNumbers)
    #print(mBin)
    mBin="".join(mBin)
    print("-->Message in pure binary form\t"+str(mBin))
    return mBin


#CREATING SxGxP ARRAY
def gMaker(G):
    G=matrix(GF(2),G)
    rows=G.nrows()
    #PERMUTATING THE IDENTITY MATRIX
    S=matrix.identity(rows)
    for i in range(0,random.randint(1,rows+1)):
        first=random.randint(0,rows-1)
        second=random.randint(0,rows-1)
        temp=S[first]
        S[first]=S[second]
        S[second]=temp
    S=matrix(GF(2),S)
    print("-->Array S(random invertible array)")
    print(S)
    SG=S*G
    #print(SG)
    rows=SG.ncols()
    P=matrix.identity(rows)
    #CREATING THE RANDOM ARRAY 
    for i in range(0,rows):
        first=random.randint(0,rows-1)
        second=random.randint(0,rows-1)
        P[first]=P[first]+P[second]
    P=matrix(GF(2),P)
    print("\n\n")
    print("-->Array P(random identity array permutation)")
    print(P)
    SGP=SG*P
    print("\n\n")
    print("-->SxGxP")
    print(SGP)
    return SGP

#CALCULATING THE c*SGP
def cMaker(sgp,msg):
    m=list(msg)
    rows=sgp.nrows()
    c=[]
    while(len(m)>0):
        l=[]
        if(len(m)>rows):
            for i in range(0,rows):
                l.append(m[i])
            for i in range(0,rows):
                del m[0]
        else:
            i=len(m)
            add=rows-i
            for j in range(0,i):
                l.append(m[j])
            for j in range(0,add):
                l.append('0')
            for i in range(0,i):
                del m[0]
        h=vector(GF(2),l)
        pl=h*sgp
        for i in pl:
            c.append(i)
    print("-->Message c' is")
    stringC=""
    for i in c:
        stringC+=str(i)
    print(stringC)
    return c
            
        
#ADDING EXTRA BITS IF NEEDED SO THE CODE CAN ENCODE THE MESSAGE
def prepareForEncode(c,k):
    original=len(c)
    if(len(c)%k==0):
        return c,len(c)
    else:
        while(len(c)%k!=0):
            c.append(0)
    return c,original

#ADDING ERROR VECTOR,m IS THE HAMMING DISTANCE
def errorEncode(m,c):
    cLength=len(c)
    counter=0
    errorVector=[0]*cLength
    while(counter<m):
        pos=random.randint(0,cLength)
        errorVector[pos]=1
        counter+=1
    v=[]
    clist=list(c)
    for i in clist:
        v.append(int(i))
    v=vector(GF(2),v)
    errorVector=vector(GF(2),errorVector)
    v=v+errorVector
    c_errorred=""
    for i in v:
        c_errorred+=str(i)
    return errorVector,c_errorred
    
        
#ENCODING THE MESSAGE AND THEN ADDING THE LENGTH
def encode(c,k,CODE,length):
    newMsg=[]
    for i in range(0,len(c),k):
        part=[]
        v=vector(GF(2),c[i:i+k])
        part=CODE.encode(v)
        for i in part:
            newMsg.append(i)
    msg=""
    for i in newMsg:
        msg+=str(i)
    print("-->Encoded message is")
    print(msg+hex(length))
    return msg,hex(length)



