import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("result.csv", delimiter=",")
num_of_elements = data[0].T
treap_time = data[1].T
list_time = data[2].T
plt.plot(num_of_elements, treap_time, "o--b", label="implicit treap time", color="blue")
plt.plot(num_of_elements, list_time, "o--b", label="list time", color="red")
plt.legend()
plt.title("Comparison")
plt.xlabel("number of elements")
plt.ylabel("time, s")
plt.show()
