import string
def removePunctuation(sentence):
    aux = [char for char in sentence if char not in string.punctuation]
    aux = ''.join(aux)
    return aux
