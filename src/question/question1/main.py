from encode import *
from decode import *

print("=====FIRST CODE=====")
print("-->please enter length of Code (n)")
n1=int(input())
print("-->please enter dimension of Code (k)")
k1=int(input())
print("=====SECOND CODE=====")
print("-->please enter length of Code (n)")
n2=int(input())
print("-->please enter dimension of Code (k)")
k2=int(input())
print("=====MESSAGE=====")
print("-->please enter the message you want encoded")
msg=input()
print("\n\n")
C1=generateCode(n1,k1)
minC1=C1.minimum_distance()
print("-->Generator matrix for code no 1")
print(C1.generator_matrix())
print("--Minimum distance for code no 1")
print(minC1)
print("\n\n")
C2=generateCode(n2,k2)
minC2=C2.minimum_distance()
print("-->Generator matrix for code no 2")
print(C2.generator_matrix())
print("--Minimum distance for code no 2")
print(minC2)
print("\n\n")

mBin=messageConverter(msg)
sgp=gMaker(C1.generator_matrix())
print("\n\n")
c=cMaker(sgp,mBin)
c,length=prepareForEncode(c,k2)
error,c=errorEncode(minC2,c)
print("\n\n")
encodedMessage,hexL=encode(c,k2,C2,length)
print("\n\n")
print("-->With error vector")
print(error)
print("\n\n")


decode(C2,encodedMessage,hexL,n2)




