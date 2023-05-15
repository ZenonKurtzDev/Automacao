#Debugando o código
#F9  -Marcar um breakpoint
#F5  -Abrir o modo debug
#F10 - Passar sobre uma linha,sem entar  em método interno
#F11 - Passar sobre uma linha e ,entar em método interno

print('Olá')
def    calcular_preco_combo(pizza,refrigente):
       total= pizza + refrigente
       print(total)
calcular_preco_combo(30,20)
print('Programa finalizado')
        