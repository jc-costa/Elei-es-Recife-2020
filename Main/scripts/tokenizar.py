import nltk
nltk.download('punkt')
from nltk.tokenize import TweetTokenizer

def Tokenizar(sentence):
  return TweetTokenizer().tokenize(sentence)
