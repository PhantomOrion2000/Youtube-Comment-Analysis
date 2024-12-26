import emoji
import string, nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
 

class Preprocessor:
  def __init__(self, comments):
    nltk.download('punkt')          
    nltk.download('punkt_tab')
    nltk.download('stopwords')      
    nltk.download('wordnet') 
    self.comments = comments
    self.lemmatizer = WordNetLemmatizer()
    self.stop_words = set(stopwords.words("english"))

  def preprocess_comment(self, text):
    #Demojize
    text = emoji.demojize(text)

    # to lowercase
    text = text.lower()

    #Removing punctuations
    text = text.translate(str.maketrans('', '', string.punctuation))

    #Removing URLS/emails
    text = re.sub(r'http\S+|www\S+|@\S+|[\w.-]+@[\w.-]+\.\w+', '', text)

    #Tokenization
    words = word_tokenize(text)

    #Removing special characters
    words = [word for word in words if word.isalnum()]

    #Removing Numbers
    words = [word for word in words if not word.isdigit()]

    #Removing Stopwords
    words = [word for word in words if word not in self.stop_words]

    #Stemming
    words = [self.lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)

  def preprocess_all_comments(self):
    self.comments['cleaned_text'] = self.comments['text'].apply(self.preprocess_comment)

    return self.comments
