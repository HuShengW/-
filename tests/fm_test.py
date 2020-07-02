import numpy as np
import os

os.chdir('../')
import matplotlib.pyplot as plt
from ml_models.fm import FM

data1 = np.linspace(1, 10, num=100)
data2 = np.linspace(1, 10, num=100) + np.random.random(size=100)
data3 = np.linspace(10, 1, num=100)
target = data1 * 2 + data3 * 0.1 + data2 * 1 + 10 * data1 * data2 + np.random.random(size=100)
data = np.c_[data1, data2, data3]

model = FM(batch_size=2, lr=1e-3, epochs=1, lamb=1e-3, hidden_dim=4)
losses = model.fit(data, target)

plt.scatter(data[:, 0], target)
plt.plot(data[:, 0], model.predict(data), color='r')
plt.show()
plt.plot(range(0, len(losses)), losses)
plt.show()
print(model.V)
print(model.w)
