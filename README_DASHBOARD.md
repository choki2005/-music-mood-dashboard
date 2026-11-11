# Music Mood Dashboard

A Streamlit dashboard for exploring the supplied 500-response music survey dataset.

## Navigation

All pages are available under **Overview**:
- Dashboard
- Music Preferences
- Listening Habits
- Music & Mood
- K-Means Clustering
- About Page

The age-group and gender filters work together and update the displayed survey visualisations. The K-Means clustering branch has been carried over unchanged from the supplied project.

## Run on Windows

1. Extract the ZIP file.
2. Open the `Music_Mood_Dashboard_Final` folder in VS Code.
3. Open the VS Code terminal in that folder.
4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Run the dashboard:

   ```powershell
   python -m streamlit run dashboard.py
   ```

6. Open the local URL shown in the terminal, usually `http://localhost:8501`.

If `python` is not recognised, try `py` in place of `python`.

## Main files

- `dashboard.py` — Streamlit application
- `music_mood_transformed.csv` — dashboard dataset with the existing score columns
- `music_mood_survey_500_synthetic_responses.csv` — supplied 500-response source dataset
- `music_mood_cleaned.csv` — supplied cleaned dataset
- `requirements.txt` — Python dependencies
- `data_cleaning.py`, `data_transformation.py`, `eda.py`, `analysis.py`, `visualizations.py`, `hypothesis.py` — supporting scripts

Keep the CSV files and `dashboard.py` together in the project folder. The dashboard reads `music_mood_transformed.csv`; it does not overwrite the original survey file.
