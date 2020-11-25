import nltk
from nltk.corpus import stopwords

def removeStopWords(tweet):
    stop_words = stopwords.words('portuguese')
    novo_tweet = [word for word in tweet.split() if word.lower() not in stop_words] #novo_tweet é uma lista de palavras
    return ' '.join(novo_tweet) # Juntando a lista de palavras em uma única string
