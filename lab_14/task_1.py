import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 5, 1000)

y = x * np.sin(5 * x)

plt.plot(x, y, linestyle='-', color='b', linewidth=2, label='$Y(x) = x \cdot \sin(5x)$')

plt.xlabel('x', fontsize=12, color='blue') 
plt.ylabel('y', fontsize=12, color='blue') 
plt.title('Графік функції Y(x)')

plt.legend()

plt.grid(True)

plt.show()

