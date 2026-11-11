# Music Mood Dashboard — Streamlit deployment

## Run locally
1. Extract this folder.
2. Open it in VS Code.
3. In the terminal run: `py -m pip install -r requirements.txt`
4. Run: `py -m streamlit run dashboard.py`

## Publish with Streamlit Community Cloud
1. Sign in to GitHub and create a **new public repository** (for example, `music-mood-dashboard`).
2. Upload the complete contents of this folder to the repository root. Keep `dashboard.py`, `requirements.txt`, and `music_mood_transformed.csv` together.
3. Visit https://share.streamlit.io/ and sign in with the same GitHub account.
4. Choose **Create app**, select your repository and branch (`main`), and set the main file path to `dashboard.py`.
5. Select **Deploy**. Wait for the build to finish; Streamlit will provide your shareable app URL.

Do not upload private or personally identifying data. The included survey CSV is synthetic according to the project files.

## Design change
Only the Age group and Gender selectbox selected-value text in the sidebar has been changed to black for readability. The dashboard layout, charts, colours, and other styling are unchanged.
