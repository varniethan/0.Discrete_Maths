from PIL import Image, ImageDraw
from Mandelbrot import mandelbrot, max_iterations

# Image size (pixels)
width = 600
height = 400

# Plot window
re_start = -2
re_end = 1
im_start = -1
im_end = 1

palette = []

im = Image.new('RGB', (width, height), (0,0,0))
draw = ImageDraw.Draw(im)

for x in range(0, width):
    for y in range(0, height):
        # Converting a pixel coordinate to complex number
        c = complex(re_start + (x/width) * (re_end - re_start), im_start + (y/height) * (im_end - im_start))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        color = 255 - int(m * 255 / max_iterations)
        # Plot the point
        draw.point([x, y], (color, color, color))
im.save('black_and_white_mandelbrot.png', 'PNG')


