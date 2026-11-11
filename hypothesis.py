
import pandas as pd
from scipy.stats import chisquare, chi2_contingency

# ============================================================
# MUSIC MOOD DASHBOARD - FORMAL HYPOTHESIS TESTING
# Dataset: music_mood_transformed.csv
# Significance level: 0.05
# ============================================================

FILE_NAME = "music_mood_transformed.csv"
ALPHA = 0.05


# ============================================================
# 1. LOAD DATA AND DEFINE ACTUAL COLUMN NAMES
# ============================================================

df = pd.read_csv(FILE_NAME)

genre_col = "3. What is your favorite music genre?"
frequency_col = "5. How often do you listen to music?"
mood_col = (
    "9. What mood do you most commonly experience "
    "when listening to music?"
)
age_col = "1. What is your age group?"
platform_col = (
    "7. Which platform do you use most often "
    "to listen to music?"
)
context_col = (
    "8. When do you usually listen to music? "
    "(Select all that apply)"
)

print("=" * 65)
print("MUSIC MOOD DASHBOARD: HYPOTHESIS TESTING")
print("=" * 65)
print("Dataset shape:", df.shape)

required_columns = [
    genre_col, frequency_col, mood_col,
    age_col, platform_col, context_col
]

missing_columns = [c for c in required_columns if c not in df.columns]

if missing_columns:
    raise ValueError(
        "These columns were not found in the CSV:\n"
        + "\n".join(missing_columns)
    )

print("All required columns were found.")


# ============================================================
# 2. GENERAL FUNCTION: CHI-SQUARE GOODNESS-OF-FIT TEST
# ============================================================

def goodness_of_fit_test(series, title, h0, h1):
    print(f"\n\n{title}")
    print("-" * 65)
    print("H0:", h0)
    print("H1:", h1)

    data = series.dropna().astype(str).str.strip()
    data = data[data != ""]

    observed = data.value_counts()
    observed = observed[observed > 0]

    if len(observed) < 2:
        print("ERROR: At least two categories are required.")
        return

    # H0 assumes equal proportions across categories
    expected = [len(data) / len(observed)] * len(observed)

    chi_stat, p_value = chisquare(
        f_obs=observed.values,
        f_exp=expected
    )

    dfree = len(observed) - 1

    print("\nObserved counts:")
    print(observed.to_string())

    print("\nExpected counts under H0:")
    expected_table = pd.DataFrame({
        "Category": observed.index,
        "Observed": observed.values,
        "Expected": expected
    })
    print(expected_table.to_string(index=False))

    print("\nSample size:", len(data))
    print("Chi-square statistic:", round(chi_stat, 4))
    print("Degrees of freedom:", dfree)
    print("P-value:", f"{p_value:.6g}")
    print("Significance level:", ALPHA)

    if min(expected) < 5:
        print("WARNING: Some expected counts are below 5.")
        print("Review the suitability of the chi-square approximation.")

    if p_value < ALPHA:
        print("Decision: Reject H0")
        print("Conclusion:", h1)
    else:
        print("Decision: Fail to reject H0")
        print("Conclusion: There is insufficient evidence to reject H0.")


# ============================================================
# 3. GENERAL FUNCTION: CHI-SQUARE TEST OF INDEPENDENCE
# ============================================================

def independence_test(table, title, h0, h1):
    print(f"\n\n{title}")
    print("-" * 65)
    print("H0:", h0)
    print("H1:", h1)

    table = table.loc[
        table.sum(axis=1) > 0,
        table.sum(axis=0) > 0
    ]

    print("\nObserved contingency table:")
    print(table.to_string())

    if table.shape[0] < 2 or table.shape[1] < 2:
        print("ERROR: At least two categories per variable are required.")
        return

    chi_stat, p_value, dfree, expected = chi2_contingency(table)

    print("\nChi-square statistic:", round(chi_stat, 4))
    print("Degrees of freedom:", dfree)
    print("P-value:", f"{p_value:.6g}")
    print("Significance level:", ALPHA)
    print("Smallest expected cell count:", round(expected.min(), 4))

    cells_below_5 = int((expected < 5).sum())
    total_cells = expected.size

    print(
        f"Expected cells below 5: {cells_below_5} "
        f"out of {total_cells}"
    )

    if (expected < 1).any() or (expected < 5).sum() / expected.size > 0.20:
        print(
            "WARNING: Expected counts may be too small for the "
            "usual chi-square approximation. Review the test."
        )
    else:
        print("Expected-frequency guideline: Acceptable.")

    if p_value < ALPHA:
        print("Decision: Reject H0")
        print("Conclusion:", h1)
    else:
        print("Decision: Fail to reject H0")
        print("Conclusion: There is insufficient evidence to reject H0.")


# ============================================================
# H1: ARE FAVOURITE MUSIC GENRES EQUALLY POPULAR?
# Chi-square goodness-of-fit test
# ============================================================

goodness_of_fit_test(
    df[genre_col],
    "H1: Favourite Music Genre",
    "Favourite music genres are equally distributed.",
    "Favourite music genres are not equally distributed."
)


# ============================================================
# H2: IS LISTENING FREQUENCY EQUALLY DISTRIBUTED?
# Chi-square goodness-of-fit test
# ============================================================

goodness_of_fit_test(
    df[frequency_col],
    "H2: Listening Frequency",
    "Responses are equally distributed across frequency categories.",
    "Responses are not equally distributed across frequency categories."
)


