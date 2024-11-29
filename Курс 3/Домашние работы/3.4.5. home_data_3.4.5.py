import numpy
X1 = numpy.array([[7., 3., 0.], [2., 1., 5.], [1., 6., -2.]])
X2 = numpy.array([28., 33., 17.])
print((round(numpy.linalg.solve(X1, X2)[0], 4), round(numpy.linalg.solve(X1, X2)[1], 4), round(numpy.linalg.solve(X1, X2)[2], 4)))
