import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

class Visualizer:
  def __init__(self, comments):
    self.comments = comments

  def generate_word_cloud(self):
    # Generate text for word clouds
    positive_text = " ".join(self.comments[self.comments['sentiment'] == 1]['cleaned_text'])
    negative_text = " ".join(self.comments[self.comments['sentiment'] == -1]['cleaned_text'])

    # Create word clouds
    positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
    negative_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(negative_text)

    # Streamlit columns for side-by-side display
    col1, col2 = st.columns(2)

    # Display the positive word cloud
    with col1:
        st.markdown("##### Word Cloud for Positive Comments")
        st.image(positive_wordcloud.to_array(), use_container_width=True)

    # Display the negative word cloud
    with col2:
        st.markdown("##### Word Cloud for Negative Comments")
        st.image(negative_wordcloud.to_array(), use_container_width=True)



  def display_top_comments(self):
    sentiments = {1:"Positive", -1: "Negetive", 0 : "Neutral"}

    for sentiment, label in sentiments.items():
      filtered_data = self.comments[self.comments['sentiment'] == sentiment]
      
      if not filtered_data.empty:
        top_comment = filtered_data.sort_values(by = 'compound_score', ascending = False).iloc[0]
        st.markdown(f"**{label}:**")
        st.markdown(f"- {top_comment['text']} (Score: {top_comment['compound_score']:.2f})")
      else:
        st.markdown(f"**{label}:** No comments found for this sentiment.")
  
  
  def plot_sentiment_pie_chart(self):
    """
    Plots sentiment distribution as a pie chart.
    Assumes 'sentiment' column is present in the data.
    Sentiments are represented as:
    1: Positive
    -1: Negative
    0: Neutral
    """
    # Count the number of each sentiment
    sentiment_counts = self.comments['sentiment'].value_counts()

    # Define labels and colors
    labels = ['Positive', 'Negative', 'Neutral']
    colors = ['green', 'red', 'blue']

    # Ensure all sentiments are represented in the chart, even if count is 0
    sentiment_values = [sentiment_counts.get(1, 0), sentiment_counts.get(-1, 0), sentiment_counts.get(0, 0)]

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(3,3))
    ax.pie(
        sentiment_values,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 6}
    )
    fig.tight_layout()
    return fig
  
  def plot_sentiment_over_time(self):
    """
    Plots sentiment distribution over time as a line chart.
    Assumes 'publishDate' column is present in the data.
        """
    # Convert 'publishDate' to datetime and handle errors
    self.comments['publishDate'] = pd.to_datetime(self.comments['publishDate'], errors='coerce')

    # Handle missing dates (fill with the video publish date if available, or today's date)
    video_publish_date = pd.Timestamp("2005-02-14")  # Example publish date (YouTube's launch date)
    self.comments['publishDate'] = self.comments['publishDate'].fillna(video_publish_date)

    # Drop timezone information if present
    self.comments['publishDate'] = self.comments['publishDate'].dt.tz_localize(None)

    # Calculate the time range of the data
    date_range = self.comments['publishDate'].max() - self.comments['publishDate'].min()

    # Choose granularity based on the time range
    if date_range <= pd.Timedelta(days=30):  # Group by day for short ranges
        granularity = 'D'
    elif date_range <= pd.Timedelta(days=365):  # Group by week for up to a year
        granularity = 'W'
    elif date_range <= pd.Timedelta(days=365 * 20):  # Group by month for up to 20 years
        granularity = 'M'
    else:  # Group by year for very long durations
        granularity = 'Y'

    # Group by the chosen granularity and sentiment
    sentiment_time = (
        self.comments.groupby([self.comments['publishDate'].dt.to_period(granularity), 'sentiment'])
        .size()
        .unstack(fill_value=0)
    )

    # Convert Period index to string for better visualization
    sentiment_time.index = sentiment_time.index.astype(str)

    # Debug: Check grouped data
    # print(sentiment_time.head())

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    sentiment_colors = {1: 'green', -1: 'red', 0: 'blue'}
    sentiment_labels = {1: 'Positive', -1: 'Negative', 0: 'Neutral'}

    # Plot each sentiment line
    for sentiment in sentiment_colors.keys():
        if sentiment in sentiment_time.columns:  # Ensure the sentiment column exists
            ax.plot(
                sentiment_time.index,  # Use string index directly (PeriodIndex already converted to string)
                sentiment_time[sentiment],
                label=sentiment_labels[sentiment],
                color=sentiment_colors[sentiment],
                linewidth=2
            )

    # Adding labels, title, and legend
    ax.set_title('Sentiment Distribution Over Time', fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Count of Comments', fontsize=12)
    ax.legend(title="Sentiment", fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    # Adjust layout to prevent overlap
    fig.tight_layout()
    return fig

    # Save the plot as an image (optional)
    # fig.savefig('sentiment_over_time.png', dpi=300)

    # # Show the plot
    # plt.show()

