import numpy as np
import matplotlib.pyplot as plt

p = 0.6 # chance de sair cara
vp = [] # lista que armazena a frequência de ocorrências
vsim = [] # armazena o número de simulações
Nmax = 1000 # número máximo de simulações
for nsim in np.arange(1, Nmax, 10) : # simula de 1 até Nmax
    nhead = 0 # número de caras
    for i in range(1,nsim) : # o número de simulações aumenta
        if (np.random.uniform() < p) :
            nhead = nhead + 1
    vp.append(nhead/nsim)
    vsim.append(nsim)
# Mostra os resultados
plt.figure(figsize=(8,6))
plt.plot(vsim, vp, linestyle='-', color="blue", linewidth=2, label='Valor simulado')
plt.axhline(y=p, color='r', linestyle='--', label='Valor teórico')
plt.ylabel("Fração de caras", fontsize=20)
plt.xlabel("Número de experimentos", fontsize=20)
plt.xlim([0.0, Nmax])
plt.ylim([0.0, 1.0])
plt.legend()
plt.show()
