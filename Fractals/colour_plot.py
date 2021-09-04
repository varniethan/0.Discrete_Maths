from PIL import Image, ImageDraw
from Mandelbrot import mandelbrot, max_iterations

# Image size (pixels)
WIDTH = 600
HEIGHT = 400

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)
print("I am here 1")
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the number of iterations
        print("I am here NO")
        m = mandelbrot(c)
        print("I am here YES")
        # The color depends on the number of iterations
        hue = int(255 * m / max_iterations)
        saturation = 255
        value = 255 if m < max_iterations else 0
        # Plot the point
        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('output.png', 'PNG')
print("Process Finished")