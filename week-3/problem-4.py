import numpy as np;
marks = np.array([
    [80, 90, 70],
    [50, 60, 70],
    [90, 95, 85]
])

studentAverages = np.mean(marks, axis=1);

print(np.where(studentAverages > 75)[0]);