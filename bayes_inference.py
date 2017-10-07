import numpy as np
from bayespy.nodes import Gaussian,GaussianARD, Wishart,Gamma
from bayespy.nodes import Dot
import bayespy.plot as bpplt

# X = Gaussian([2, 5], [[1.0, 0.3], [0.3, 1.0]])

# mu = Gaussian([0, 0], [[1e-6, 0],[0, 1e-6]])
# Lambda = Wishart(2, [[1, 0], [0, 1]])
# X = Gaussian(mu, Lambda, name="x")
D = 3
X = GaussianARD(0, 1,shape=(D,),plates=(1,100),name='X')
alpha = Gamma(1e-3, 1e-3,plates=(D,),name='alpha')

C = GaussianARD(0, alpha,shape=(D,),plates=(10,1),name='C')
F = Dot(C, X)
tau = Gamma(1e-3, 1e-3, name='tau')
Y = GaussianARD(F, tau, name='Y')

c = np.random.randn(10, 2)
x = np.random.randn(2, 100)
data = np.dot(c, x) + 0.1*np.random.randn(10, 100)


Y.observe(data)
Y.observe(data, mask=[[True], [False], [False], [True], [True],
                     [False], [True], [True], [True], [False]])
from bayespy.inference import VB
Q = VB(Y, C, X, alpha, tau)
Q['X']

X.initialize_from_parameters(np.random.randn(1, 100, D), 10)
Q.update()
Q.update(C, X)
Q.update(C, X, C, tau)
Q.update(repeat=10)
# Q.update(repeat=1000)
# Q.update(repeat=10000, tol=1e-6)

C.update()

from bayespy.inference.vmp import transformations
rotX = transformations.RotateGaussianARD(X)
rotC = transformations.RotateGaussianARD(C, alpha)
R = transformations.RotationOptimizer(rotC, rotX, D)
R.rotate()
alpha.initialize_from_prior()
C.initialize_from_prior()
X.initialize_from_parameters(np.random.randn(1, 100, D), 10)
tau.initialize_from_prior()
Q = VB(Y, C, X, alpha, tau)
Q.callback = R.rotate
Q.update(repeat=1000, tol=1e-6)

bpplt.pyplot.figure()
bpplt.pdf(Q['tau'], np.linspace(60, 140, num=100))


V = Gaussian([3, 5], [[4, 2], [2, 5]])
bpplt.pyplot.figure()
bpplt.contour(V, np.linspace(1, 5, num=100), np.linspace(3, 7, num=100))


bpplt.pyplot.figure()
bpplt.hinton(C)

bpplt.pyplot.figure()
bpplt.plot(X, axis=-2)

bpplt.pyplot.show()
