import numpy as np;
traffic = np.array([
 [100,120,110],
 [90,95,100],
 [500,550,600]
]);

averageTraffic = traffic.mean();

print(np.where(traffic.mean(axis = 1)>averageTraffic)[0]);