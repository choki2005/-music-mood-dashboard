import pandas as pd

# Load the transformed dataset
df = pd.read_csv("music_mood_transformed.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Q3: Favorite music genre
genre = "3. What is your favorite music genre?"

print("\nFavorite Music Genres:")
print(df[genre].value_counts())

# Q9: Most common mood
mood = "9. What mood do you most commonly experience when listening to music?"

print("\nMost Common Moods:")
print(df[mood].value_counts())

# Q7: Most used music platform
platform = "7. Which platform do you use most often to listen to music?"

print("\nMost Used Music Platforms:")
print(df[platform].value_counts())

# Q5: Listening frequency
frequency = "5. How often do you listen to music?"

print("\nListening Frequency:")
print(df[frequency].value_counts())

# Q6: Daily listening hours
hours = "6. Approximately how many hours do you listen to music per day?"

print("\nDaily Listening Hours:")
print(df[hours].value_counts())