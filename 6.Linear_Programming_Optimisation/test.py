import numpy

x = numpy.array([[1, 7, 0], [6, 2, 5]], dtype=object)
y = [[1, 7, 0], [6, 2, 5, 6]]

simplex = [[0.0, -0.5, -3.0, -1.0, -4.0], [40.0, 1.0, 1.0, 1.0, 1.0, 0], [10.0, -2.0, -1.0, 1.0, 1.0], [10.0, 0.0, 1.0, 0.0, -1.0]]
numy = numpy.array(simplex, dtype=object)
numy = numpy.insert(numy, (1,4), 4)
print(numy)

# print(y)
# print(x)