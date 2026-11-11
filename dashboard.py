
from pathlib import Path
import warnings
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Music Mood Dashboard",
    page_icon="♫",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE = Path(__file__).resolve().parent
DATA = BASE / "music_mood_transformed.csv"

AGE = "1. What is your age group?"
GENDER = "2. What is your gender?"
GENRE = "3. What is your favorite music genre?"
IMPORTANCE = "4. How important is music in your daily life?"
FREQUENCY = "5. How often do you listen to music?"
HOURS = "6. Approximately how many hours do you listen to music per day?"
PLATFORM = "7. Which platform do you use most often to listen to music?"
SITUATIONS = "8. When do you usually listen to music? (Select all that apply)"
MOOD = "9. What mood do you most commonly experience when listening to music?"
MOOD_CHANGE = "10. Does the type of music you listen to change depending on your mood?"
MOOD_EFFECT = "11. How does music generally affect your mood?"
RELAX = "12. Which music genre do you usually listen to when you want to feel relaxed?"
ENERGY = "13. Which music genre do you usually listen to when you want to feel energetic?"

COLORS = [
    "#7651A8", "#C05A93", "#318A83", "#D6A64B", "#6289C5",
    "#A66B4F", "#6C9B72", "#8B79B8", "#D17B62", "#4F91A6"
]


@st.cache_data
def load():
    if not DATA.exists():
        raise FileNotFoundError(
            "Keep music_mood_transformed.csv beside dashboard.py."
        )

    return pd.read_csv(DATA).drop(
        columns=["Email Address"],
        errors="ignore"
    )


data = load()

# --------------------------------------------------
# PAGE DESIGN AND CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: #F5F3F8;
    color: #292238;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #241832 0%,
        #38234B 100%
    );
}

[data-testid="stSidebar"] * {
    color: #F8F4FC;
}

[data-testid="stSidebar"] label {
    color: #F8F4FC !important;
    font-weight: 600;
}

.hero {
    padding: 1.45rem 1.65rem;
    border-radius: 18px;
    background: linear-gradient(
        112deg,
        #241832,
        #5B347A 58%,
        #A3447E
    );
    color: white;
    margin: 0 0 1.15rem;
}

.hero h1 {
    color: white !important;
    margin: 0 0 .3rem;
    font-size: 1.9rem;
}

.hero p {
    color: #F5EAFE !important;
    margin: 0;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 14px 16px;
    border: 1px solid #E5DDED;
    border-radius: 14px;
    box-shadow: 0 2px 10px rgba(38,24,50,.04);
}

/* ================================================
   AGE AND GENDER SELECTBOX FIX
   Force selected values to BLACK
   ================================================ */

/* White background for both filter boxes */
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}

/* Selected Age and Gender text */
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] div,
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] span,
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] input,
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] [class*="singleValue"],
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] [class*="valueContainer"] {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    opacity: 1 !important;
}

