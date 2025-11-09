**Text2Infographica: Project Overview**

Text2Infographica is a web app that simplifies long and complex text by generating a concise summary and suggesting focused YouTube videos to help users quickly understand the core concepts. The goal is to make learning easier and faster by combining NLP-based summarization with smart YouTube query generation.
Built using Transformer models from Hugging Face and deployed on Hugging Face Spaces, this app takes any input text, summarizes it, extracts relevant keywords and returns carefully aligned YouTube video suggestions.

**Deployment:** **[Launch Text2Infographica 🚀](https://huggingface.co/spaces/Fathima9Mehek/text2infographica)**

**What the app does:**

Summarizes long paragraphs, articles or notes into clear shorter text.
Extracts key concepts from the summary to form a YouTube search query.
Fetches educational YouTube videos that match the summarized content.
This helps students, researchers and self-learners quickly grasp topics without searching through irrelevant videos manually.

**Code and Resources Used:**
1. Python Version: 3.12.7
2. Packages: transformers, torch, requests, streamlit
3. To install all dependencies: pip install -r requirements.txt

**Key Models Used:**
1. Summarization Model: sshleifer/distilbart-cnn-12-6
2. Keyword/Query Generator Model: google/flan-t5-small
3. YouTube Search: Uses YouTube Data API v3 (Requires an API key)

**App Flow:**
1. Text Summarization: The raw input text is passed into a DistilBART summarizer model to reduce it into a clean, informative summary.
2. Query Extraction: A FLAN-T5 model is used to extract a short, meaningful YouTube search query from the summary.
3. YouTube Video Suggestion: The search query is sent to the YouTube Data API to fetch video titles, thumbnails and URLs. The top results are displayed directly in the Streamlit interface.

**Usage:**
1. Run the App: streamlit run app.py
2. Enter any long text: Example: Paste lecture notes, articles, research papers or chapters.
3. Click "Generate Summary + Videos":
You will receive:
A clean summarized explanation.
A smartly generated YouTube search query.
A list of recommended video resources.

**Key Idea Behind the App:**
Students often search YouTube manually after reading something difficult.
Text2Infographica automates that workflow by:
Understanding the text,
summarizing it,
identifying the central learning topic
and recommending videos that align with that topic.

**This improves:**
Learning efficiency,
concept clarity and
study time productivity.

**Future Improvements:**
Multi-language summarization support,
infographic-style visual summaries,
option to save summaries and
support for PDF uploads and OCR extraction.

**Deployment:** 
The web app is deployed on Hugging Face Spaces, accessible publicly.
The YouTube API key is hidden from the public interface for security.


