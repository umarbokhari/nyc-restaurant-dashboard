import pandas as pd

# Load original full dataset
df = pd.read_csv(
    "data/DOHMH_New_York_City_Restaurant_Inspection_Results.csv"
)

# Create representative sample
sample_df = df.sample(10000, random_state=42)

# Save smaller dataset
sample_df.to_csv(
    "data/sample_restaurant_data.csv",
    index=False
)

print("Sample dataset created successfully!")