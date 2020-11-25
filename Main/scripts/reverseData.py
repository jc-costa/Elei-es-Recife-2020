def reverseData():
  tweets = []
  aux = 0
  for frase in vectorizer.inverse_transform(X_test):
    for indice in range(0,len(frase)):
        if indice == len(frase) - 1:
            print(frase[indice], end = ' ')
            print('Resultado: ', predict[aux])
            aux += 1
        else:
            print(frase[indice], end = ' ')