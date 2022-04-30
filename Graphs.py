# #numpy fns
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()
# =====================
# #numpy fns
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0, 3*np.pi, 0.1)
# print(x)
# y = np.tan(x)
# print(y)
#
# plt.plot(x, y)
# plt.show()
# =====================
#numpy fns
# import numpy as np
# arr = np.array([1, 2, 3])
# print(np.log(arr))
# print(np.log10(arr))
# =====================
# from matplotlib import pyplot as plt
# from matplotlib import style
# style.use("ggplot")
# x1 = [5, 6, 8]
# y1 = [12, 16, 6]
#
# x2 = [2, 5, 1]
# y2 = [1, 16, 8]
#
# # plt.plot([1, 2, 3], [4, 5, 6])
# plt.plot(x1, y1, 'g', label='dataset1', linewidth=5)
# plt.plot(x2, y2, 'r', label='dataset2', linewidth=5)
# plt.title("TITLE")
# plt.ylabel("y axis")
# plt.xlabel("x axis")
# plt.grid(True, color='k')
# plt.legend()
# plt.axis('on')
# plt.show()

# ================
# histogram
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.random.normal(170, 10, 250)
#
# plt.hist(x)
# plt.show()
# =========================
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#
# plt.scatter(x, y)
# plt.show()

# =========================
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()



