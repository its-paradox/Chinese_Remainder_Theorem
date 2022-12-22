# CODE BY OMKAR NAIK
# DESIGNED TO FIND RESULT OF CHINESE REMAINDER THEOREM

def findm(M, m):
    return M/m

def inv(x, y):
    for i in range(100):
        if (x*i)%y==1:
            break
    return i

print("\nEnter a1, a2, a3 value: ",end="")
a1, a2, a3 = map(int, input().split())
print("\nEnter m1, m2, m3 value: ",end="")
m1, m2, m3 = map(int, input().split())

M = m1*m2*m3
print("\nM = ",M)

M1 = findm(M, m1)
M2 = findm(M, m2)
M3 = findm(M, m3)

print("\nM1 = ",M1,"\nM2 = ",M2,"\nM3 = ",M3)


p = inv(M1,m1)
q = inv(M2,m2)
r = inv(M3,m3)

print("\nM1 inverse = ",p,"\nM3 inverse = ",q,"\nM3 inverse = ",r)

x = ((a1*M1*p) + (a2*M2*q) + (a3*M3*r))%M

print("\nFinal result = ",x)