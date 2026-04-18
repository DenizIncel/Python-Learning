# MATRİS ÇARPIMLARI #

import numpy as np

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A * B
print("Elemanlarin carpimi: ", C)

C = A @ B
print("Matrislerin carpimi: ", C)


print("-" * 30)

# MATRIS DEGISTIRME #

# Eleman Degistirme
D = np.array([
    [1,2,3],
    [4,5,6],
])

D[0,1] = 99  # 1.satır,2.sutun degisir ve 99 olur.

print(D)

# Satır Degistirme
D[1] = [7,8,9] # 2.satırı degistirir.

print("\n",D)

# Sutun Degistirme
D[:, 0] = [10, 20] # 1.sutunu degistirir.
print("\n",D)


print("-" * 30)

# Birim Matris ve Ters Matris #

I = np.eye(2) # 2x2'lik bir birim matris olusturur.
print(I)


E = np.array([
    [1,2],
    [3,4]
])

E_inv = np.linalg.inv(A)

print("\n",E_inv)