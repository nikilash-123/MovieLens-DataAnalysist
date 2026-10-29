import pandas as pd

# ==================================================
# MOVIELENS DATASET ANALYSIS
# ==================================================

# Load cleaned dataset
df = pd.read_excel("MovieLens_Cleaned.xlsx")

print("\n======================================")
print("       MOVIELENS DATASET ANALYSIS")
print("======================================")

# --------------------------------------------------
# 1. HEAD()
# --------------------------------------------------
print("\n1. FIRST 5 RECORDS")
print(df.head())


# --------------------------------------------------
# 2. TAIL()
# --------------------------------------------------
print("\n2. LAST 5 RECORDS")
print(df.tail())


# --------------------------------------------------
# 3. INFO()
# --------------------------------------------------
print("\n3. DATASET INFORMATION")
df.info()


# --------------------------------------------------
# 4. ISNA()
# --------------------------------------------------
print("\n4. MISSING VALUES")
print(df.isna().sum())


# --------------------------------------------------
# 5. BOOLEAN FILTERING
# Movies with Rating >= 4
# --------------------------------------------------
print("\n5. HIGH RATED MOVIES (Rating >= 4)")

high_rated = df[df["Rating"] >= 4]

print(high_rated.head(10))


# --------------------------------------------------
# 6. BOOLEAN FILTERING
# Movies released after 2000
# --------------------------------------------------
print("\n6. MOVIES RELEASED AFTER 2000")

recent_movies = df[df["Release_Year"] > 2000]

print(recent_movies.head(10))


# --------------------------------------------------
# 7. SORTING
# Highest rated movies
# --------------------------------------------------
print("\n7. TOP RATED MOVIES")

top_rated = df.sort_values(
    by="Rating",
    ascending=False
)

print(top_rated.head(10))


# --------------------------------------------------
# 8. SORTING
# Most rated movies
# --------------------------------------------------
print("\n8. MOST RATED MOVIES")

popular_movies = df.sort_values(
    by="Movie_Rating_Count",
    ascending=False
)

print(popular_movies.head(10))


# --------------------------------------------------
# 9. DESCRIBE()
# --------------------------------------------------
print("\n9. DESCRIPTIVE STATISTICS")

print(df.describe())


# --------------------------------------------------
# 10. MIDDLE 5 RECORDS
# --------------------------------------------------
print("\n10. MIDDLE 5 RECORDS")

mid = len(df) // 2

print(
    df.iloc[mid-2:mid+3]
)


# --------------------------------------------------
# 11. DATASET SHAPE
# --------------------------------------------------
print("\n11. DATASET SIZE")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# --------------------------------------------------
# END
# --------------------------------------------------
print("\n======================================")
print("       ANALYSIS COMPLETED")
print("======================================")