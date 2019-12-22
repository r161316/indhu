import numpy as np
a=np.array(input("enetr the first matrix a:"))
b=np.array(input("enetr the second matrix b:"))
ad=np.add(a,b)
c=np.subtract(a,b)
d=np.multiply(a,b)
e=np.divide(a,b)
f=np.linalg.det(a)
g=np.trace(a)
h=np.linalg.inv(a)
i=np.linalg.eig(a)
j=np.transpose(a)
k=np.linalg.matrix_rank(a)
print ad
print c
print d
print e
print f
print g
print h
print i
print j
print k

