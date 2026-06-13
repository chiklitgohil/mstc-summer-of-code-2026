import numpy as np;

transactions = [[1000,50,0], [5000,20,2], [3000,80,5]];

k = 2

transactions = np.array(transactions);

colMin = np.min(transactions, axis=0);
colMax = np.max(transactions, axis=0);

# print(colMax - colMin);

normalizedArr = (transactions - colMin) / (colMax - colMin);
weights = np.array([0.6,0.3,0.1]);


ans = np.sum(normalizedArr * weights, axis = 1);
sorted_indices = np.argsort(ans);
print(sorted_indices[-k:][::-1]);
