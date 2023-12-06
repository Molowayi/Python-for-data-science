import numpy as np

a = np.array([1, 7, 12])
b = np.array([[1.5, 2, 3], [3, 17, 42]])
d = np.zeros((2, 3))
e = np.ones((2, 3))
c = np.array([[x*y for y in range(1, 6)] for x in range(1, 6)])

print(a)
print(b)
print(b[1, 0])


print(f"c  {c}")
print(f"d  + {d}")
print(f"e  + {e}")

print([1, 2, 3]*3)
print(a*3)
print(a*a)
