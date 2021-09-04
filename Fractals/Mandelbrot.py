max_iterations = 10000000
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + c
        n += 1
    return n

# if __name__ == "__main__":
#     for a in range(-10, 10, 5):
#         for b in range(-10, 10, 5):
#             c = complex(a/10, b/10)
#             print(c, mandelbrot(c))

#This will return the number of itereations needed to reach a modulus greater than 2.
#If the number of itereations is greater than MAX ITER, then stop and return the MAX_ITER