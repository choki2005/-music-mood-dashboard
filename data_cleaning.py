import pandas as pd

# Read the CSV file
df = pd.read_csv("music_mood_survey_500_synthetic_responses.csv")

# Show the number of rows and columns
print("Dataset shape:")
print(df.shape)

# Show the column names
print("\nColumn names:")
print(df.columns.tolist())

# Show the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
print(df.head())

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Check unique responses in each column
print("\nUnique responses in each column:")

for column in df.columns:
    print(f"\n{column}")
    print(df[column].unique())

# Save the cleaned dataset
df.to_csv("music_mood_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")