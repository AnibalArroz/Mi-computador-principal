from numpy import zeros
from time import perf_counter


n = 100
a = zeros((n, n))+1
b = zeros((n, n))+2

# print (f"a = {a}")
# print (f"a = {b}")

t1 = perf_counter()
c = a@b
t2 = perf_counter()

dt = t2 - t1
print (dt)
print (f"dt = (")
print (dt)
print (")s")
