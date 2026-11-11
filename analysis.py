import pandas as pd

# Load the transformed dataset
df = pd.read_csv("music_mood_transformed.csv")

# Select the music importance scores
importance = df["Music_Importance_Score"]

print("Music Importance Analysis")
print("-------------------------")

print("Mean:", importance.mean())
print("Median:", importance.median())
print("Mode:", importance.mode()[0])
print("Minimum:", importance.min())
print("Maximum:", importance.max())
print("Standard Deviation:", importance.std())


# Listening frequency analysis
frequency = df["Listening_Frequency_Score"]

print("\nListening Frequency Analysis")
print("---------------------------")

print("Mean:", frequency.mean())
print("Median:", frequency.median())
print("Mode:", frequency.mode()[0])
print("Minimum:", frequency.min())
print("Maximum:", frequency.max())
print("Standard Deviation:", frequency.std())


# Daily listening hours analysis
hours = df["Listening_Hours_Score"]

print("\nDaily Listening Hours Analysis")
print("------------------------------")

print("Mean:", hours.mean())
print("Median:", hours.median())
print("Mode:", hours.mode()[0])
print("Minimum:", hours.min())
print("Maximum:", hours.max())
print("Standard Deviation:", hours.std())


# Q10: Music type changes depending on mood
print("\nMusic Type Change by Mood")
print("-------------------------")

print(df["10. Does the type of music you listen to change depending on your mood?"].value_counts())


# Q10 numerical analysis
mood_change = df["Mood_Change_Score"]

print("\nMusic Type Change Depending on Mood Analysis")
print("---------------------------------------------")

print("Mean:", mood_change.mean())
print("Median:", mood_change.median())
print("Mode:", mood_change.mode()[0])
print("Minimum:", mood_change.min())
print("Maximum:", mood_change.max())
print("Standard Deviation:", mood_change.std())



# Q1: Age Group Analysis
print("\nAge Group Analysis")
print("------------------")

q1 = df["1. What is your age group?"]

print(q1.value_counts())

print("\nPercentages:")
print(q1.value_counts(normalize=True).mul(100).round(2))


# Q2: Gender Analysis
print("\nGender Analysis")
print("---------------")

q2 = df["2. What is your gender?"]

print(q2.value_counts())

print("\nPercentages:")
print(q2.value_counts(normalize=True).mul(100).round(2))


# Q11: How Music Generally Affects Mood
print("\nHow Music Generally Affects Mood")
print("--------------------------------")

q11 = df["11. How does music generally affect your mood?"]

print(q11.value_counts())

print("\nPercentages:")
print(q11.value_counts(normalize=True).mul(100).round(2))


# Q12: Genre Usually Listened to When Relaxed
print("\nGenre Usually Listened to When Relaxed")
print("--------------------------------------")

q12 = df[
    "12. Which music genre do you usually listen to when you want to feel relaxed?"
]

print(q12.value_counts())

print("\nPercentages:")
print(q12.value_counts(normalize=True).mul(100).round(2))


# Q13: Genre Usually Listened to When Energetic
print("\nGenre Usually Listened to When Energetic")
print("-----------------------------------------")

q13 = df[
    "13. Which music genre do you usually listen to when you want to feel energetic?"
]

print(q13.value_counts())

print("\nPercentages:")
print(q13.value_counts(normalize=True).mul(100).round(2))

# Q4: Music Importance Percentage Analysis

print("\nQ4: Music Importance Percentage Analysis")
print("----------------------------------------")

q4 = df["4. How important is music in your daily life?"]

print("\nFrequencies:")
print(q4.value_counts())

print("\nPercentages:")
print(q4.value_counts(normalize=True).mul(100).round(2))

# Q14: Relationship Analysis
print("\nQ14: Relationship Between Listening Frequency and Daily Listening Hours")
print("---------------------------------------------------------------------")

correlation = df["Listening_Frequency_Score"].corr(
    df["Listening_Hours_Score"]
)

print("Pearson Correlation:", correlation)


# FORMAL HYPOTHESIS TESTING
# Add this section to analysis.py

import pandas as pd
from scipy.stats import chisquare, chi2_contingency

alpha = 0.05

# Research question variables
genre_col = "3. What is your favorite music genre?"
frequency_col = "5. How often do you listen to music?"
platform_col = "7. Which platform do you use most often to listen to music?"
age_col = "1. What is your age group?"
mood_col = "9. What mood do you most commonly experience when listening to music?"
context_col = "8. When do you usually listen to music? (Select all that apply)"


def goodness_of_fit_test(series, name, h0, h1):
    counts = series.dropna().value_counts()
    chi2, p_value = chisquare(counts.values)

    print(f"\n{name}")
    print("-" * len(name))
    print("H0:", h0)
    print("H1:", h1)
    print("Chi-square statistic:", round(chi2, 4))
    print("Degrees of freedom:", len(counts) - 1)
    print("P-value:", f"{p_value:.6g}")
    print("Significance level:", alpha)

    if p_value < alpha:
        print("Decision: Reject H0")
        print("Conclusion: The category proportions are not equal.")
    else:
        print("Decision: Fail to reject H0")
        print("Conclusion: There is insufficient evidence that")
        print("the category proportions differ.")


def independence_test(table, name, h0, h1):
    chi2, p_value, dof, expected = chi2_contingency(table)

    print(f"\n{name}")
    print("-" * len(name))
    print("H0:", h0)
    print("H1:", h1)
    print("Chi-square statistic:", round(chi2, 4))
    print("Degrees of freedom:", dof)
    print("P-value:", f"{p_value:.6g}")
    print("Significance level:", alpha)
    print("Smallest expected cell count:", round(expected.min(), 2))

    if (expected < 5).any():
        print("WARNING: Some expected counts are below 5.")
        print("Review category grouping before interpreting the test.")

    if p_value < alpha:
        print("Decision: Reject H0")
        print("Conclusion: There is evidence of an association.")
    else:
        print("Decision: Fail to reject H0")
        print("Conclusion: There is insufficient evidence of an association.")


