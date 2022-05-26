import matplotlib
import matplotlib.pyplot as plt
data = [
        [10, 0, 0, 0, 10],
        [10, 0 ,10, 0, 10],
        [10, 0, 10, 0, 10],
        [10, 0, 10, 0, 10],
        [10, 0, 0, 0, 10]
]
plt.imshow(data, cmap = "hot")
plt.show()