from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:

  def __init__(self, comments):
    self.comments = comments
    self.analyzer = SentimentIntensityAnalyzer()

  def analyze_sentiment(self, text):
    scores = self.analyzer.polarity_scores(text)

    #Classify sentiment based on compound score
    if scores['compound'] > 0.03:
      return 1
    elif scores['compound'] < -0.03:
      return -1
    else:
      return 0

  def compound_score(self, text):
    return self.analyzer.polarity_scores(text)['compound']

  def analyze_all_comments(self):
    self.comments['sentiment'] = self.comments['cleaned_text'].apply(self.analyze_sentiment)
    self.comments['compound_score'] = self.comments['cleaned_text'].apply(self.compound_score)


    return self.comments

