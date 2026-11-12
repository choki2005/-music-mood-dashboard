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
