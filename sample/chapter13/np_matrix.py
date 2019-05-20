import numpy

a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[5, 6], [7, 8]])

print(a@b)
print(a.dot(b))
print(numpy.dot(a, b))
print(numpy.matmul(a, b))
