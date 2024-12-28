# Youtube-Comment-Analysis

This project focuses on analyzing YouTube video comments to extract meaningful insights using Python. It includes modules for data fetching, preprocessing, sentiment analysis, and visualization, providing a comprehensive workflow for comment analysis. The project allows users to visualize data trends and sentiments interactively.

---

## 🚀 Features
- **Sentiment Analysis**: Evaluate the polarity of YouTube comments (positive, neutral, negative).
- **Word Clouds**: Generate word clouds for different sentiment categories.
- **Interactive Visualizations**: Bar charts and line graphs to explore comment sentiment trends over time.
- **Custom Preprocessing**: Clean and standardize raw text data to improve analysis accuracy.

---

## 📂 Project Structure

### Explanation of Key Items:
- **`.py` Files**:
  - `main.py`: Entry point for the application.
  - `analyzer.py`: Performs comment sentiment analysis and related computations.
  - `preprocessor.py`: Preprocesses and cleans the YouTube comments.
  - `visualizer.py`: Generates visualizations like word clouds and sentiment trends.
  - `youtube_data_fetcher.py`: Fetches comments from a YouTube video using the YouTube Data API.
- **`__pycache__/`**: Contains Python bytecode (ignored in `.gitignore`).
- **`.gitignore`**: Specifies files and folders to ignore in Git (e.g., `.DS_Store`, `.pyc` files).
- **`README.md`**: This file, containing project documentation.
- **`requirements.txt`**: Lists all Python libraries needed to run the project.

---

## ⚙️ Tools & Technologies
- **Languages**: Python
- **Libraries**: Pandas, Matplotlib, Seaborn, Wordcloud, Google-API-Python-Client
- **APIs**: YouTube Data API for fetching video comments

---

## 📊 Data Preprocessing
- **Cleaning**: Removed unnecessary symbols, emojis, and stopwords from comments.
- **Sentiment Mapping**: Applied sentiment analysis to classify comments into positive, neutral, or negative categories.
- **Data Structuring**: Organized comments into a structured format for analysis and visualization.

---

## 🧠 Analysis and Visualizations
- **Sentiment Trends**: Visualize sentiment distribution over time.
- **Word Clouds**: Generate word clouds for positive, neutral, and negative comments.
- **Top Comments**: Display the most impactful comments sorted by sentiment intensity.

---

## 🖥️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Youtube-Comment-Analysis.git
