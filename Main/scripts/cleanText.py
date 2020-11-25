import re
def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
 text = re.sub('#', '', text) # Removing '#' hash tag
 text = re.sub('RT[\s]+', '', text) # Removing RT
 text = re.sub(r"http\S+", "", text) # Removing hyperlink 
 text = re.sub('\n', ' ', text)
 return text
