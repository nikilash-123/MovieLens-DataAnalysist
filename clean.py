import pandas as pd

# Load dataset
df = pd.read_excel(
    "MovieLens_Project_Uncleaned_10000.xlsx",
    sheet_name="Uncleaned_Data"
)

print("Before Cleaning:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with important missing values
df = df.dropna(
    subset=["User_ID", "Movie_ID", "Movie_Title", "Genres", "Rating"]
)

# Clean text columns
df["Movie_Title"] = df["Movie_Title"].str.strip()
df["Genres"] = df["Genres"].str.strip()

# Keep valid ratings only
df = df[
    (df["Rating"] >= 0.5) &
    (df["Rating"] <= 5.0)
]

# Convert date
df["Rating_Date"] = pd.to_datetime(
    df["Rating_Date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["Rating_Date"])

# Save cleaned dataset
df.to_excel(
    "MovieLens_Cleaned.xlsx",
    index=False
)

print("After Cleaning:", df.shape)
print("Cleaning Completed!")