import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Criar uma figura com múltiplos subplots
fig = plt.figure(figsize=(8, 4))

# Primeiro subplot para a esfera
ax1 = fig.add_subplot(121, projection='3d')

# Parâmetros da esfera
radius = 1
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = radius * np.outer(np.cos(u), np.sin(v))
y = radius * np.outer(np.sin(u), np.sin(v))
z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

# Desenhar a esfera
ax1.plot_surface(x, y, z, color='gray')
ax1.set_title('Esfera')

# Segundo subplot para o toro
ax2 = fig.add_subplot(122, projection='3d')

# Parâmetros do toro
R = 1  # Raio maior
r = 0.4  # Raio menor
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# Desenhar o toro
ax2.plot_surface(x, y, z, color='gray')
ax2.set_title('Toro')

plt.axis('equal')

# Mostrar a figura
plt.show()