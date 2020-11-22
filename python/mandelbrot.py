import numpy
from PIL import Image
import matplotlib.pyplot as plt
import os


def mandelbrot(Re, Im, max_iter):
  c = complex(Re, Im)
  z = 0.0j
  for i in range(max_iter):
    z = z*z + c
    if(z.real*z.real + z.imag*z.imag) >= 4:
      return i
  return max_iter
columns = 1000
rows = 1000

zoom = 1
point = (0.3, 0.5)

for i in range(100):
  print(f'iter{i}')
  zoom += i * 0.1
  result = numpy.zeros([rows, columns])
  for row_index, Re in enumerate(numpy.linspace(-2 + (3 - 3 / zoom) / 4, 1 - (3 - 3 / zoom) * 3 / 4, num=rows)):
      for column_index, Im in enumerate(numpy.linspace(-1 + (2 - 2 / zoom) * 15 / 32, 1 - (2 - 2 / zoom) * 17 / 32, num=columns)):
          result[row_index, column_index] = mandelbrot(Re, Im, 100)

  plt.figure(figsize=(columns / 100, rows / 100))
  plt.axis('off')
  plt.imshow(result.T, cmap="hot", interpolation="bilinear", extent=[-2, 1, -1, 1])
  plt.savefig(f'images/mandelbrot{i:03d}.png', bbox_inches='tight')

os.system('ffmpeg -y -framerate 24 -i images/mandelbrot%03d.png -pix_fmt yuv420p output.mp4')
os.system('open output.mp4')