import numpy as np
from scipy.linalg import solve

# variable
# v = The number of vanilla ice cream
# s = The number of strawberry ice cream  

# Equations to solve
# objective
    # MAX = 2v+3s
# constrains
    # 0.5v+ 0.2s <= 10
    # v+s <= 30
    # v,s >= 0

A1 = np.array([[0.5,0.2],[1,1]])
A2 = np.array([[0.5,0.2],[1,0]])
A3 = np.array([[0.5,0.2],[0,1]])
A4 = np.array([[1,1],[1,0]])
A5 = np.array([[1,1],[0,1]])
B1 = np.array([[10],[30]])
B2 = np.array([[10],[0]])
B3 = np.array([[10],[0]])
B4 = np.array([[30],[0]])
B5 = np.array([[30],[0]])

C1 = solve(A1, B1)
C2 = solve(A2, B2)
C3 = solve(A3, B3)
C4 = solve(A4, B4)
C5 = solve(A5, B5)
C = np.array([[13,16],[0,50],[20,0],[0,30],[30,0]])

for i in range(5):
    MAX = (2*C[i][0])+(3*C[i][1])
    print (" Max[{}] get profit {}$".format(i,MAX))

#I don't choose 150$ profit because the number of strawberry ice cream is more than 30 boxes.
#Therefore, choose a profit of 90$. Only 30 boxes of strawberry ice cream will be produced.




