# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, maxiter):
    z = c
    n = 0
    while abs(z) <= 2 and n < maxiter:
        z = z*z + c
        n += 1
    return n

width, height = 500, 500
maxiter = 255

real = np.linspace(-2, 1, width)
imag = np.linspace(-1.5, 1.5, height)

mandelbrot_set = np.zeros((height, width))

for row in range(height):
    for col in range(width):
        c = complex(real[col], imag[row])
        mandelbrot_set[row, col] = mandelbrot(c, maxiter)

plt.imshow(mandelbrot_set, extent=[-2, 1, -1.5, 1.5], cmap='hot')
plt.title('Множество Мандельброта')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.savefig('ide/fractal_generator/mandelbrot.png')
plt.show()