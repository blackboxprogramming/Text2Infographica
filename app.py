import streamlit as st
from utils.summarizer import summarize_text
from utils.query_extractor import generate_search_query
from utils.youtube_suggestor import get_youtube_videos

# Replace with your actual YouTube API key
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

# Streamlit App Config
st.set_page_config(page_title="Text2Infographica", layout="centered")
st.title("📘 Text2Infographica")
st.subheader("🧠 Text ➜ Summary ➜ Focused YouTube Suggestions")

# Input Text Box
text = st.text_area("✍️ Enter your content below:")

# Button to run summarization and fetch videos
if st.button("✨ Generate Summary + Videos"):
    if text:
        # Step 1: Generate Summary
        with st.spinner("Generating summary..."):
            summary = summarize_text(text)
        st.success("✅ Summary:")
        st.write(summary)

        # Step 2: Generate Focused Search Query
        with st.spinner("🔍 Generating YouTube search query..."):
            search_query = generate_search_query(summary)
        st.info(f"🎯 YouTube search query: {search_query}")

        # Step 3: Search YouTube
        st.subheader("📺 Suggested YouTube Videos")
        with st.spinner("Fetching videos..."):
            videos = get_youtube_videos(search_query, api_key=YOUTUBE_API_KEY)

        # Display YouTube videos
        if videos:
            for video in videos:
                st.markdown(f"""
                    <a href="{video['link']}" target="_blank">
                        <img src="{video['thumbnail']}" width="320"/><br>
                        <b>{video['title']}</b>
                    </a>
                    <br><br>
                """, unsafe_allow_html=True)
        else:
            st.warning("❌ No relevant videos found. Try a different input.")
    else:
        st.warning("Please enter some text above.")

