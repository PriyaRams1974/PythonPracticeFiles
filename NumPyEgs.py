#numpy
# import numpy as np
# a = np.array([1, 2, 3])
# print(a)
# b = np.array([(1, 2, 3), (5, 6, 7)])
# print(b)
# ===============
#numpy/list
#
# import numpy as np
# import time
# import sys
# s = range(1000)
# print(sys.getsizeof(5) * len(s))
#
# D = np.arange(1000)
# print(D.size*D.itemsize)
# ====================
# execution time
# import numpy as np
# import time
#
# SIZE = 1000
# L1 = range(SIZE)
# L2 = range(SIZE)
#
# start = time.time()
# result = [(x, y) for x, y in zip(L1, L2)]
# print('normal list', (time.time() - start)*1000)
#
#
#
# A1 = np.arange(SIZE)
# A2 = np.arange(SIZE)
# start = time.time()
# result = A1 + A2
# print('numpy array', (time.time() - start)*1000)
#
# ====================

# numpy/list
# import numpy as np
# a = np.array([(1, 2, 3, 4, 5), (4, 5, 6, 7, 8), (9, 6, 4, 3, 2)])
# print(a.ndim)
# b = np.array((1, 2, 3))
# print(b.ndim)
# print(b.itemsize)
# print(b.dtype)
# print(a.shape)
# a = a.reshape(5, 3)
# print(a)
# ======================
# numpy/list
# import numpy as np
# a = np.array([(1, 2, 3, 4, 5), (4, 5, 6, 7, 8), (9, 6, 4, 3, 2)])
# print(a[0, 3])
# print(a[0:2, 3])
# print(a[0:3, 3])

# ===================
# numpy/linspace
# import numpy as np
# a = np.linspace(1, 3, 10)
# print(a)
# ===================
# numpy/sum
# import numpy as np
# a = np.array([(1, 2, 3), (5, 6, 7)])
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# ===================
# numpy/std
# import numpy as np
# a = np.array([(1, 2, 3), (5, 6, 7)])
# print(np.sqrt(a))
# print(np.std(a))

# ===================
import numpy as np
a = np.array([(1, 2, 3), (5, 6, 7)])
b = np.array([(1, 2, 3), (5, 6, 7)])
print(a+b)
print(a-b)