# ============================================================
# H3: IS FAVOURITE GENRE ASSOCIATED WITH MOOD?
# Chi-square test of independence
# ============================================================

h3_data = df[[genre_col, mood_col]].dropna().copy()

h3_data[genre_col] = h3_data[genre_col].astype(str).str.strip()
h3_data[mood_col] = h3_data[mood_col].astype(str).str.strip()

h3_data = h3_data[
    (h3_data[genre_col] != "") &
    (h3_data[mood_col] != "")
]

genre_group = h3_data[genre_col].where(
    h3_data[genre_col].isin(
        ["Pop", "Hip-hop/Rap", "R&B/Soul", "Rock"]
    ),
    "Other genres"
)

mood_group = h3_data[mood_col].where(
    h3_data[mood_col].isin(
        ["Happy", "Energetic", "Relaxed", "Calm"]
    ),
    "Other moods"
)

table_h3 = pd.crosstab(genre_group, mood_group)

independence_test(
    table_h3,
    "H3: Music Genre and Mood",
    "Favourite genre and commonly experienced mood are independent.",
    "Favourite genre and commonly experienced mood are associated."
)


# ============================================================
# H4: DOES LISTENING FREQUENCY VARY BY AGE GROUP?
# Chi-square test of independence
# ============================================================

h4_data = df[[age_col, frequency_col]].dropna().copy()

h4_data[age_col] = h4_data[age_col].astype(str).str.strip()
h4_data[frequency_col] = (
    h4_data[frequency_col].astype(str).str.strip()
)

# Standardize common age-label variations
age_group = h4_data[age_col].replace({
    "Under 18": "Under 25",
    "18–24": "Under 25",
    "18-24": "Under 25",
    "18–24 years": "Under 25",
    "18-24 years": "Under 25",
    "25–34": "25–34",
    "25-34": "25–34",
    "25–34 years": "25–34",
    "25-34 years": "25–34",
    "35–44": "35+",
    "35-44": "35+",
    "35–44 years": "35+",
    "35-44 years": "35+",
    "45–54": "35+",
    "45-54": "35+",
    "45–54 years": "35+",
    "45-54 years": "35+",
    "55 and above": "35+",
    "55+": "35+",
    "55 and above years": "35+"
})

# Standardize common listening-frequency labels
frequency_group = h4_data[frequency_col].replace({
    "Rarely": "1–2 days/week",
    "Once or twice a week": "1–2 days/week",
    "1-2 days/week": "1–2 days/week",
    "1–2 days a week": "1–2 days/week",
    "3–4 days a week": "3–4 days/week",
    "3-4 days a week": "3–4 days/week",
    "3-4 days/week": "3–4 days/week",
    "5–6 days a week": "5–7 days/week",
    "5-6 days a week": "5–7 days/week",
    "5–7 days/week": "5–7 days/week",
    "Every day": "5–7 days/week",
    "Everyday": "5–7 days/week"
})

table_h4 = pd.crosstab(age_group, frequency_group)

print("\nAge categories after grouping:")
print(age_group.value_counts().to_string())

print("\nFrequency categories after grouping:")
print(frequency_group.value_counts().to_string())

independence_test(
    table_h4,
    "H4: Age Group and Listening Frequency",
    "Age group and listening frequency are independent.",
    "Age group and listening frequency are associated."
)


# ============================================================
# H5: ARE MUSIC PLATFORMS EQUALLY USED?
# Chi-square goodness-of-fit test
# ============================================================

# The survey asks which platform respondents use MOST OFTEN.
# Each respondent should contribute one platform response.

goodness_of_fit_test(
    df[platform_col],
    "H5: Music Platform Usage",
    "All platform categories are used in equal proportions.",
    "Platform usage proportions are not all equal."
)


# ============================================================
# H6: IS STUDYING/WORKING CONTEXT ASSOCIATED WITH MOOD?
# Chi-square test of independence
# ============================================================

# The context question allows multiple selections.
# Each respondent is classified once:
# studying/working selected versus not selected.

h6_data = df[[context_col, mood_col]].copy()

# Exclude rows missing either context or mood
h6_data = h6_data.dropna(subset=[context_col, mood_col])

h6_data[context_col] = h6_data[context_col].astype(str).str.strip()
h6_data[mood_col] = h6_data[mood_col].astype(str).str.strip()

h6_data = h6_data[
    (h6_data[context_col] != "") &
    (h6_data[mood_col] != "")
]

print("\n\nH6: Original context response examples")
print("-" * 65)
print(h6_data[context_col].value_counts().head(15).to_string())

# Identify selections referring to studying or working.
# This accommodates responses such as "Studying/working, Relaxing".
study_work = h6_data[context_col].str.contains(
    r"studying|working|study|work",
    case=False,
    regex=True
)

mood_group_h6 = h6_data[mood_col].where(
    h6_data[mood_col].isin(
        ["Happy", "Energetic", "Relaxed", "Calm"]
    ),
    "Other moods"
)

table_h6 = pd.crosstab(study_work, mood_group_h6)

table_h6.index = table_h6.index.map({
    True: "Studying/working selected",
    False: "Studying/working not selected"
})

independence_test(
    table_h6,
    "H6: Studying/Working Context and Mood",
    "Studying/working selection and mood are independent.",
    "Studying/working selection and mood are associated."
)


# ============================================================
# COMPLETION
# ============================================================

print("\n\n" + "=" * 65)
print("ALL SIX HYPOTHESIS TESTS COMPLETED")
print("=" * 65)
print("Significance level:", ALPHA)