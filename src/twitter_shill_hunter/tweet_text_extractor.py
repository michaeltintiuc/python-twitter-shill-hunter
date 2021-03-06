

class TweetTextExtractor():

    tweet_json = {}
    processed_tweets = []

    def __init__(self, tweet_json):
        """
        Grab the input
        JSON object for
        processing
        """

        self.tweet_json = tweet_json


    def extract_text(self):
        """
        Extract text content
        from tweets ready for
        processing.
        """
        
        for i in self.tweet_json:
            tweet_data = {}
            tweet_data['date'] = i['created_at']
            tweet_data['text'] = i['text']
            self.processed_tweets.append(tweet_data)

        return self.processed_tweets

            
  
     
