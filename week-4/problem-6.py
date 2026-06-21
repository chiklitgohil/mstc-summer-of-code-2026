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

# print("Data : " , df)
print(df.columns);
print(df.groupby("Sex")[["Survived"]].mean());
print(df.groupby("Pclass")[["Age"]].mean());
print(df.groupby("Pclass")[["Age"]].count());

classSurvival = df.groupby("Pclass")["Survived"].mean();
print(df.loc[classSurvival.idxmax(),"Name"]);

print(df.groupby("Pclass")[["Fare"]].mean());

# It seems like females on this ship had a much higher survival chance, then also class of passenger is inversnly proportional to the age, and also that 3rd class passanger were signifficinlty more on board. class one passangers paid a signifficanlty higher cost.