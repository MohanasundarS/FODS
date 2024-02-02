import numpy as np
house_data = np.array([
    [4, 2000, 350000],
    [3, 1800, 300000],
    [5, 2200, 400000],
    [4, 2400, 380000],
    [6, 2800, 450000]
])
k=0
l=0
for i in range(0,5):
    j=0
    if(house_data[i,j]>4):
        k=k+ house_data[i,2]
        l=l+1
print(k/l)        
        
