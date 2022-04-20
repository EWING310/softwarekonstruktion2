import numpy as np

O = np.array([(1,2,3,), (4,5,6), (7,8,9), (10,11,12)])
print(O)

"""
print(O[0,:]) Række 1
print(O[1,:]) Række 2
print(O[2,:]) Række 3
print(O[3,:]) Række 4

print(O[:,0]) Kolonne 1
print(O[:,1]) Kolonne 2
print(O[:,2]) Kolonne 3
"""




print(O[2,:])
print(O[:,1])

V = (O[2, :])

G = sum(O[:,0])+sum(O[:,1])+sum(O[:,2])

T = np.array([i * 10 for i in O])

print("opg1", O)
print("opg2", sum(V))
print("opg3", (G))
print("opg4", T)
