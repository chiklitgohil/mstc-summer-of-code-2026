import numpy as np;
import pandas as pd;

df = pd.DataFrame(
  {
  "Product":pd.Categorical(["Laptop", "Mouse", "Keyboard", "Moniter"]),
  "Price": [50000, 500, 1500,12000],
  "Quantity": [5,20,15,7],
  }
)

print(df.loc[:,"Price"]);
print("\n");
print(df.loc[:,["Product", "Price"]]);
print("\n");
print(df[df["Price"] > 1000]);
print("\n");
print(df[df["Quantity"] < 10]);
print("\n");
print(df[(df["Quantity"] < 10) & (df["Price"] > 1000)]);