import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# LOAD DATA
# ==========================================





df = pd.read_excel("MovieLens_Cleaned.xlsx")

print("Dataset Shape:", df.shape)


# ==========================================
# 1. HEAD()
# ==========================================

print("\n1. FIRST 5 RECORDS")
print(df.head())


# ==========================================
# 2. TAIL()
# ==========================================

print("\n2. LAST 5 RECORDS")
print(df.tail())


# ==========================================
# 3. INFO()
# ==========================================

print("\n3. DATASET INFORMATION")
df.info()


# ==========================================
# 4. ISNA()
# ==========================================

print("\n4. MISSING VALUES")
print(df.isna().sum())


# ==========================================
# 5. BOOLEAN FILTERING
# Rating >= 4
# ==========================================

print("\n5. HIGH RATED MOVIES")

high_rated = df[df["Rating"] >= 4]

print(high_rated.head(10))


# ==========================================
# 6. BOOLEAN FILTERING
# Release Year > 2000
# ==========================================

print("\n6. MOVIES RELEASED AFTER 2000")

recent_movies = df[df["Release_Year"] > 2000]

print(recent_movies.head(10))


# ==========================================
# 7. SORTING
# Highest Rating
# ==========================================

print("\n7. TOP RATED MOVIES")

top_rated = df.sort_values(
    by="Rating",
    ascending=False
)

print(top_rated.head(10))


# ==========================================
# 8. SORTING
# Most Rated Movies
# ==========================================

print("\n8. MOST POPULAR MOVIES")

popular_movies = df.sort_values(
    by="Movie_Rating_Count",
    ascending=False
)

print(popular_movies.head(10))


# ==========================================
# 9. DESCRIBE()
# ==========================================

print("\n9. DESCRIPTIVE STATISTICS")

print(df.describe())


# ==========================================
# 10. MIDDLE RECORDS
# ==========================================

print("\n10. MIDDLE 5 RECORDS")

mid = len(df) // 2

print(df.iloc[mid-2:mid+3])


# ==========================================
# 11. RATING DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Rating"],
    bins=10,
    kde=True
)

plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Ratings")

plt.tight_layout()
plt.show()


# ==========================================
# 12. TOP 10 MOVIES BY RATING
# ==========================================

top10 = (
    df.groupby("Movie_Title")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

top10.plot(kind="bar")

plt.title("Top 10 Movies by Average Rating")
plt.xlabel("Movie")
plt.ylabel("Average Rating")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# ==========================================
# 13. ENGAGEMENT DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Engagement_Score"],
    bins=20,
    kde=True
)

plt.title("Distribution of Engagement Score")
plt.xlabel("Engagement Score")
plt.ylabel("Count")

plt.tight_layout()
plt.show()


# ==========================================
# 14. CORRELATION HEATMAP
# ==========================================

numeric_columns = [
    "Rating",
    "Release_Year",
    "Movie_Average_Rating",
    "Movie_Rating_Count",
    "User_Average_Rating",
    "User_Rating_Count",
    "Engagement_Score"
]

plt.figure(figsize=(10, 7))

sns.heatmap(
    df[numeric_columns].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("MovieLens Correlation Heatmap")

plt.tight_layout()
plt.show()


# ==========================================
# END
# ==========================================

print("\n================================")
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("================================")