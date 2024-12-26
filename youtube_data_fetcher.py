import requests

class YouTubeDataFetcher:
  def __init__(self, api_key, video_id):
    self.api_key = api_key
    self.video_id = video_id
    self.comments = []

  def fetch_comments(self, max_results = 100):

      # Base URL for the YouTube Data API to fetch comment threads
      url = "https://www.googleapis.com/youtube/v3/commentThreads"

      # Parameters for the API request
      params = {
          "part": "snippet",  # Specifies the data to include in the response (snippet contains comment details)
          "videoId": self.video_id,  # The ID of the video to fetch comments for
          "key":  self.api_key,  # Your API key to authenticate the request
          "maxResults": 100,  # Maximum number of comments to retrieve (max limit is 100 per request)
          "textFormat": "plainText"  # Ensures comments are returned in plain text format
      }

      # Make the GET request to the API with the provided parameters
      response = requests.get(url, params=params)

      # Check if the request was successful (status code 200)
      if response.status_code == 200:
          # Parse the response JSON data
          data = response.json()

          # Initialize an empty list to store the fetched comments
          comments = []

          # Loop through each item (comment thread) in the response data
          for item in data["items"]:
              # Extract the snippet containing the comment details
              curr_item = item['snippet']["topLevelComment"]["snippet"]

              # Extract specific fields from the comment snippet
              text = curr_item['textDisplay']  # The comment text
              author_name = curr_item['authorDisplayName']  # Name of the comment author
              author_profile_picture_url = curr_item['authorProfileImageUrl']  # URL of the author's profile picture
              author_channel_url = curr_item['authorChannelUrl']  # URL of the author's YouTube channel
              like_count = curr_item['likeCount']  # Number of likes the comment received
              reply_count = item['snippet']['totalReplyCount']  # Number of replies to the comment
              published_date = curr_item['publishedAt']  # Date and time when the comment was published

              # Create a dictionary to represent the comment
              comment = {
                  "text": text,
                  "author": author_name,
                  "authorProfilePictureUrl": author_profile_picture_url,
                  "authorChannelUrl": author_channel_url,
                  "likeCount": like_count,
                  "replyCount": reply_count,
                  "publishDate": published_date
              }

              # Append the comment dictionary to the comments list
              self.comments.append(comment)

          return self.comments

      else:
          # If the request failed, print the status code and error details
          print(f"Failed to fetch comments: {response.status_code}")
          print(response.json())

# fetcher = YouTubeDataFetcher('AIzaSyA0y8QjmOa_LngNsGbcEzkl6APXy2P1ZKQ', 'c6D-KTdi5cs')
# print( fetcher.fetch_comments())




