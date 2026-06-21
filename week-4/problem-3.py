import numpy as np;
import pandas as pd;

df = pd.DataFrame(
  {
  "Student":pd.Categorical(["A", "B", "C", "D"]),
  "Maths": [85, 70, 95,60],
  "Science": [90,65,88,75],
  }
)

df["Total"] = df.loc[:,"Maths"] + df.loc[:,"Science"];

df["Average"] = df["Total"] / 2;

print(df.loc[df["Total"].idxmax(), "Student"]);

df = df.sort_values("Average", ascending=False);
print(df[df["Average"] > 80]);

