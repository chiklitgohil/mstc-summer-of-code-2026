import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("yasserh/titanic-dataset")

print("Path to dataset files:", path)



files_in_directory = os.listdir(path)

csv_file = None
for file in files_in_directory:
    if file.endswith('.csv'):
        csv_file = file
        break

if csv_file:
    full_csv_path = os.path.join(path, csv_file)
    df = pd.read_csv(full_csv_path)
    df.head()
else:
    print(f"No CSV file found in the directory: {path}")
    df = None 

print("Data : " , df)

print(df[df["Sex"] == "female"]);
print(df[df["Age"] > 30]);
print(df[df["Survived"] == 1]);
print(df[(df["Sex"] == "female") & (df["Survived"] == 1)]);
print(df["Age"].mean());
print(df.loc[df["Age"].idxmax(), "Name"]);