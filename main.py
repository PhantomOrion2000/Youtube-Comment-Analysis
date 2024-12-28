import streamlit as st
from youtube_data_fetcher import YouTubeDataFetcher
from preprocessor import Preprocessor
from analyzer import SentimentAnalyzer
from visualizer import Visualizer
from dotenv import load_dotenv
import os
import pandas as pd

# Streamlit configuration
st.set_page_config(page_title="YouTube Comment Analyzer", layout="wide")

# App Title
st.title("🎥 YouTube Comment Analyzer")

# Input section
video_url = st.text_input("Paste YouTube Video Link", placeholder="https://www.youtube.com/watch?v=...")
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY") 
analyze_button = st.button("Analyze Comment")

# Extract Video ID from URL
def extract_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1][0:11]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1]
    return None

# print(extract_video_id(video_url))

if video_url:
    video_id = extract_video_id(video_url)
    if not video_id:
        st.error("Invalid YouTube URL! Please try again.")
    else:
        try:
            # Fetch comments
            fetcher = YouTubeDataFetcher(api_key, video_id)
            comments_data = fetcher.fetch_comments()
            comments = pd.DataFrame(comments_data)

            # Preprocess comments
            preprocessor = Preprocessor(comments)
            processed_comments = preprocessor.preprocess_all_comments()

            # Analyze sentiment
            analyzer = SentimentAnalyzer(processed_comments)
            analyzed_comments = analyzer.analyze_all_comments()

            # Display results
            visualizer = Visualizer(analyzed_comments)

            st.subheader("📊 Sentiment Insights")

            with st.container():
                col1, col2 = st.columns([1,1])

                # Pie Chart
                with col1:
                    st.write("#### Sentiment Distribution")
                    fig1 = visualizer.plot_sentiment_pie_chart()
                    st.pyplot(fig1)

                # Line Chart
                with col2:
                    st.write("#### Sentiment Over Time")
                    fig2 = visualizer.plot_sentiment_over_time()
                    st.pyplot(fig2)

            # Top comments
            st.write("#### Top Positive, Neutral, and Negative Comments")
            st.write(visualizer.display_top_comments())

            # Word cloud
            st.write("#### Word Clouds")
            visualizer.generate_word_cloud()
            
            # Show raw data
            st.write("#### Sample of Analyzed Comments")
            st.dataframe(analyzed_comments[['text', 'cleaned_text', 'sentiment', 'compound_score']])

        except Exception as e:
            st.error(f"Error: {e}")


























