import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
f = np.cos(x) * np.exp(x)

'''fig = plt.figure()
plt.plot(x, f)
plt.title("-2Pi to 2Pi Plot of cox(x) * exp(x)")
plt.xlabel("x")
plt.ylabel("cos(x) * exp(x)")
plt.show()'''

mean, stdD = 5.0, 2.0
n = np.random.normal(mean, stdD, 100000)

u = np.random.uniform(0, 10, 100000)

# HIstograms Plot Here.
num_bins = 10
fig = plt.figure(figsize= (12, 3))
plt.subplot(121)
n, bins, patches = plt.hist(n, num_bins, facecolor='blue', alpha=0.5)
plt.subplot(122)
n, bins, patches = plt.hist(u, num_bins, facecolor='red', alpha=0.5)
plt.show()



d = np.array([[2/3, 2/3, -1/3], [2/3, -1/3, 2/3], [-1/3, 2/3, 2/3]])
dt = d.transpose()
p = d.dot(dt)

e = np.array_equal(p, np.identity(3))

def check_orthogonal(M):
    # make sure the input is a matrix
    if len(np.shape(M)) != 2:
        print("error: input is not a matrix")
        return
    # make sure the input is a square matrix

    dim = np.shape(M)[0]
    if dim != np.shape(M)[1]:
        print("error: input is not a square matrix")
        return
    A = np.dot(M, M.T)
    if np.array_equal(A, np.identity(dim)):
        print("matrix is orthogonal")
    else:
        print("matrix is not orthogonal")


D = 1./3. * np.array([[2, 2, -1],
                        [2, -1, 2],
                        [-1, 2, 2]])


check_orthogonal(D)



