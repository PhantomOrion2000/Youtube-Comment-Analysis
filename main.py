# # import sys
# # import nltk , emoji
# # print("Streamlit is using Python: ", sys.executable)

# import nltk
# # print(nltk.data.path)
# nltk.download('punkt_tab')

# # print(nltk.data.find('tokenizers/punkt'))

# from nltk.tokenize import word_tokenize

# sample_text = "This is a test sentence!"
# tokens = word_tokenize(sample_text)
# print(tokens)


import streamlit as st
from youtube_data_fetcher import YouTubeDataFetcher
from preprocessor import Preprocessor
from analyzer import SentimentAnalyzer
from visualizer import Visualizer
import pandas as pd

# Streamlit configuration
st.set_page_config(page_title="YouTube Comment Analyzer", layout="wide")

# App Title
st.title("🎥 YouTube Comment Analyzer")

# Input section
video_url = st.text_input("Paste YouTube Video Link", placeholder="https://www.youtube.com/watch?v=...")
# api_key = st.secrets["API_KEY"]  # Use Streamlit secrets for API keys
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
            fetcher = YouTubeDataFetcher("ctyrytrty", video_id)
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
            # Sentiment distribution
            st.write("#### Sentiment Distribution Over Time")
            visualizer.plot_sentiment_over_time()

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


























# # from youtube_data_fetcher import YouTubeDataFetcher
# # from preprocessor import Preprocessor
# # import pandas as pd
# # from analyzer import SentimentAnalyzer
# # from visualizer import Visualizer
# #
# # # Set the max column width to display full text
# # pd.set_option('display.max_colwidth', None)
# #
# # API_KEY = 'AIzaSyA0y8QjmOa_LngNsGbcEzkl6APXy2P1ZKQ'
# # VIDEO_ID = "Llr2dcd-VBo"
# #
# # fetcher = YouTubeDataFetcher(API_KEY, VIDEO_ID)
# #
# # comments_data = fetcher.fetch_comments()
# #
# # # Converting to dataframe
# # comments = pd.DataFrame(comments_data)
# #
# # preprocessor = Preprocessor(comments)
# # processed_comments = preprocessor.preprocess_all_comments()
# #
# # # Analyze sentiment
# # analyzer = SentimentAnalyzer(processed_comments)
# # analyzed_comments = analyzer.analyze_all_comments()
# #
# # visualizer = Visualizer(analyzed_comments)
# #
# # # visualizer.generate_word_cloud()
# # visualizer.display_top_comments()
# # visualizer.plot_sentiment_over_time()
# #
# # print(analyzed_comments.sample(5)[['text','cleaned_text','sentiment', 'compound_score']])
# #