/* Streamlit selected-value text */
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] [class*="ValueContainer"] * {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* Dropdown arrow */
[data-testid="stSidebar"] [data-testid="stSelectbox"]
[data-baseweb="select"] svg {
    fill: #7651A8 !important;
    color: #7651A8 !important;
}

/* Dropdown menu background */
[data-baseweb="popover"],
[data-baseweb="popover"] ul,
[role="listbox"] {
    background-color: #FFFFFF !important;
}

/* Dropdown choices in black */
[data-baseweb="popover"] *,
[role="listbox"] *,
[role="option"] {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* Selected or hovered dropdown option */
[role="option"]:hover,
[role="option"][aria-selected="true"],
[aria-selected="true"] {
    background-color: #EEE7F4 !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* Keep Age group and Gender labels white */
[data-testid="stSidebar"] [data-testid="stSelectbox"] label {
    color: #FFFFFF !important;
}

h2, h3 {
    color: #39254D;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

@media(max-width:700px) {
    .hero {
        padding: 1.1rem;
    }

    .hero h1 {
        font-size: 1.5rem;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.markdown("# Music Mood Dashboard")
st.sidebar.caption("Music preferences · Listening habits · Mood")

st.sidebar.markdown("### Overview")

page = st.sidebar.radio(
    "Overview navigation",
    [
        "Dashboard",
        "Music Preferences",
        "Listening Habits",
        "Music & Mood",
        "K-Means Clustering",
        "About Page"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Filters")


# --------------------------------------------------
# AGE AND GENDER FILTERS
# --------------------------------------------------

ages = sorted(data[AGE].dropna().astype(str).unique())
genders = sorted(data[GENDER].dropna().astype(str).unique())

a = st.sidebar.selectbox(
    "Age group",
    ["All age groups"] + ages,
    key="age_filter"
)

g = st.sidebar.selectbox(
    "Gender",
    ["All genders"] + genders,
    key="gender_filter"
)


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

df = data.copy()

if a != "All age groups":
    df = df[df[AGE].astype(str) == a]

if g != "All genders":
    df = df[df[GENDER].astype(str) == g]

st.sidebar.caption(
    "Filters apply to the survey visualisations."
)

if df.empty:
    st.warning(
        "No responses match the selected filters. "
        "Clear one or both filters to view responses."
    )
    st.stop()


# --------------------------------------------------
# REUSABLE FUNCTIONS
# --------------------------------------------------

def hero(title, subtitle=""):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def finish(fig, h=390):
    fig.update_layout(
        template="plotly_white",
        height=h,
        margin=dict(l=12, r=25, t=55, b=18),
        font=dict(color="#39254D"),
        title_font=dict(size=18),
        legend_title_text=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )


def counts(col):
    return (
        df[col]
        .dropna()
        .astype(str)
        .value_counts()
        .rename_axis("Category")
        .reset_index(name="People")
    )


def horizontal_bar(col, title, height=None):
    d = counts(col).sort_values("People", ascending=True)

    fig = px.bar(
        d,
        x="People",
        y="Category",
        orientation="h",
        text="People",
        color="Category",
        color_discrete_sequence=COLORS,
        title=title
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False,
        marker_line_width=0
    )

    fig.update_layout(
        xaxis_title="Number of respondents",
        yaxis_title="",
        showlegend=False
    )

    finish(fig, height or max(340, 38 * len(d)))


def column_chart(col, title, order=None, height=390):
    d = counts(col)

    if order:
        d["Category"] = pd.Categorical(
            d["Category"],
            categories=order,
            ordered=True
        )
        d = d.sort_values("Category")

    fig = px.bar(
        d,
        x="Category",
        y="People",
        text="People",
        color="Category",
        color_discrete_sequence=COLORS,
        title=title
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Number of respondents",
        showlegend=False,
        xaxis_tickangle=-12
    )

    finish(fig, height)


def donut(col, title):
    d = counts(col)

    fig = px.pie(
        d,
        names="Category",
        values="People",
        hole=.57,
        color_discrete_sequence=COLORS,
        title=title
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate=(
            "%{label}<br>"
            "%{value} respondents (%{percent})"
            "<extra></extra>"
        )
    )

    finish(fig, 400)


def multi_counts():
    vals = []

    for value in df[SITUATIONS].dropna().astype(str):
        vals.extend(
            x.strip()
            for x in value.split(",")
            if x.strip()
        )

    return (
        pd.Series(vals)
        .value_counts()
        .rename_axis("Situation")
        .reset_index(name="Selections")
    )


# --------------------------------------------------
# DASHBOARD PAGE
# --------------------------------------------------

if page == "Dashboard":

    hero(
        "Music Mood Dashboard",
        "A snapshot of the 500-participant music listening survey."
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Survey responses", f"{len(df):,}")
    c2.metric("Age groups", df[AGE].nunique())
    c3.metric("Gender categories", df[GENDER].nunique())
    c4.metric("Survey questions", "13")

    left, right = st.columns(2)

    with left:
        donut(GENDER, "Respondents by gender")

    with right:
        horizontal_bar(AGE, "Respondents by age group")


# --------------------------------------------------
# MUSIC PREFERENCES PAGE
# --------------------------------------------------

elif page == "Music Preferences":

    hero(
        "Music Preferences",
        "Genres, music importance and platform choices."
    )

    left, right = st.columns([1.2, 1])

    with left:
        horizontal_bar(GENRE, "Favourite music genres")

    with right:

        score = pd.to_numeric(
            df["Music_Importance_Score"],
            errors="coerce"
        ).dropna()

        average = float(score.mean()) if not score.empty else 0

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=average,
                number={
                    "suffix": " / 5",
                    "font": {"size": 34, "color": "#39254D"}
                },
                title={
                    "text": "Average importance of music",
                    "font": {"size": 17}
                },
                gauge={
                    "axis": {
                        "range": [0, 5],
                        "tickwidth": 1,
                        "tickcolor": "#8A7A99"
                    },
                    "bar": {"color": "#7651A8"},
                    "bgcolor": "#F1ECF5",
                    "steps": [
                        {"range": [0, 2], "color": "#F3E4EC"},
                        {"range": [2, 4], "color": "#E9E1F1"},
                        {"range": [4, 5], "color": "#DCEDE8"}
                    ],
                    "threshold": {
                        "line": {"color": "#C05A93", "width": 4},
                        "thickness": .8,
                        "value": average
                    }
                }
            )
        )

        finish(gauge, 400)

    platform = counts(PLATFORM)

    tree = px.treemap(
        platform,
        path=["Category"],
        values="People",
        color="People",
        color_continuous_scale=["#E9DDF2", "#7651A8"],
        title="Most-used music platforms"
    )

    tree.update_traces(textinfo="label+value+percent root")
    finish(tree, 420)

    left, right = st.columns(2)

    with left:
        horizontal_bar(RELAX, "Music genres for relaxation")

    with right:

        d = counts(ENERGY).sort_values(
            "People",
            ascending=True
        )

        fig = px.bar(
            d,
            x="People",
            y="Category",
            orientation="h",
            text="People",
            color="People",
            color_continuous_scale=["#F2D9A6", "#C05A4A"],
            title="Music genres for energy"
        )

        fig.update_traces(
            textposition="outside",
            cliponaxis=False
        )

        fig.update_layout(
            xaxis_title="Number of respondents",
            yaxis_title="",
            coloraxis_showscale=False
        )

        finish(fig, max(340, 38 * len(d)))


# --------------------------------------------------
# LISTENING HABITS PAGE
# --------------------------------------------------

elif page == "Listening Habits":

    hero(
        "Listening Habits",
        "How often, how long and in which situations respondents listen."
    )

    left, right = st.columns(2)

    with left:
        column_chart(
            FREQUENCY,
            "Listening frequency",
            [
                "Rarely",
                "Once or twice a week",
                "3–4 days a week",
                "5–6 days a week",
                "Every day"
            ]
        )

    with right:

        d = counts(HOURS)

        hour_order = [
            "Less than 1 hour",
            "1–2 hours",
            "2–3 hours",
            "3–4 hours",
            "More than 4 hours"
        ]

        d["Category"] = pd.Categorical(
            d["Category"],
            categories=hour_order,
            ordered=True
        )

        d = d.sort_values("Category")

        fig = px.line(
            d,
            x="Category",
            y="People",
            markers=True,
            title="Daily listening hours",
            color_discrete_sequence=["#7651A8"],
            text="People"
        )

        fig.update_traces(
            line=dict(width=3),
            marker=dict(size=10),
            textposition="top center"
        )

        fig.update_layout(
            xaxis_title="Hours per day",
            yaxis_title="Number of respondents"
        )

        finish(fig, 400)

    situations = multi_counts().sort_values(
        "Selections",
        ascending=True
    )

    fig = px.bar(
        situations,
        x="Selections",
        y="Situation",
        orientation="h",
        text="Selections",
        color="Situation",
        color_discrete_sequence=COLORS,
        title="Listening Situations"
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False,
        hovertemplate="%{y}<br>%{x} selections<extra></extra>"
    )

    fig.update_layout(
        xaxis_title="Number of Selections",
        yaxis_title="",
        showlegend=False,
        margin=dict(l=15, r=35, t=58, b=25)
    )

    finish(fig, max(360, 42 * len(situations)))


# --------------------------------------------------
# MUSIC AND MOOD PAGE
# --------------------------------------------------

elif page == "Music & Mood":

    hero(
        "Music & Mood",
        "Self-reported moods, emotional effects and music choices."
    )

    left, right = st.columns(2)

    with left:
        donut(MOOD, "Most common mood while listening")

    with right:

        d = counts(MOOD_EFFECT)

        fig = px.bar_polar(
            d,
            r="People",
            theta="Category",
            color="Category",
            color_discrete_sequence=COLORS,
            title="How music affects mood"
        )

        fig.update_traces(opacity=.86)
        finish(fig, 420)

    d = counts(MOOD_CHANGE)

    order = ["Never", "Rarely", "Sometimes", "Often", "Always"]

    d["Category"] = pd.Categorical(
        d["Category"],
        categories=order,
        ordered=True
    )

    d = d.sort_values("Category")
    d["Percentage"] = d["People"] / d["People"].sum() * 100

    fig = px.bar(
        d,
        x=["Responses"] * len(d),
        y="Percentage",
        color="Category",
        text=d["Percentage"].map(lambda x: f"{x:.1f}%"),
        color_discrete_sequence=COLORS,
        title="Does music choice change with mood?",
        category_orders={"Category": order}
    )

    fig.update_layout(
        barmode="stack",
        xaxis_title="",
        yaxis_title="Share of responses",
        yaxis=dict(range=[0, 100], ticksuffix="%")
    )

    fig.update_traces(
        textposition="inside",
        hovertemplate=(
            "%{fullData.name}: %{y:.1f}%"
            "<extra></extra>"
        )
    )

    finish(fig, 390)

    relax = (
        df[RELAX]
        .dropna()
        .astype(str)
        .value_counts()
        .rename("Relaxation")
    )

    energy = (
        df[ENERGY]
        .dropna()
        .astype(str)
        .value_counts()
        .rename("Energy")
    )

    comparison = pd.concat(
        [relax, energy],
        axis=1
    ).fillna(0).astype(int)

    comparison.index.name = "Genre"
    comparison = comparison.reset_index()

    comparison["Total"] = (
        comparison["Relaxation"] +
        comparison["Energy"]
    )

    comparison = comparison.sort_values(
        "Total",
        ascending=True
    )

    comparison_long = comparison.melt(
        id_vars="Genre",
        value_vars=["Relaxation", "Energy"],
        var_name="Listening Purpose",
        value_name="Number of Respondents"
    )

    fig = px.bar(
        comparison_long,
        x="Number of Respondents",
        y="Genre",
        color="Listening Purpose",
        barmode="group",
        orientation="h",
        text="Number of Respondents",
        color_discrete_map={
            "Relaxation": "#7651A8",
            "Energy": "#D6A64B"
        },
        title="Relaxation Genres vs Energy Genres"
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        xaxis_title="Number of Respondents",
        yaxis_title="",
        legend=dict(orientation="h", y=1.08, x=0),
        margin=dict(l=15, r=40, t=75, b=25)
    )

    finish(fig, max(400, 48 * len(comparison)))


# --------------------------------------------------
# K-MEANS CLUSTERING PAGE
# --------------------------------------------------

elif page == "K-Means Clustering":

    hero(
        "K-Means Clustering",
        "Grouping respondents with similar music-listening score patterns."
    )

    cols = [
        "Listening_Frequency_Score",
        "Listening_Hours_Score",
        "Music_Importance_Score",
        "Mood_Change_Score"
    ]

    cols = [c for c in cols if c in df]

    frame = df[cols].apply(
        pd.to_numeric,
        errors="coerce"
    ).dropna()

    if len(frame) < 5:

        st.warning(
            "Clustering requires at least five complete responses."
        )

    else:

        maxk = min(6, len(frame) - 1)

        k = st.slider(
            "Number of clusters (K)",
            2,
            maxk,
            min(3, maxk)
        )

        scaled = StandardScaler().fit_transform(frame)

        labels = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        ).fit_predict(scaled)

        xy = PCA(
            n_components=2,
            random_state=42
        ).fit_transform(scaled)

        plot = pd.DataFrame({
            "Component 1": xy[:, 0],
            "Component 2": xy[:, 1],
            "Cluster": [
                f"Cluster {i+1}" for i in labels
            ]
        })

        fig = px.scatter(
            plot,
            x="Component 1",
            y="Component 2",
            color="Cluster",
            color_discrete_sequence=COLORS,
            title="Respondent clusters",
            opacity=.82
        )

        fig.update_traces(marker=dict(size=9))
        finish(fig, 490)

        sizes = (
            pd.Series(labels)
            .value_counts()
            .sort_index()
            .rename_axis("Cluster")
            .reset_index(name="Respondents")
        )

        sizes["Cluster"] = sizes["Cluster"].map(
            lambda n: f"Cluster {n+1}"
        )

        fig = px.bar(
            sizes,
            x="Cluster",
            y="Respondents",
            text="Respondents",
            color="Cluster",
            color_discrete_sequence=COLORS,
            title="Number of respondents in each cluster"
        )

        fig.update_traces(textposition="outside")
        finish(fig, 350)

        profile = (
            frame.assign(
                Cluster=[
                    f"Cluster {i+1}" for i in labels
                ]
            )
            .groupby("Cluster")[cols]
            .mean()
            .round(2)
            .reset_index()
            .melt(
                id_vars="Cluster",
                var_name="Score variable",
                value_name="Average score"
            )
        )

        fig = px.bar(
            profile,
            x="Score variable",
            y="Average score",
            color="Cluster",
            barmode="group",
            text="Average score",
            color_discrete_sequence=COLORS,
            title="Average score profile by cluster"
        )

        fig.update_layout(xaxis_tickangle=-15)
        finish(fig, 420)


# --------------------------------------------------
# ABOUT PAGE
# --------------------------------------------------

elif page == "About Page":

    hero(
        "About the Project",
        "Project purpose, scope, analytical approach and sources."
    )

    st.markdown("### About the Project")

    st.write(
        "The Music Mood Dashboard explores how people choose and use "
        "music in everyday life. Using survey responses, it presents "
        "patterns in favourite genres, music platforms, listening "
        "frequency and duration, listening situations, and self-reported "
        "mood. The dashboard also includes a K-Means clustering view "
        "to explore groups of respondents with similar listening-score "
        "patterns."
    )

    st.markdown("### Project Information")

    info1, info2 = st.columns(2)

    with info1:

        st.markdown("**Project title**")

        st.write(
            "Music Mood Dashboard: Exploring Music Preferences, "
            "Listening Habits, and Mood"
        )

        st.markdown("**Dataset**")
        st.write("500 survey responses · 13 survey questions")

        st.markdown("**Main areas**")

        st.write(
            "Music preferences · Listening habits · "
            "Music and mood · K-Means clustering"
        )

    with info2:

        st.markdown("**Technologies**")

        st.write(
            "Python · Streamlit · Pandas · Plotly · scikit-learn"
        )

        st.markdown("**Analytical approach**")

        st.write(
            "Descriptive frequency counts and percentages, "
            "score-based summaries, multi-response counting for "
            "listening situations, and K-Means clustering using "
            "the existing numerical score features."
        )

    st.markdown("### Dashboard Features")

    feature_cols = st.columns(2)

    feature_text = [
        (
            "Dashboard",
            "Overall respondent profile and survey snapshot."
        ),
        (
            "Music Preferences",
            "Favourite genres, music importance, platforms, "
            "relaxation and energy genres."
        ),
        (
            "Listening Habits",
            "Listening frequency, daily listening duration "
            "and listening situations."
        ),
        (
            "Music & Mood",
            "Common moods, reported emotional effects, "
            "mood-based music choices and genre comparison."
        ),
        (
            "K-Means Clustering",
            "Explores respondent groupings using the existing "
            "clustering implementation."
        )
    ]

    for i, (name, description) in enumerate(feature_text):

        with feature_cols[i % 2]:

            st.markdown(f"**{name}**")
            st.write(description)

    st.markdown("### References")

    references = [
        "McKinney, W. (2010). Data structures for statistical computing in Python. Proceedings of the 9th Python in Science Conference, 56–61. https://doi.org/10.25080/Majora-92bf1922-00a",
        "Plotly Technologies Inc. (n.d.). Plotly Python graphing library. https://plotly.com/python/",
        "Python Software Foundation. (n.d.). Python documentation. https://docs.python.org/3/",
        "scikit-learn developers. (n.d.). 2.3. Clustering. https://scikit-learn.org/stable/modules/clustering.html",
        "Streamlit, Inc. (n.d.). Streamlit documentation. https://docs.streamlit.io/",
        "The pandas development team. (n.d.). pandas documentation. https://pandas.pydata.org/docs/"
    ]

    for reference in references:
        st.markdown(f"- {reference}")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Music Mood Dashboard · The supplied survey source file "
    "identifies the responses as synthetic."
)
