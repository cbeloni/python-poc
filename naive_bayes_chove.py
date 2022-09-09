#Importa a biblioteca do modelo Naive Bayes Gaussiano
from sklearn.naive_bayes import GaussianNB
import numpy as np

#Designa as variáveis previsor e alvo
temperatura= np.array([[-3,7],[15,17], [16,17], [-2,0], [2,3], [-4,0], [-1,1], [15,18], [16,18], [17,19], [20,25]])
tempo = np.array(['chove','chove','nao_chove','chove','chove','chove','chove','nao_chove','nao_chove','nao_chove','nao_chove']);
#print (temperatura)  

#x= np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
#y= np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

#Cria um classificador Gaussiano
model = GaussianNB()

#Treina o modelo usando os dados de treino 
model.fit(temperatura, tempo)

#Resultado de previsão 
predicted= model.predict([[1,2],[16,19]])
print(predicted)