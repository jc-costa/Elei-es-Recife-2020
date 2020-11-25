import statistics

def porcent(predict, tipo):
       n = list(filter(lambda x: x == tipo, predict))
       porcent = (len(n) / len(predict)) * 100
       return print((tipo) + 's:', '%.2f' %(porcent), '%')

def moda(predict):
       return print('Moda: ' + statistics.mode(predict))

