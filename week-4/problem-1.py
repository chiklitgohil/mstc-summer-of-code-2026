import numpy as np;
import pandas as pd;

df = pd.DataFrame(
  {
  "Name":pd.Categorical(["Alice", "Bob", "Charlie", "Davie"]),
  "Age": [21,19,22,20],
  "City":pd.Categorical(["Delhi", "Mumbai", "Ahemadabad", "Pune"]),
  }
)

print(df.head(2));
print(df.columns);
print(df.shape);
print(df.describe());