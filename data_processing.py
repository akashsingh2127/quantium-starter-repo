import pandas as pd
from pathlib import Path


data_path = Path("data")

csv_files = list(data_path.glob("*.csv"))

processed_frames = []

for file in csv_files:
    df = pd.read_csv(file)

   
    df = df[df["product"] == "Pink Morsel"]

    
    df["sales"] = df["quantity"] * df["price"]

    df = df[["sales", "date", "region"]]

    processed_frames.append(df)


final_df = pd.concat(processed_frames, ignore_index=True)


final_df.to_csv("processed_sales_data.csv", index=False)

print("✅ Data processing complete. Output saved as processed_sales_data.csv")
