from sklearn.feature_extraction.text import CountVectorizer

def Vectorizar(tweets):
	vectorizer = CountVectorizer()
	data_vectorize = vectorizer.fit_transform(tweets)
	return data_vectorize
