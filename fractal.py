import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, maxiter):
    z = c
    n = 0
    while abs(z) <= 2 and n < maxiter:
        z = z*z + c
        n += 1
    return n

x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5
x, y = np.mgrid[x_min:x_max:0.005, y_min:y_max:0.005]
c = x + 1j*y

mandelbrot_set = np.array([mandelbrot(c, 255) for c in c.flatten()]).reshape(x.shape)

plt.imshow(mandelbrot_set, extent=(x_min, x_max, y_min, y_max), cmap='hot')
plt.savefig('ide/fractal_generator/mandelbrot.png')

