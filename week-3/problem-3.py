import numpy as np;

arr = np.array([
    [1, 2, 3],
    [5, 5, 5],
    [2, 2, 2]
])

sumArr = np.zeros(3,);
for i in range(sumArr.size):
  sumArr[i] = arr[i].sum();

print(np.argmax(sumArr));