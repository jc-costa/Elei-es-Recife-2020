from nltk.corpus import stopwords

stop_words = set(stopwords.words('portuguese'))

file = open("tweets_limpados")

line = file.readline()

while line:
    words = line.split()
    for r in words:
        if not r.lower() in stop_words: 
            appendFile = open('tweets_semStopWords','a')
            appendFile.write(" " + r)
            appendFile.close()
    appendFile = open('tweets_semStopWords','a')
    appendFile.write("\n")
    appendFile.close()
    line = file.readline()