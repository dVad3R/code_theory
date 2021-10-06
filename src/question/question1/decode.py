from sage.all import *
import ast


def decode(CODE,msg,length,n):
    enList=list(msg)
    numC=[]
    D=CODE.decoder()
    for i in enList:
        numC.append(int(i))
    decMsg=[]
    for i in range(0,len(numC),n):
        part=[]
        r=vector(GF(2),numC[i:i+n])
        part=D.decode_to_message(r)
        for i in part:
            decMsg.append(i)

    decMsgStr=""
    lDec=ast.literal_eval(length)
    #print(lDec)
    counter=0
    for i in decMsg:
        if(counter>=lDec):
            break
        else:
            decMsgStr+=str(i)
            counter+=1
    print("-->Decoded Message:")
    print(decMsgStr)
    
