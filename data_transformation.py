import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("music_mood_cleaned.csv")

# Question 8
q8 = "8. When do you usually listen to music? (Select all that apply)"

# Split multiple answers into individual activities
q8_data = df[q8].str.split(", ")

# Count each individual activity
q8_expanded = q8_data.explode()

print("Individual listening activities:")
print(q8_expanded.value_counts())

# Save the transformed Q8 counts
q8_counts = q8_expanded.value_counts()
q8_counts.to_csv("listening_situations.csv", header=["Number of Responses"])

print("\nTransformed Q8 data saved successfully!")

# Convert selected survey responses into numerical values

# Q4: Importance of music
importance_map = {
    "Not important": 1,
    "Slightly important": 2,
    "Moderately important": 3,
    "Very important": 4,
    "Extremely important": 5
}

# Q5: Listening frequency
frequency_map = {
    "Rarely": 1,
    "Once or twice a week": 2,
    "3–4 days a week": 3,
    "5–6 days a week": 4,
    "Every day": 5
}

# Q6: Hours of listening
hours_map = {
    "Less than 1 hour": 1,
    "1–2 hours": 2,
    "2–3 hours": 3,
    "3–4 hours": 4,
    "More than 4 hours": 5
}

df["Music_Importance_Score"] = df[
    "4. How important is music in your daily life?"
].map(importance_map)

df["Listening_Frequency_Score"] = df[
    "5. How often do you listen to music?"
].map(frequency_map)

df["Listening_Hours_Score"] = df[
    "6. Approximately how many hours do you listen to music per day?"
].map(hours_map)

print("\nTransformed numerical columns:")
print(df[
    ["Music_Importance_Score",
     "Listening_Frequency_Score",
     "Listening_Hours_Score"]
].head())

# Save the transformed dataset
df.to_csv("music_mood_transformed.csv", index=False)

print("\nTransformed dataset saved successfully!")

# Q10: Music type changes depending on mood
mood_change_mapping = {
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Often": 4,
    "Always": 5
}

df["Mood_Change_Score"] = df[
    "10. Does the type of music you listen to change depending on your mood?"
].map(mood_change_mapping)

df.to_csv("music_mood_transformed.csv", index=False)
print("Transformed dataset saved successfully.")
