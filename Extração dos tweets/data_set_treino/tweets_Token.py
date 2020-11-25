from nltk.tokenize import word_tokenize

with open('tweets_semStopWords') as f:
	line = f.readline()
	while line:
		appendFile = open('tweets_Token','a')
		appendFile.write(str(word_tokenize(line))+"\n")
		appendFile.close()
		line = f.readline()
