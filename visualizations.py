import pandas as pd
import matplotlib.pyplot as plt

# Load the transformed dataset
df = pd.read_csv("music_mood_transformed.csv")

# Count favorite music genres
genre_counts = df["3. What is your favorite music genre?"].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))

genre_counts.plot(kind="bar")

plt.title("Favorite Music Genre")
plt.xlabel("Music Genre")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()

# Show the graph
# Save the graph
plt.savefig("favorite_music_genre.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()

"""# Count most common moods
mood_counts = df["9. What mood do you most commonly experience when listening to music?"].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))

mood_counts.plot(kind="bar")

plt.title("Most Common Mood When Listening to Music")
plt.xlabel("Mood")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph
plt.savefig("most_common_mood.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

"""# Count most used music platforms
platform_counts = df["7. Which platform do you use most often to listen to music?"].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))

platform_counts.plot(kind="bar")

plt.title("Most Used Music Platform")
plt.xlabel("Music Platform")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph
plt.savefig("most_used_platform.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

"""# Count listening frequency
frequency_counts = df["5. How often do you listen to music?"].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))

frequency_counts.plot(kind="bar")

plt.title("How Often Respondents Listen to Music")
plt.xlabel("Listening Frequency")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph
plt.savefig("listening_frequency.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

"""# Count daily listening hours
hours_counts = df["6. Approximately how many hours do you listen to music per day?"].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))

hours_counts.plot(kind="bar")

plt.title("Daily Music Listening Hours")
plt.xlabel("Hours per Day")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph
plt.savefig("daily_listening_hours.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

"""# Graph 6: Listening Situations

situations_df = pd.read_csv("listening_situations.csv")

# Use the first column for situations and second column for counts
situation_names = situations_df.iloc[:, 0]
situation_counts = situations_df.iloc[:, 1]

plt.figure(figsize=(10, 6))

plt.bar(situation_names, situation_counts)

plt.title("Situations When Respondents Listen to Music")
plt.xlabel("Listening Situation")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the graph
plt.savefig("listening_situations.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

"""# Graph 7: Importance of Music

importance_counts = df["4. How important is music in your daily life?"].value_counts()

plt.figure(figsize=(10, 6))

importance_counts.plot(kind="bar")

plt.title("Importance of Music in Daily Life")
plt.xlabel("Importance Level")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the graph
plt.savefig("music_importance.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

"""# Graph 8: Music Type Changes Depending on Mood

mood_change_counts = df[
    "10. Does the type of music you listen to change depending on your mood?"
].value_counts()

plt.figure(figsize=(10, 6))

mood_change_counts.plot(kind="bar")

plt.title("Music Type Changes Depending on Mood")
plt.xlabel("Response")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the graph
plt.savefig("music_type_change_by_mood.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

"""# Graph 9: Listening Frequency vs Daily Listening Hours

import numpy as np

# Add a small amount of jitter to make overlapping points visible
np.random.seed(42)

x = df["Listening_Frequency_Score"] + np.random.uniform(-0.15, 0.15, len(df))
y = df["Listening_Hours_Score"] + np.random.uniform(-0.15, 0.15, len(df))

plt.figure(figsize=(10, 6))

plt.scatter(
    x,
    y,
    alpha=0.4
)

plt.title("Listening Frequency vs Daily Listening Hours")
plt.xlabel("Listening Frequency Score")
plt.ylabel("Daily Listening Hours Score")

plt.xticks([1, 2, 3, 4, 5])
plt.yticks([1, 2, 3, 4, 5])

plt.xlim(0.5, 5.5)
plt.ylim(0.5, 5.5)

plt.tight_layout()

# Save the graph
plt.savefig("frequency_vs_hours.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()"""

# Graph 10: Age Group Distribution

plt.figure(figsize=(8, 5))

age_counts = df["1. What is your age group?"].value_counts()

plt.bar(age_counts.index, age_counts.values)

plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Respondents")

plt.tight_layout()

plt.savefig("age_group.png", dpi=300, bbox_inches="tight")

plt.show()


# Graph 11: Gender Distribution

plt.figure(figsize=(8, 5))

gender_counts = df["2. What is your gender?"].value_counts()

plt.bar(gender_counts.index, gender_counts.values)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Respondents")

plt.tight_layout()

plt.savefig("gender_distribution.png", dpi=300, bbox_inches="tight")

plt.show()


# Graph 12: How Music Affects Mood

plt.figure(figsize=(8, 5))

mood_effect_counts = df[
    "11. How does music generally affect your mood?"
].value_counts()

plt.bar(mood_effect_counts.index, mood_effect_counts.values)

plt.title("How Music Generally Affects Mood")
plt.xlabel("Effect on Mood")
plt.ylabel("Number of Respondents")

plt.xticks(rotation=30, ha="right")

plt.tight_layout()

plt.savefig("music_mood_effect.png", dpi=300, bbox_inches="tight")

plt.show()


# Graph 13: Genre Usually Listened to When Relaxed

plt.figure(figsize=(10, 6))

relaxed_genre_counts = df[
    "12. Which music genre do you usually listen to when you want to feel relaxed?"
].value_counts()

plt.bar(relaxed_genre_counts.index, relaxed_genre_counts.values)

plt.title("Music Genre Usually Listened to When Relaxed")
plt.xlabel("Music Genre")
plt.ylabel("Number of Respondents")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("relaxation_genre.png", dpi=300, bbox_inches="tight")

plt.show()


# Graph 14: Genre Usually Listened to When Energetic

plt.figure(figsize=(10, 6))

energetic_genre_counts = df[
    "13. Which music genre do you usually listen to when you want to feel energetic?"
].value_counts()

plt.bar(energetic_genre_counts.index, energetic_genre_counts.values)

plt.title("Music Genre Usually Listened to When Energetic")
plt.xlabel("Music Genre")
plt.ylabel("Number of Respondents")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("energy_genre.png", dpi=300, bbox_inches="tight")

plt.show()