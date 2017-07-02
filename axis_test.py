import numpy as np

a = np.sum([[0,1,2],[2,1,3]],axis=0)
#[2 2 5]  每一列加起来

b = np.sum([[0,1,2],[2,1,3]],axis=1)
#[3 6]   每一行加起来

print(a)


print(b)
