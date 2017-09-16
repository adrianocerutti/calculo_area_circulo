#Imprime uma mensagem na tela
print("Cálculo de Área de uma Circunferência")
#Recupera o valor digitado pelo usuário e armazena na variável R
R = float(input("Digite o valor do raio: "))
#Inicialização da variável pi utilizada na fórmula (A = πR²) para o cálculo da área
pi = 3.14
#Realiza o cálculo e armazena o resultado na variável A
A = pi * (R**2)
#Imprime uma mensagem na tela com a resposta
print("Para um raio de",R,"metro(s), você possui uma área de",A,"m²")
