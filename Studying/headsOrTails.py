import numpy as np
p = 0.6
nsim = 10
nhead = 0
out = []
for i in range(0, nsim) :
    if (np.random.uniform() < p) :
        nhead = nhead + 1
        out.append(1)
    else :
        out.append(0)
print("Output:", out)
print("Head frequency:", nhead / nsim)