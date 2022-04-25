from matplotlib import pyplot as plt
plt.bar([0.25, 1.25, 2.25, 3.25,  4.25], [50, 40, 70, 90, 100], label="BMW", color='green',  width= .5)
plt.bar([0.15, 1.55, 2.55, 3.75,  5.25], [30, 80, 70, 20, 60], label="Audi",color='red', width= .5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()